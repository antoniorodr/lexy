from bs4 import BeautifulSoup
import requests
from rich.progress import track
import json
import re
import datetime
from pathlib import Path



class LexyScraper:
    def __init__(self):
        self.homedir = Path.home()
        self.lexy_dir = self.homedir / ".config/lexy"
        self.log_path = self.lexy_dir / "log"
        self.file_path = self.lexy_dir / "files"
        self.json_path = self.lexy_dir / "json"
        self.XNY_URL = "https://learnxinyminutes.com"
        self.response = requests.get(self.XNY_URL)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.languages = self.soup.select("tr td.name a")
        self.pattern = r"\.[\w]+"
        self.force = False
        self.languages_list = []
        self.update_interval_days = 60

    def fetch_language(self):
        self.lexy_dir.mkdir(exist_ok=True)
        self.log_path.mkdir(exist_ok=True)
        self.file_path.mkdir(exist_ok=True)
        self.json_path.mkdir(exist_ok=True)
        for language in track(
            self.languages,
            description="Fetching languages from 'Learn X in Y minutes'...",
        ):
            language_name = language.text.strip()
            if not language.get("href") or language_name == "AWK":
                language_url = None
                language_full_url = None
            else:
                language_url = language.get("href")
                language_full_url = self.XNY_URL + language_url
                language_response = requests.get(language_full_url)
                language_soup = BeautifulSoup(language_response.text, "html.parser")
                language_file = language_soup.select("p.filelink a")
            try:
                language_file_url = language_file[0].get("href")
                file_extension = re.search(self.pattern, language_file_url).group()
                language_file_full_url = self.XNY_URL + language_file_url
                language_dict = {
                    "language": language_name,
                    "language_url": language_full_url,
                    "language_file_url": language_file_full_url,
                    "file_extension": file_extension,
                }
                if self.force:
                    self.languages_list.append(language_dict)
                    self.create_file(
                        language_file_full_url, file_extension, language_name
                    )
                    self.save_to_json()
                    self.create_log()
                if not self.force and language_name not in [
                    lang["language"] for lang in self.languages_list
                ]:
                    self.languages_list.append(language_dict)
                    self.create_file(
                        language_file_full_url, file_extension, language_name
                    )
                    self.save_to_json()
                    self.create_log()
            except (IndexError, AttributeError):
                file_extension = ".txt"

    def save_to_json(self):
        with open(f"{self.json_path}/languages.json", "w") as f:
            json.dump(self.languages_list, f, indent=4)

    def create_file(self, language_full_file_url, file_extension, language_name):
        content_response = requests.get(language_full_file_url)
        content_soup = BeautifulSoup(content_response.text, "html.parser")
        with open(f"{self.file_path}/{language_name}{file_extension}", "w") as file:
            file.write(content_soup.text)

    def auto_update(self):
        today = datetime.date.today()
        try:
            with open(f"{self.log_path}/last_update.txt", "r") as file:
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
        with open(f"{self.log_path}/last_update.txt", "w") as file:
            file.write(str(datetime.date.today()))
        self.force = False

    def create_log(self):
        today = datetime.date.today()
        with open(f"{self.log_path}/last_update.txt", "w") as file:
            file.write(str(today))

    def last_modified(self):
        try:
            with open(f"{self.log_path}/last_update.txt", "r") as file:
                last_update = file.read()
                last_update = datetime.datetime.strptime(last_update, "%Y-%m-%d").date()
                last_update = last_update.strftime("%d.%m.%Y")
                return last_update
        except FileNotFoundError:
            return None


if __name__ == "__main__":
    lexy_scraper = LexyScraper()
    lexy_scraper.force_update()
