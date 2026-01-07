"""
Size preset definitions for ComfyUI Easy Resize plugin.

Contains curated size presets optimized for SDXL/Flux workflows.
"""

from __future__ import annotations

# ============================================================================
# Size Presets (Curated List)
# ============================================================================

SIZE_PRESETS: dict[str, tuple[int, int]] = {
    # --- The Essentials ---
    "1024x1024 (1:1) - Square": (1024, 1024),
    # --- Portrait (Phone/Character) ---
    "864x1152 (3:4) - Classic Portrait": (864, 1152),
    "896x1152 (7:9) - Standard Portrait": (896, 1152),
    "832x1216 (2:3) - Tall Portrait": (832, 1216),
    "768x1344 (9:16) - Phone Wallpaper": (768, 1344),
    # --- Landscape (Desktop/Movie) ---
    "1152x864 (4:3) - Classic Landscape": (1152, 864),
    "1152x896 (9:7) - Standard Landscape": (1152, 896),
    "1216x832 (3:2) - Classic Photo": (1216, 832),
    "1344x768 (16:9) - Widescreen": (1344, 768),
    "1536x640 (21:9) - Cinematic Ultrawide": (1536, 640),
    # --- The "King Size" (High VRAM Only) ---
    "1280x1280 (1:1) - High Detail Square": (1280, 1280),
}

# Default selection
DEFAULT_SIZE_PRESET = "1024x1024 (1:1) - Square"

# List of preset names for dropdown
SIZE_PRESET_LIST: list[str] = list(SIZE_PRESETS.keys())

# ============================================================================
# Method Constants
# ============================================================================

CROP_METHODS: list[str] = [
    "Center Crop",
    "Top-Left Crop",
    "Bottom-Right Crop",
    "Scale to Fit",
    "Stretch to Fill",
]

SCALE_METHODS: list[str] = ["lanczos", "bilinear", "bicubic", "nearest"]

# Mapping from scale method names to PyTorch interpolation modes
INTERPOLATION_MODES: dict[str, str] = {
    "lanczos": "bicubic",  # PyTorch doesn't have lanczos, use bicubic
    "bilinear": "bilinear",
    "bicubic": "bicubic",
    "nearest": "nearest",
}

# ============================================================================
# Helper Functions
# ============================================================================


def get_size_from_preset(preset: str) -> tuple[int, int]:
    """
    Get dimensions from a preset string.

    Args:
        preset: Preset key like "1024x1024 (1:1) - Square"

    Returns:
        Tuple of (width, height), defaults to (1024, 1024) if not found
    """
    return SIZE_PRESETS.get(preset, (1024, 1024))
