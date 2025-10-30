from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.output_helpers import LexyFinder, LexyInit
import click
import json


@click.command()
@click.version_option()
@click.argument("language", metavar="<LANGUAGE>")
def lexy(language):
    """Display <LANGUAGE> documentation using bat.

    <LANGUAGE> refers to the language name or the following options:

    - Use "list" to view all available languages.

    - Use "update" to force update Lexy.

    - Use "modified" to view the last modified date of Lexy.

    - Use "editor" to set up your default editor for viewing documentation.
    """
    lexy_scraper = LexyScraper()
    lexy_init = LexyInit(lexy_scraper)
    lexy_init.ensure_languages_file()
    lexy_scraper.auto_update()
    language = language.lower()
    with open(f"{lexy_scraper.json_path}/languages.json", "r", encoding="utf-8") as f:
        languages = json.load(f)
        lexy_finder = LexyFinder(languages, lexy_scraper)
        match language:
            case "list":
                lexy_finder.get_language()
            case "update":
                lexy_scraper.force_update()
            case "modified":
                last_modified = lexy_scraper.last_modified()
                click.echo(f"The most recent update to Lexy was on: {last_modified}")
            case "editor":
                click.echo(
                    f"\nYour current default editor is set to {lexy_finder.editor}\n"
                )
                if click.confirm("Do you want to change it?", abort=True):
                    lexy_init.default_editor_setup()
            case _:
                lexy_finder.language_finder(language)
