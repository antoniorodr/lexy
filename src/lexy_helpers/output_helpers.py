import subprocess
import os
import click
from lexy_helpers.fetch_lexy import LexyScraper
from pathlib import Path


class LexyFinder:
    def __init__(self, language: str, languages: list, lexy: LexyScraper):
        self.language = language
        self.languages = languages
        self.lexy = lexy
        self.homedir = Path.home()
        self.directory = self.homedir / ".config/lexy/files"

    def language_finder(self):
        file_path = self.lexy.file_path
        if not any(
            self.language.lower() == d["language"].lower() for d in self.languages
        ):
            click.secho(f"Language {self.language} not found", fg="red")
            return exit(1)
        for lang in self.languages:
            language_name = lang["language"].lower()
            language_file = lang["language"] + lang["file_extension"]
            if language_name == self.language:
                with open(f"{file_path}/{language_file}", "r") as file:
                    full_path = os.path.abspath(file.name)
                    subprocess.run(["bat", full_path])

    def _get_language(self):
        fzf_command = r"""
        fzf --style=full \
        --border --padding=1,2 \
        --info=inline \
        --border-label=' Enter: Open with bat │ Ctrl-D/U: scroll preview ' \
        --input-label=' Input ' \
        --preview='bat --style=plain --color=always {}' \
        --preview-window=right:60%:wrap:cycle \
        --bind='ctrl-d:preview-down' \
        --bind='ctrl-u:preview-up' \
        --bind='enter:execute(bat {})' \
        --bind='result:transform-list-label:
            if [[ -z $FZF_QUERY ]]; then
            echo " $FZF_MATCH_COUNT items "
            else
            echo " $FZF_MATCH_COUNT matches for [$FZF_QUERY] "
            fi' \
        --bind='focus:transform-preview-label:[[ -n {} ]] && printf " Previewing [%s] " {}' \
        --bind='focus:+transform-header:file --brief {} || echo "No file selected"' \
        --color='border:#aaaaaa,label:#cccccc' \
        --color='preview-border:#9999cc,preview-label:#ccccff' \
        --color='list-border:#669966,list-label:#99cc99' \
        --color='input-border:#996666,input-label:#ffcccc' \
        --color='header-border:#6699cc'
        """
        subprocess.run(fzf_command, shell=True, cwd=self.directory)


class LexyInit:
    def __init__(self, lexy: LexyScraper):
        self.lexy = lexy

    def ensure_languages_file(self):
        json_path = self.lexy.json_path
        if not json_path.exists():
            self.lexy.fetch_language()
