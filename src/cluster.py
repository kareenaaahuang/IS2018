import math
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.cluster import KMeans
from sklearn import metrics
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

def makeCluster(df, n, rs, cols):
    '''
    Parameters:
    1) df: master data frame
    2) n: number of clusters
    3) rs: random state
    4) cols: list of clustering variables
    '''
    #copy dataframe
    dfCluster = df.copy()

    #fit clusters
    kmeans = KMeans(n_clusters = n, random_state = rs)
    kmeans.fit(dfCluster.loc[:, cols])

    #get location of cluster centroids and label
    center = kmeans.cluster_centers_
    label = kmeans.labels_
    dfCluster['cluster_label'] = label

    #append centroids to data frame
    for a in range(len(center)):
        for b in range(len(center[0])):
            dfCluster['c'+ str(a) + cols[b]] = center[a][b]


    #compute distance to centroids
    distances = defaultdict(list)
    for c in range(len(center)):
        for d in range(len(cols)):
            distances['c'+str(c)+'distance'].append(abs(dfCluster[cols[d]]
                                                        - dfCluster['c'+str(c)+cols[d]]))

    #append distance to centroids to data frame
    for key in distances:
        dfCluster[key] = sum(distances[key])

    #record points closest to centroids
    centroids = defaultdict(list)
    for e in range(len(center)):
        centroids['c'+str(e)].append(dfCluster[dfCluster['c'+str(e)+'distance']
                                               == dfCluster['c'+str(e)+'distance'].min()])

    return dfCluster, centroids

def visualizeCluster(df, n, cols1, cols2):
    '''
    Parameters:
    1) df: dfCluster output by makeCluster()
    2) n: number of clusters
    3) cols1: list of scaled columns
    4) cols2: list of original columns (len(cols2) == len(cols1))
    '''
    dfList = list() #cache list for data frames by cluster labels
    plot = defaultdict(list) #cache dictionary for plots
    for i in range(n):
        dfList.append(df[df['cluster_label'] == i])
        plot['clusters'].append('cluster'+str(i+1))

    for data in dfList:
        for a in range(len(cols1)):
            plot[cols1[a]].append(data[cols1[a]].mean())
            plot[cols2[a]].append(data[cols2[a]].mean())

    #convert to data frame
    dfPlot = pd.DataFrame.from_dict(plot)

    items = plot['clusters']

    options = ['r','g','b','y','purple','grey','pink','black', 'indigo', 'crimson', 'limegreen', 'gold']
    colors = np.random.choice(options, n, replace = False)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20, 8))
    for i in range(len(dfPlot)):
        ax1.scatter(range(len(cols1)), dfPlot[dfPlot['clusters'] == items[i]][cols1].values.reshape(-1,1), color = colors[i], label = items[i], alpha = 0.5)
    for i in range(len(dfPlot)):
        ax2.scatter(range(len(cols2)), dfPlot[dfPlot['clusters'] == items[i]][cols2].values.reshape(-1,1), color = colors[i], label = items[i], alpha = 0.5)
    ax1.set_xticks(range(0, len(cols1), 1))
    ax2.set_xticks(range(0, len(cols2), 1))
    ax1.set_xticklabels(labels = cols1)
    ax2.set_xticklabels(labels = cols2)
    ax1.legend()
    ax2.legend()
    plt.show()

def timeCluster(df, n):
    '''
    Parameters:
    1) df: dfCluster output by makeCluster()
    2) n: number of clusters
    '''
    timeCluster = pd.DataFrame(df.groupby(['session', 'cluster_label'])['index'].count()).reset_index().reset_index()
    cols = dict()
    for i in range(n):
        cols.update({i: 'timeCluster'+str(i+1)})
    cols.update({'session': 'Session'})
    timeCluster = timeCluster.pivot(index = 'session', columns = 'cluster_label', values = 'index').reset_index().rename(columns = cols)
    timeCluster = timeCluster.loc[:, 'Session': 'timeCluster'+str(n)]

    return timeCluster

def removeMissingData(a, b):
    """ takes in two lists and removes rows with missing data """
    x = list(a)
    y = list(b)
    i = len(x) -1
    while(i != -1):  # get rid of missing values
        if x[i] == None or y[i] == None \
        or math.isnan(x[i]) or math.isnan(y[i]):
            del x[i]; del y[i]
        i -= 1
    return (x,y)

def calculate_pvalues(df):
    """ computes the p-value for each correlation """
    #df = df.dropna()._get_numeric_data()
    df = df._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            x,y = removeMissingData(df[r],df[c])
            results = stats.pearsonr(x,y)
            pvalues[r][c] = round(results[1], 4)
            #pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues
