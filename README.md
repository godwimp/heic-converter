# HEIC to JPG Converter

## Overview
This Python script automatically converts all HEIC image files in the current directory to JPG format.

## Features
- Converts all .HEIC files in the current directory
- Renames converted files with `_converted.jpg` suffix
- Works cross-platform (Windows, macOS, Linux)

## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

## Dependencies
- Pillow
- pillow-heif

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/godwimp/heic-converter.git
   cd heic-converter
   ```

2. Install required dependencies:
   ```bash
   pip install pillow-heif Pillow
   ```

## Usage

1. Place the script in the folder containing your HEIC files
2. Run the script:
   ```bash
   python heic_converter.py
   ```

## Example
```
# Before running
my_folder/
├── image1.HEIC
├── image2.HEIC
└── heic_converter.py

# After running
my_folder/
├── image1.HEIC
├── image1_converted.jpg
├── image2.HEIC
├── image2_converted.jpg
└── heic_converter.py
```

## Output
The script will display:
- Each successful conversion
- Any errors during conversion
- A summary of total conversions

## Troubleshooting
- Ensure you have the latest version of Python
- Verify all dependencies are correctly installed
- Check file permissions in the target directory

## Limitations
- Only converts .HEIC files
- Preserves original .HEIC files
- May not maintain exact image metadata

## Contributing
Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License
[Choose an appropriate license, e.g., MIT]

## Author
[godwimp]

## Version
1.0.0
```
