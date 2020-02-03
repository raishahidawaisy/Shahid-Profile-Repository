#Task1: To change list/dictionary to dataframe and remove columns and rows

# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Hello', 'to', 'all', 'Devs']
 
# Calling DataFrame constructor on list
lst_df = pd.DataFrame(lst)
print(lst_df)

# create a dictionary with five fields each 
data = { 
    'A':['A1', 'A2', 'A3', 'A4', 'A5'],  
    'B':['B1', 'B2', 'B3', 'B4', 'B5'],  
    'C':['C1', 'C2', 'C3', 'C4', 'C5'],  
    'D':['D1', 'D2', 'D3', 'D4', 'D5'],  
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] } 
  
# Convert the dictionary into DataFrame  
data_df = pd.DataFrame(data) 
print(data_df)

# Remove column name 'A' 
mod1_data_df = data_df.drop(['B', 'C'], axis = 1) 
print(mod1_data_df)

#print(lst_df)
#print(data_df)

# Remove two columns name is 'C' and 'D' 
#data_df.drop(['C', 'D'], axis = 1) 

mod2_data_df = data_df.drop(columns =['A','D'])
print(mod2_data_df)

mod3_data_df = data_df.drop(data_df.loc[:, 'A':'C'].columns, axis = 1)
print(mod3_data_df)

mod4_data_df = data_df.drop([2,3])
print(mod4_data_df)


