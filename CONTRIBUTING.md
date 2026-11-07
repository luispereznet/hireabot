# Submit your bot to Hireabot

Built a useful bot? You are welcome to propose it for the catalog. Contributing is optional and never required to build or use a bot. Bot Designer can help you build first.

## Submit in five steps

1. Build your bot, with Bot Designer's help if useful.
2. Prepare a public repository containing a loadable Hermes plugin and choose its full 40-character commit SHA.
3. Pass `audit_bot.py`, validation, and doctor for that commit before opening a PR.
4. Write the plain-language disclosures and check results listed below.
5. Open a PR to Hireabot for Luis's review before catalog inclusion.

## Prepare a new contribution

Your bot must live in a public repository as a loadable Hermes plugin. Pin the submission to a full 40-character Git commit SHA, not a branch, tag, or short SHA. Submit only content you have the right to share, with no credentials, personal memories, sessions, or other private data.

These requirements apply to new contributions. Existing catalog profile archives are not automatically loadable plugins. Bot Designer output may need further packaging work; there is no automatic conversion promised here.

From the local checkout of your plugin at the exact commit you plan to submit, run:

```bash
hermes plugins validate "$PWD" --install-deps
hermes plugins doctor "$PWD" --ci
```

Both checks must pass. Save their results, including exit codes and any warnings.

## Keep your bot safe and ready for review

Please follow these requirements:

- No deleting files.
- No spending money without asking the user.
- No pasting secrets.
- No hidden network calls.
- No impersonating real people or brands.
- No collecting personal data without disclosing it.
- No hardcoded keys or credentials.
- Every submission must pass `audit_bot.py` before opening a PR. Broken bots must not reach review.

The audit is a separate submission gate, in addition to validation and doctor. Include its results for the pinned commit. Validation and doctor do not replace the audit or prove that every policy behavior is safe. No public download location for `audit_bot.py` is established in this guide. If you do not have the required audit tool and instructions, the submission must wait until those are available and the audit passes.

## Open a submission PR

For your pull request to [luispereznet/hireabot](https://github.com/luispereznet/hireabot), describe these six required fields in plain-language Markdown, so someone who cannot read code understands what they would install:

1. Bot name.
2. A short description of what the bot does.
3. End intent: what the installing user will do with it and the intended result.
4. Every included skill and the purpose of each. Say "none" if there are no included skills.
5. Every included script and the purpose of each. Say "none" if there are no included scripts.
6. Whether any included skill supports becoming a runnable script after installation. Identify each supported skill and the resulting script's purpose, or say "none". Any supported conversion must be an optional choice the installing user can accept or decline, never automatic. Do not imply that all skills support conversion.

This is a disclosure requirement, not a request to implement conversion. Use prose or lists, not code or JSON, for these descriptions. Explain the contents and choices before installation.

Also include:

- Its public repository URL and full 40-character pinned commit SHA.
- The audit, validation, and doctor commands, results, exit codes, and any warnings for that commit.

Luis reviews submissions before catalog inclusion. A submission is not a promise of acceptance.

Nothing is published or submitted automatically. Making a repository public is a contributor prerequisite, not permission for an assistant to publish it. Ask for explicit approval before any assistant publishes, uploads, or opens a submission PR on your behalf.
