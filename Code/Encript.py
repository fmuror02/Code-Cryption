# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:06:17 2022

@author: fmuror02

Script that encripts in binary a python script.

"""

def Encript():
    
    import string
    import time
    
    printable = list(string.printable) #Get all printable characters.
    
    filename = input('Enter file name:') #Get filename.
    
    try:
        f = open(f'{filename}','r')
        content = f.readlines()
        f.close()
    except:
        print('File does not exist or the name is incorrect.')
        time.sleep(4)
        raise FileNotFoundError('File does not exist or the name is incorrect.')
    
    #Checking if filename is correct or if the file exists.        
    
    
    del f
    f = open(f'crp{filename}.py','w') #Creating new cripted script.
    
    for line in content:
        for i in line:
            code = printable.index(i)
            code = bin(code).replace('0b','')
            print(code,end='#')
            f.write(code+'#')
            
        print()
        f.write('\n')
    
    #Changing characters in script for the binary of the index in the printable characters list and adding it to the new cripted file.
    
    f.close()

Encript()

