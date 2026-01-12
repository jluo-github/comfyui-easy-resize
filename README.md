# Easy Resize - ComfyUI Custom Nodes

A ComfyUI plugin for quick image size selection with curated presets optimized for SDXL/Flux.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Nodes-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- 🎯 **11 curated presets** - All aspect ratios with both orientations
- 📐 **1328×1328 default** - Ready for SDXL/Flux out of the box
- ✂️ **Flexible cropping** - Center, Top-Left, Bottom-Right, Scale to Fit, Stretch

## Installation

### Method 1: Clone Repository

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jluo-github/comfyui-easy-resize.git
```

### Method 2: Manual Download

1. Download this repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/comfyui-easy-resize/`
3. Restart ComfyUI

## Nodes

### Easy Image Size

**Category:** `image/size`

| Input | Type | Description |
|-------|------|-------------|
| `size_preset` | dropdown | Resolution preset |
| `crop_method` | dropdown | How to handle aspect ratio |
| `scale_method` | dropdown | Interpolation algorithm |
| `image` | IMAGE | Optional input image |
| `mask` | MASK | Optional input mask |

| Output | Type |
|--------|------|
| `image` | IMAGE |
| `mask` | MASK |
| `width` | INT |
| `height` | INT |

### Easy Image Size - Latent

**Category:** `latent`

| Input | Type | Description |
|-------|------|-------------|
| `size_preset` | dropdown | Resolution preset |
| `batch_size` | INT | Number of latents (1-4096) |

| Output | Type |
|--------|------|
| `latent` | LATENT |

## Size Presets

| Preset | Resolution | Use Case |
|--------|------------|----------|
| **Square** | 1328×1328 | Default, balanced |
| **Ultrawide Landscape** | 2016×928 | Cinematic ultrawide |
| **Ultrawide Portrait** | 928×2016 | Tall ultrawide |
| **Widescreen Landscape** | 1664×928 | Desktop wallpapers |
| **Widescreen Portrait** | 928×1664 | Phone screens |
| **Classic Landscape** | 1472×1104 | Traditional 4:3 |
| **Classic Portrait** | 1104×1472 | Portrait 3:4 |
| **Standard Landscape** | 1584×1056 | Photo 3:2 |
| **Standard Portrait** | 1056×1584 | Photo 2:3 |
| **Wide Landscape** | 1856×928 | Panoramic 2:1 |
| **Tall Portrait** | 928×1856 | Tall 1:2 |

## Crop Methods

| Method | Behavior |
|--------|----------|
| **Center Crop** | Scale to cover, crop from center |
| **Top-Left Crop** | Scale to cover, crop from top-left |
| **Bottom-Right Crop** | Scale to cover, crop from bottom-right |
| **Scale to Fit** | Fit inside target, add black bars |
| **Stretch to Fill** | Stretch to exact dimensions |

## File Structure

```
my-easy-size/
├── __init__.py    # Entry point
├── presets.py     # Size preset definitions
├── resize.py      # Image/mask resize utilities
├── nodes.py       # Node class definitions
└── README.md
```

## Requirements

- ComfyUI (latest version recommended)
- Python 3.10+
- PyTorch (included with ComfyUI)

## License

MIT License

---

Made with ❤️ for the ComfyUI community
