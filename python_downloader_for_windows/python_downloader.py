import requests
from bs4 import BeautifulSoup
import re
import os
import subprocess

def get_python_versions():
    """Fetch and return all available Python versions from the website."""
    url = "https://www.python.org/doc/versions/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        version_strings = re.findall(r'Python\s+(\d+\.\d+(?:\.\d+)?)', text, re.IGNORECASE)
        
       
        def version_key(version_str):
            version_part = version_str.lower().replace('python', '').strip()
            return tuple(map(int, version_part.split('.')))
        sorted_versions = sorted(version_strings, key=version_key)
        formatted_versions = [f"Python {version}" for version in sorted_versions]
        return formatted_versions
        
    except requests.RequestException as e:
        print(f"Error fetching versions: {e}")
        return []

def download_python_version(version, download_dir):
    version_number = version.lower().replace('python', '').strip()
    download_url = f'https://www.python.org/ftp/python/{version_number}/python-{version_number}-amd64.exe'
    filename = f'python-{version_number}-amd64.exe'
    global filepath
    filepath = os.path.join(download_dir, filename)
    
    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        
        print(f"Successfully downloaded {version} to: {filepath}")
        return True
        
    except requests.RequestException as e:
        print(f"Error downloading {version}: {e}")
        return False

def main():
    
    show_versions = input('Show available Python versions? [y/n]: ').strip().lower()
    
    if show_versions == 'y':
        versions = get_python_versions()
        if versions:
            print("\nAvailable Python versions (earliest to latest):")
            print("-" * 45)
            for i, version in enumerate(versions, 1):
                print(f"{i:2d}. {version}")
        else:
            print("Could not retrieve version list.")
    
    
    target_version = input('\nEnter the Python version to download (e.g., "3.8.0" or "Python 3.8.0"): ').strip()
    
    
    if target_version[0].isdigit():
        target_version = f"Python {target_version}"
    
    
    download_dir = input(
        'Enter download directory (press Enter for current directory): '
    )
    
   
    if not download_dir:
        download_dir = os.getcwd()
    
    
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
        print(f"Created directory: {download_dir}")
    
    
    print(f"\nDownloading {target_version}...")
    success = download_python_version(target_version, download_dir)
    
    if success:
        print("Download completed successfully!")
        return download_dir
    else:
        print("Download failed. Please check the version and try again.")
        return False

def execute(output_dir):
    if output_dir:
     exe_ask=input('Do you to execute the file(y/n): ')        
     if exe_ask=='y' :
      subprocess.run(filepath)
    return
    
if __name__ == "__main__":
    output_dir=main()
    execute(output_dir)
