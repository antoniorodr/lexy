import click

from lexy.services.config.config_services import ConfigServices
from lexy.services.requests.lexy_scraper import LexyScraper


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
                ConfigServices.change_default_editor("bat")
                changed = True
                click.secho(
                    "\nDefault editor set to 'bat'.",
                    fg="green",
                )
            elif choice == 2:
                ConfigServices.change_default_editor("nvim")
                changed = True
                click.secho(
                    "\nDefault editor set to 'nvim'.",
                    fg="green",
                )
            else:
                click.secho("\nInvalid choice. Please try again.", fg="red")
