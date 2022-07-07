import os 
import random
path= '/home/sarch/Pictures/wallpapers'
contenido = os.listdir(path)
a=len(contenido)
print(a)
num=random.randint(0,a-1)
print(num)
os.system(f'feh --bg-scale /home/sarch/Pictures/wallpapers/"{contenido[num]}"')

