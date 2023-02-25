#%%
import os

for (dirpath, dirnames, filenames) in os.walk("output/"):
    for filename in filenames:
        if filename[:-3] in dirnames:
            print("Removing", filename)
            os.remove(os.path.join(dirpath, filename))
