# Clutter Clearer 🧹

**Clutter Clearer** is a simple Python script that helps you quickly rename and organize files in a directory by their format (extension).  
It can rename all files or only those of specific formats, giving them clean, ordered names.

---

## 📌 Features

- Rename **all files** in a directory in order.
- Rename **only specific file formats** (e.g., `.pdf`, `.jpg`, `.txt`).
- Automatically appends the file extension twice to avoid accidental overwrites.
- Handles `FileExistsError` gracefully with a friendly message.

---

## 📂 How It Works

1. **`clutter_clearer(*format, directory_path)`**
   - `format`: File extensions to target (e.g., `'pdf'`, `'jpg'`) or `"all"` to target all files.
   - `directory_path`: Path to the folder containing the files.
   
2. **`corrector(arg, path)`**
   - A helper function to make calling `clutter_clearer` easier.
   - Splits a `/`-separated string of formats and sends them to `clutter_clearer`.

---

## 🖥 Example Usage

```python
import os

# Rename only PDF files in the given directory
corrector('pdf', r"C:\Users\risha\OneDrive\Desktop\test")

# Rename JPG and PNG files
corrector('jpg/png', r"C:\Users\risha\OneDrive\Desktop\test")` ``` `



⚠ Notes
The script appends the extension twice intentionally to prevent overwriting files with the same name.

Make sure to run this script on a test directory first before using it on important files.

If you run the same command twice on the same folder, you might trigger a FileExistsError.

Windows users: Always put an r before the path string (e.g., r"C:\path\to\folder") to avoid escape sequence errors.


# Rename all files
corrector('all', r"C:\Users\risha\OneDrive\Desktop\test")
