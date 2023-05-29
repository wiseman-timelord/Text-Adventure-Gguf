<br># Stable-RPG
<br>Version: 000-Alpha

<br>## Overview
<br>Stable-RPG is an AI-powered text-based role-playing game that provides an immersive and interactive gaming experience. The game leverages advanced AI models to create dynamic dialogues and scenarios, offering a unique role-playing experience every time. The user can choose from a variety of realistic locations and interact with a diverse set of AI roleplayers. The game continues indefinitely until the user decides to exit, providing an endless role-playing experience.

<br>In each chosen location, a random set of AI roleplayers from various categories like gang members, police, friends, or strangers are present. The user interacts with these AI roleplayers through actions and speech, to which the AI responds accordingly. After each interaction, the AI provides a summary of the actions and speech, creating a continuous loop of user input, AI response, and AI summary.

<br>The game utilizes StableLM for text generation, a powerful language model developed by OpenAI, and Stable Diffusion for scene generation, providing a graphical representation of user and AI actions. The game interface initially uses curses for a text-based interface, with plans to incorporate more graphical elements in future versions for Stable Diffusion Integration from local models.

<br>Early versions of the game will be text-only, leveraging local models for text generation and game mechanics. Later versions plan to incorporate multi-character scene image generation through local models, enhancing the immersive experience of the game.

<br>## The Plan
<br>### Done
<br>1. Created fleshed out scripts from the framework already created by GPT4 +, VoxScript & Wolfram & LinkReader, Plugins.
<br>2. Adapted the game to work on StableLM, leveraging its 4096 context length for improved memory functions.
<br>3. Integrated a text user interface using curses.
<br>4. Developed scripts for game mechanics, user interaction, AI response generation, and game parameters.
<br>5. Created a list of locations and roleplayers for the game.

<br>### To Do
<br>6. Improve memory functions to maintain a 1-2k token memory of events.
<br>7. Integrate Stable Diffusion 1.5 output to generate a graphical representation of user and AI actions.
<br>8. Improve multi-character scenes through scripts to stitch generated characters onto generated scenes.
<br>9. Add an option for scene animation.
<br>10. Further develop and finalize the scripts for game mechanics, user interaction, AI response generation, and game parameters.

<br>## Target Models
<br>- StableLM for text generation Model Card: "https://huggingface.co/OpenAssistant/stablelm-7b-sft-v7-epoch-3".
<br>- Stable Diffusion for scene generation Model Card: "https://huggingface.co/runwayml/stable-diffusion-v1-5".

<br>## Technologies
<br>The game is developed in Python 3.8.10 on a Windows 10 system. It uses the transformers library for interacting with the StableLM model, and windows-curses for the text-based interface. The game's state is managed using JSON, and the scripts are organized to separate concerns like user interaction, AI response generation, and game mechanics.
