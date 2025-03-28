# Filename: installer.py
import os
import sys
import json
import shutil
import requests
import subprocess
from pathlib import Path
from zipfile import ZipFile
from scripts.temporary import BASE_DIR, DATA_DIR, VENV_DIR, TEMP_DIR, BACKEND_OPTIONS, CONFIG_TEMPLATE, REQUIREMENTS

def clean_installation():
    """Remove existing data and venv directories"""
    for path in [DATA_DIR, VENV_DIR]:
        if path.exists():
            shutil.rmtree(path)
            print(f"Removed existing {path.name} directory")

def create_directories():
    (DATA_DIR / "temp").mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "scripts").mkdir(exist_ok=True)
    (DATA_DIR / "models").mkdir(exist_ok=True)  # Add models directory
    print("Created directory structure")

def select_backend():
    """Backend selection menu"""
    print("\nAvailable backends:")
    for i, (name, config) in enumerate(BACKEND_OPTIONS.items(), 1):
        print(f"{i}. {name}")
    
    while True:
        choice = input("\nSelect backend (1-2): ")
        if choice in ["1", "2"]:
            return list(BACKEND_OPTIONS.keys())[int(choice)-1]
        print("Invalid selection")

def download_backend(backend):
    """Download and extract backend files"""
    config = BACKEND_OPTIONS[backend]
    temp_zip = TEMP_DIR / "llama.zip"
    
    # Download
    print(f"Downloading {backend} package...")
    response = requests.get(config["url"], stream=True)
    with open(temp_zip, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract
    extract_path = DATA_DIR / config["dest"]
    with ZipFile(temp_zip, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    temp_zip.unlink()
    print(f"Installed {backend} to {extract_path}")

def create_venv():
    """Create fresh virtual environment"""
    subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    print("Created virtual environment")

def install_dependencies():
    pip_exe = VENV_DIR / "Scripts" / "pip.exe"
    subprocess.run([str(pip_exe), "install"] + REQUIREMENTS, check=True)
    
    # Add NLTK data download
    nltk_script = [
        str(VENV_DIR / "Scripts" / "python.exe"),
        "-c",
        "import nltk; nltk.download('punkt', quiet=True)"
    ]
    subprocess.run(nltk_script, check=True)
    print("Installed Python dependencies and NLTK data")

def create_config(backend):
    """Create persistent.json configuration"""
    config = CONFIG_TEMPLATE.copy()
    backend_config = BACKEND_OPTIONS[backend]
    
    config["backend_config"]["backend_type"] = backend
    config["backend_config"]["llama_bin_path"] = str(DATA_DIR / backend_config["dest"])
    config["model_settings"]["llama_cli_path"] = str(DATA_DIR / backend_config["cli_path"])
    
    with open(DATA_DIR / "persistent.json", "w") as f:
        json.dump(config, f, indent=2)
    print("Created persistent configuration")

def run_installer():
    """Main installation flow"""
    try:
        clean_installation()
        create_directories()
        
        backend = select_backend()
        download_backend(backend)
        
        create_venv()
        install_dependencies()
        create_config(backend)
        
        print("\nInstallation completed successfully!")
        
    except Exception as e:
        print(f"\nInstallation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_installer()