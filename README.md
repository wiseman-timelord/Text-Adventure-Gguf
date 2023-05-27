<br># Stable-RPG
<br>AI powered role-playing game
<br>
<br>
<br>The game:
<br>The user will choose from set locations: house, street, park, woods, pub, lake, car, van.
<br>In each location, there will be a random set of AI roleplayers present from these choices: gang, police, friends, strangers.
<br>The user will be able to interact with the, environment or AI roleplayers, the AI must then print a response in relevance to the users, actions and speech, with its own actions and speech.
<br>After each response from the AI, the AI must then summarize the, user and AI, actions and speech, this will result in a loop of, 1 user input, then 1 AI response, then 1 AI summary.
<br>The game will end, when the user decides to, end the game and exit, otherwise the roleplay could go on forever.
<br>the locations should be able to be chosen by the user, the user should be able to travel at any point, resulting in a, shuffle of the roleplayers and change of prompts.
<br>
<br>
<br>The plan:
<br>-Create fleshed out scripts from framework already created by GPT4 + VoxScript Plugin, using upto date information from internet.
<br>-Try to get it to work on StableLM, just because this would be both the word Stable in the name, maybe train a new one if I have to..
<br>-Integrate interface, it will be curses to start with then more graphical later for Stable Diffusion Integration from local models.
<br>-Improve memory functions, fur StableLM there will be 4096 context length, this would be good for a 1-2k token memory of events.
<br>-Integrade Sable Diffusion 1.5 output to generate representation of, user and AI, actions as multiple characters in a scene.
<br>
<br>
<br>Models Information:
<br>-StableLM for text generation Model Card = "https://huggingface.co/OpenAssistant/stablelm-7b-sft-v7-epoch-3". 
<br>-Stable Diffusion for text generation Model Card = "https://huggingface.co/runwayml/stable-diffusion-v1-5". 
<br>
<br>
