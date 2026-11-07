/**
 * Hire a Bot — desktop half of the hireabot unified package.
 * Plain ESM (no JSX). Imports only @hermes/plugin-sdk, react, react/jsx-runtime.
 */
import * as sdk from '@hermes/plugin-sdk'
import { useCallback, useEffect, useMemo, useState } from 'react'
import { jsx, jsxs } from 'react/jsx-runtime'

const ID = 'hireabot'
const PATH = '/hireabot'

const {
  Button,
  Badge,
  EmptyState,
  ErrorState,
  GlyphSpinner,
  SearchField,
  ScrollArea,
  Separator,
  Tip,
  host,
  cn,
  haptic
} = sdk

const ROUTES_AREA = sdk.ROUTES_AREA
const SIDEBAR_NAV_AREA = sdk.SIDEBAR_NAV_AREA
const PALETTE_AREA = sdk.PALETTE_AREA

function useBots(query, rest) {
  const [state, setState] = useState({ status: 'loading', bots: [], error: null, source: null })

  const load = useCallback(async () => {
    if (typeof rest !== 'function') {
      setState({
        status: 'error',
        bots: [],
        error: 'This Desktop build has no plugin REST bridge. Update Hermes Desktop, or use /hireabot in chat.',
        source: null
      })
      return
    }
    setState(s => ({ ...s, status: 'loading', error: null }))
    try {
      const q = (query || '').trim()
      const path = q ? `/bots?q=${encodeURIComponent(q)}&limit=60` : '/bots?limit=80'
      const data = await rest(path)
      setState({
        status: 'ready',
        bots: Array.isArray(data?.bots) ? data.bots : [],
        error: null,
        source: data?.source || null
      })
    } catch (err) {
      const message =
        (err && (err.message || err.detail)) ||
        String(err) ||
        'Could not load the Hireabot catalog. Is the hireabot plugin enabled for this gateway?'
      setState({ status: 'error', bots: [], error: message, source: null })
    }
  }, [query, rest])

  useEffect(() => {
    load()
  }, [load])

  return { ...state, reload: load }
}

function BotRow({ bot, busySlug, onInstall, onOpen }) {
  const installing = busySlug === bot.slug
  return jsxs('div', {
    className: cn(
      'flex items-start gap-3 rounded-lg border border-(--ui-stroke-secondary) bg-(--ui-panel) px-3 py-3',
      'hover:border-(--ui-stroke-primary)'
    ),
    children: [
      jsxs('div', {
        className: 'min-w-0 flex-1',
        children: [
          jsxs('div', {
            className: 'flex flex-wrap items-center gap-2',
            children: [
              jsx('div', {
                className: 'truncate text-sm font-medium text-(--ui-text-primary)',
                children: bot.name || bot.slug
              }),
              jsx(Badge, {
                variant: 'muted',
                children: `v${bot.version || '0.1.0'}`
              }),
              bot.installed
                ? jsx(Badge, { variant: 'outline', children: 'installed' })
                : null
            ]
          }),
          jsx('div', {
            className: 'mt-1 text-[length:var(--conversation-caption-font-size)] text-(--ui-text-tertiary)',
            children: bot.description || 'No description.'
          }),
          jsx('div', {
            className: 'mt-1 font-mono text-[0.6875rem] text-(--ui-text-quaternary)',
            children: bot.slug
          })
        ]
      }),
      jsxs('div', {
        className: 'flex shrink-0 flex-col gap-1.5',
        children: [
          bot.installed
            ? jsx(Button, {
                size: 'sm',
                variant: 'secondary',
                onClick: () => onOpen(bot),
                children: 'Open'
              })
            : jsx(Tip, {
                label: 'Installs this bot as a new Hermes profile',
                children: jsx(Button, {
                  size: 'sm',
                  disabled: installing || Boolean(busySlug),
                  onClick: () => onInstall(bot),
                  children: installing ? 'Hiring…' : 'Hire'
                })
              }),
          jsx(Button, {
            size: 'sm',
            variant: 'ghost',
            onClick: () => onOpen(bot),
            children: 'Details'
          })
        ]
      })
    ]
  })
}

