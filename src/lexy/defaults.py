DEFAULTS: dict[str, dict[str, str]] = {
    "fzf": {
        "preview_command": "bat --color=always {}",
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
