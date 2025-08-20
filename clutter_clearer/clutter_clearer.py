import os
def clutter_clearer(*format,directory_path):
 try:  
  mainlist=os.listdir(directory_path)
  if format==("all",):
   for i in range(len(mainlist)):
    extension=os.path.splitext(mainlist[i])[-1]
    os.rename(f"{directory_path}\\{mainlist[i]}",f"{directory_path}\\{i+1}{extension}{extension}")  
  else:
   for i in range(len(format)):
    l=[extension for extension in mainlist if extension.endswith(f'{format[i]}')]   
    for index in range(len(l)):
     ex=os.path.splitext(l[index])[-1]
     os.rename(f"{directory_path}\\{l[index]}",f"{directory_path}\\{index+1}{ex}{ex}")
 except FileExistsError:
  print('The following command already perform or a file already exists\nPlease recheck the directory or format')

def corrector(arg,path):
 l=str(arg).split('/')
 maintp=tuple(l)
 maindict={"directory_path":f'{path}'}
 return clutter_clearer(*maintp,**maindict)







