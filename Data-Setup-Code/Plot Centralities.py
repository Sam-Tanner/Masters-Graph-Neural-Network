import pandas as pd
#import matplotlib.pyplot as plt

#reads .csv as dataframe
panda = pd.read_csv(r'JOPCS_Cent1.csv')

#plots a range of centralities
panda[panda['FR']==0].hist('BC',bins=300,figsize=(16,16))
panda[panda['FR']==1].hist('BC',bins=300,figsize=(16,16))

panda[panda['FR']==0].hist('CC',bins=300,figsize=(16,16))
panda[panda['FR']==1].hist('CC',bins=300,figsize=(16,16))

panda[panda['FR']==0].hist('DC',bins=300,figsize=(16,16))
panda[panda['FR']==1].hist('DC',bins=300,figsize=(16,16))

panda[panda['FR']==0].hist('EC',bins=300,figsize=(16,16))
panda[panda['FR']==1].hist('EC',bins=300,figsize=(16,16))

panda[panda['FR']==0].hist('LC',bins=300,figsize=(16,16))
panda[panda['FR']==1].hist('LC',bins=300,figsize=(16,16))