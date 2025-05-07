# Changelog

All notable changes to this project will be documented in this file.

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

[0.3.1]: https://github.com/antoniorodr/lexy/releases/tag/v0.3.1
[0.3.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.3.0
[0.2.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.2.0
[0.1.0]: https://github.com/antoniorodr/lexy/releases/tag/v0.1.0
