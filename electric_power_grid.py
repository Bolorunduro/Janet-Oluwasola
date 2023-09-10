# -*- coding: utf-8 -*-
"""Electric Power Grid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kAoBKUcZUZdlDjMPXm0ouX6EJkKggHTS
"""

import numpy as np
import random
import networkx as nx
from IPython.display import Image
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import seaborn as sns
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics as skm
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

pip install networkx

n=4941
m = 6594
G=nx.read_gml('power.gml', label=None) #label="label"


pos = nx.spring_layout(G)
nx.draw(G, cmap = plt.get_cmap('rainbow'), with_labels=True, pos=pos)

G =nx.read_gml('power.gml',label=None) #lable="label"
n = G.number_of_nodes()
m = G.number_of_edges()

print("Number of nodes: %d" % n)
print("Number of edges: %d" % m)
print("Number of connected components: %d" % nx.number_connected_components(G))



plt.figure(figsize=(12,8))
nx.draw(G)
plt.gca().collections[0].set_edgecolor("#000000")

# Remove 20% of the edges
proportion_edges = 0.2
edge_subset = random.sample(G.edges(), int(proportion_edges * G.number_of_edges()))

# Create a copy of the graph and remove the edges
G_train = G.copy()
G_train.remove_edges_from(edge_subset)



plt.figure(figsize=(12,8))
nx.draw(G_train)
plt.gca().collections[0].set_edgecolor("#000000") # set node border color to black

edge_subset_size = len(list(edge_subset))
print("Number of edges deleted : %d" % edge_subset_size)
print("Number of edges remaining : %d" % (m - edge_subset_size))

from sklearn.metrics import classification_report, roc_auc_score
from sklearn.metrics import classification_report, roc_curve, roc_auc_score

# Make prediction using Jaccard Coefficient
pred_jaccard = list(nx.jaccard_coefficient(G_train))
score_jaccard, label_jaccard = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_jaccard])

# Make prediction using jaccard coefficient
pred_jaccard = list(nx.jaccard_coefficient(G_train))
score_jaccard, label_jaccard = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_jaccard])

# Compute the ROC AUC Score
fpr_jaccard, tpr_jaccard, _ = roc_curve(label_jaccard, score_jaccard)
auc_jaccard = roc_auc_score(label_jaccard, score_jaccard)

# Prediction using Adamic Adar
pred_adamic = list(nx.adamic_adar_index(G_train))
score_adamic, label_adamic = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_adamic])

# Compute the ROC AUC Score
fpr_adamic, tpr_adamic, _ = roc_curve(label_adamic, score_adamic)
auc_adamic = roc_auc_score(label_adamic, score_adamic)

# Prediction using Preferential Attachment
pred_pref = list(nx.preferential_attachment(G_train))
score_pref, label_pref = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_pref])

# Compute the ROC AUC Score
fpr_pref, tpr_pref, _ = roc_curve(label_pref, score_pref)
auc_pref = roc_auc_score(label_pref, score_pref)

print("Jaccard Model Accuracy:", auc_jaccard )
print("Adamic Adar Model Accuracy:", auc_adamic)
print("Preferential Attachment Model Accuracy",auc_pref)
plt.title('Similarity (Test set)')
plt.xlabel('Electric Power Grid')
plt.ylabel('Accuracy')
plt.show()



from networkx.algorithms.link_prediction import preferential_attachment
print("Jaccard Model Accuracy:", auc_jaccard )
print("Adamic Adar Model Accuracy:", auc_adamic)
print("Preferential Attachment Model Accuracy",auc_pref)

plt.figure(figsize=(8,5))

plt.title('Similarity (Test set)', fontdict={'fontweight':'bold','fontsize':22})

import numpy as np
import matplotlib.pyplot as plt

x =np.arange(0, 5, 0.8)
y= np.sin(x)
plt.plot(x,y)

x= plt.xlabel('Electric Power Grid',fontdict={'fontweight':'bold','fontsize':15})
y= plt.ylabel('Accuracy',fontdict={'fontweight':'bold','fontsize':15})


plt.legend()

plt.savefig('Similarity_Test_ set_figure.png',dpi=300)


plt.show()