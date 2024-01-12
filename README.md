# Minecraft Bedrock Pack Creator / Manifest Editor


## Simple manifest.json generator and pack creator
something i cooked up while bored and modding minecraft bedrock.

## Features:
- It can generate the required ``manifest.json`` file for your Minecraft packs by user input
- It can generate pack **UUID**s for you in said manifest file.
- Several different pack types supported, like ``data``, or ``resources``.
- It can replace the existing ``manifest.json``, in case you want to use it to package an existing pack you opened instead of making one ground-up.
- Automatically zips and converts to ``.mcpack`` using the set mod directory.
- GUI powered by Tkinter for ease of use.
- Herobrine finally removed.

## How to use:
Pretty simple. Just run the exe. It should open a debug console, as well as the GUI. 
Now, click "Set Directory". Set this to wherever the manifest.json will be placed. The hieracry should be:

**Downloads (or wherever the main folder is)/**


**├─ mod_folder/**  <----- set the directory here


**│  ├─ textures (or whatever folders you need)/**


**│  │  ├─ example.png**

Next, change any of the fields to what you need.
**│  ├─ manifest.json**


**│  ├─ pack_icon.png**

Now just edit the fields to whatever you need. the program will handle the placing of this info and the uuids.
> [!NOTE]
>Manifest format is 1 for skin packs, and it is 2 for anything else!.

The last step is to click "Create Pack" This will create the pack and place it in the same source directory.

That's it!
