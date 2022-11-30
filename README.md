# Proyek Pertama : Predictive Analytics

## Domain Proyek
Bank *Customer Churn* adalah kehilangan pelanggan dari suatu bank. *Churn* dihitung dari berapa banyak pelanggan meninggalkan suatu bank dalam waktu tertentu. Bank *Customer churn* penting diketahui karena merupakan gambaran kesuksesan suatu bank dalam mempertahankan pelanggan. Selain itu, Bank *Customer churn* penting untuk dihentikan, karena bank akan mengalami kerugian besar jika kehilangan pelanggannya. Dalam kasus ini, seorang manajer di sebuah bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya. Dan meminta bantuan agar dapat memprediksi pelanggan mana yang ingin berhenti sehingga bank tersebut dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, sehingga pada akhirnya dapat mencapai laba atas investasi yang positif bagi bank.

## Business Understanding
Seorang manajer di bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya.Dan meminta bantuan agar dapat memprediksi pelanggan mana yang dapat diharapkan untuk berhenti sehingga bank tersebut dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, dan pada akhirnya mencapai laba atas investasi yang positif bagi bank.

### Problem Statements
Pernyataan masalah yang terdapat dalam proyek ini, yakni:
- Adanya pelanggan yang meninggalkan layanan kartu kreditnya
- Menarik kembali pelanggan yang ingin berhenti
- Bagaimana caranya agar dapat mencapai laba atas investasi yang positif bagi bank

### Goals / Project Summary
Menjelaskan tujuan proyek yang akan menjawab pernyataan masalah:
- Membangun model klasifikasi untuk memprediksi churn nasabah kartu kredit suatu bank.
- Klasifikasi yang dilakukan menggunakan Optimized Linear Regression, Random Forest, and XGBoost.
- Menentukan model terbaik yang akan digunakan.

## Data Understanding
- Dataset ini diperoleh dari Kaggle: https://www.kaggle.com/sakshigoyal7/credit-card-customers
- Dataset ini menggambarkan perilaku pelanggan selama 12 bulan terakhir.

Berikut fitur-fitur yang terdapat pada dataset dan deskripsinya:
- Customer_Age: Usia Pelanggan
- Dependent_count: Jumlah Tanggungan
- Months_on_book: Jangka waktu hubungan dengan bank
- Total_Relationship_Count: Jumlah total produk yang dimiliki oleh pelanggan
- Months_Inactive_12_mon: Jumlah bulan tidak aktif dalam 12 bulan terakhir
- Contacts_Count_12_mon: Jumlah Kontak dalam 12 bulan terakhir
- Credit_Limit:Limit Kredit pada Kartu Kredit
- Total_Revolving_Bal: Total Saldo Bergulir pada Kartu Kredit
- Avg_Open_To_Buy: Terbuka untuk Beli Credit Line (Rata-rata 12 bulan terakhir)
- Total_Amt_Chng_Q4_Q1: Perubahan Jumlah Transaksi (Q4 over Q1)
- Total_Trans_Amt: Total Jumlah Transaksi (12 bulan terakhir)
- Total_Trans_Ct: Jumlah Transaksi (12 bulan terakhir)
- Total_Ct_Chng_Q4_Q1: Perubahan Jumlah Transaksi (Q4 over Q1)
- Avg_Utilization_Ratio: Rasio Pemanfaatan Kartu Rata-Rata

### Exploratory Data Analysis

- **Correlation heatmap**:

Tiga variabel yang paling berkorelasi dengan respons adalah 'Total_Revolving_Bal', 'Total_Trans_Ct', dan 'Total_Ct_Chng_Q4_Q1'. Masing-masing prediktor tersebut memiliki korelasi negatif > 0,2 dengan variabel respon 'y'.

