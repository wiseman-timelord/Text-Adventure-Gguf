# Stable-RPG
Status: Alpha.

## Description

Stable-RPG is an AI-powered text-based role-playing game that offers an immersive and interactive gaming experience. The game leverages advanced AI models to create dynamic dialogues and scenarios, providing a unique role-playing experience with every playthrough. The user can choose from a variety of realistic locations and interact with a diverse set of AI roleplayers. The game continues indefinitely until the user decides to exit, offering an endless role-playing experience. The game utilizes StableLM for text generation, a powerful language model developed by OpenAI. The game interface initially uses curses for a text-based interface, with plans to incorporate more graphical elements in future versions.

## Features
- TBA.

## Usage
1. Use the installer to install the program.
2. Launch the game using the appropriate command or script.
3. Interact with the AI roleplayers through actions and speech, to which the AI responds accordingly.
4. The game continues indefinitely until the user decides to exit.

## Requirements
- Developed in Python 3.8.10 on a Windows 10 system.

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
