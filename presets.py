"""
Size preset definitions for ComfyUI Easy Resize plugin.

Contains curated size presets optimized for SDXL/Flux workflows.
"""

from __future__ import annotations

# ============================================================================
# Size Presets (Curated List)
# ============================================================================

SIZE_PRESETS: dict[str, tuple[int, int]] = {
    # --- Square ---
    "1328x1328 (1:1) - Square": (1328, 1328),
    # --- Ultrawide ---
    "2016x928 (21:9) - Ultrawide Landscape": (2016, 928),
    "928x2016 (9:21) - Ultrawide Portrait": (928, 2016),
    # --- Widescreen ---
    "1664x928 (16:9) - Widescreen Landscape": (1664, 928),
    "928x1664 (9:16) - Widescreen Portrait": (928, 1664),
    # --- Classic Photo ---
    "1472x1104 (4:3) - Classic Landscape": (1472, 1104),
    "1104x1472 (3:4) - Classic Portrait": (1104, 1472),
    # --- Standard Photo ---
    "1584x1056 (3:2) - Standard Landscape": (1584, 1056),
    "1056x1584 (2:3) - Standard Portrait": (1056, 1584),
    # --- Tall/Wide ---
    "1856x928 (2:1) - Wide Landscape": (1856, 928),
    "928x1856 (1:2) - Tall Portrait": (928, 1856),
}

# Default selection
DEFAULT_SIZE_PRESET = "1328x1328 (1:1) - Square"

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
