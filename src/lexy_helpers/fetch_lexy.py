from bs4 import BeautifulSoup
import requests
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TimeRemainingColumn,
    TextColumn,
    TaskProgressColumn,
)
import json
import re
import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import click


class LexyScraper:
    def __init__(self):
        self.homedir = Path.home()
        self.lexy_dir = self.homedir / ".config/lexy"
        self.log_path = self.lexy_dir / "log"
        self.file_path = self.lexy_dir / "files"
        self.json_path = self.lexy_dir / "json"
        self.XNY_URL = "https://learnxinyminutes.com"
        self.session = requests.Session()
        self.soup = None
        self.languages = []
        self.pattern = r"\.[\w]+"
        self.force = False
        self.languages_list = []
        self.update_interval_days = 60
        self._create_mapping()

    def _load_languages_from_json(self):
        try:
            with open(self.json_path / "languages.json", "r", encoding="utf-8") as f:
                self.languages_list = json.load(f)
            return True
        except FileNotFoundError:
            return False

    def fetch_language(self):
        if self._load_languages_from_json() and not self.force:
            return
        try:
            response = self.session.get(self.XNY_URL, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return click.secho(
                "No internet connection and no cached languages found.", fg="red"
            )

        self.soup = BeautifulSoup(response.text, "html.parser")
        self.languages = self.soup.select("tr td.name a")

        def process_language(language):
            language_name = language.text.strip()
            if not language.get("href") or language_name == "AWK":
                return None
            try:
                language_url = language.get("href")
                language_full_url = self.XNY_URL + language_url
                language_response = self.session.get(language_full_url)
                language_soup = BeautifulSoup(language_response.text, "html.parser")
                language_file = language_soup.select("p.filelink a")
                language_file_url = language_file[0].get("href")
                file_extension = re.search(self.pattern, language_file_url).group()
                language_file_full_url = self.XNY_URL + language_file_url
                language_dict = {
                    "language": language_name,
                    "language_url": language_full_url,
                    "language_file_url": language_file_full_url,
                    "file_extension": file_extension,
                }
                return (
                    language_dict,
                    language_file_full_url,
                    file_extension,
                    language_name,
                )
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [
                executor.submit(process_language, lang) for lang in self.languages
            ]

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
            ) as progress:
                task = progress.add_task(
                    "[cyan]Fetching languages...", total=len(futures)
                )

                for future in as_completed(futures):
                    result = future.result()
                    progress.update(task, advance=1)

                    if result:
                        lang_dict, file_url, extension, name = result
                        if self.force or name not in [
                            lang["language"] for lang in self.languages_list
                        ]:
                            self.languages_list.append(lang_dict)
                            self.create_file(file_url, extension, name)

        self.save_to_json()
        self.create_log()

    def save_to_json(self):
        with open(f"{self.json_path}/languages.json", "w", encoding="utf-8") as f:
            json.dump(self.languages_list, f, indent=4)

    def create_file(self, language_full_file_url, file_extension, language_name):
        content_response = self.session.get(language_full_file_url)
        content_soup = BeautifulSoup(content_response.text, "html.parser")
        with open(f"{self.file_path}/{language_name}{file_extension}", "w", encoding="utf-8") as file:
            file.write(content_soup.text)

    def auto_update(self):
        today = datetime.date.today()
        self._create_mapping()
        try:
            with open(f"{self.log_path}/last_update.txt", "r", encoding="utf-8") as file:
                last_update = file.read()
                days_since_last_update = (
                    today - datetime.datetime.strptime(last_update, "%Y-%m-%d").date()
                ).days
                if days_since_last_update >= self.update_interval_days:
                    self.fetch_language()
        except FileNotFoundError:
            self.fetch_language()
            self.create_log()

    def force_update(self):
        self.force = True
        self.fetch_language()
        with open(f"{self.log_path}/last_update.txt", "w", encoding="utf-8") as file:
            file.write(str(datetime.date.today()))
        self.force = False

    def create_log(self):
        today = datetime.date.today()
        with open(f"{self.log_path}/last_update.txt", "w", encoding="utf-8") as file:
            file.write(str(today))

    def last_modified(self):
        try:
            with open(f"{self.log_path}/last_update.txt", "r", encoding="utf-8") as file:
                last_update = file.read()
                last_update = datetime.datetime.strptime(last_update, "%Y-%m-%d").date()
                last_update = last_update.strftime("%d.%m.%Y")
                return last_update
        except FileNotFoundError:
            return None

    def _create_mapping(self):
        self.lexy_dir.mkdir(exist_ok=True)
        self.log_path.mkdir(exist_ok=True)
        self.file_path.mkdir(exist_ok=True)
        self.json_path.mkdir(exist_ok=True)


if __name__ == "__main__":
    lexy_scraper = LexyScraper()
    lexy_scraper.force_update()
