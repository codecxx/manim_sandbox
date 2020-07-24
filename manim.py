#!/usr/bin/env python
import manimlib
# import shutil
# import os

# #删除文件残留
# texts_path = r"C:\FromLaptop\manim_sandbox\media\texts"
# Tex_path = r"C:\FromLaptop\manim_sandbox\media\Tex"
# mypath = (texts_path,Tex_path)
# for ipath in mypath:
#     if os.path.exists(ipath):
#         shutil.rmtree(ipath)
#         os.makedirs(ipath)

# def gci(filepath):
# #遍历filepath下所有文件，包括子目录,递归
#   files = os.listdir(filepath)
#   for fi in files:
#       fi_d = os.path.join(filepath, fi)
#       if fi == "partial_movie_files":
#           shutil.rmtree(fi_d)
#           os.makedirs(fi_d)
#           continue
#       if os.path.isdir(fi_d):
#           gci(fi_d)
#
# gci(r"C:\FromLaptop\manim_sandbox\media\videos")



if __name__ == "__main__":

    manimlib.main()