from SQL import *
from functions import *
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor


execute_query(connection, build_recent(userid))

recent_df = pd.DataFrame(pd.read_sql_query(''' 
                              select * from recent
                              '''
                              ,connection))


recent_update = recent_df[['win','kills','deaths','XPM','GPM','damage','cs']]

# add .to_numpy to remove header names

X = recent_update[['kills','deaths','XPM','GPM','damage','cs']].to_numpy()

y = recent_update['win'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Check for what the best K value is
knn_acc = []

for i in range(1,10,1):
    knn = KNeighborsRegressor(n_neighbors=i)
    knn.fit(X_train,y_train)
    test_score = knn.score(X_test,y_test)
    train_score = knn.score(X_train,y_train)
    knn_acc.append((i, test_score ,train_score))
df = pd.DataFrame(knn_acc, columns=['K','Test Score','Train Score'])

print(df)

# finding that the data test score is really low, probably needs more data to be more accurate


# KneighborsClassifier will find the 6 closest data points to our query and vote for the most common outcome
knn = KNeighborsClassifier(n_neighbors = 3)

# fit the trainin data to our model
knn.fit(X_train, y_train)

# Change variables here to determine if it will result in a win or loss
# printing a 1 indicates win, a 0 indicates loss
print(knn.predict([[9,4,787,569,18547,200]]))