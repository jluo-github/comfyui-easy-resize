"""
ComfyUI node class definitions for Easy Resize plugin.

Provides EasyImageSize and EasyImageSizeLatent nodes.
"""

from __future__ import annotations

import torch

from .presets import (
    SIZE_PRESET_LIST,
    DEFAULT_SIZE_PRESET,
    CROP_METHODS,
    SCALE_METHODS,
    get_size_from_preset,
)
from .resize import resize_image, resize_mask


# ============================================================================
# Node 1: EasyImageSize
# ============================================================================


class EasyImageSize:
    """
    Easy Image Size node.

    Scales and crops loaded images to preset sizes.
    Supports both image and mask inputs.
    Single dropdown for all model presets (radio-button style).
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "size_preset": (SIZE_PRESET_LIST, {"default": DEFAULT_SIZE_PRESET}),
                "crop_method": (CROP_METHODS, {"default": "Center Crop"}),
                "scale_method": (SCALE_METHODS, {"default": "lanczos"}),
            },
            "optional": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK", "INT", "INT")
    RETURN_NAMES = ("image", "mask", "width", "height")
    FUNCTION = "process"
    CATEGORY = "image/size"

    def process(
        self,
        size_preset: str,
        crop_method: str,
        scale_method: str,
        image: torch.Tensor | None = None,
        mask: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor, int, int]:
        """Process image and mask with the selected size preset."""
        target_width, target_height = get_size_from_preset(size_preset)

        # Process image
        if image is not None:
            output_image = resize_image(
                image, target_width, target_height, crop_method, scale_method
            )
        else:
            output_image = torch.zeros((1, target_height, target_width, 3))

        # Process mask
        if mask is not None:
            output_mask = resize_mask(
                mask, target_width, target_height, crop_method, scale_method
            )
        else:
            output_mask = torch.zeros((1, target_height, target_width))

        return (output_image, output_mask, target_width, target_height)


# ============================================================================
# Node 2: EasyImageSizeLatent
# ============================================================================


class EasyImageSizeLatent:
    """
    Easy Image Size Latent node.

    Creates empty latent tensors at preset sizes.
    Replaces the standard Empty Latent Image node.
    Single dropdown for all model presets (radio-button style).
    """

    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "size_preset": (SIZE_PRESET_LIST, {"default": DEFAULT_SIZE_PRESET}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "generate"
    CATEGORY = "latent"

    def generate(
        self,
        size_preset: str,
        batch_size: int = 1,
    ) -> tuple[dict[str, torch.Tensor]]:
        """Generate empty latent tensor at the selected size."""
        target_width, target_height = get_size_from_preset(size_preset)

        # Latent space is 1/8 of pixel dimensions
        latent_width = target_width // 8
        latent_height = target_height // 8

        latent = torch.zeros([batch_size, 4, latent_height, latent_width])

        return ({"samples": latent},)


# ============================================================================
# Node Mappings
# ============================================================================

NODE_CLASS_MAPPINGS: dict[str, type] = {
    "EasyImageSize": EasyImageSize,
    "EasyImageSizeLatent": EasyImageSizeLatent,
}

NODE_DISPLAY_NAME_MAPPINGS: dict[str, str] = {
    "EasyImageSize": "Easy Image Size",
    "EasyImageSizeLatent": "Easy Image Size - Latent",
}
