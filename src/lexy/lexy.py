from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.output_helpers import LexyFinder, LexyInit
import click
import json

lexy_scraper = LexyScraper()


@click.command()
@click.version_option()
@click.argument("language", metavar="<LANGUAGE>")
def lexy(language):
    """Display <LANGUAGE> documentation using bat.

    <LANGUAGE> refers to the language name or the following options:

    - Use "list" to view all available languages.

    - Use "update" to force update Lexy.

    - Use "modified" to view the last modified date of Lexy.
    """
    LexyInit(lexy_scraper).ensure_languages_file()
    lexy_scraper.auto_update()
    language = language.lower()
    with open(f"{lexy_scraper.json_path}/languages.json", "r") as f:
        languages = json.load(f)
        lexy_finder = LexyFinder(language, languages, lexy_scraper)
        if language == "list":
            lexy_finder._get_language()
        elif language == "update":
            lexy_scraper.force_update()
        elif language == "modified":
            last_modified = lexy_scraper.last_modified()
            click.echo(f"The last time Lexy was updated is: {last_modified}")
        else:
            lexy_finder.language_finder()
