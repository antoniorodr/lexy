import tomllib
from pathlib import Path
from typing import cast

import tomlkit

from lexy.defaults import DEFAULTS
from lexy.services.config.config import Config
from lexy.services.config.fzf_config import FzfConfig


class ConfigServices:
    @staticmethod
    def create_config_file() -> Path:
        config_path: Path = Path.home() / ".config/lexy/config.toml"
        if not config_path.exists():
            with config_path.open("w") as f:
                f.write("[editor]\n")
                f.write(tomlkit.dumps({"default_editor": "bat"}))
                f.write("\n")
                f.write("[fzf]\n")
                f.write(
                    tomlkit.dumps(
                        {
                            "preview_percent": "60",
                            "input_label": " Input ",
                            "border_label": " Enter: Open with bat │ Ctrl-D/U: scroll preview ",
                        }
                    )
                )
                f.write("\n")
                f.write(tomlkit.dumps({"colors": DEFAULTS["colors"]}))
        return config_path

    @staticmethod
    def change_default_editor(editor: str, config_path: Path | None = None) -> None:
        config_path: Path = config_path or ConfigServices.create_config_file()

        with config_path.open("r") as f:
            content: str = f.read().strip()
            config: tomlkit.TOMLDocument = (
                tomlkit.parse(content) if content else tomlkit.document()
            )
            config["editor"]["default_editor"] = editor
            f.close()

        with config_path.open("w") as f:
            f.write(tomlkit.dumps(config))

    @staticmethod
    def load_config(config_path: Path | None = None) -> Config:
        config_path: Path = config_path or ConfigServices.create_config_file()
        config: Config = {}
        if config_path.exists():
            try:
                with config_path.open("rb") as f:
                    config: Config = cast(Config, tomllib.load(f))
            except Exception as e:
                print(f"Warning: Failed to load config: {e}")
        return config

    @staticmethod
    def build_fzf_command(config: Config) -> str:
        preview_command: str = DEFAULTS["fzf"]["preview_command"]
        editor: str = config.get("editor", {}).get("default_editor", "bat")

        editor_command: str = (
            f"{editor} -R -c 'lua vim.diagnostic.enable(false)'"
            if editor == "nvim"
            else editor
        )

        fzf_config: FzfConfig = config.get("fzf", {})
        colors: dict[str, str] | object = {
            **DEFAULTS["colors"],
            **config.get("colors", {}),
        }

        preview_percent: str = fzf_config.get("preview_percent", "60")
        preview_window: str = DEFAULTS["fzf"]["preview_window"].format(
            percent=preview_percent
        )

        return f"""
        fzf --style=full \
        --border --padding=1,2 \
        --info=inline \
        --border-label="{fzf_config.get("border_label", DEFAULTS["fzf"]["border_label"])}" \
        --input-label="{fzf_config.get("input_label", DEFAULTS["fzf"]["input_label"])}" \
        --preview="{preview_command}" \
        --preview-window={preview_window} \
        --bind="ctrl-d:preview-down" \
        --bind="ctrl-u:preview-up" \
        --bind="enter:execute({editor_command} {{}})" \
        --bind="result:transform-list-label:
            if [[ -z $FZF_QUERY ]]; then
            echo ' $FZF_MATCH_COUNT items '
            else
            echo ' $FZF_MATCH_COUNT matches for [$FZF_QUERY] '
            fi" \
        --bind="focus:transform-preview-label:[[ -n {{}} ]] && printf ' Previewing [%s] ' {{}}" \
        --bind="focus:+transform-header:file --brief {{}} || echo 'No file selected'" \
        --color="border:{colors["border"]},label:{colors["label"]}" \
        --color="preview-border:{colors["preview_border"]},preview-label:{colors["preview_label"]}" \
        --color="list-border:{colors["list_border"]},list-label:{colors["list_label"]}" \
        --color="input-border:{colors["input_border"]},input-label:{colors["input_label"]}" \
        --color="header-border:{colors["header_border"]}"
        """.strip()
