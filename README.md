# 🎬 AI Video Upscale & Interpolation (4K 60fps)

This project provides a ready-to-use Google Colab workflow for upscaling videos (especially anime/animation) to 4K and increasing the frame rate to 60fps.

## 🚀 Quick Start

1. **Upload Notebook**: Upload `Upscale_Workflow.ipynb` to [Google Colab](https://colab.research.google.com/).
2. **Setup GPU**: In Colab, go to `Edit` -> `Notebook settings` -> `Hardware accelerator` -> `T4 GPU`.
3. **Connect Drive**: Prepare your input video in a folder on Google Drive (e.g., `Movie/Input`).
4. **Run Cells**: Follow the instructions in the notebook to:
   - Mount Google Drive.
   - Install Real-ESRGAN and RIFE.
   - Run the Upscale process.
   - (Optional) Run the Interpolation process.

## 🛠 Features

- **Real-ESRGAN**: High-quality upscaling (Model: `realesr-animevideov3`).
- **RIFE**: Smooth 60fps interpolation.
- **FFmpeg Utils**: Tools for splitting large videos into manageable chunks.

## 💡 Tips for Huy

- **Scale**: Use `-s 2` for 1080p -> 4K.
- **RIFE Exponent**: Use `--exp=1` to double the frame rate (e.g., 24fps -> 48fps or 30fps -> 60fps).
- **Long Videos**: If a movie is > 30 minutes, split it into chunks using the FFmpeg cell, process them separately, and merge back.
- **Keep Colab Alive**: Use a Chrome extension like "Colab Alive" to prevent timeouts.

## 🗂 File Structure (Suggested)

```text
/drive/MyDrive/
└── Movie/
    ├── Input/   <-- Original 1080p files
    └── Output/  <-- Upscaled 4K files
```

## ⚖️ License
This project leverages [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) and [RIFE](https://github.com/hzwer/Practical-RIFE). Please respect their respective licenses.
