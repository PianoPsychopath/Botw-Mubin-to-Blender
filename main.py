import bpy
import os
import datetime
from discord.ext import commands
import discord
import asyncio
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
global obj_file_name
global synctest

@client.event
async def on_ready():
    global synctest
    channel = discord.utils.get(client.get_all_channels(), name="logs")
    
    start_message = await channel.send("Starting Export Process...")
    if synctest == 1:
        await send_discord_message(f"Exported: {obj_file_name}")
        end_time_log = datetime.datetime.now()
        total_time_elapsed = end_time_log - start_time_log
        await start_message.delete()
        await send_discord_message(f"Time elapsed {total_time_elapsed}")
        await client.close()
        
async def send_discord_message(message):
    channel = discord.utils.get(client.get_all_channels(), name="logs")
    if channel:
        await channel.send(message)
        

def start_time():
    """Logs the start time."""
    global start_time_log
    global obj_file_name
    global synctest
    global total_time_elapsed
    total_time_elapsed = 0
    obj_file_name = None
    start_time_log = datetime.datetime.now()
    synctest = 0
    import_dae_files(directory, text_file)
  
def import_dae_files(directory, text_file):    
    with open(text_file, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 1):  # Adjust the step to match every 1th line
        line = lines[i].strip()
        if not line:
            continue  # Skip empty lines

        dae_file = os.path.join(directory, line + ".dae")

        # Check if the DAE file exists.
        if os.path.exists(dae_file):
            # Import the DAE file.
            bpy.ops.wm.collada_import(filepath=dae_file)

            # Find the armature object and rename it.
            armature = None
            for obj in bpy.data.objects:
                if obj.type == 'ARMATURE':
                    armature = obj
                    break

            if armature:
                armature.name = line  # Rename the armature to match the model name

                # Rename the armature hierarchy bones.
                for bone in armature.data.bones:
                    bone.name = bone.name.replace("Armature", line)

            # Print a message to the console.
            print("Model Imported:", dae_file)
        #else:
            # Print an error message for non-existent files.
            #print("Model not found:", dae_file)

    # After all models are imported, call the second script.
    run_second_script()

def run_second_script():
    """Run the second script."""
   # Get the file path to the text file
    global obj_file_name
    global synctest
    # Define the export directory and OBJ file name
    export_dir = "C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/exportedOBJ"
    obj_file_name = os.path.splitext(os.path.basename(filepath))[0] + ".obj"
    obj_file_path = os.path.join(export_dir, obj_file_name)
    synctest = 1
    # Open the text file
    with open(filepath, "r") as f:
        lines = f.readlines()

    # Initialize variables to store transformation, rotation, and scale
    tx, ty, tz = 0.0, 0.0, 0.0
    rx, ry, rz = 0.0, 0.0, 0.0
    sx, sy, sz = 1.0, 1.0, 1.0
    
    decimateval = 1

    # Loop through the lines in the text file
    for i in range(0, len(lines), 8):  # Advance by 8 lines for each armature block
        armature_name = lines[i].strip()
        print("Looking for armature:", armature_name)

        # Get the object from the data if it exists
        armature = bpy.data.objects.get(armature_name)
        if armature:
            print("Found armature:", armature_name)
            # Parse the values for transformation, rotation, and scale
            rx = float(lines[i + 1])
            ry = float(lines[i + 2])
            rz = float(lines[i + 3])
            tx = float(lines[i + 4])
            ty = float(lines[i + 5])
            tz = float(lines[i + 6])
            sx = float(lines[i + 7])
            sy = float(lines[i + 7])
            sz = float(lines[i + 7])

            # Apply transformation, rotation, and scale to the armature
            armature.location = (tx, ty, tz)
            armature.rotation_euler = (rx, ry, rz)
            armature.scale = (sx, sy, sz)
        else:
            print("Armature not found in Blender data:", armature_name)

    print("Writing to dimensions.txt")

    # Export the project as an OBJ file
    bpy.ops.export_scene.obj(filepath=obj_file_path, check_existing=False)

    # Append the dimensions to the existing dimensions.txt file or create a new one
    dimensions_file_path = os.path.join(export_dir, "dimensions_dynamic.txt")
    with open(dimensions_file_path, "a") as dimensions_file:
        # Get all objects in the scene
        objects = bpy.context.scene.objects

        # Initialize min and max coordinates with extreme values
        min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
        max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')

        # Iterate through all objects to find the project dimensions
        for obj in objects:
            if obj.type == 'MESH':
                for vertex in obj.data.vertices:
                    world_coords = obj.matrix_world @ vertex.co
                    min_x = min(min_x, world_coords.x)
                    min_y = min(min_y, world_coords.y)
                    min_z = min(min_z, world_coords.z)
                    max_x = max(max_x, world_coords.x)
                    max_y = max(max_y, world_coords.y)
                    max_z = max(max_z, world_coords.z)

        # Calculate dimensions in meters
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        depth = abs(max_z - min_z)

        # Write dimensions to the file with the OBJ file name as the title
        dimensions_file.write(f"\n{obj_file_name} Dimensions (meters):\n")
        dimensions_file.write(f"Width: {width}m\n")
        dimensions_file.write(f"Height: {height}m\n")
        dimensions_file.write(f"Depth: {depth}m\n")
        """writing out muh coords"""
        # Calculate the center coordinates for the entire exported OBJ
        center_x = (max_x + min_x) / 2
        center_y = (max_y + min_y) / 2
        center_z = (max_z + min_z) / 2
        # Write the center coordinates to the file
        dimensions_file.write(f"Coordinates (meters):\n")
        dimensions_file.write(f"XYZ: {center_x}, ")
        dimensions_file.write(f"{center_y}, ")
        dimensions_file.write(f"{center_z}\n")
        # Calculate the total number of faces
        total_faces = sum([len(obj.data.polygons) for obj in objects if obj.type == 'MESH'])
        # Write the number of vertices and faces to the file
        dimensions_file.write(f"Total Faces: {total_faces} ")
        if total_faces > 999999:
            dimensions_file.write(f"WARNING! Faces exceed 1 MILLION!\n")
            decimateval = 999999 / total_faces
            dimensions_file.write(f"Decimate to:{decimateval}\n")
        else:
            dimensions_file.write(f"\n")

    print(f"Exported OBJ to: {obj_file_path}")
    print(f"Appended dimensions to: {dimensions_file_path}")
    clean_scene()

def clean_scene():
    print("Starting Clear Sequence...")
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

   
    end_time()
    
def end_time():
    
    end_time_log = datetime.datetime.now()
    total_time_elapsed = end_time_log - start_time_log
    print("End time:", end_time_log)
    print("Total time elapsed:", total_time_elapsed)
    synctest = 2
        
if __name__ == "__main__":
    directory = "C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/MODELS"
    text_file = "C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/MUBIN/A-1_Static.txt"
    filepath = "C:/Users/piano/Desktop/BOTWMUBIN-2-BLENDER/MUBIN/NUMBERED/A-1_Static.txt"
    start_message = asyncio.run(send_discord_message("Starting Export Process..."))
    start_time()
    client.run('BOT_TOKEN')    
    

    