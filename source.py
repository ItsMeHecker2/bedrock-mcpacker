import uuid
import time
import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import shutil
from pathlib import Path

ui= Tk()
ui.title("Minecraft Bedrock/Pocket/Education Pack File Generator")
maingrid = ttk.Frame(ui, padding="3 3 12 12")
maingrid.grid(column=0, row=0, sticky=(N, W, E, S))
ui.columnconfigure(0, weight=1)
ui.rowconfigure(0, weight=1)

#packname entry
packname = StringVar()
packname_field = ttk.Entry(maingrid, width=24, textvariable=packname)
packname_field.grid(column=2, row=1, columnspan=6, sticky=(W))

#description entry
desc_field = StringVar()
desc_field_entry = ttk.Entry(maingrid, textvariable=desc_field, width=24).grid(column=2, row=2, columnspan=6, sticky=(W))

#format version entry: default 2
formatid = IntVar(value=2)
format_entry = ttk.Entry(maingrid, textvariable=formatid, width=4).grid(column=2, row=3, sticky=(W))

#entries for the version id: default 1.0.0
versionid1 = IntVar(value=1)
version_entry1 = ttk.Entry(maingrid, textvariable=versionid1, width=4).grid(column=2, row=4, sticky=(W))
versionid2 = IntVar(value=0)
version_entry2 = ttk.Entry(maingrid, textvariable=versionid2, width=4).grid(column=3, row=4, sticky=(W))
versionid3 = IntVar(value=0)
version_entry3 = ttk.Entry(maingrid, textvariable=versionid3, width=4).grid(column=4, row=4, sticky=(W))

#entries for the minimum engine requirement: default 1.16.2
enginever1 = IntVar(value=1)
engine_entry1 = ttk.Entry(maingrid, textvariable=enginever1, width=4).grid(column=2, row=5, sticky=(W))
enginever2 = IntVar(value=16)
engine_entry2 = ttk.Entry(maingrid, textvariable=enginever2, width=4).grid(column=3, row=5, sticky=(W))
enginever3 = IntVar(value=2)
engine_entry3 = ttk.Entry(maingrid, textvariable=enginever3, width=4).grid(column=4, row=5, sticky=(W))
mcpackfilename = StringVar(value="pack")
mcpackfn_entry = ttk.Entry(maingrid, textvariable=mcpackfilename, width=24).grid(column=2, row=7, columnspan=6, sticky=(W))

dropdown_var = StringVar()
dropdown = ttk.Combobox(maingrid, textvariable=dropdown_var, values=["resources", "skin_pack", "data", "world_template", "script"], state="readonly", width=24).grid(column=2, row=6, columnspan=6, sticky=(W))

def setdir():
    #tkinter file dialog
    global packdir
    packdir = filedialog.askdirectory()
#the packaging script
def package():
    #create v4 UUIDs
    uuid01 = uuid.uuid4()
    uuid02 = uuid.uuid4()
    #define the body of the json file
    manifestdotjson = {
    "format_version": formatid.get(),
    "header": {
        "description": f"{desc_field.get()}",
        "name": f"{packname.get()}",
        "uuid": f"{uuid01}",
        "version": [
            versionid1.get(),
            versionid2.get(),
            versionid3.get()
        ],
        "min_engine_version": [
            enginever1.get(),
            enginever2.get(),
            enginever3.get()
        ]
    },
    "modules": [
        {
            "description": f"{desc_field.get()}",
            "type": f"{dropdown_var.get()}",
            "uuid": f"{uuid02}",
            "version": [
                versionid1.get(),
                versionid2.get(),
                versionid3.get()
            ]
        }
    ]
}
    #print values for debug

    print(desc_field.get())
    print(packname.get())
    print(dropdown_var.get())
    #dump and/or update the json file
    json_object = json.dumps(manifestdotjson, indent=4)
    with open("manifest.json", "w") as outfile:
        outfile.write(json_object)
    #write to the pack directory
    cwd = os.getcwd()
    src_file = os.path.join(cwd, "manifest.json")
    dst_file = os.path.join(packdir, "manifest.json")
    if os.path.exists(dst_file):
        os.remove(dst_file) # remove the existing file if any
        shutil.move(src_file, packdir)
    else:
        shutil.move(src_file, packdir)
    #zip the file and create mcpack
    shutil.make_archive(mcpackfilename.get(), "zip", packdir)
    pack_path = Path(f'{mcpackfilename.get()}.zip')
    pack_path.rename(pack_path.with_suffix('.mcpack'))
    pack_src = os.path.join(cwd, f"{mcpackfilename.get()}.mcpack")
    shutil.move(pack_src, packdir)
#the go button
ttk.Button(maingrid, text="Create Pack", command=package).grid(column=4, row=8, columnspan=2,sticky=(W))
ttk.Button(maingrid, text="Set Directory", command=setdir).grid(column=2, row=8, columnspan=2,sticky=(W))

#the labels for the fields
ttk.Label(maingrid, text="Pack Name").grid(column=1, row=1, sticky=(W))
ttk.Label(maingrid, text="Description").grid(column=1, row=2, sticky=(W))
ttk.Label(maingrid, text="Manifest Format").grid(column=1, row=3, sticky=(W))
ttk.Label(maingrid, text="Version ID").grid(column=1, row=4, sticky=(W))
ttk.Label(maingrid, text="Min Engine Ver").grid(column=1, row=5, sticky=(W))
ttk.Label(maingrid, text="Pack Type").grid(column=1, row=6, sticky=(W))
ttk.Label(maingrid, text="File Name").grid(column=1, row=7, sticky=(W))


#some keybinds and fanciness i took from tkdocs
for child in maingrid.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
packname_field.focus()
ui.bind("<Return>", package)

#start the window
ui.mainloop()