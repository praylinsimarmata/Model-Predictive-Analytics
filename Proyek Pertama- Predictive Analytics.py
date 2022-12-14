# -*- coding: utf-8 -*-
"""Proyek Pertama - Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwR-LHPVPSSuHARybjOOnKVKL3c4uBbZ

# **Memprediksi Churn Nasabah Bank**

## **Import Libraries**
"""

pip install seaborn --upgrade

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""## **Data Preparation**

### **Melakukan Load Data dan Menampilkan Data**
"""

df = pd.read_csv('/content/BankChurners.csv')
df

y = pd.Series(np.where(df['Attrition_Flag'] == 'Attrited Customer', 1, 0), df.index)
#Menambahkan kolom y ke dalam tabel
df.insert(0,'y', pd.Series(np.where(df['Attrition_Flag'] == 'Attrited Customer', 1, 0), df.index))

#Menghapus dua kolom pertama yang tidak prediktif
df = df.drop(['Attrition_Flag','CLIENTNUM'],axis=1)
df = df.iloc[:,0:-2]

"""### **Melihat Informasi Data**"""

df.shape

df.describe()

df.info()

"""### **Mengecek Baris Kosong**"""

print('Jumlah baris kosong:')
pd.DataFrame(df.isnull().sum().reset_index()).rename( columns={0:"Total Kosong","index":"Kolom"})

"""## **Exploratory Data Analysis**

### **Plotting Data Hasil Import**
"""

#correlation plot
df.corr()

#correlation heatmap
sns.set_style('whitegrid')
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True,lw=1,robust=True,fmt='.2f',vmin=-0.5,vmax=0.5)

sns.pairplot(df, y_vars=['y'],x_vars=['Contacts_Count_12_mon',
                      'Total_Revolving_Bal','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1'],kind='scatter')

fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(18,8))

sns.boxplot(x='y',y='Total_Ct_Chng_Q4_Q1', data=df, ax=axs[0,0])
sns.boxplot(x='y',y='Total_Trans_Ct', data=df, ax=axs[0,1])
sns.boxplot(x='y',y='Total_Revolving_Bal', data=df, ax=axs[0,2])

sns.kdeplot(x='Total_Ct_Chng_Q4_Q1',data=df, hue='y', shade=True, ax=axs[1,0])
sns.kdeplot(x='Total_Trans_Ct',data=df, hue='y', shade=True, ax=axs[1,1])
sns.kdeplot(x='Total_Revolving_Bal',data=df, hue='y', shade=True, ax=axs[1,2])

#rata-rata jumlah transaksi tahunan untuk churner dan non-churner
df.groupby('y').agg({'Total_Trans_Amt':np.average, 'Months_on_book':np.average})

"""## **Data Preprocessing**

### **Missing Values**

Diketahui pada dataset ini tidak ada missing values. Kode di bawah ini adalah template untuk ***impute missing values***. Untuk fitur kategori dipilih imputasi *'most frequent'* dan untuk fitur numerik dipilih *'median'*.
"""

#impute pada kolom kategorikal
from sklearn.impute import SimpleImputer

categorical_features = df.select_dtypes(include=['object']).columns
cat = SimpleImputer(strategy='most_frequent',copy=False)
cat1 = cat.fit(df[categorical_features].astype(str))
df[categorical_features] = cat1.transform(df[categorical_features])

#impute pada kolom numerik
numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
num = SimpleImputer(strategy='median',copy=False)
num1 = num.fit(df[numeric_features])
df[numeric_features] = num1.transform(df[numeric_features])

"""### **Categorical Features**"""

#Membuat kolom numerikal baru dan menghapus kolom sebelumnya
categorical_features = df.select_dtypes(include=['object']).columns
X = pd.get_dummies(df[categorical_features], prefix_sep='_')
X = pd.merge(df,X,how='outer',left_index=True,right_index=True)
X = X.drop(categorical_features, axis=1)
X.head()

"""### **Normalization / Scaling**"""

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
index = X.columns

transformer = scaler.fit_transform(X)
X = pd.DataFrame(transformer, columns = index)
X.head()

"""### **Test-Train Split**"""

from sklearn.model_selection import train_test_split

X = X.drop(columns='y')
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 12)
x_train.shape

"""### **Over/Under Sampling**"""

y.value_counts()

#Menyeimbangkan training set
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=12)
x_train, y_train = sm.fit_resample(x_train, y_train)
x_train.shape

"""## **Modeling and Evaluation**"""

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

reg = LogisticRegression(solver='liblinear', max_iter=100)
reg.fit(x_train,y_train)

Logistic_Model_Score=reg.score(x_train,y_train)*100
Logistic_Model_Score

print("Akurasi training yang diperoleh : ", "{:.2f}%".format(Logistic_Model_Score))

accuracy_list = []

from sklearn.metrics import accuracy_score
log_reg_pred = reg.predict(x_test)
log_reg_acc = accuracy_score(y_test, log_reg_pred)
accuracy_list.append(100*log_reg_acc)

print("Akurasi testing yang diperoleh : ", "{:.2f}%".format(100* log_reg_acc))

from sklearn.metrics import confusion_matrix
from mlxtend.plotting import plot_confusion_matrix

cm = confusion_matrix(y_test, log_reg_pred)

plt.rcParams.update()
plt.figure()
plot_confusion_matrix(cm, figsize=(12,8), hide_ticks=True, cmap=plt.cm.Blues)
plt.title("Logistic Regression Model - Confusion Matrix")
plt.xticks(range(2), ["Attrited Customer","Existing Customer"], fontsize=16)
plt.yticks(range(2), ["Attrited Customer","Existing Customer"], fontsize=16)
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test, reg.predict(x_test)))