# Text-Adventure-Gguf
Status: Alpha - Not Working, long-term side project.

## Description

Text-Adventure-Gguf is an AI-powered text-based role-playing game that offers an immersive and interactive gaming experience. The game leverages advanced AI models to create dynamic dialogues and scenarios, providing a unique role-playing experience with every playthrough. The user can choose from a variety of realistic locations and interact with a diverse set of AI roleplayers. The game continues indefinitely until the user decides to exit, offering an endless role-playing experience. The game utilizes Fast Small LLM's for text generation, a powerful language model developed by OpenAI. The game interface initially uses curses for a text-based interface, with plans to incorporate more graphical elements in future versions.

## Features
- TBA.

## Usage
1. Use the installer to install the program.
2. Launch the game using the appropriate command or script.
3. Interact with the AI roleplayers through actions and speech, to which the AI responds accordingly.
4. The game continues indefinitely until the user decides to exit.

## Requirements
- Python 3.8.10
- Windows 10.

### Development
Outstanding Areas of Work, use the research notes in `.\docs` to progress the scripts for while implenting the following...
- Decide on AI Model Integration: Choose between switching to StableLM with an 8k context via Hugging Face's transformers or optimizing Llama for the same context size.
- Integrate Stable Diffusion: Add Stable Diffusion to generate scene descriptions (or images), deciding if it’s for the current or future version.
- Enhance Game Mechanics: Implement quests, stat-based combat, expanded inventory, and varied encounters like puzzles.
- Improve the User Interface: Upgrade the TUI with a map display, inventory/stats window, and dynamic time tracking.
- Add Error Handling: Include try-except blocks for file loading, AI responses, and input edge case handling.
- Optimize Performance: Enhance ai_integration.py with batch processing or caching and profile the game loop for bottlenecks.
- backend/model compatibility.
- Increase Configuration Flexibility: Expand persistent.json to allow customizable settings like encounter rates and roamer frequency.

### Structure
```
Text-Adventure-Gguf/
├── launcher.py                (New main entry point)
├── installer.py               (Standalone installer)
├── data/
│   ├── persistent.json        (Game config)
│   └── scripts/               (Consolidated scripts)
│       ├── game_logic.py
│       ├── user_interface.py
│       ├── ai_integration.py
│       └── input_handling.py
└── venv/                      (Virtual environment)
```

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.
