# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.4] - 10.11.2026

### Changed
- Bump project version
- Merge pull request #24 from antoniorodr/dependabot/uv/certifi-2026.10.18 by @antoniorodr in [#24](https://github.com/antoniorodr/lexy/pull/24)
- Bump certifi from 2026.2.25 to 2026.10.18 by @dependabot[bot]
- Merge pull request #23 from antoniorodr/dependabot/uv/urllib3-2.8.0 by @antoniorodr in [#23](https://github.com/antoniorodr/lexy/pull/23)
- Bump urllib3 from 2.7.0 to 2.8.0 by @dependabot[bot]
- Merge pull request #21 from antoniorodr/dependabot/uv/pymdown-extensions-11.0.1 by @antoniorodr in [#21](https://github.com/antoniorodr/lexy/pull/21)
- Bump pymdown-extensions from 11.0 to 11.0.1 by @dependabot[bot]
- Merge pull request #20 from antoniorodr/dependabot/uv/pymdown-extensions-11.0 by @antoniorodr in [#20](https://github.com/antoniorodr/lexy/pull/20)
- Bump pymdown-extensions from 10.21.3 to 11.0 by @dependabot[bot]
- Merge pull request #19 from antoniorodr/dependabot/uv/soupsieve-2.8.4 by @antoniorodr in [#19](https://github.com/antoniorodr/lexy/pull/19)
- Bump soupsieve from 2.8.3 to 2.8.4 by @dependabot[bot]
- Merge pull request #15 from antoniorodr/dependabot/uv/idna-3.15 by @antoniorodr in [#15](https://github.com/antoniorodr/lexy/pull/15)
- Bump idna from 3.11 to 3.15 by @dependabot[bot]
- Merge pull request #16 from antoniorodr/dependabot/uv/pymdown-extensions-10.21.3 by @antoniorodr in [#16](https://github.com/antoniorodr/lexy/pull/16)
- Bump pymdown-extensions from 10.21.2 to 10.21.3 by @dependabot[bot]
- Merge pull request #14 from antoniorodr/dependabot/uv/urllib3-2.7.0 by @antoniorodr in [#14](https://github.com/antoniorodr/lexy/pull/14)
- Bump urllib3 from 2.6.3 to 2.7.0 by @dependabot[bot]
- Update feil mirror workflow by @antoniorodr
- Update docs and mirror workflows by @antoniorodr
- Update tests workflow by @antoniorodr
- Update cliff config by @antoniorodr
- Untrack site folder by @antoniorodr
- Update changelog with last version by @antoniorodr

### Fixed
- Handle missing directory in fetch_lexy helper

### New Contributors
* @dependabot[bot] made their first contribution

## [0.6.3] - 21.04.2026

### Added
- Add type annotation to load_config by @antoniorodr

### Changed
- Update version by @antoniorodr
- Start tracking the file by @antoniorodr
- Substitute mkdocs.yml for zensical.toml by @antoniorodr
- Update docs workflow with workflow_dispatch by @antoniorodr
- Update release workflow by @antoniorodr
- Update changelog with last version by @antoniorodr

### Removed
- Remove code which avoided create awk docs by @antoniorodr
- Remove uv.lock and add site folder by @antoniorodr

## [0.6.2] - 19.04.2026

### Changed
- Create changelog using git-cliff by @antoniorodr
- Update release workflow to use git-cliff by @antoniorodr

## [0.6.1] - 17.04.2026

### Added
- Add typing to all files, where possible by @antoniorodr
- Add lexy.nvim to the readme by @antoniorodr
- Add stale workflow by @antoniorodr

### Changed
- Merge branch 'chore/update-dependencies' by @antoniorodr
- Update changelog with the last version by @antoniorodr
- Update gitignore by @antoniorodr
- Update dependencies to the last version by @antoniorodr
- Merge branch 'style/typing' by @antoniorodr
- Delete logo from readme by @antoniorodr
- Delete logo from assets by @antoniorodr
- Delete back to top from readme by @antoniorodr
- Adjust logo size by @antoniorodr
- Update license on pyproject by @antoniorodr
- Update logo size by @antoniorodr
- Update readme by @antoniorodr
- Update tests workflow by @antoniorodr
- Update readme by @antoniorodr
- Update license by @antoniorodr
- Update release workflow by @antoniorodr

### Fixed
- Fix typo by @antoniorodr

## [0.6.0] - 31.03.2026

### Changed
- Update changelog and pyproject for new version by @antoniorodr
- Improve fetching by @antoniorodr
- Merge pull request #13 from antoniorodr/fix/diagnostics_disable by @antoniorodr

## [0.5.4] - 31.03.2026

### Added
- Add agents.md for no autopilot workflow by @antoniorodr
- Add test yml for mirroring by @antoniorodr

### Changed
- Update changelog and pyproject for new version by @antoniorodr
- Change command to disable diagnostics on neovim by @antoniorodr
- Delete notify job from PR workflow by @antoniorodr
- Update mkdocs file by @antoniorodr
- Update pyproject by @antoniorodr
- Update contributing file by @antoniorodr
- Update gitignore by @antoniorodr
- Move tests from test/ to tests/ by @antoniorodr
- Update site with Zensical by @antoniorodr
- Create a few workflows for auto testing and release by @antoniorodr
- Undo license change. Back to MIT. by @antoniorodr
- Disable SSH host verification for mirror workflow by @antoniorodr
- Fix mirror workflow: use SSH authentication by @antoniorodr
- Update test yml by @antoniorodr
- Update test yml and LICENSE file by @antoniorodr
- Update test yml by @antoniorodr
- Update changelog by @antoniorodr

## [0.5.3] - 17.02.2026

