import pandas as pd
from itertools import combinations

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



def getColumns(df):
    cols = [c for c in list(df) if df[c].nunique() <= 3 and df[c].nunique() != 0]
    return cols

def getCombinations(df):
    cols = getColumns(df)
    totalcombs = []
    for i in range(1,len(cols)):
        combs = combinations(cols,i)
        for i in list(combs):
            #print(i)
            totalcombs.append(i)
    return totalcombs


def getClusters(combination,df):
    grouped = df.groupby(combination)
    grname = []
    columns_name = []
    missingcounts = []
    record_counts = []
    indcount = []
    i = 0

    originalcols = []
    originalcols.append('group')
    originalcols.append('columns')
    originalcols.append('Total record count')
    for col in df.columns:
        originalcols.append(col)

    for name, group in grouped:
        grname.append("".join(str(name)))
        columns_name.append(combination)
        record_counts.append(group.count().max())

    countdf = pd.DataFrame(index=range(0, len(grouped)), columns=originalcols)

    for col in df.columns:
        indcount = []
        for name, group in grouped:
            indcount.append((group.count().max() - group.count())[col])
        missingcounts.append(indcount)
        countdf[col] = indcount
    countdf['group'] = grname
    countdf['columns'] = columns_name
    countdf['Total record count'] = record_counts
    return countdf


def missing_main_final(path):
    df = pd.read_csv (path)
    #finaldf = pd.DataFrame(columns=originalcols)
    combinations = getCombinations(df)
    frames = []
    for comb in combinations:
        tempdf = getClusters(comb,df)
        frames.append(tempdf)

    finaldf = pd.concat(frames)

    finaldf.reset_index(drop=True,inplace=True)
    return finaldf

def missing_main(path):
    df = pd.read_csv (path)
    #finaldf = pd.DataFrame(columns=originalcols)
    combinations = getCombinations(df)

    tempdf = getClusters(combinations[6])
    #frames.append(tempdf)

    #finaldf = pd.concat(frames)
    #print(finaldf)
    #finaldf.to_excel("clusters.xlsx")
    return tempdf
