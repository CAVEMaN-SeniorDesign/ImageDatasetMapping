import shutil
import os

images_color_path = "/root/images_Color"
images_depth_path = "/root/images_Depth"
repo_path = "/root/ImageDatasetMapping"

try:
    shutil.copytree(images_color_path, os.path.join(repo_path, "images_Color"))
    shutil.copytree(images_depth_path, os.path.join(repo_path, "images_Depth"))
except:
    for f in os.listdir(images_color_path): 
        if os.path.isdir(os.path.join(images_color_path, f)):
            try:
                shutil.copytree(os.path.join(images_color_path, f), os.path.join(repo_path, f))
                shutil.rmtree(os.path.join(images_color_path, f))
            except:
                print(f"{f} folder already exists")


    for f in os.listdir(images_depth_path):
        if os.path.isdir(os.path.join(images_depth_path, f)):
            try:
                shutil.copytree(os.path.join(images_depth_path, f), os.path.join(repo_path, f))
                shutil.rmtree(os.path.join(images_depth_path, f))
            except:
                print(f"{f} folder already exists")