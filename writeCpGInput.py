import pandas as pd
import glob
import os


path = '/Users/chuyangzhang/Downloads/20230607-Bioinformatics/'

filenames = glob.glob(path+ "/*.xlsx")

f = open("allSeq.fa", "w")

for file in filenames:
    # skip the last two rows
    df1 = pd.read_excel(file, usecols=['Name of Sequence', 'Full Promoter Sequence'], skipfooter=2)
    df1 = df1.dropna().reset_index(drop=True)

    for i in range(len(df1['Name of Sequence'])):
        # get rid of ".xlsx" part
        name = os.path.basename(file)[:-5]
        name = ">" + name + " " + df1['Name of Sequence'][i] + "\n"
        seq = df1['Full Promoter Sequence'][i] + "\n"
        f.write(name)
        f.write(seq)
        f.write("\n")

f.close()
