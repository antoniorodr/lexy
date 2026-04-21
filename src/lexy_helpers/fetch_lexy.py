from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from concurrent.futures import Future
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TaskID,
    TimeRemainingColumn,
    TextColumn,
    TaskProgressColumn,
)
import json
import re
import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TypedDict
import click


class LanguageData(TypedDict):
    language: str
    language_url: str
    language_file_url: str
    file_extension: str


class LexyScraper:
    def __init__(self):
        self.homedir: Path = Path.home()
        self.lexy_dir: Path = self.homedir / ".config/lexy"
        self.log_path: Path = self.lexy_dir / "log"
        self.file_path: Path = self.lexy_dir / "files"
        self.json_path: Path = self.lexy_dir / "json"
        self.XNY_URL: str = "https://learnxinyminutes.com"
        self.session: requests.Session = requests.Session()
        self.soup: BeautifulSoup | None = None
        self.languages: list[Tag] = []
        self.pattern: str = r"\.[\w]+"
        self.force: bool = False
        self.languages_list: list[LanguageData] = []
        self.update_interval_days: int = 60
        self._create_mapping()

    def _load_languages_from_json(self) -> bool:
        try:
            with open(self.json_path / "languages.json", "r", encoding="utf-8") as f:
                self.languages_list = json.load(f)
            return True
        except FileNotFoundError:
            return False

    def _get_string_attribute(self, tag: Tag, attribute: str) -> str:
        value = tag.get(attribute)
        if not isinstance(value, str):
            raise ValueError(f"Expected '{attribute}' to be a string.")
        return value

    def fetch_language(self) -> None:
        if self._load_languages_from_json() and not self.force:
            return
        try:
            response: requests.Response = self.session.get(self.XNY_URL, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return click.secho(
                "No internet connection and no cached languages found.", fg="red"
            )

        self.soup = BeautifulSoup(response.text, "html.parser")
        self.languages = self.soup.select("tr td.name a")

        existing_names: set[str] = {lang["language"] for lang in self.languages_list}

        def process_language(language: Tag) -> LanguageData | None:
            language_name: str = str(language.get_text().strip())
            if not self.force and language_name in existing_names:
                return None
            try:
                language_url: str = self._get_string_attribute(language, "href")
                language_full_url: str = self.XNY_URL + language_url
                language_response: requests.Response = self.session.get(
                    language_full_url
                )
                language_response.raise_for_status()
                language_soup: BeautifulSoup = BeautifulSoup(
                    language_response.text, "html.parser"
                )
                language_file: Tag | None = language_soup.select_one("p.filelink a")
                if not isinstance(language_file, Tag):
                    raise ValueError("Missing language file link.")
                language_file_url: str = self._get_string_attribute(
                    language_file, "href"
                )
                file_extension_match: re.Match[str] | None = re.search(
                    self.pattern, language_file_url
                )
                if file_extension_match is None:
                    raise ValueError("Missing file extension in language file URL.")
                file_extension: str = file_extension_match.group()
                language_file_full_url: str = self.XNY_URL + language_file_url
                language_dict: LanguageData = {
                    "language": language_name,
                    "language_url": language_full_url,
                    "language_file_url": language_file_full_url,
                    "file_extension": file_extension,
                }
                self.create_file(language_file_full_url, file_extension, language_name)
                return language_dict
            except (requests.RequestException, ValueError):
                return None

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures: list[Future[LanguageData | None]] = [
                executor.submit(process_language, lang) for lang in self.languages
            ]

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
            ) as progress:
                task: TaskID = progress.add_task(
                    "[cyan]Fetching languages...", total=len(futures)
                )

                for future in as_completed(futures):
                    result: LanguageData | None = future.result()
                    progress.update(task, advance=1)

                    if result:
                        self.languages_list.append(result)

        self.save_to_json()
        self.create_log()

    def save_to_json(self) -> None:
        with open(f"{self.json_path}/languages.json", "w", encoding="utf-8") as f:
            json.dump(self.languages_list, f, indent=4)

    def create_file(
        self, language_full_file_url: str, file_extension: str, language_name: str
    ) -> None:
        content_response: requests.Response = self.session.get(language_full_file_url)
        content_response.raise_for_status()
        with open(
            f"{self.file_path}/{language_name}{file_extension}", "w", encoding="utf-8"
        ) as file:
            file.write(content_response.text)

    def auto_update(self) -> None:
        today: datetime.date = datetime.date.today()
        self._create_mapping()
        try:
            with open(
                f"{self.log_path}/last_update.txt", "r", encoding="utf-8"
            ) as file:
                last_update: str = file.read()
                days_since_last_update: int = (
                    today - datetime.datetime.strptime(last_update, "%Y-%m-%d").date()
                ).days
                if days_since_last_update >= self.update_interval_days:
                    self.force = True
                    self.fetch_language()
                    self.force = False
        except FileNotFoundError:
            self.force = True
            self.fetch_language()
            self.create_log()
            self.force = False

    def force_update(self) -> None:
        self.force = True
        self.fetch_language()
        with open(f"{self.log_path}/last_update.txt", "w", encoding="utf-8") as file:
            file.write(str(datetime.date.today()))
        self.force = False

    def create_log(self) -> None:
        today: datetime.date = datetime.date.today()
        with open(f"{self.log_path}/last_update.txt", "w", encoding="utf-8") as file:
            file.write(str(today))

    def last_modified(self) -> str | None:
        try:
            with open(
                f"{self.log_path}/last_update.txt", "r", encoding="utf-8"
            ) as file:
                last_update_str: str = file.read()
                last_update: datetime.date = datetime.datetime.strptime(
                    last_update_str, "%Y-%m-%d"
                ).date()
                last_update_strftime: str = last_update.strftime("%d.%m.%Y")
                return last_update_strftime
        except FileNotFoundError:
            return None

    def _create_mapping(self) -> None:
        self.lexy_dir.mkdir(exist_ok=True)
        self.log_path.mkdir(exist_ok=True)
        self.file_path.mkdir(exist_ok=True)
        self.json_path.mkdir(exist_ok=True)


if __name__ == "__main__":
    lexy_scraper: LexyScraper = LexyScraper()
    lexy_scraper.force_update()
