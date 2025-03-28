import shutil
import os
import subprocess
import datetime as dt

images_color_path = "/root/images_Color"
images_depth_path = "/root/images_Depth"
repo_path = "/root/ImageDatasetMapping"
repo_path_color = repo_path + "/images_Color"
repo_path_depth = repo_path + "/images_Depth"

if os.name == 'posix':
    try:
        shutil.copytree(images_color_path, os.path.join(repo_path, "images_Color"))
        shutil.copytree(images_depth_path, os.path.join(repo_path, "images_Depth"))
    except:
        for f in os.listdir(images_color_path): 
            if os.path.isdir(os.path.join(images_color_path, f)):
                try:
                    shutil.copytree(os.path.join(images_color_path, f), os.path.join(repo_path_color, f))
                except:
                    print(f"{f} folder already exists")
                shutil.rmtree(os.path.join(images_color_path, f))


        for f in os.listdir(images_depth_path):
            if os.path.isdir(os.path.join(images_depth_path, f)):
                try:
                    shutil.copytree(os.path.join(images_depth_path, f), os.path.join(repo_path_depth + "", f))
                except:
                    print(f"{f} folder already exists")
                shutil.rmtree(os.path.join(images_depth_path, f))

gitAdd = subprocess.run(["git", "add", "."])
gitCommit = subprocess.run(["git", "commit", "-m", f'"copy and uploaded images on {dt.datetime.now()}"'])
gitPush = subprocess.run(["git", "push"])