function DetailPanel({ bot, onBack, busySlug, onInstall }) {
  if (!bot) return null
  const installing = busySlug === bot.slug
  return jsxs('div', {
    className: 'flex h-full flex-col gap-3 p-4',
    children: [
      jsxs('div', {
        className: 'flex items-center gap-2',
        children: [
          jsx(Button, { size: 'sm', variant: 'ghost', onClick: onBack, children: '← Back' }),
          jsx('div', {
            className: 'truncate text-base font-medium',
            children: bot.name || bot.slug
          }),
          jsx(Badge, { variant: 'muted', children: `v${bot.version || '0.1.0'}` })
        ]
      }),
      jsx(Separator, {}),
      jsx('div', {
        className: 'text-sm text-(--ui-text-secondary)',
        children: bot.summary || bot.description || ''
      }),
      Array.isArray(bot.use_cases) && bot.use_cases.length
        ? jsxs('div', {
            className: 'flex flex-col gap-1',
            children: [
              jsx('div', {
                className: 'text-[0.6875rem] font-medium uppercase tracking-wide text-(--ui-text-quaternary)',
                children: 'Use cases'
              }),
              ...bot.use_cases.slice(0, 8).map((u, i) =>
                jsx(
                  'div',
                  {
                    className: 'text-sm text-(--ui-text-tertiary)',
                    children: `• ${u}`
                  },
                  i
                )
              )
            ]
          })
        : null,
      jsxs('div', {
        className: 'mt-auto flex gap-2',
        children: [
          bot.installed
            ? jsx(Button, {
                onClick: () => {
                  haptic?.('tap')
                  host.newChat?.(bot.slug)
                  host.notify?.({ kind: 'info', message: `Opened a chat with ${bot.name || bot.slug}` })
                },
                children: 'Chat with bot'
              })
            : jsx(Button, {
                disabled: installing || Boolean(busySlug),
                onClick: () => onInstall(bot),
                children: installing ? 'Hiring…' : 'Hire this bot'
              }),
          jsx(Button, {
            variant: 'secondary',
            onClick: () => host.notify?.({ kind: 'info', message: `Slug: ${bot.slug}` }),
            children: bot.slug
          })
        ]
      })
    ]
  })
}

function HireabotPage({ rest }) {
  const [query, setQuery] = useState('')
  const [debounced, setDebounced] = useState('')
  const [selected, setSelected] = useState(null)
  const [busySlug, setBusySlug] = useState(null)
  const { status, bots, error, source, reload } = useBots(debounced, rest)

  useEffect(() => {
    const t = setTimeout(() => setDebounced(query), 220)
    return () => clearTimeout(t)
  }, [query])

  const openDetails = useCallback(
    async bot => {
      if (typeof rest !== 'function') {
        setSelected(bot)
        return
      }
      try {
        const data = await rest(`/bots/${encodeURIComponent(bot.slug)}`)
        setSelected(data?.bot || bot)
      } catch (err) {
        host.notifyError?.(err, 'Could not load bot details')
        setSelected(bot)
      }
    },
    [rest]
  )

  const install = useCallback(
    async bot => {
      if (typeof rest !== 'function') {
        host.notify?.({
          kind: 'warning',
          message: 'Install needs the Hireabot backend. Enable the plugin under Capabilities → Plugins, then try again.'
        })
        return
      }
      setBusySlug(bot.slug)
      haptic?.('tap')
      try {
        const data = await rest(`/bots/${encodeURIComponent(bot.slug)}/install`, {
          method: 'POST',
          body: { dry_run: false }
        })
        host.notify?.({
          kind: 'success',
          message: `Hired ${data?.name || bot.name || bot.slug}. Open it from your bots list.`
        })
        setSelected(s => (s && s.slug === bot.slug ? { ...s, installed: true } : s))
        await reload()
      } catch (err) {
        const detail = err?.detail
        const msg =
          (typeof detail === 'string' && detail) ||
          (detail && detail.message) ||
          err?.message ||
          'Hire failed'
        host.notify?.({ kind: 'error', message: String(msg) })
      } finally {
        setBusySlug(null)
      }
    },
    [rest, reload]
  )

  if (selected) {
    return jsx(DetailPanel, {
      bot: selected,
      onBack: () => setSelected(null),
      busySlug,
      onInstall: install
    })
  }

  return jsxs('div', {
    className: 'flex h-full flex-col gap-3 p-4',
    children: [
      jsxs('div', {
        className: 'flex flex-col gap-1',
        children: [
          jsx('div', { className: 'text-base font-medium', children: 'Hire a Bot' }),
          jsx('div', {
            className: 'text-[length:var(--conversation-caption-font-size)] text-(--ui-text-tertiary)',
            children: 'Browse ready-made Hermes bots. Hire one to install it as a new profile.'
          })
        ]
      }),
      jsxs('div', {
        className: 'flex items-center gap-2',
        children: [
          jsx('div', {
            className: 'min-w-0 flex-1',
            children: jsx(SearchField, {
              value: query,
              placeholder: 'Search by job, name, or skill…',
              onChange: setQuery
            })
          }),
          jsx(Button, {
            size: 'sm',
            variant: 'secondary',
            onClick: () => reload(),
            children: 'Refresh'
          })
        ]
      }),
      source
        ? jsx('div', {
            className: 'font-mono text-[0.6875rem] text-(--ui-text-quaternary)',
            children: `Catalog: ${source}`
          })
        : null,
      status === 'loading'
        ? jsxs('div', {
            className: 'flex flex-1 items-center justify-center gap-2 text-(--ui-text-tertiary)',
            children: [jsx(GlyphSpinner, {}), jsx('span', { children: 'Loading bots…' })]
          })
        : null,
      status === 'error'
        ? jsx(ErrorState, {
            title: 'Could not load bots',
            description: error,
            children: jsx(Button, { size: 'sm', onClick: () => reload(), children: 'Retry' })
          })
        : null,
      status === 'ready' && bots.length === 0
        ? jsx(EmptyState, {
            title: debounced ? 'No matching bots' : 'No bots in catalog',
            description: debounced
              ? 'Nothing in the catalog matches that area. Ask chat to install Bot Designer (hireabot_install slug=bot-designer); its own interview and build process helps create the bot you need. Installation needs your yes.'
              : 'Check the catalog source in Settings → Plugins → Hireabot.'
          })
        : null,
      status === 'ready' && bots.length > 0
        ? jsx(ScrollArea, {
            className: 'min-h-0 flex-1',
            children: jsx('div', {
              className: 'flex flex-col gap-2 pr-1',
              children: bots.map(bot =>
                jsx(
                  BotRow,
                  {
                    bot,
                    busySlug,
                    onInstall: install,
                    onOpen: openDetails
                  },
                  bot.slug
                )
              )
            })
          })
        : null
    ]
  })
}

