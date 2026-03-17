```markdown
# EXIF Extractor

A production‑grade Python tool to extract metadata (EXIF) from image files.  
Supports both command‑line and graphical interfaces, with two extraction backends and GPS coordinate decoding.

---

## Features

- **Dual extraction backends** – Choose between `exif` (modern, attribute‑based) and `exifread` (raw tag names).
- **CLI with advanced options** – Filter by tag, output as JSON, scan folders recursively.
- **Graphical interface** – Simple Tkinter GUI with file picker and scrollable output.
- **GPS decoding** – Converts raw GPS coordinates to decimal degrees.
- **Batch processing** – Scan entire folders for EXIF data.
- **Modular architecture** – Clean separation of concerns (extractor, formatter, scanner, logger).
- **Installable package** – Can be installed via pip for system‑wide use.

---

## Installation

### 1. Clone or download the repository

```bash
git clone https://github.com/your-username/exif-extractor.git
cd exif-extractor
```

### 2. Create and activate a virtual environment (recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the package in editable mode (optional but convenient)

```bash
pip install -e .
```
This makes the `exif-extract` command available and ensures imports work correctly.

---

## Usage

### Command‑Line Interface (CLI)

Basic extraction:
```bash
exif-extract image.jpg
```

Choose a different backend:
```bash
exif-extract image.jpg --library exifread
```

Output as JSON:
```bash
exif-extract image.jpg --json
```

Show only a specific tag:
```bash
exif-extract image.jpg --tag Model
```

Scan a folder recursively:
```bash
exif-extract photos/ --scan
```

If you haven't installed the package, you can run the module directly:
```bash
python -m exif_extractor.cli image.jpg
```

### Graphical Interface (GUI)

Launch the GUI:
```bash
python -m exif_extractor.gui
```
Click **Open Image** and select a file – EXIF data will appear in the text area.

---

## Project Structure

```
exif-extractor/
│
├── src/
│   └── exif_extractor/
│       ├── __init__.py
│       ├── cli.py              # Command‑line entry point
│       ├── gui.py              # Tkinter GUI
│       ├── extractor.py         # Core extraction logic
│       ├── formatter.py         # Output formatting (text, JSON)
│       ├── gps.py               # GPS coordinate conversion
│       ├── scanner.py           # Folder scanning
│       ├── logger.py            # Logging configuration
│       └── exceptions.py        # Custom exceptions
│
├── tests/                       # Unit tests
│   ├── test_extractor.py
│   └── test_gps.py
│
├── data/                         # Place sample images here
├── docs/                          # Documentation
├── pyproject.toml                 # Package configuration
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## Dependencies

- Python 3.6+
- [exif](https://pypi.org/project/exif/) – modern EXIF extraction
- [exifread](https://pypi.org/project/ExifRead/) – raw tag extraction (optional fallback)
- Tkinter (included with Python)

All dependencies are listed in `requirements.txt`.

---

## Troubleshooting

### “No module named 'exif_extractor'”
Make sure you are running commands from the project root and that the virtual environment is activated. If you haven't installed the package, run:
```bash
pip install -e .
```

### “33192 is not a valid TiffByteOrder”
This error occurs with the `exif` backend when the file is corrupted or not a valid image. Try the `exifread` backend:
```bash
exif-extract image.jpg --library exifread
```

### GUI doesn’t start
Ensure Tkinter is installed (it comes with Python on Windows, but on Linux you may need `python3-tk`). On Debian/Ubuntu:
```bash
sudo apt-get install python3-tk
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## Contact

Your Name – [osintbuddy.research.com](mailto:osintbuddy.research.com)  
Project Link: [https://github.com/osintBuddy-Research/exif-data-extractor](https://github.com/osintBuddy-Research/exif-data-extractor)
```

---

## Customization Tips

- Replace `your-username` with your actual GitHub username.
- Update the email and name in the "Contact" section.
- If you create a `LICENSE` file, include the MIT license text (optional).
- Adjust the repository name if you used something other than `exif-extractor`.

You can save this as `README.md` in your project root and then upload it manually or via Git. It will give visitors a clear overview of your project.
