import subprocess
import os
import click
from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.config import load_config, build_fzf_command, change_default_editor
from pathlib import Path


class LexyFinder:
    def __init__(self, languages: list, lexy: LexyScraper):
        self.available_languages = languages
        self.scraper = lexy
        self.homedir = Path.home()
        self.directory = self.homedir / ".config/lexy/files"
        self.config = load_config()
        self.editor = self.config.get("editor", {}).get("default_editor", "bat")

        if self.editor not in ["bat", "nvim"]:
            click.secho(
                f"Editor '{self.editor}' is not supported. Falling back to 'bat'.",
                fg="yellow",
            )
            self.editor = "bat"

    def language_finder(self, language: str):
        language = language.lower()
        file_path = self.scraper.file_path
        found_language = self._get_from_available_languages(language)

        if not found_language:
            click.secho(f"Language {language} not found", fg="red")
            return exit(1)

        with open(
            f"{file_path}/{found_language['language']}{found_language['file_extension']}",
            "r",
            encoding="utf-8",
        ) as file:
            full_path = os.path.abspath(file.name)
            if self.editor == "nvim":
                subprocess.run(
                    ["nvim", "-R", "-c", "lua vim.diagnostic.disable()", full_path]
                )
                return
            subprocess.run([self.editor, full_path])

    def get_language(self):
        fzf_command = build_fzf_command(self.config)
        subprocess.run(fzf_command, shell=True, cwd=self.directory)

    def _get_from_available_languages(self, requested_lang):
        for lang in self.available_languages:
            if requested_lang == lang["language"].lower():
                return lang

        return None


class LexyInit:
    def __init__(self, lexy: LexyScraper):
        self.lexy = lexy

    def ensure_languages_file(self):
        json_path = self.lexy.json_path
        if not json_path.exists():
            self.lexy.fetch_language()

    def default_editor_setup(self):
        changed = False
        while not changed:
            click.echo("\nPlease, choose your preferred editor:")
            click.echo("===================================")
            click.echo("1. bat (default)")
            click.echo("2. nvim (read-only mode)")
            choice = click.prompt("\nEnter the number of your choice", type=int)

            if choice == 1:
                change_default_editor("bat")
                changed = True
                click.secho(
                    "\nDefault editor set to 'bat'.",
                    fg="green",
                )
            elif choice == 2:
                change_default_editor("nvim")
                changed = True
                click.secho(
                    "\nDefault editor set to 'nvim'.",
                    fg="green",
                )
            else:
                click.secho("\nInvalid choice. Please try again.", fg="red")
