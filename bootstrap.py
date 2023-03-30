import subprocess
import shutil
import os
import sys
import argparse
import json

SOURCE = "https://github.com/kenk2/next-config/archive/refs/heads/main.zip"
ZIP_NAME = "main.zip"

parser = argparse.ArgumentParser(
    prog="NextBoot: Next.JS project bootstrapper",
    description="CLI interface that bootstraps a custom Next.js React Project")

parser.add_argument(
    "name",
    type=str,
    help="Name of the project. Initializes directory and project name to parameter. Aborts if directory/project already exists.")
args = parser.parse_args()

if os.path.exists(args.name):
    raise FileExistsError(f'Directory "{args.name}" already exists. Aborting.')

EXTRACT_PATH = os.path.join(args.name, "next-config-main")

subprocess.run(f"curl -LO {SOURCE}", shell=True)
shutil._unpack_zipfile(ZIP_NAME, args.name)

for path in os.listdir(EXTRACT_PATH):
    try:
        shutil.move(os.path.join(EXTRACT_PATH, path), args.name)
    except:
        pass

try:
    shutil.rmtree(EXTRACT_PATH)
    os.remove(ZIP_NAME)

    file = open(os.path.join(args.name, "package.json"), 'r+')
    data = json.load(file)
    data['name'] = args.name
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()
    file.close()

    subprocess.run('yarn', cwd=args.name, shell=True)
finally:
    print(f"Next is ready to go in directory {args.name}!")