![gambar1](https://user-images.githubusercontent.com/99348807/204719501-41b9edd6-42bd-48de-b5bf-1efa827b5299.jpg)

- **Pairplot**

![gambar2](https://user-images.githubusercontent.com/99348807/204719738-d8e405f7-ff34-45b6-874f-56948f4ac496.jpg)

- **Plot fitur yang paling berkorelasi terhadap variabel y**

![gambar3](https://user-images.githubusercontent.com/99348807/204719862-82284263-ef17-4128-a15b-59c7b2d3aed8.jpg)

- **Plot Total_Trans_Amt**

![gambar4](https://user-images.githubusercontent.com/99348807/204720201-b498b71b-f9cb-4e04-a785-1aabbf7046ad.jpg)

![gambar5](https://user-images.githubusercontent.com/99348807/204720208-451dbd19-82e1-4c84-a162-d0caaf2ba2d8.jpg)

- **Rata-rata jumlah transaksi tahunan untuk churner dan non-churner**

![gambar6](https://user-images.githubusercontent.com/99348807/204721062-12ee05f1-f209-43f0-8510-b692e4098c01.jpg)

## Data Preparation / Data Preprocessing
Pengolahan data dilakukan dalam beberapa tahap yakni: 
- Tahap 1: Melakukan Load Data dan Menampilkan Data

![gambar7](https://user-images.githubusercontent.com/99348807/204722878-31d756bd-6d77-4ac8-849d-91d7752e142c.jpg)

- Tahap 2: Setelah data tampil, tahap selanjutnya ialah mengecek ketersediaan isi pada kolom, karena ketika ada missing kolom akan menyebabkan prediksi kurang optimal

![gambar8](https://user-images.githubusercontent.com/99348807/204722961-5fcbe9ec-8935-4088-966e-0411e7069814.jpg)

- Tahap 3: Melakukan Normalize/scale features menggunakan robust scaler untuk mempertahankan hubungan outlier

![gambar9](https://user-images.githubusercontent.com/99348807/204723003-3697a300-78f0-44c9-ba4a-a3182972b9bb.jpg)

- Tahap 4: Membagi dataset menjadi training dan test dengan perbandingan 75/25 split, dengan menggunakan code dibawah ini:
```
from sklearn.model_selection import train_test_split

X = X.drop(columns='y')
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 12)
x_train.shape
```

- Tahap 5: Oversample minor class pada training set untuk menyeimbangkan kelas, dengan menggunakan code dibawah ini:
```
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=12)
x_train, y_train = sm.fit_resample(x_train, y_train)
x_train.shape 
```

## Modeling 
Pada proyek ini, dilakukan 3 pemodelan yakni menggunakan Logistic Regression, Random Forest, dan juga XG Boost.

- Logistic Regression – Dasar untuk pemodelan

![gambar11](https://user-images.githubusercontent.com/99348807/204727710-fbd39707-c4d0-4e69-9cfb-ae6cea56e9e1.jpg)

- Random Forest – Metode ansambel pohon keputusan, metode non-parametrik yang dapat bekerja lebih baik karena hubungan yang kompleks antara prediktor dan hasil.

![gambar12](https://user-images.githubusercontent.com/99348807/204727718-e97fed87-8d49-455f-9311-9e1e5edacc30.jpg)

- XGBoost – Teknik peningkatan gradien adalah teknik aditif (ensemble) yang membangun satu pohon pada satu waktu, belajar dari iterasi sebelumnya. 

![gambar10](https://user-images.githubusercontent.com/99348807/204727721-7ef81e1f-722d-4045-bbf5-550e504c4096.jpg)

![gambar13](https://user-images.githubusercontent.com/99348807/204727726-30c24a8f-301f-4832-82b6-85d844be9e11.jpg)

Di setiap model yang dibuat pada proyek ini menggunakan hyperparameters dan grid search untuk menemukan parameter terbaik yang digunakan akan pada modeling dalam machine learning.

## Evaluation
Evaluasi yang dilakukan dalam proyek ini menggunakan F1 Score metric. F1 Score metric dapat diartikan sebagai rata-rata tertimbang dari presisi dan recall, dimana skor F1 mencapai nilai terbaiknya pada 1 dan skor terburuk pada 0. Kontribusi relatif presisi dan recall terhadap skor F1 adalah sama. Rumus untuk skor F1 ialah:
```
F1 = 2 * (precision * recall) / (precision + recall)
```
F1 sangat relevan untuk masalah ini karena terdapat dampak bisnis yang jelas dalam pertukaran antara presisi dan recall. Metriks inilah yang digunakan untuk melakukan analisis ROI.

Dari ketiga model tersebut, didapat hasil sebagai berikut: 
### Result 
- Logistic Regression: 0.85
- Random Forest: 0.96
- XGBoost: 0.97

Dari hasil tersebut kita dapat mengetahui bahwa model yang paling baik ialah dengan menggunakan XGBoost.