### Added
- Add .editorconfig to the project by @antoniorodr
- Add new info in CONTRIBUTING.md file by @antoniorodr

### Changed
- Update dependencies by @antoniorodr
- Update changelog and pyproject by @antoniorodr

## [0.5.2] - 16.01.2026

### Changed
- Fix bug where Lexy did not autoupdate by @antoniorodr

## [0.5.1] - 30.10.2025

### Changed
- Fix a bug with the default config at first startup by @antoniorodr
- Update README by @antoniorodr

## [0.5.0] - 30.10.2025

### Added
- Add posibility to choose the default editor to open files by @antoniorodr

### Changed
- Change banner and demo folder path by @antoniorodr

## [0.4.6] - 19.10.2025

### Changed
- Refactoring and new test by @antoniorodr
- Merge pull request #10 from Ajmal30/lexy_update by @antoniorodr in [#10](https://github.com/antoniorodr/lexy/pull/10)
- Modified config.py and added unit test cases for lexy list by @Ajmal30
- Update sponsorship badget by @antoniorodr
- Update readme with sponsorship by @antoniorodr
- Update readme and pyproject by @antoniorodr
- Delete gitlab workflow by @antoniorodr
- Update gitlab workflow by @antoniorodr
- Update readme by @antoniorodr

### Fixed
- Fix workflow by @antoniorodr
- Fix documentation images by @antoniorodr

### New Contributors
* @Ajmal30 made their first contribution

## [0.4.5] - 25.08.2025

### Changed
- Change output lexy update command when offline by @antoniorodr

## [0.4.4] - 24.08.2025

### Changed
- Update changelog and pyproject files by @antoniorodr

### Fixed
- Fix offline bug by @antoniorodr

## [0.4.3] - 01.08.2025

### Added
- Add theming and update the documentation by @antoniorodr

### Changed
- Merge pull request #7 from AndreBonda/refactor_lexy_finder by @antoniorodr in [#7](https://github.com/antoniorodr/lexy/pull/7)
- Simplified finder logic removing multiple cycles on languages by @sbundaz

### Removed
- Remove space by @sbundaz

## [0.4.2] - 31.07.2025

### Added
- Testing commands on contributing md by @andresdanielmtz
- Usage docs by @andresdanielmtz
- Basic gitignore file by @andresdanielmtz
- Add workflow to sync with gitlab by @antoniorodr

### Changed
- Merge pull request #6 from AndreBonda/update_readme by @antoniorodr in [#6](https://github.com/antoniorodr/lexy/pull/6)
- Insert additional info in the readme by @sbundaz
- Merge pull request #5 from andresdanielmtz/documentation by @antoniorodr in [#5](https://github.com/antoniorodr/lexy/pull/5)

### Fixed
- Small markdown redirect by @andresdanielmtz

### New Contributors
* @sbundaz made their first contribution
* @andresdanielmtz made their first contribution

## [0.4.1] - 29.05.2025

### Changed
- Asynchronous execution implementation by @antoniorodr

### Fixed
- Fix a bug on windows by @antoniorodr

## [0.3.2] - 20.05.2025

### Changed
- Update lexy function to use match case by @antoniorodr
- Update uv installation by @antoniorodr
- Small code changes by @antoniorodr

## [0.3.0] - 05.05.2025

### Added
- Support fzf with 'list' argument by @antoniorodr

### Changed
- Create mkdocs docs. Release v0.3.0 by @antoniorodr

## [0.2.0] - 02.05.2025

### Added
- Added aur installation method by @blackthorne7

### Changed
- Release v0.2.0 by @antoniorodr
- Delete title from readme by @antoniorodr
- Merge pull request #2 from blackthorne7/add-aur-installation-docs by @antoniorodr in [#2](https://github.com/antoniorodr/lexy/pull/2)
- Update contributing by @antoniorodr
- Update readme by @antoniorodr
- Update issue templates by @antoniorodr
- Update issue templates by @antoniorodr
- Release v0.1.0 by @antoniorodr
- Prepare for release by @antoniorodr
- Start with cli commands by @antoniorodr
- First commit by @antoniorodr

### New Contributors
* @antoniorodr made their first contribution
* @blackthorne7 made their first contribution

[0.6.4]: https://github.com/antoniorodr/lexy/compare/v0.6.3...v0.6.4
[0.6.3]: https://github.com/antoniorodr/lexy/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/antoniorodr/lexy/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/antoniorodr/lexy/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/antoniorodr/lexy/compare/v0.5.4...v0.6.0
[0.5.4]: https://github.com/antoniorodr/lexy/compare/v0.5.3...v0.5.4
[0.5.3]: https://github.com/antoniorodr/lexy/compare/v0.5.2...v0.5.3
[0.5.2]: https://github.com/antoniorodr/lexy/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/antoniorodr/lexy/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/antoniorodr/lexy/compare/v0.4.6...v0.5.0
[0.4.6]: https://github.com/antoniorodr/lexy/compare/v0.4.5...v0.4.6
[0.4.5]: https://github.com/antoniorodr/lexy/compare/v0.4.4...v0.4.5
[0.4.4]: https://github.com/antoniorodr/lexy/compare/v0.4.3...v0.4.4
[0.4.3]: https://github.com/antoniorodr/lexy/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/antoniorodr/lexy/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/antoniorodr/lexy/compare/v0.3.2...v0.4.1
[0.3.2]: https://github.com/antoniorodr/lexy/compare/v0.3.0...v0.3.2
[0.3.0]: https://github.com/antoniorodr/lexy/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/antoniorodr/lexy/compare/v0.1.0...v0.2.0

<!-- generated by git-cliff -->
