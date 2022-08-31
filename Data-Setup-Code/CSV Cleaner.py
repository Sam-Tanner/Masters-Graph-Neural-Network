import pandas as pd
#accessess each filwe
for file in ['JOPCS_t.csv','JIFS_t.csv','IJEEEE_t.csv','GIJ_t.csv','AMM_t.csv','JMS_t.csv']:
    #opens each file with panda
    panda = pd.read_csv(file)

    #goes through the pandas index
    for i in panda.index:
        Cur=str(panda['AU'][i]).split(';')[0]
        count = 0
        
        #goes through the remaining pandas index
        for j in range(i,len(panda.index)):
            
            #compares authors between two papers to see if they're identicle
            if Cur==str(panda['AU'][j]).split(';')[0]:
                count +=1
                AU=str(panda['AU'][j]).split(';')
                AU[0]= AU[0]+str(count)
                string = str()
                
                #loops for each author
                for k in range(0,len(AU)):
                    
                    #reformats authors name if repeated so all are unique
                    string = string+AU[k]
                    if k!=len(AU)-1:
                        string = string+'; '
                panda['AU'][j]=string
    #saves changes
    panda=panda.dropna(axis=0,subset=['CR'])
    panda.reset_index()
    print(len(panda.index))
    panda.to_csv(file,index=False)
    print(file)
        

