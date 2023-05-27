<br># Stable-RPG
<br>Version: 000
<br>
<br>
<br>## Overview
<br>Stable-RPG is an AI-powered role-playing game that provides an immersive and interactive text-based gaming experience. The game leverages advanced AI models to create dynamic dialogues and scenarios, offering a unique role-playing experience every time. The user can choose from a variety of realistic locations and interact with a diverse set of AI roleplayers. The game continues indefinitely until the user decides to exit, providing an endless role-playing experience.
<br>
<br>
<br>In each chosen location, a random set of AI roleplayers from various categories like gang members, police, friends, or strangers are present. The user interacts with these AI roleplayers through actions and speech, to which the AI responds accordingly. After each interaction, the AI provides a summary of the actions and speech, creating a continuous loop of user input, AI response, and AI summary.
<br>
<br>
<br>The game utilizes StableLM for text generation, a powerful language model developed by OpenAI, and Stable Diffusion for scene generation, providing a graphical representation of user and AI actions. The game interface initially uses curses and plans to incorporate more graphical elements in future versions for Stable Diffusion Integration from local models.
<br>
<br>
<br>## The Plan
<br>1. Create fleshed out scripts from the framework already created by GPT4 + VoxScript Plugin, using up-to-date information from the internet.
<br>2. Adapt the game to work on StableLM, leveraging its 4096 context length for improved memory functions.
<br>3. Integrate a text user interface using curses, with plans for more graphical elements in the future.
<br>4. Improve memory functions to maintain a 1-2k token memory of events.
<br>5. Integrate Stable Diffusion 1.5 output to generate a graphical representation of user and AI actions.
<br>6. Improve multi-character scenes through scripts to stitch generated characters onto generated scenes.
<br>7. Add an option for scene animation.
<br>
<br>
<br>## Models Information
<br>- StableLM for text generation Model Card: "https://huggingface.co/OpenAssistant/stablelm-7b-sft-v7-epoch-3".
<br>- Stable Diffusion for scene generation Model Card: "https://huggingface.co/runwayml/stable-diffusion-v1-5".
<br>
<br>
