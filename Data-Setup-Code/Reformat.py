import pandas as pd

#lists and variable setup
header = ['PT', 'AU', 'BA', 'BE', 'GP', 'AF', 'BF', 'CA', 'TI', 'SO',
          'SE', 'BS', 'LA', 'DT', 'CT', 'CY', 'CL', 'SP', 'HO', 'DE',
          'ID', 'AB', 'C1', 'RP', 'EM', 'RI', 'OI', 'FU', 'FX', 'CR',
          'NR', 'TC', 'Z9', 'U1', 'U2', 'PU', 'PI', 'PA', 'SN', 'EI',
          'BN', 'J9', 'JI', 'PD', 'PY', 'VL', 'IS', 'PN', 'SU', 'SI',
          'MA', 'BP', 'EP', 'AR', 'DI', 'D2', 'PG', 'WC', 'SC', 'GA',
          'UT', 'PM', 'OA', 'HC', 'HP', 'DA']

headers = ['Publication Type', 'Authors', 'Book Authors', 'Book Editors',
           'Book Group Authors', 'Author Full Names', 'Book Author Full Names',
           'Group Authors', 'Article Title', 'Source Title', 'Book Series Title',
           'Book Series Subtitle', 'Language', 'Document Type', 'Conference Title',
           'Conference Date', 'Conference Location', 'Conference Sponsor',
           'Conference Host', 'Author Keywords', 'Keywords Plus', 'Abstract',
           'Addresses', 'Reprint Addresses', 'Email Addresses',
           'Researcher Ids', 'ORCIDs', 'Funding Orgs',
           'Funding Text', 'Cited References', 'Cited Reference Count',
           'Times Cited, WoS Core', 'Times Cited, All Databases', '180 Day Usage Count',
           'Since 2013 Usage Count', 'Publisher', 'Publisher City', 'Publisher Address',
           'ISSN', 'eISSN', 'ISBN', 'Journal Abbreviation', 'Journal ISO Abbreviation',
           'Publication Date', 'Publication Year', 'Volume', 'Issue', 'Part Number',
           'Supplement', 'Special Issue', 'Meeting Abstract', 'Start Page', 'End Page',
           'Article Number', 'DOI', 'Book DOI',
           'Number of Pages', 'WoS Categories', 'Research Areas',
           'IDS Number', 'UT (Unique WOS ID)', 'Pubmed Id', 'Open Access Designations',
           'Highly Cited Status', 'Hot Paper Status', 'Date of Export']

header_dict={}

#fills dict using appropriate lists
for i in range(0,len(headers)):
    header_dict[headers[i]]=header[i]
    
#reformats JOPCS files
xls = pd.ExcelFile('JOPCS.xls')
df1 = pd.read_excel(xls, 'savedrecs')

JOP = df1
JOP.reset_index()
JOP = JOP[headers]
JOP = JOP.rename(header_dict,axis=1)
JOP.to_csv("JOPCS.csv", index=False)

###################################
#reformats AMM files
xls = pd.ExcelFile('AMM.xls')
df1 = pd.read_excel(xls, 'savedrecs')

AMM = df1
AMM.reset_index()
AMM = AMM[headers]
AMM = AMM.rename(header_dict,axis=1)
AMM.to_csv("AMM.csv", index=False)

###################################
#reformats JMS files
xls = pd.ExcelFile('JMS.xls')
df1 = pd.read_excel(xls, 'savedrecs')

JMS = df1
JMS.reset_index()
JMS = JMS[headers]
JMS = JMS.rename(header_dict,axis=1)
JMS.to_csv("JMS.csv", index=False)

###################################
#reformats JIFS files
xls = pd.ExcelFile('JIFS1.xls')
df1 = pd.read_excel(xls, 'savedrecs')
xls = pd.ExcelFile('JIFS2.xls')
df2 = pd.read_excel(xls, 'savedrecs')
xls = pd.ExcelFile('JIFS3.xls')
df3 = pd.read_excel(xls, 'savedrecs')

JIF = pd.concat((df1,df2))
JIF = pd.concat((JIF,df3))
JIF.reset_index()
JIF = JIF[headers]
JIF = JIF.rename(header_dict,axis=1)
JIF.to_csv("JIFS.csv", index=False)

###################################
#reformats GJI files
xls = pd.ExcelFile('GJI1.xls')
df1 = pd.read_excel(xls, 'savedrecs')
xls = pd.ExcelFile('GJI2.xls')
df2 = pd.read_excel(xls, 'savedrecs')


GJI = pd.concat((df1,df2))
GJI.reset_index()
GJI = GJI[headers]
GJI = GJI.rename(header_dict,axis=1)
GJI.to_csv("GIJ.csv", index=False)
#print(list(GJI.columns.values))

###################################
#reformats IJEEEE files
xls = pd.ExcelFile('IJEEEE.xls')
df1 = pd.read_excel(xls, 'savedrecs')

IJE = df1
IJE.reset_index()
IJE = IJE[headers]
IJE = IJE.rename(header_dict,axis=1)
IJE.to_csv("IJEEEE.csv", index=False)