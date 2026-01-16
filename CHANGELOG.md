# Changelog

All notable changes to this project will be documented in this file.

## [0.5.2] - 16.01.2026

### Fixed

- Fixed a bug where Lexy did not auto-update each 60 days

## [0.5.1] - 30.10.2025

### Fixed

- Fixed a bug with the default configuration file creation on first run.

## [0.5.0] - 30.10.2025

### Added

- Lexy will now create the `config.toml` with the default values the first time it runs. This file is located in `~/.config/lexy/`.
- The `default editor` is still `bat`, but now it's possible to change it to `nvim` using the `Lexy editor` command. This closes #11.

## [0.4.6] - 19.10.2025

### Added

- New test to verify that `lexy list` works correctly.

### Changed

- Modified some `fzf` options to follow best practices and improve user experience.
- Refactored some code to improve readability and maintainability.

Thanks @Ajmal30 for the improvements!

## [0.4.5] - 25.08.2025

### Changed

- Improved the error message shown by `lexy update` when no internet connection is available, making it clearer for users.

## [0.4.4] - 24.08.2025

### Fixed

- Fixed a bug where Lexy was not able to open the files cashed when offline.

## [0.4.3] - 01.08.2025

### Changed

- Refactored `LexyFinder` to simplify logic:
    - Removed multiple iterations through languages.
    - Renamed some parameters for improved readability.

Thanks @AndreBonda for the refactoring!

## [0.4.2] - 31.07.2025

### Added

- Possibility to customize the theme of the fzf window.

### Changed

- Created documentation for the theming

## [0.4.1] - 29.05.2025

### Fixed

- Fixed a bug where Lexy was not able to create the path on windows.

## [0.4.0] - 26.05.2025

### Changed

- Refactored the code to improve readability and maintainability.
- Implementation of asynchronous execution to significantly enhance performance during documentation retrieval.

## [0.3.2] - 21.05.2025

### Changed

- Refactored the lexy command to use match case instead of if statements for better readability.

### Fixed

- Resolved the issue where lexy needed Hatchling to be built, when Lexy is not using it at the moment.

## [0.3.1] - 07.05.2025

### Changed

- Refactored the code to improve readability and maintainability.
- Small changes to the fzf configuration to improve the user experience.

## [0.3.0] - 05.05.2025

### Added

- Added support to fuzzy search when using the 'list' argument.
- Created documentation using Material for MkDocs.You can find it [here](https://antoniorodr.github.io/lexy/).

### Changed

- Updated the README file to include information about the new fuzzy search feature.

## [0.2.0] - 02.05.2025

### Added

- Added test for the `lexy` command to ensure it works as expected.
- Added "last_modified" function to the LaxyScraper class to allow the "modified" argument to work.
- Added the argument "modified" to check the last update date of the local copy.

### Changed

- Refactored the some code to improve readability and maintainability.
- Updated the README file to include information about the new "modified" argument.

### Fixed

- Resolved an issue where Lexy failed to produce any output when an invalid argument was provided.

## [0.1.0] - 29.04.2025

Initial Release.

### Added

Initial release with the following features:

- Check documentation from "Learn X in Y minutes" directly from the terminal
- Syntax highlighting using [bat](https://github.com/sharkdp/bat)
- Local copy to speed up the process and avoid too many requests to the "Learn X in Y minutes" server
- Auto-update every 60 days

[0.5.2]: https://github.com/antoniorodr/lexy/releases/tag/v0.5.2
[0.5.1]: https://github.com/antoniorodr/lexy/releases/tag/v0.5.1
[0.5.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.5.0
[0.4.6]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.6
[0.4.5]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.5
[0.4.4]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.4
[0.4.3]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.3
[0.4.2]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.2
[0.4.1]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.1
[0.4.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.4.0
[0.3.2]: https://github.com/antoniorodr/lexy/releases/tag/v0.3.2
[0.3.1]: https://github.com/antoniorodr/lexy/releases/tag/v0.3.1
[0.3.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.3.0
[0.2.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.2.0
[0.1.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.1.0
