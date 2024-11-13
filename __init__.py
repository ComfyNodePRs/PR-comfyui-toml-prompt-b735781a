from .toml_prompt.toml_prompt_decode import TomlPromptDecode
from .toml_prompt.multipart_clip_text_encode import MultipartCLIPTextEncode
from .toml_prompt.multiple_lora_tag_loader import MultipleLoraTagLoader
from .toml_prompt.prompt_loader import PromptLoader
from .toml_prompt.string_concat import StringConcat
from .toml_prompt.string_sub import StringSub
from .toml_prompt.string_viewer import StringViewer

NODE_CLASS_MAPPINGS = {
    "TomlPromptDecode": TomlPromptDecode,
    "MultipartCLIPTextEncode": MultipartCLIPTextEncode,
    "MultipleLoraTagLoader": MultipleLoraTagLoader,
    "PromptLoader": PromptLoader,
    "StringConcat": StringConcat,
    "StringSub": StringSub,
    "StringViewer": StringViewer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TomlPromptDecode": "TomlPromptDecode",
    "MultipartCLIPTextEncode": "MultipartCLIPTextEncode",
    "MultipleLoraTagLoader": "MultipleLoraTagLoader",
    "PromptLoader": "PromptLoader",
    "StringConcat": "StringConcat",
    "StringSub": "StringSub",
    "StringViewer": "StringViewer",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
