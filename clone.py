from git import Repo
import os
import shutil
import stat

def unset_readonly(func, path, exec_info):
  os.chmod( path, stat.S_IWRITE )
  os.unlink( path )

destination_folder = "SNSC3-Translation-master"
repo_link = "https://github.com/salixa/SNSC3-Translation"

if os.path.exists(destination_folder):
  shutil.rmtree(destination_folder, onerror = unset_readonly)
  
Repo.clone_from(repo_link, destination_folder)