from typing import TypedDict

from lexy.services.config.colors_config import ColorsConfig
from lexy.services.config.editor_config import EditorConfig
from lexy.services.config.fzf_config import FzfConfig


class Config(TypedDict, total=False):
    editor: EditorConfig
    fzf: FzfConfig
    colors: ColorsConfig
