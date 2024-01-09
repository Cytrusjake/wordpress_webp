import os
from PIL import Image
import PIL
import os
import glob


path = "ABSOLUTE_PATH_TO_UPLOADS_DIR"

for dirpath, dirs, files in os.walk(path):
        for File in files:
                Name, Ext = os.path.splitext(File)

                if(Ext == '.jpeg' or Ext == '.jpg' or Ext == '.png'):
                        try:

                                image = Image.open(dirpath+'/'+File)
                                image = image.convert('RGB')
                                image.save(dirpath+'/'+File+'.webp', 'webp')
                                #print(dirpath+'/'+File+'.webp')
                        except:
                                print(dirpath+'/'+File)
