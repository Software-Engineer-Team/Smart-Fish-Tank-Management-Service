import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# create the dataframe
df = pd.read_csv('fish_autofeeding.csv')

# create new columns for time_of_day ranges
df['time_6-9'] = df['time_of_day'].apply(
    lambda x: 1 if 5 <= int(x.split(":")[0]) <= 8 else 0)
df['time_11-13'] = df['time_of_day'].apply(
    lambda x: 1 if 11 <= int(x.split(":")[0]) < 13 else 0)
df['time_17-19'] = df['time_of_day'].apply(
    lambda x: 1 if 17 <= int(x.split(":")[0]) < 19 else 0)
df['time_others'] = df['time_of_day'].apply(
    lambda x: 1 if not (6 <= int(x.split(":")[0]) <= 8 or 11 <= int(x.split(":")[0]) <= 13 or 17 <= int(x.split(":")[0]) <= 19) else 0)

# create new columns for light levels
df['light_low'] = df['light'].apply(lambda x: 1 if x == 'low' else 0)
df['light_medium'] = df['light'].apply(lambda x: 1 if x == 'medium' else 0)
df['light_high'] = df['light'].apply(lambda x: 1 if x == 'high' else 0)

df['prediction'] = df['prediction'].astype(int)

# df['temperature'] = (df['temperature'] - df['temperature'].min()) / \
#     (df['temperature'].max() - df['temperature'].min())

columns = ['time_6-9', 'time_11-13', 'time_17-19', 'time_others', 'light_low',
           'light_medium', 'light_high', 'temperature', 'prediction']
new_df = df.loc[:, columns]
X = new_df.iloc[:, :-1].values
y = new_df.iloc[:, -1].values
# print(X)
# print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.35, random_state=1)

sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
# print(X_test)
X_test = sc.transform(X_test)

# Training the K-NN model on the Training set
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)

# Use the trained classifier to predict the test data
y_pred = classifier.predict(X_test)

# Predicting a new result
# print(classifier.predict(sc.transform([[0, 0, 0, 1, 1, 0, 0, 10], [0, 0, 0, 1, 1, 0, 0, 25], [
#       0, 0, 0, 1, 0, 0, 1, 25], [0, 1, 0, 0, 0, 0, 1, 25], [1, 0, 0, 0, 0, 0, 1, 25]])))

# Print the confusion matrix and accuracy score of the model on the test data
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))


# # Plot confusion matrix
# cm = confusion_matrix(y_test, y_pred)
# plt.imshow(cm, cmap=plt.cm.Blues)

# # Add labels and title to the plot
# plt.title("Confusion Matrix")
# plt.ylabel('True label')
# plt.xlabel('Predicted label')

# # Add colorbar to the plot
# plt.colorbar()

# # Add tick marks to the plot
# tick_marks = np.arange(len(set(y)))
# plt.xticks(tick_marks, ['0', '1'])
# plt.yticks(tick_marks, ['0', '1'])

# # Add numbers to the plot
# thresh = cm.max() / 2.
# for i, j in np.ndindex(cm.shape):
#     plt.text(j, i, format(cm[i, j], 'd'),
#              horizontalalignment="center",
#              color="white" if cm[i, j] > thresh else "black")

# # Show the plot
# plt.show()
