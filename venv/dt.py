import sklearn
import pandas as pd
from collections import Counter
import math

from sklearn.datasets import load_iris

### compute entropy for a set of classification, provided as either a pandas
### series, or as a list: ['yes','no','yes','yes','no']

def entropy(classes) :
    vals = set(classes)
    counts = Counter(classes)
    ent = 0.0
    for val in vals :
        frequency = counts[val] / len(classes)
        ent += -1 * frequency * math.log(frequency, 2)
    return ent

### Remainder should call entropy.
### For each value of attribute, compute the entropy. Then return the weighted sum
## your data should be in the form: [(value1, class1), (value2, class2), ..., (valuen,
### classn)]
### or in an equivalent pandas dataframe.

def remainder(data) :
   pass



### For each attribute, compute the remainder and select the one with the highest gain.
### You can assume that data is either a pandas dataframe or a list of lists, like so:
### [[a1, a2, ..., c1], [b1,b2,...,c2], ... ]
### assume that attributeList is a list that indicates the attribute represented by each column.
### e.g. ['outlook','temperature','humidity','windy','play]
### if you are using pandas, this is stored in the dataframe, and so you won't need the attributeList..


def selectAttribute(data, attributeList) :
   pass

### Now we're ready to build a Decision Tree.
### A tree consists of one or more Nodes.
### A Node is either a leaf node, which has a value and no children
### Or it is a non-leaf, in which case it has an attribute that it tests and a set of children.

class Node :
    def __init__(self, attribute=None, value=None):
        self.attribute = attribute
        self.value=value
        self.children={}

    def isLeaf(self):
        return len(self.children) == 0

    ### you'll implement this
    ### classify should take as input an instance, which is either a pandas Series or a list,
    ## and a second list that indicates the attribute names. If you're using a dataframe, you won't need this.

    def classify(self, instance, attributeList):
       pass

    def __repr__(self) :
        return "%s %s" % (self.attribute, self.value)

##
class DecisionTree :
    def __init__(self, root) :
        self.root = root

    ### assume instance is a pandas dataframe - use node.classify as a helper.
    def classify(self, instance):
        pass


### construct a decision tree. Inputs are either a pandas dataframe containing a dataset
### or a list of lists with a dataset and an attributeDict that maps each attribute to
### the possible values it can take on.

### We make the tree recursively. There are three base cases:
### 1. All the data is of the same class.
###   In this case, we are at a leaf node. set the value to be the classification.
### 2. We are out of attributes to test.
###   In this case, apply ZeroR.
### 3 We are out of data
###   In this case, apply ZeroR.
### Return the node
### Otherwise :
###  1. Use selectAttribute to find the attribute with the largest information gain.
###  2. Break the data into subsets according to each value of that attribute.
###  3. For each subset, call makeNode

def makeNode(df, attributeDict) :
    pass



