# WikiTech Builders practice repository

Practice repository for the Masterclass 3 hands-on (WikiTech Builders Programme 2026).

1. Fork this repository on GitHub.
2. Edit `CONTRIBUTORS.md` and add a single line in this format: `Name - Wikimedia username - one tool idea`.
3. Commit your change with a short message, for example `Add Ada Okafor to contributors`.
4. Open a Pull Request against `main`.
5. Check the GitHub Actions CI status. If it fails, fix your line and push the update to your branch.

Run the check yourself: `python check_contributors.py`

This repository is released under the MIT License. Everything here may be reused under its terms.

## Live repository dashboard

The [WTB Practice dashboard](https://devjadiya.github.io/wtb-practice/) shows open pull requests and recent GitHub Actions runs. It reads public repository data from the GitHub API and refreshes automatically. Try the [Pipeline Lab](https://devjadiya.github.io/wtb-practice/lab/) to safely simulate a change moving through Gerrit, GitLab, or GitHub CI. Use GitHub's [Watch settings](https://github.com/devjadiya/wtb-practice/subscription) to subscribe to repository notifications.

To publish the dashboard, enable **Settings → Pages → Build and deployment → Source: GitHub Actions**. The `Deploy dashboard` workflow publishes the contents of `site/` from `main`.
