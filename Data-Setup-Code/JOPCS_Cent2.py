import metaknowledge as mk
import networkx as nx
import pandas as pd
import numpy as np

#produces networks from reformatted .txt file
RC = mk.RecordCollection("JOPCS_t.txt")

#takes data from .csv file
panda = pd.read_csv(r'JOPCS_FRt.csv')
panda.drop_duplicates()
panda.reset_index()

#runs through each entry (required by variable class)
for r in RC:
    R = r

#prints errors (if any)
print(RC.errors)

#creates a journal citation network
#networkj = RC.networkCitation(nodeType='journal',coreOnly=True)

#creates a series of networks containg core, non-core and mixed networks
network1 = RC.networkCitation(nodeType='full',coreOnly=True)
network1 = nx.Graph(network1)
network1 = network1.to_undirected()

network2 = RC.networkCitation(nodeType='full',coreOnly=False)
network2 = nx.Graph(network2)
network2 = network2.to_undirected()

network3 = nx.compose(network1,network2)

#creates a list of core nodes using centrality dict and a list of sub-graphs for the mixed network
ACent = nx.degree_centrality(network1)
sub_graphs=(network3.subgraph(c).copy() for c in nx.connected_components(network3))

#sets up counter
c=0

#loops for each node in each subgraph
for idx,g in enumerate(sub_graphs,start=1):
    
    #sets up more counters
    count1=0
    count2=0
    count3=0
    
    #ensures only large subgraphs used
    if len(g.nodes())>1000:
        #prints subgraph details and notifies progress as centralities calculated
        print(f"Component {idx}: Nodes: {len(g.nodes())}")
        DCent = nx.degree_centrality(g)
        print('DCent')
        ECent = nx.eigenvector_centrality(g,max_iter=1000)
        print('ECent')
        LCent = nx.load_centrality(g)
        print('LCent')
        CCent = nx.closeness_centrality(g)
        print('CCent')
        BCent = nx.betweenness_centrality(g)
        print('BCent')
        
        #adds all centralities to a dataframe
        panda2 = pd.DataFrame(index=range(0,len(list(DCent.keys()))),columns=['ND','DC','EC','LC','CC','BC'])
        panda2['ND'] = DCent.keys()
        panda2['DC'] = DCent.values()
        panda2['EC'] = ECent.values()
        panda2['LC'] = LCent.values()
        panda2['CC'] = CCent.values()
        panda2['BC'] = BCent.values()
        panda2['FR'] = 0
        #FR = [0]*len(list(DCent.keys()))
        
        #reformats all authors as needed and makes a list of them
        for i in ACent:
            try:
                PA=i.split(',')[0].split(' ')
                AU=[]
                if PA[0]!="":
                    try:
                        AU.append(PA[0]+' '+PA[1]+' '+PA[2]+', '+PA[3])
                        AU.append(PA[0]+' '+PA[1]+', '+PA[2])
                        AU.append(PA[0]+', '+PA[1])
                    except:
                        try:
                            AU.append(PA[0]+' '+PA[1]+', '+PA[2])
                            AU.append(PA[0]+', '+PA[1])
                        except:
                            AU.append(PA[0]+', '+PA[1])
                else:
                    try:
                        AU.append(PA[1]+' '+PA[2]+' '+PA[3]+', '+PA[4])
                        AU.append(PA[1]+' '+PA[2]+', '+PA[3])
                        AU.append(PA[1]+', '+PA[2])
                    except:
                        try:
                            AU.append(PA[1]+' '+PA[2]+', '+PA[3])
                            AU.append(PA[1]+', '+PA[2])
                        except:
                            AU.append(PA[1]+', '+PA[2])
                #print(AU,'1')
            except:
                try:
                    PA=i.split(',')[0]
                    AU.append(str(PA))
                    #print(PA,AU,'2')
                except:
                    PA=i.split(',')[0]
                    AU.append(PA[0])
                    #print(PA,AU,'3')
            #loops through panda index
            for j in range(0,len(panda.index)):
                #loops for each author found
                for author in AU:
                    #checks if any authors match
                    if str(panda['AU'][j]).split(';')[0]==author:
                        #if so checks to see if the author is in both dataframes and is related to fraud
                        try:
                            if panda.at[j,'FR']==1:
                                #if so changes appropriately
                                if sum(panda2['ND']==i)>0:
                                    count3+=1
                                    panda2.at[(panda2['ND']==i),'FR'] = 1
                                #print(panda2.at[(panda2['ND']==i),'FR'])
                                count2+=1
                            count1+=1
                        except:
                            #print('oops')
                            filler=1
        #exports new dataframe for use by machine learning
        c+=1
        print(count1,count2,count3)
        print(idx," has ",panda2['FR'].sum()," cases of citation fraud")
        panda2.to_csv('JOPCS_Cent'+str(c)+'.csv',index=False)
        