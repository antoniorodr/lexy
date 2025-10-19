import tomllib
from pathlib import Path

DEFAULTS = {
    "fzf": {
        "preview_command": "bat --style=full {}",
        "preview_window": "right:{percent}%:wrap:cycle",
        "input_label": " Input ",
        "border_label": " Enter: Open with bat │ Ctrl-D/U: scroll preview ",
    },
    "colors": {
        "border": "#aaaaaa",
        "label": "#cccccc",
        "preview_border": "#9999cc",
        "preview_label": "#ccccff",
        "list_border": "#669966",
        "list_label": "#99cc99",
        "input_border": "#996666",
        "input_label": "#ffcccc",
        "header_border": "#6699cc",
    },
}


def load_config():
    config_path = Path.home() / ".config/lexy/config.toml"
    config = {}
    if config_path.exists():
        try:
            with config_path.open("rb") as f:
                config = tomllib.load(f)
        except Exception as e:
            print(f"Warning: Failed to load config: {e}")
    return config


def build_fzf_command(config: dict) -> str:
    preview_command = DEFAULTS["fzf"]["preview_command"]

    fzf_config = config.get("fzf", {})
    colors = {**DEFAULTS["colors"], **config.get("colors", {})}

    preview_percent = fzf_config.get("preview_percent", "60")
    preview_window = DEFAULTS["fzf"]["preview_window"].format(percent=preview_percent)

    return f"""
    fzf --style=full \
    --border --padding=1,2 \
    --info=inline \
    --border-label="{fzf_config.get('border_label', DEFAULTS['fzf']['border_label'])}" \
    --input-label="{fzf_config.get('input_label', DEFAULTS['fzf']['input_label'])}" \
    --preview="{preview_command}" \
    --preview-window={preview_window} \
    --bind="ctrl-d:preview-down" \
    --bind="ctrl-u:preview-up" \
    --bind="enter:execute(bat {{}})" \
    --bind="result:transform-list-label:
        if [[ -z $FZF_QUERY ]]; then
        echo ' $FZF_MATCH_COUNT items '
        else
        echo ' $FZF_MATCH_COUNT matches for [$FZF_QUERY] '
        fi" \
    --bind="focus:transform-preview-label:[[ -n {{}} ]] && printf ' Previewing [%s] ' {{}}" \
    --bind="focus:+transform-header:file --brief {{}} || echo 'No file selected'" \
    --color="border:{colors['border']},label:{colors['label']}" \
    --color="preview-border:{colors['preview_border']},preview-label:{colors['preview_label']}" \
    --color="list-border:{colors['list_border']},list-label:{colors['list_label']}" \
    --color="input-border:{colors['input_border']},input-label:{colors['input_label']}" \
    --color="header-border:{colors['header_border']}"
    """.strip()
