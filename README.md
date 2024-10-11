# PDF Blank Page 2 Inserter

![PDF Icon](https://raw.githubusercontent.com/OlsenSM91/PDF-Page-2-Blanker/refs/heads/main/pdf.ico)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Compilation](#compilation)
- [Attribution](#attribution)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

**PDF Page 2 Blanker** is a Python-based application designed to automate the process of adding a blank page immediately after the first (cover) page of PDF files within a selected directory. This tool is particularly useful for preparing documents for printing, binding, or other formatting needs where a blank page separation is required.

## Features

- **Batch Processing:** Automatically processes all PDF files in a chosen directory.
- **Customizable:** Easily modify the script to adjust page insertion rules.
- **User-Friendly:** Utilizes a graphical folder selection dialog for ease of use.
- **Lightweight Executable:** Compiled into a standalone executable for convenience.
- **Minimal Dependencies:** Uses a virtual environment to ensure a small executable size.

## Prerequisites

Before installing and running the application, ensure you have the following:

- **Operating System:** Windows (The script uses Windows-specific paths and commands)
- **Python:** Version 3.6 or later
- **Python Packages:** `PyPDF2`, `PyInstaller`
- **Icon File:** `pdf.ico` (Provided in the project or downloadable from Flaticon)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/OlsenSM91/PDF-Page-2-Blanker.git
cd PDF-Page-2-Blanker
```

### 2. Set Up a Virtual Environment

Using a virtual environment ensures that the project dependencies are isolated from your global Python installation.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Upgrade `pip`

Ensure that `pip` is up to date.

```bash
pip install --upgrade pip
```

### 5. Install Required Packages

```bash
pip install PyPDF2 pyinstaller
```

## Usage

### Running the Script Directly

1. **Activate the Virtual Environment:**

   ```bash
   .\venv\Scripts\activate
   ```

2. **Run the Script:**

   ```bash
   python page2blanker.py
   ```

3. **Follow the Prompts:**

   - A folder selection dialog will appear. Choose the directory containing your PDF files.
   - The script will process each PDF, adding a blank page after the first page.
   - Modified PDFs will be saved with a `_modified` suffix in the same directory.

### Running the Compiled Executable

After compilation (see [Compilation](#compilation)), you can run the application without needing Python:

1. **Navigate to the `dist` Directory:**

   ```bash
   cd dist
   ```

2. **Run the Executable:**

   - **Windows:**

     Double-click `page2blanker.exe` or run via command prompt:

     ```bash
     .\page2blanker.exe
     ```

3. **Use the Application:**

   - Select the directory containing your PDF files.
   - The application will process the PDFs and notify you upon completion.

## Compilation

To distribute the application as a standalone executable, follow these steps:

### 1. Ensure You're in the Virtual Environment

Activate the virtual environment where you've installed the dependencies.

```bash
.\venv\Scripts\activate
```

### 2. Prepare the Icon File

Ensure that the `pdf.ico` file is in the project directory. If it's located elsewhere, provide the correct path.

### 3. Use PyInstaller to Compile

Run the following command to compile the script into a single executable file with a custom icon:

```bash
pyinstaller --onefile --windowed --icon=pdf.ico page2blanker.py
```

#### **Command Breakdown:**

- `--onefile`: Packages the application into a single executable file.
- `--windowed`: Hides the console window when running the executable (suitable for GUI applications).
- `--icon=pdf.ico`: Sets the icon of the executable to `pdf.ico`.

### 4. Locate the Executable

After successful compilation, the executable `page2blanker.exe` will be located in the `dist` directory:

```
pdf-blank-page-inserter/
├── dist/
│   └── page2blanker.exe
├── build/
├── venv/
├── page2blanker.py
├── pdf.ico
├── README.md
└── ...
```

### 5. Test the Executable

Navigate to the `dist` folder and run `page2blanker.exe` to ensure it functions as expected.

### 6. (Optional) Optimize Executable Size

For a smaller executable, consider using UPX compression:

1. **Download UPX:**

   - Visit the [UPX Releases Page](https://github.com/upx/upx/releases) and download the appropriate version for your OS.

2. **Extract and Add to System PATH:**

   - Extract the UPX archive and add the extracted directory to your system's PATH environment variable.

3. **Recompile with UPX:**

   ```bash
   pyinstaller --onefile --windowed --icon=pdf.ico page2blanker.py
   ```

   PyInstaller will automatically use UPX if it's available in the PATH.

## Attribution

The PDF icon used in this application is provided by [Flaticon](https://www.flaticon.com). Please see the attribution below:

[Pdf icons created by surang](https://www.flaticon.com/free-icons/pdf) - [Flaticon](https://flaticon.com)

## Contributing

Contributions are welcome!

## Contact

For any questions or suggestions, feel free to open an issue

---

**Happy PDF Editing!**
