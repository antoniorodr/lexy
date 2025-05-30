<div align="center" id="top">
  <img height=200px src="./.github/lexy.png" alt="lexy" />

&#xa0;

</div>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/antoniorodr/lexy?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/antoniorodr/lexy?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/antoniorodr/lexy?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/antoniorodr/lexy?color=56BEB8">

  <img alt="Github issues" src="https://img.shields.io/github/issues/antoniorodr/lexy?color=56BEB8" />

  <img alt="Github forks" src="https://img.shields.io/github/forks/antoniorodr/lexy?color=56BEB8" />

  <img alt="Github stars" src="https://img.shields.io/github/stars/antoniorodr/lexy?color=56BEB8" />
</p>

 <h4 align="center">
 🚧  lexy 🚀 Under developing...  🚧
</h4>

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#computer-demo">Demo</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-installation">Installation</a> &#xa0; | &#xa0;
  <a href="#bookmark_tabs-documentation">Documentation</a> &#xa0; | &#xa0;
  <a href="#lexy-license">License</a>
</p>

<br>

## :dart: About

**Lexy** is a lightweight CLI tool that fetches programming tutorials from [Learn X in Y Minutes](https://learnxinyminutes.com) directly into your terminal. Quickly search, learn, and reference code examples without leaving your workflow.

Lexy saves a local copy of the documentation, so you can access it even when you're offline. It also provides syntax highlighting using [bat](https://github.com/sharkdp/bat) and fuzzy search using [fzf](https://github.com/junegunn/fzf).

This project would not be possible without the amazing work of the [Learn X in Y Minutes](https://github.com/adambard/learnxinyminutes-docs) community. A huge thanks to all contributors for making high-quality learning resources freely available!

## :computer: Demo

[![asciicast](https://asciinema.org/a/717362.svg)](https://asciinema.org/a/717362)

## :sparkles: Features

:heavy_check_mark: Check documentation from "Learn X in Y minutes" directly from the terminal\
:heavy_check_mark: Syntax highlighting using [bat](https://github.com/sharkdp/bat)\
:heavy_check_mark: Local copy to speed up the process and avoid too many requests to the "Learn X in Y minutes" server\
:heavy_check_mark: Auto-update every 60 days\
:heavy_check_mark: Searching powered by [fzf](https://github.com/junegunn/fzf)

## :rocket: Technologies

The following tools were used in this project:

- [Click](https://click.palletsprojects.com/en/stable/)
- [Typer](https://typer.tiangolo.com)
- [Beautifulsoup](https://pypi.org/project/beautifulsoup4/)
- [fzf](https://github.com/junegunn/fzf)
- [bat](https://github.com/sharkdp/bat)

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [bat](https://github.com/sharkdp/bat) and [fzf](https://github.com/junegunn/fzf) installed.

## :checkered_flag: Installation

#### Manual Installation

```bash
git clone https://github.com/antoniorodr/lexy

cd lexy

pip install .
```

#### Homebrew Installation

```bash
brew tap antoniorodr/lexy
brew install antoniorodr/lexy/lexy
```

#### AUR Installation

```bash
yay -S lexy
```

#### Installation using [uv](https://docs.astral.sh/uv/)

```bash
uv tool install git+https://github.com/antoniorodr/lexy
```

## :bookmark_tabs: Documentation

First, make sure you have [bat](https://github.com/sharkdp/bat) and [fzf](https://github.com/junegunn/fzf) installed. Lexy requires it for syntax highlighting and searching.

You can use the command `lexy --help` to see all available options.

```bash
lexy --help
Usage: lexy [OPTIONS] <LANGUAGE>

  Display <LANGUAGE> documentation using bat.

  <LANGUAGE> refers to the language name or the following options:

  - Use "list" to view all available languages.

  - Use "update" to force update Lexy.

  - Use "modified" to view the last modified date of Lexy.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

Lexy keeps a local copy of the documentation in `$HOME/.config/lexy`, which is created automatically the first time you run Lexy, and it will be updated every 60 days. You can force an update using "update" as `<LANGUAGE>`.

You can find the full documentation [here](https://antoniorodr.github.io/lexy/).

## :memo: License

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

## :eyes: Do you like my work?

<a href="https://www.buymeacoffee.com/antoniorodr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-white.png" alt="Buy Me A Coffee" height="48"></a>

Made with :heart: by <a href="https://github.com/antoniorodr" target="_blank">Antonio Rodriguez</a>

&#xa0;

<a href="#top">Back to top</a>
