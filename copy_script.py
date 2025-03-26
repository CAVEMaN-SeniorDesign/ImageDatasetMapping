import shutil
import os

images_color_path = "/root/images_Color"
images_depth_path = "/root/images_Depth"
repo_path = "/root/ImageDatasetMapping"

try:
    shutil.copytree(images_color_path, os.path.join(repo_path, "images_Color"))
except:
    


