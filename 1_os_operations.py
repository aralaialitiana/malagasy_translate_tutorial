"""
Simple python script. Execute it and see how it uses your Windows :)

Exercises:
1. This program prints a list of all files in this directory. Change it so the names are printed in separated lines:
'.git'
'.gitignore'
'1_os_operations.py'
...

"""


import os #library for doing stuff related to the operatin system

#Greeting
print("This is my first script")
print("It executes program line-by-line")

currentDirectory = os.getcwd() #same as `dir` in windows and `pwd` in linux
print("Nous sommes dans le repertoire:", currentDirectory)
print("La liste suivante donne la liste des fichiers dans le repertoire encours:")
print(os.listdir())



print("Here it ends")
