# Working with Files in Python

## What was learnt

Retrieve file properties  
Create directories  
Delete files and directories  
Copy, move, or rename files and directories  
Traverse directories

os.walk() returns three values on each iteration of the loop:

 - The name of the current folder
 - A list of folders in the current folder
 - A list of files in the current folder

On each iteration, it prints out the names of the subdirectories and files.
To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk().

## Operations with code samples

To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the directory you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. Here is how to delete a folder:


import os

trash_dir = 'my_documents/bad_dir'  
try:
~ os.rmdir(trash_dir)
except OSError as e:
~ print(f'Error: {trash_dir} : {e.strerror}')

Let’s suppose you want to find .txt files that meet certain criteria.

for filename in os.listdir('.'):  
~ if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
~~ print(filename)  

Resource: https://realpython.com/working-with-files-in-python/  
Quiz: https://realpython.com/quizzes/working-with-files-in-python/

