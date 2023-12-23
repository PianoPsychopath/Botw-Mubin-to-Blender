# DESCRIPTION

Exports static mubin and dynamic mubin regions into blender in mass. Can also send notification to discord when process is completed

![4kmega_oof](https://github.com/PianoPsychopath/Botw-Mubin-to-Blender/assets/136649946/9f02a341-f3e3-47a2-b49b-0fffdebb4db8)


# SETUP

you might need to do a few powershell/cmd stuff like ```pip install discord```  (just look at the imports from line 1 to 11 and see what you're missing)

The folder must be in your Desktop or readjust the file path:
C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/

**DISCORD ALERT SYSTEM**(it takes a long time sometimes so its nice to have an alert)

![image](https://github.com/PianoPsychopath/Botw-Mubin-to-Blender/assets/136649946/6b964037-a29c-418e-a1f8-4405d95ae046)

-Setup a discord bot in a server.

-Change ```logs``` on line 16 and line 28 to preffered channel

-Change ```BOT_TOKEN``` on line 228 to your bot token

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


![image](https://github.com/PianoPsychopath/Botw-Mubin-to-Blender/assets/136649946/e710fa4b-62e2-4de9-8d7b-e603498f6eba)



Imgae From 
https://objmap.zeldamods.org/#/map/z3,0,0


The txt files where converted from the xml format to csv then converted to txt in a format that was easier for me to work with. 


