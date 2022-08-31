import csv
import pandas as pd

#reformats the citation information
###############################################################################
#reformats the IJEEEE files citation information
with open('IJEEEE.txt', encoding="utf-8") as f:
    lines = f.readlines()
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
IJEEE = pd.read_csv("IJEEEE.csv")    
IJEEE['CR'] = CR_rows
IJEEE.to_csv("IJEEEE_t.csv", index=False)    

###############################################################################
#reformats the JOPCS files citation information
with open('JOPCS1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    
with open('JOPCS2.txt', encoding="utf-8") as f:
    lines2 = f.readlines()

for i in lines2:
    lines.append(i)
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
JOPCS = pd.read_csv("JOPCS.csv")    
JOPCS['CR'] = CR_rows
JOPCS.to_csv("JOPCS_t.csv", index=False)    

###############################################################################
#reformats the AMM files citation information
with open('AMM1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    
with open('AMM2.txt', encoding="utf-8") as f:
    lines2 = f.readlines()
    
for i in lines2:
    lines.append(i)
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
AMM = pd.read_csv("AMM.csv")    
AMM['CR'] = CR_rows
AMM.to_csv("AMM_t.csv", index=False)

###############################################################################
#reformats the JMS files citation information
with open('JMS1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    
with open('JMS2.txt', encoding="utf-8") as f:
    lines2 = f.readlines()
    
for i in lines2:
    lines.append(i)
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
JMS = pd.read_csv("JMS.csv")    
JMS['CR'] = CR_rows
JMS.to_csv("JMS_t.csv", index=False)

###############################################################################
#reformats the JIFS files citation information
with open('JIFS1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    
for k in ['2','3','4','5','6']:
    with open('JIFS'+k+'.txt', encoding="utf-8") as f:
        lines2 = f.readlines()
        
    for i in lines2:
        lines.append(i)
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
JIF = pd.read_csv("JIFS.csv")    
JIF['CR'] = CR_rows
JIF.to_csv("JIFS_t.csv", index=False)

###############################################################################
#reformats the GJI files citation information
with open('GJI1.txt', encoding="utf-8") as f:
    lines = f.readlines()
    
for k in ['2','3','4']:
    with open('GJI'+k+'.txt', encoding="utf-8") as f:
        lines2 = f.readlines()
        
    for i in lines2:
        lines.append(i)
        
#sets up variables 
CR_rows = []
check2 = 0
count=0

#loops for each line
for i in range(0,len(lines)):
    #checks line holds data
    if len(lines[i])>1:
        #checks line holds citation information
        if (lines[i])[:2] == 'CR':
            
            #sets up additional variables 
            check1 = 1
            check2 = 1
            CR_row = str()
            j=0
            
            #loops while using citation information
            while check1 == 1:
                #appends all current citation information with new loops information
                CR_row = CR_row+str((lines[i+j])[3:-2])+'; '
                
                #makes sure next line is still citation information or ends loop
                if (lines[i+j+1])[:2] != '  ':
                    check1 = 0
                j+=1
        #checks that citation data is recorded for a given article
        if (lines[i])[:2] == 'ER':
            count+=1
            #if not fills with nan value
            if check2 == 0:
                CR_rows.append('nan')
            #if so adds all appended citation information without the final +'; '
            else:
                CR_rows.append(CR_row[:-2])
            check2 = 0
print(count)
#saves files
GJI = pd.read_csv("GIJ.csv")    
GJI['CR'] = CR_rows
GJI.to_csv("GIJ_t.csv", index=False)
