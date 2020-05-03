/*

Worst Channel
Description
You again have the wholesale dataset but this time it is cleaned. Here are the first few rows:﻿
﻿
Each of the columns except for the column 'Channel' tells you the sales for each kind of product and the 'Channel' column tells you which 'Channel' you're selling to. Your task is to find out which of the three channels has the least total sales (for all the products combined). For example, if the total sales to Cafe, Hotel, and Restaurant turn out to be 1 lakh, 2 lakh, and 3 lakh rupees, you need to print 'Cafe' since it has the lowest sales. 
Execution Time Limit
20 seconds



*/

# Import Pandas and read the dataframe
import pandas as pd
import numpy as np
wholesale = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/OqwpypRKN09x5GYej2LvVrprn/Wholesale_Data_Cleaned.csv')

# Write your code here

wholesale["Total"] = wholesale["Fresh"] + wholesale["Milk"] + wholesale["Grocery"] + wholesale["Frozen"] + wholesale["Detergents_Paper"] + wholesale["Delicassen"]
worst_channel = pd.pivot_table(wholesale, values=["Total"], index=["Channel"], aggfunc=np.sum)

worst_channel_name = worst_channel[worst_channel["Total"] == worst_channel["Total"].min()].index[0]
print(worst_channel_name)
