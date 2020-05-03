/*

Data Quality
Description
You have a Wholesale Customers dataset. Here are the first few rows of the dataset:
﻿
﻿The last column 'Channel' contains information about the type of channel the items are supplied to. There are only three types of channels - 'Hotel', 'Restaurant', and 'Cafe'. But as you can notice, there are quality issues in the last data. A lot of the times Cafe as been written as 'C', Hotel has been written as 'Hot', etc. Inspect these incorrect values and replace them with their actual full names. 


After this operation, the final column should only have 3 kinds of label - 'Hotel', 'Restaurant', and 'Cafe'. 

The dataframe has already been read to you in the variable 'wholesale'.

The print statement to print the final dataframe has also been provided. You just need to perform the operations for correcting the names present in the last column.
Execution Time Limit
20 seconds


*/

# Importing the Pandas package and reading the data
import pandas as pd
wholesale = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/OkbnaOBqrBXZOpRQw1JGMgaM9/Wholesale_Data.csv')

# Write your code here. Make sure that you change the values in the column 'Channel' inplace. 

wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Cafe" if x == "C" else x)
wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Cafe" if x == "Caffe" else x)

wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Hotel" if x == "H" else x)
wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Hotel" if x == "Hote" else x)
wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Hotel" if x == "Hot" else x)

wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Restaurant" if x == "R" else x)
wholesale["Channel"] = wholesale["Channel"].astype(str).apply(lambda x: "Restaurant" if x == "Rest" else x)



# The final print statement. Please don't edit this part. Also don't write any other
# print statement otherwise your answer will not match even if it is correct
print(wholesale['Channel'].value_counts())
