import pandas as pd
import urllib.request
from tensorflow import keras as K
from sklearn.model_selection import train_test_split

# Download the Mice Protein Expression dataset from uci
# https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00342/Data_Cortex_Nuclear.xls'
file_name = 'Data_Cortex_Nuclear.xls'
urllib.request.urlretrieve(url, file_name)

# Prepare dataset for training
xls_file = pd.read_excel(file_name, index_col=0)
# remove missing values by row: axis=0, column: axis=1
xls_file.dropna(axis=0)
# get feautres
X = xls_file[xls_file.columns[0:-4]].values
y = xls_file['class'].astype('category').cat.codes.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

num_samples = X.shape[0]
num_features = X.shape[1]