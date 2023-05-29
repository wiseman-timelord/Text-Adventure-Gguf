<br># Stable-RPG
<br>Version: 000-Alpha
<br>
<br>## Overview
<br>Stable-RPG is an AI-powered text-based role-playing game that offers an immersive and interactive gaming experience. The game leverages advanced AI models to create dynamic dialogues and scenarios, providing a unique role-playing experience with every playthrough. The user can choose from a variety of realistic locations and interact with a diverse set of AI roleplayers. The game continues indefinitely until the user decides to exit, offering an endless role-playing experience.
<br>
<br>In each chosen location, a random set of AI roleplayers from various categories like gang members, police, friends, or strangers are present. The user interacts with these AI roleplayers through actions and speech, to which the AI responds accordingly. After each interaction, the AI provides a summary of the actions and speech, creating a continuous loop of user input, AI response, and AI summary.
<br>
<br>The game utilizes StableLM for text generation, a powerful language model developed by OpenAI. The game interface initially uses curses for a text-based interface, with plans to incorporate more graphical elements in future versions.
<br>
<br>## Progress
<br>### Completed
<br>1. Created fleshed out scripts from the framework already created by GPT4 + Plugins.
<br>2. Adapted the game to work on StableLM, leveraging its 4096 context length for improved memory functions.
<br>3. Integrated a text user interface using curses.
<br>4. Developed scripts for game mechanics, user interaction, AI response generation, and game parameters.
<br>5. Created a list of locations and roleplayers for the game.
<br>6. Updated and improved eight scripts that form the backbone of our game.
<br>7. Compiled a new "requirements.txt" file to help in setting up the necessary environment for running the game.
<br>8. Updated the README.md file to provide a comprehensive description of the application, its purpose, gameplay, and the technologies used.
<br>
<br>### To Do
<br>9. Improve memory functions to maintain a 1-2k token memory of events.
<br>10. Further develop and finalize the scripts for game mechanics, user interaction, AI response generation, and game parameters.
<br>11. Test each script individually and as part of the whole system to ensure they function as expected.
<br>12. Integrate the scripts into a cohesive application.
<br>13. Develop the game scenarios, characters, and dialogues further.
<br>14. Refine the AI's responses to ensure they are contextually relevant and enhance the gaming experience.
<br>
<br>## Target Models
<br>- StableLM for text generation Model Card: "https://huggingface.co/OpenAssistant/stablelm-7b-sft-v7-epoch-3".
<br>
<br>## Technologies
<br>The game is developed in Python 3.8.10 on a Windows 10 system. It uses the transformers library for interacting with the StableLM model, and windows-curses for the text-based interface. The game's state is managed using JSON, and the scripts are organized to separate concerns like user interaction, AI response generation, and game mechanics.
<br>
