import pandas as pd
import array
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pickle

df=pd.read_pickle('./output/DataSetAudios.pkl')

y=df['name']
X=list(map(lambda x: x,df['fft+mfcc']))

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
clf=RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)

df_pred=pd.DataFrame({'gt':y_test, 'pred':y_pred})

for i in list(df_pred['gt'].index):
    if df_pred['gt'][i]!=df_pred['pred'][i]:
        print(df_pred['gt'][i],df_pred['pred'][i])

print('Accuracy',accuracy_score(df_pred["gt"],df_pred['pred']))
print("Precision", precision_score(df_pred["gt"],df_pred['pred'],average='weighted'))
print("Recall", recall_score(df_pred["gt"],df_pred['pred'],average='weighted'))

pickle.dump(clf, open('modelo3', 'wb'))

#df_pred[df_pred['gt']=='SeoRa']['pred'].value_counts().index[0]




