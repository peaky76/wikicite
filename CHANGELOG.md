# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] (2023-10-16)

#### New Features

- allow book as a cite type

#### Refactorings

- split `book/news/web` into different fns
- extract shared options and functions
- make `source` an option not and argument
- make sources file `toml` not `yaml`

#### Others

- add `prep.sh`
- fix failing `test_basic_full_citation`

## [0.1.4] - 2023-01-28

### Fixed

- `os` based referencing of `sources.yaml`

## [0.1.3] - 2023-01-28

### Fixed

- Correct referencing of `sources.yaml`

## [0.1.2] - 2023-01-28

### Fixed

- Ensure `sources.yaml` is packaged

## [0.1.1] - 2023-01-28

### Fixed

- Replace `sources_default.yaml` with `sources.yaml` for correct referencing when installed. This removes the intended way of configuring sources. Configuration will be reinstated in later releases.

## [0.1.0.post1] - 2023-01-28

### Fixed

- Correct pypi link and version number in README

## [0.1.0] - 2023-01-28

### Added

- `wikicite` cli with options for title, author, url and date
