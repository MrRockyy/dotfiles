import os 
import shutil 
path='/home/sarch/Downloads' 
file = os.listdir(path)
for f in file:
    formt =  f.split('.')[-1]
    file1=f'{path}/{f}'
    if f == 'docx' or  f == 'images' or f == 'pdf' or f == 'other' or f== 'code' or f == 'Folders':
        pass
    
    elif formt == 'pdf':
         shutil.move(file1,f'{path}/pdf/{f}')
    elif len(f.split('.')) == 1:
        shutil.move(file1,f'{path}/Folders/{f}')
    elif formt == 'png' or formt == 'jpg' or formt == 'git' or formt =='jpeg':
        shutil.move(file1,f'{path}/images/{f}')
    elif formt == 'docx' or formt == 'doc':
         shutil.move(file1,f'{path}/docx/{f}')
    elif formt == 'py' or formt == 'js' or formt == 'html' or formt == 'csv' or formt == 'json' or formt == 'css' or formt == 'sh': 
         shutil.move(file1,f'{path}/code/{f}')

    else:
        shutil.move(file1,f'{path}/other/{f}')

