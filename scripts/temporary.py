# Filename: scripts/temporary.py
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
VENV_DIR = BASE_DIR / "venv"
TEMP_DIR = DATA_DIR / "temp"

# Backend configurations
BACKEND_OPTIONS = {
    "CPU-AVX2": {
        "url": "https://github.com/ggml-org/llama.cpp/releases/download/b4873/llama-b4873-bin-win-avx2-x64.zip",
        "dest": "llama-avx2-bin",
        "cli_path": "llama-avx2-bin/llama-cli.exe"
    },
    "CPU-Basic": {
        "url": "https://github.com/ggml-org/llama.cpp/releases/download/b4873/llama-b4873-bin-win-noavx-x64.zip",
        "dest": "llama-noavx-bin",
        "cli_path": "llama-noavx-bin/llama-cli.exe"
    }
}

# Persistent config template
CONFIG_TEMPLATE = {
    "model_settings": {
        "model_dir": "models",
        "model_file": "text-adventure.gguf",  # Default model
        "context_size": 8192,
        "llama_cli_path": "",
        "starting_location": "house"
    },
    "backend_config": {
        "backend_type": "",
        "llama_bin_path": ""
    }
}

REQUIREMENTS = ["llama-cpp-python", "nltk", "windows-curses"]