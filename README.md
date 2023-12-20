# DESCRIPTION

Exports static mubin and dynamic mubin regions into blender in mass. Can also send notification to discord with process is completed

https://cdn.discordapp.com/attachments/316759660445040642/1186847705448861746/4kmega_oof.png?ex=6594bd0f&is=6582480f&hm=dbd1012751958db10bdff37b438b40e33f3e1574c1bfbdc4cf90048225d02054&

# SETUP

The folder must be in your Desktop or readjust the file path:
C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/

**DISCORD ALERT SYSTEM**

-Setup a discord bot in a server.

-Change "logs" on line 16 and line 28 to preffered channel

-Change "BOT_TOKEN" on line 228 to your bot token

**MODELS**

Using a tool like SwitchToolBox export your desired models (just trees, just mountains etc) and textures to the "MODELS" Folder
Completed obj will be exported to the "exportedOBJ" folder

**HOW TO USE**

In blender open up scripts and open Main.py

At the very bottom line 224-225 change A-1_Static to your desired region ex: B-4_Static.txt, J-1_Dynamic etc.

Hit run - recommend opening console to see if it froze.

After all processes are done it will delete the model so that you can continue onto another region. Just import obj from the exportedOBJ folder.

**Extra Info**

Regions are labeled A-J with 1-8 for each one. Static basically means terrain, Dynamic means things that temporarily exists like trees (since they can be cut down) or mobs.





