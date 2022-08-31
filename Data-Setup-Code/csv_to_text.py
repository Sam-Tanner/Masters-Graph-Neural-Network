 import pandas as pd

#converts csv back to text to allow for use by MetaKnowledge
###############################################################################
#converts JOPCS to .txt

#opens file and imports as a dataframe
JOPCS = pd.read_csv(r'JOPCS_t.csv')
JOPCS = JOPCS.drop_duplicates()
JOPCS = JOPCS.drop("OA",axis=1)
JOPCS.reset_index()


#creates and opens .txt file
with open('JOPCS_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN JOPCS \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in JOPCS.index:
        #loops for each column
        for j in list(JOPCS.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(JOPCS[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(JOPCS[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(JOPCS[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF")
    
###############################################################################
#converts IJEEEE to .txt
IJEEEE = pd.read_csv(r'IJEEEE_t.csv')
IJEEEE = IJEEEE.drop_duplicates()
#IJEEEE = IJEEEE.drop("OA",axis=1)
IJEEEE.reset_index()


#creates and opens .txt file
with open('IJEEEE_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN IJEEEE \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in IJEEEE.index:
        #loops for each column
        for j in list(IJEEEE.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(IJEEEE[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(IJEEEE[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(IJEEEE[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF")
    
###############################################################################
#converts AMM to .txt
AMM = pd.read_csv(r'AMM_t.csv')
AMM = AMM.drop_duplicates()
#AMM = AMM.drop("OA",axis=1)
AMM.reset_index()


#creates and opens .txt file
with open('AMM_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN AMM \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in AMM.index:
        #loops for each column
        for j in list(AMM.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(AMM[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(AMM[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(AMM[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF") 

###############################################################################
#converts JMS to .txt
JMS = pd.read_csv(r'JMS_t.csv')
JMS = JMS.drop_duplicates()
#JMS = JMS.drop("OA",axis=1)
JMS.reset_index()


#creates and opens .txt file
with open('JMS_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN JMS \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in JMS.index:
        #loops for each column
        for j in list(JMS.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(JMS[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(JMS[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(JMS[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF") 
    
###############################################################################
#converts JIF to .txt
JIF = pd.read_csv(r'JIFS_t.csv')
JIF = JIF.drop_duplicates()
JIF = JIF.drop("OA",axis=1)
JIF.reset_index()


#creates and opens .txt file
with open('JIF_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN JIF \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in JIF.index:
        #loops for each column
        for j in list(JIF.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(JIF[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(JIF[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(JIF[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF") 
    
###############################################################################
#converts GIJ to .txt
GIJ = pd.read_csv(r'GIJ_t.csv')
GIJ = GIJ.drop_duplicates()
GIJ = GIJ.drop("OA",axis=1)
GIJ.reset_index()


#creates and opens .txt file
with open('GIJ_t.txt', 'w', encoding="utf-8") as f:
    #writes initail format
    f.write('FN GIJ \n')
    f.write('VR 1.0 \n')
    
    #loops for each index
    for i in GIJ.index:
        #loops for each column
        for j in list(GIJ.columns.values):
            
            #writes each line as per the needed format, with prints for errors
            if j != "source":
                if str(GIJ[j][i])!=' ' and j!='PY':
                    f.write(str(j)+" ")
                    check = 0
                    
                    #splits data as needed and loops for each split
                    for x in str(GIJ[j][i]).split(";"):
                        #print(x)
                        if check == 0:
                            try:
                                f.write(x+"\n")
                                check = 1
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                        else:
                            try:
                                f.write("   "+x+"\n")
                            except:
                                f.write("\n")
                                print("oops ,",str(i),str(j))
                #writes year, or 9999 if not present
                elif j=='PY':
                    try:
                        num = str(int(GIJ[j][i]))
                        output=(str(j)+" "+num)
                        f.write(output+'\n')
                    except:
                        output=(str(j)+" "+(str(9999)))
                        f.write(output+'\n')
        #prints to show progress
        if i%100==0:
            print(i)
        #writes to show end of article
        f.write("ER \n \n")
    #prints last article index and writes to show end of .txt file
    print(i)
    f.write("\n"+"EF") 