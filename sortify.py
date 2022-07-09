from distutils import extension
import os
import shutil
import json
import datetime

execpath = os.path.join(os.path.dirname(__file__))

def load_config(config):
    global execpath
    with open(os.path.join(execpath, "configs", f"{config}.json")) as file:
        return json.load(file)

def create_new_path(old_path: str, dest_path: str) -> str:
    basename = os.path.basename(old_path)
    name, ext = os.path.splitext(basename)
    i = 1
    # This will start the renaming with i = 2 which is the Windows default
    while os.path.exists(os.path.join(dest_path, basename)):
        i += 1
        basename = f"{name} ({i}){ext}"
    return os.path.join(dest_path, basename)

def match_items(items: list, match_by: dict) -> list:
    matches = []
    for item in items:
        if "ext" in match_by and os.path.isfile(item):
            if any(item.endswith("." + ext) for ext in match_by["ext"]): matches.append(item)
            continue
        if "contains" in match_by and os.path.isdir(item):
            if len(match_items([os.path.join(item, child) for child in os.listdir(item)], match_by["contains"])) > 0: matches.append(item)
            continue
        if "type" in match_by:
            if match_by["type"] == "file" and os.path.isfile(item): matches.append(item)
            if match_by["type"] == "dir" and os.path.isdir(item): matches.append(item)
            continue
    return matches

def sort(config = "default", log = 1):
    rules = load_config(config)
    path = os.getcwd()
    items = [os.path.join(path, item) for item in os.listdir(path)]
    start_time = datetime.datetime.now()
    if log == 1: file = open(os.path.join(execpath, "logs", str(f"{config}-{start_time.strftime('%Y%m%d-%H%M%S')}.log")), "w")

    for rule in rules:
        matches = match_items(items, rule["match"])
        items = [item for item in items if item not in matches]

        for match in matches:
            dest = create_new_path(match, rule["dest"])
            if not os.path.exists(os.path.dirname(dest)):
                os.mkdir(os.path.dirname(dest))

            outtext = f"Sorted> {match} -> {dest}"
            if log == 1: file.write(outtext + "\n")
            print(outtext)

            shutil.move(match, dest)
    if log == 1: file.close() 
    time = datetime.datetime.now() - start_time
    print(f"===> Sorting finished in {time.microseconds}ms <===")