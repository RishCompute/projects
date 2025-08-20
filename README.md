# 🐍 Python Version Downloader

A simple Python script that **fetches all available Python versions** from [python.org](https://www.python.org/doc/versions/), lets you choose one, downloads it as a Windows installer (`.exe`), and optionally **executes the installer** directly from your terminal.

---

## ✨ Features
- 🔍 Fetches and displays **all available Python versions** from python.org.  
- ⬇️ Downloads the selected version’s Windows installer (`.exe`) automatically.  
- 📂 Allows you to choose a **custom download directory** (defaults to current directory).  
- ⚡ Optionally **executes the installer** after download.  

---

## 📦 Requirements
- Python **3.7+**
- Dependencies:
  - `requests`
  - `beautifulsoup4`

Install them with:
```bash
pip install requests beautifulsoup4
```
🚀 Usage
Clone or download this repository.
```
python python_downloader.py
```
Follow the prompts:

- Choose whether to view available versions.

- Enter the version to download (e.g. 3.8.0 or Python 3.8.0).

- Select the download directory (press Enter for current directory).

- Optionally execute the downloaded .exe.

🖼 Example Run
```
Show available Python versions? [y/n]: y

Available Python versions (earliest to latest):
---------------------------------------------
 1. Python 1.0.1
 2. Python 1.1
 ...
45. Python 3.13.0

Enter the Python version to download (e.g., "3.8.0" or "Python 3.8.0"): 3.13.0
Enter download directory (press Enter for current directory): C:\Users\User\Downloads

Downloading Python 3.13.0...
Successfully downloaded Python 3.13.0 to: C:\Users\User\Downloads\python-3.13.0-amd64.exe

Do you want to execute the file (y/n): y
```
⚠️ Notes

- This script currently downloads Windows 64-bit installers only (-amd64.exe).

- Make sure you run this script with proper permissions if saving to system directories.

- Execution will open the official Python installer GUI.