export default {
  id: ID,
  name: 'Hire a Bot',
  // Unified packages ship opt-in; flip Desktop on under Capabilities → Plugins.
  defaultEnabled: false,
  register(ctx) {
    const rest = typeof ctx.rest === 'function' ? ctx.rest.bind(ctx) : null
    const canRoutes = typeof ROUTES_AREA === 'string'
    const canNav = typeof SIDEBAR_NAV_AREA === 'string'

    if (!canRoutes || !canNav) {
      host.notify?.({
        kind: 'warning',
        message: 'Hire a Bot needs a newer Desktop for its sidebar page. Chat /hireabot still works.'
      })
      // Still try a palette entry if available so something is reachable.
      if (typeof PALETTE_AREA === 'string') {
        ctx.register({
          id: 'open-fallback',
          area: PALETTE_AREA,
          data: {
            id: 'hireabot.open',
            label: 'Open Hire a Bot',
            keywords: ['hire', 'bot', 'catalog', 'hireabot'],
            run: () =>
              host.notify?.({
                kind: 'info',
                message: 'Hire a Bot page needs a newer Desktop. Use /hireabot in chat.'
              })
          }
        })
      }
      return
    }

    ctx.registerMany([
      {
        id: 'page',
        area: ROUTES_AREA,
        data: { path: PATH },
        render: () => jsx(HireabotPage, { rest })
      },
      {
        id: 'nav',
        area: SIDEBAR_NAV_AREA,
        order: 55,
        data: { path: PATH, label: 'Hire a Bot', codicon: 'person-add' }
      }
    ])

    if (typeof PALETTE_AREA === 'string') {
      ctx.register({
        id: 'open',
        area: PALETTE_AREA,
        data: {
          id: 'hireabot.open',
          label: 'Open Hire a Bot',
          keywords: ['hire', 'bot', 'catalog', 'hireabot', 'install'],
          run: () => host.navigate(PATH)
        }
      })
    }

    ctx.registerSettingsPage?.({
      id: 'settings',
      title: 'Hire a Bot',
      icon: 'person-add',
      render: () =>
        jsxs('div', {
          className: 'flex flex-col gap-2 p-1 text-sm',
          children: [
            jsx('div', {
              className: 'text-(--ui-text-secondary)',
              children: 'Browse and hire ready-made Hermes bots from the sidebar Hire a Bot section.'
            }),
            jsx(Button, {
              size: 'sm',
              onClick: () => host.navigate(PATH),
              children: 'Open Hire a Bot'
            })
          ]
        })
    })
  }
}
