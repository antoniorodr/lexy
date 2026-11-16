from typing import TypedDict


class ColorsConfig(TypedDict, total=False):
    border: str
    label: str
    preview_border: str
    preview_label: str
    list_border: str
    list_label: str
    input_border: str
    input_label: str
    header_border: str
