from typing import TypedDict


class FzfConfig(TypedDict, total=False):
    preview_percent: str
    input_label: str
    border_label: str
