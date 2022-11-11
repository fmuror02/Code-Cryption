# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:43:33 2022

@author: fmuror02

Script that decripts from binary encripted code.

"""

def Decript():
    
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
    f = open('nsscscript.py','w') #Creating new cripted script.
    
    for i in content:
        binary = i.split('#')
        lines = []
        
        for line in binary:
            line = line.replace('\n','')
            lines.append(line)
    
        lines.remove('')
        
        for n in lines:
            dec = int(n,2)
            codeline = printable[dec]
            f.write(codeline)
            print(codeline,end='')
            
        f.write('\n')  
        
    #Changing binary characters in script for the ASCII of the index in the printable characters list and adding it to the new cripted file.        

    f.close()    
        
        
Decript()


    