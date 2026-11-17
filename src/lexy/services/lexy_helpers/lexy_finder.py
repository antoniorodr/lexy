import os
import subprocess
from pathlib import Path

import click

from lexy.services.config.config_services import ConfigServices
from lexy.services.requests.lexy_scraper import LanguageData, LexyScraper


class LexyFinder:
    def __init__(self, languages: list[LanguageData], lexy: LexyScraper) -> None:
        self.available_languages: list[LanguageData] = languages
        self.scraper: LexyScraper = lexy
        self.homedir: Path = Path.home()
        self.directory: Path = self.homedir / ".config/lexy/files"
        self.config = ConfigServices.load_config()
        self.editor: str = self.config.get("editor", {}).get("default_editor", "bat")

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
                    ["nvim", "-R", "-c", "lua vim.diagnostic.enable(false)", full_path]
                )
                return
            subprocess.run([self.editor, full_path])

    def get_language(self):
        fzf_command = ConfigServices.build_fzf_command(self.config)
        subprocess.run(fzf_command, shell=True, cwd=self.directory)

    def _get_from_available_languages(self, requested_lang):
        for lang in self.available_languages:
            if requested_lang == lang["language"].lower():
                return lang

        return None
