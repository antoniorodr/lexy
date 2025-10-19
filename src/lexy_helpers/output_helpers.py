import subprocess
import os
import click
from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.config import load_config, build_fzf_command
from pathlib import Path


class LexyFinder:
    def __init__(self, languages: list, lexy: LexyScraper):
        self.available_languages = languages
        self.scraper = lexy
        self.homedir = Path.home()
        self.directory = self.homedir / ".config/lexy/files"

    def language_finder(self, language: str):
        language = language.lower()
        file_path = self.scraper.file_path
        found_language = self._get_from_available_languages(language)

        if not found_language:
            click.secho(f"Language {language} not found", fg="red")
            return exit(1)

        with open(
            f"{file_path}/{found_language["language"]}{found_language["file_extension"]}",
            "r", encoding="utf-8"
        ) as file:
            full_path = os.path.abspath(file.name)
            subprocess.run(["bat", full_path])

    def get_language(self):
        config = load_config()
        fzf_command = build_fzf_command(config)
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
