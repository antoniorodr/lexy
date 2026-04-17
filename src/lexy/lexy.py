from lexy_helpers.fetch_lexy import LexyScraper, LanguageData
from lexy_helpers.output_helpers import LexyFinder, LexyInit
import click
import json


@click.command()
@click.version_option()
@click.argument("language", metavar="<LANGUAGE>")
def lexy(language: str) -> None:
    """Display <LANGUAGE> documentation using bat.

    <LANGUAGE> refers to the language name or the following options:

    - Use "list" to view all available languages.

    - Use "update" to force update Lexy.

    - Use "modified" to view the last modified date of Lexy.

    - Use "editor" to set up your default editor for viewing documentation.
    """
    lexy_scraper: LexyScraper = LexyScraper()
    lexy_init: LexyInit = LexyInit(lexy_scraper)
    lexy_init.ensure_languages_file()
    lexy_scraper.auto_update()
    language_lower: str = language.lower()
    with open(f"{lexy_scraper.json_path}/languages.json", "r", encoding="utf-8") as f:
        languages: list[LanguageData] = json.load(f)
        lexy_finder: LexyFinder = LexyFinder(languages, lexy_scraper)
        match language_lower:
            case "list":
                lexy_finder.get_language()
            case "update":
                lexy_scraper.force_update()
            case "modified":
                last_modified: str | None = lexy_scraper.last_modified()
                click.echo(f"The most recent update to Lexy was on: {last_modified}")
            case "editor":
                click.echo(
                    f"\nYour current default editor is set to {lexy_finder.editor}\n"
                )
                if click.confirm("Do you want to change it?", abort=True):
                    lexy_init.default_editor_setup()
            case _:
                lexy_finder.language_finder(language_lower)
