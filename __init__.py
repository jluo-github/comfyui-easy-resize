"""
ComfyUI Easy Resize Plugin

Custom node plugin for image size adjustment and settings.
Provides preset sizes for SDXL, and Flux models.
"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
