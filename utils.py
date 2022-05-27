import pandas as pd
import numpy as np
from pprint import pprint
data_file_path = ""
csv_file_name = "Austin Bicycle Crashes 2010-2017.csv"
dataset = pd.read_csv(data_file_path+csv_file_name)

# store the fields in another csv file
data_file_path = ""
csv_file_name = "Austin Bicycle Crashes 2010-2017.csv"

def save_df_csv(csv_str, file_name, path=""):
	f = open(path+file_name, "w")
	f.write(csv_str)
	f.close()

li = list(dataset.columns)
df = pd.DataFrame(li, columns=["fields"])
save_df_csv(df.to_csv(index=False, line_terminator="\n"), "fields before grouping.csv")


file_path = "data fields grouping.csv"
super_grp = pd.read_csv(file_path)
super_grp = {grp_name: super_grp[grp_name].dropna() for grp_name in super_grp}

# check
from functools import reduce
grp_set = reduce(lambda acm, cur: acm.union(cur), [super_grp[n] for n in super_grp], set())
assert(set([n for n in dataset]).difference(grp_set) == set())
pprint(super_grp)

