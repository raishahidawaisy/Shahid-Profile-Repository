#Task1: To read csv file using pandas and extracting data in different ways

# import pandas as pd
import pandas as pd

# Case1:making data frame from csv file and setting 3rd column as index column
data = pd.read_csv("pandas_dataframe_c2.csv", index_col ="Run Status") 
  
# retrieving column by loc method 
run_status_pass = data.loc["Pass"]
run_status_fail = data.loc["Fail"]   
print(run_status_pass)
print(run_status_fail)

# Case2:making data frame from csv file and setting first column as Index column 
data = pd.read_csv("pandas_dataframe_c2.csv", index_col ="Test Name") 
  
# retrieving column by loc method 
test_name1 = data.loc[["Test 1","Test 3"]] 
test_name2 = data.loc["Test 10"] 
  
print(test_name1, "\n\n\n", test_name2) 