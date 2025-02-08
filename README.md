# HEIF Image Converter 🖼️

A robust Python utility that converts HEIF/HEIC images (commonly used by iPhones) to other formats while maintaining maximum possible quality. The converter includes a quality analysis feature that calculates and reports any potential quality loss during conversion.

## ✨ Features

- Convert HEIF/HEIC images to PNG (lossless) or JPEG formats
- Automatic quality loss calculation using Structural Similarity Index (SSIM)
- Batch processing of multiple images
- Organized output in a separate directory
- Original files remain untouched
- Detailed conversion reports

## 🚀 Coming Soon

- Support for additional formats (WebP, TIFF, BMP)
- Custom quality settings for JPEG conversion
- Multi-threading for faster batch processing
- GUI interface
- Metadata preservation

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/MananKateshiya/heif-image-converter.git
cd heif-converter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Open terminal in the directory containing your HEIF/HEIC images

2. Run the converter with your desired output format:
```bash
# For PNG conversion (lossless)
python heif_converter.py png

# For JPEG conversion
python heif_converter.py jpg
```

The script will:
- Create a new folder named after the parent directory (e.g., "Photos-png" or "Photos-jpg")
- Convert all HEIF/HEIC images in the current directory
- Display quality analysis for each conversion

## 📊 Quality Analysis

The converter provides quality metrics for each conversion:
- PNG conversions are lossless (0% quality loss)
- JPEG conversions include a quality loss percentage based on SSIM analysis
- Detailed report shown for each converted image

## 📁 Output Structure

```
Your-Photos-Directory/
├── original.HEIC
├── another.HEIC
└── Your-Photos-Directory-png/
    ├── original.png
    └── another.png
```

## ⚠️ Error Handling

The converter includes robust error handling:
- Skips non-HEIF files automatically
- Continues processing if individual conversions fail
- Provides detailed error messages for troubleshooting

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pillow-heif](https://github.com/bigcat88/pillow_heif) for HEIF support
- [scikit-image](https://scikit-image.org/) for quality analysis
- All contributors and users of this project

## Contact

For any inquiries or support, feel free to open an issue on GitHub, or contact me at [contact@manankateshiya.com](mailto:contact@manankateshiya.com).

---

If you found this project helpful and would like to support my work, consider buying me a coffee! Your support is greatly appreciated.  [Buy Me a Coffee ☕](https://buymeacoffee.com/manankateshiya)

---
