# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2019-12-29
### Added
- Added CHANGELOG.md file.
- Added "-m" argument to give matrix name list from command line.
- Added "-v" argument to print the current version number.

### Changed
- Changed verbose mode argument from "-v" to "-V".
- Rewrite the method for reading matrix names. Renamed as "read_matrix_names".
- Changed verbose mode. Now logger output is only visible if verbose mode
is activated.

### Fixed
- Fixed successful logging even there were errors.

### Removed
- Removed Todo list from README.md