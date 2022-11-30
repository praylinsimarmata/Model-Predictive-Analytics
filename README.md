# Proyek Pertama: Predictive Analytics

## Domain Proyek
Bank *Customer Churn* adalah kehilangan pelanggan dari suatu bank. *Churn* dihitung dari berapa banyak pelanggan meninggalkan suatu bank dalam waktu tertentu. Bank *Customer churn* penting diketahui karena merupakan gambaran kesuksesan suatu bank dalam mempertahankan pelanggan. Selain itu, Bank *Customer churn* penting untuk dihentikan, karena bank akan mengalami kerugian besar jika kehilangan pelanggannya. Dalam kasus ini, seorang manajer di sebuah bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya. Dan meminta bantuan agar dapat memprediksi pelanggan mana yang ingin berhenti sehingga bank tersebut dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, sehingga pada akhirnya dapat mencapai laba atas investasi yang positif bagi bank.

## Business Understanding
Seorang manajer di bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya.Dan meminta bantuan agar dapat memprediksi pelanggan mana yang dapat diharapkan untuk berhenti sehingga bank tersebut dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, dan pada akhirnya mencapai laba atas investasi yang positif bagi bank.

### Problem Statements
Pernyataan masalah yang terdapat dalam proyek ini, yakni:
- Adanya pelanggan yang meninggalkan layanan kartu kreditnya.
- Menarik kembali pelanggan yang ingin berhenti.
- Bagaimana caranya agar dapat mencapai laba atas investasi yang positif bagi bank.

### Goals / Project Summary
Menjelaskan tujuan proyek yang akan menjawab pernyataan masalah:
- Membangun model klasifikasi untuk memprediksi churn nasabah kartu kredit suatu bank.
- Klasifikasi yang dilakukan menggunakan *Optimized Linear Regression*, *Random Forest*, and *XGBoost*.
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

- **Correlation heatmap**

Tiga variabel yang paling berkorelasi dengan respons adalah 'Total_Revolving_Bal', 'Total_Trans_Ct', dan 'Total_Ct_Chng_Q4_Q1'. Masing-masing prediktor tersebut memiliki korelasi negatif > 0,2 dengan variabel respon 'y'.

![gambar1](https://user-images.githubusercontent.com/99348807/204719501-41b9edd6-42bd-48de-b5bf-1efa827b5299.jpg)

- **Pairplot**

Melakukan pairplot pada fitur 'Contacts_Count_12_mon', 'Total_Revolving_Bal','Total_Trans_Ct', dan 'Total_Ct_Chng_Q4_Q1'. Pairplot ini tidak terlalu berguna dengan respon biner.

![gambar2](https://user-images.githubusercontent.com/99348807/204719738-d8e405f7-ff34-45b6-874f-56948f4ac496.jpg)

- **Plot fitur yang paling berkorelasi terhadap variabel y**

Selanjutnya dilakukan plot untuk ketiga prediktor, yaitu pada 'Total_Revolving_Bal', 'Total_Trans_Ct', dan 'Total_Ct_Chng_Q4_Q1' untuk mendapatkan gambaran yang lebih baik tentang distribusi dan hubungan dengan respons. Dari plot tersebut diketahui bahwa terdapat sejumlah besar outlier untuk 'Total_Trans_Ct' dan 'Total_Ct_Chng_Q4_Q1'. Untuk 'Total_Revolving_Balance' diketahui ada penambahan distribusi, dengan mayoritas churner berpusat di sekitar saldo $0.

![gambar3](https://user-images.githubusercontent.com/99348807/204719862-82284263-ef17-4128-a15b-59c7b2d3aed8.jpg)

- **Rata-rata jumlah transaksi tahunan untuk churner dan non-churner**

| y | Total_Trans_Amt | Months_on_book |
|---|-----------------|----------------|
| 0 | 4654.655882     | 35.880588      |
| 1 | 3095.025814     | 36.178242      |

## Data Preparation / Data Preprocessing
Pengolahan data dilakukan dalam beberapa tahap yakni: 
- Tahap 1: Melakukan Load Data dan Menampilkan Data.

- Tahap 2 : Menampilkan informasi data dengan menggunakan df.info() untuk melihat jenis data, ketersediaan data setiap kolom, dan jenis jenis colom. Kemudian menggunakan df.describe() untuk mengetahui persebaran data.

- Tahap 3: Kemudian tahap selanjutnya ialah mengecek ketersediaan isi pada kolom, karena ketika ada missing kolom akan menyebabkan prediksi kurang optimal. Dan pada dataset ini, kita tidak menemukan missing values.

| Kolom                    | Total Kosong |
|--------------------------|--------------|
| Customer_Age             |       0      |
| Dependent_count          |       0      |
| Months_on_book           |       0      |
| Total_Relationship_Count |       0      |
| Months_Inactive_12_mon   |       0      |
| Contacts_Count_12_mon    |       0      |
| Credit_Limit             |       0      |
| Total_Revolving_Bal      |       0      |
| Avg_Open_To_Buy          |       0      |
| Total_Amt_Chng_Q4_Q1     |       0      |
| Total_Trans_Am           |       0      |
| Total_Trans_Ct           |       0      |
| Total_Ct_Chng_Q4_Q       |       0      |
| Avg_Utilization_Ratio    |       0      |

- Tahap 4: Melakukan Normalize/scale features menggunakan robust scaler untuk mempertahankan hubungan outlier.

- Tahap 5: Membagi dataset menjadi training dan test dengan perbandingan 75/25 split.

- Tahap 6: Oversample minor class pada training set untuk menyeimbangkan kelas.

## Modeling 
Pada proyek ini, dilakukan 3 pemodelan yakni menggunakan *Logistic Regression*, *Random Forest*, dan juga *XGBoost*.

- **Logistic Regression** – Dasar untuk pemodelan

Pada proyek ini, model yang pertama dibuat ialah model *Logistic Regression*. *Logistic Regression* ialah salah satu jenis pemodelan yang digunakan untuk melakukan prediksi apakah sesuatu bernilai benar atau salah. Dalam hal ini kita ingin melakukan prediksi apakah seorang pelanggan akan melakukan churn atau tidak. Algoritma ini bekerja dengan cara menjalankan fungsi LogisticRegression() serta *hyperparameters* yang ditampung di dalam *grid search*. *GridSearch* akan melakukan validasi terhadap model dan juga *hyperparameters* masing-masing secara otomatis dan sistematis. Dalam algoritma ini, *Hyperparameters* yang digunakan ialah:
```
solvers = ['newton-cg','lbfgs','liblinear']
penalty = ['l1','l2']
c = [100,10,1,.1,.01]
```
Dengan menggunakan *GridSearch* nantinya akan dipilih parameter yang terbaik yang akan digunakan dan akan dilatih menggunakan grid_search.fit.

- **Random Forest** – Metode ansambel pohon keputusan, metode non-parametrik yang dapat bekerja lebih baik karena hubungan yang kompleks antara prediktor dan hasil.

Model yang kedua dibuat pada proyek ini ialah *Random Forest*. *Random Forest* merupakan salah satu algoritma dalam *Decision Tree* yang nantinya algoritma ini akan melakukan prediksi apakah seorang pelanggan akan melakukan churn atau tidak. Algoritma ini bekerja dengan cara menjalankan fungsi RandomForestClassifier() serta *hyperparameters* yang ditampung di dalam *grid search*. *GridSearch* akan melakukan validasi terhadap model dan juga *hyperparameters* masing-masing secara otomatis dan sistematis. Dalam algoritma ini, *Hyperparameters* yang digunakan ialah:
```
n_estimators = [10,100,1000]
max_features = ['sqrt','log2']
```
Dengan menggunakan *GridSearch* nantinya akan dipilih parameter yang terbaik yang akan digunakan dan akan dilatih menggunakan grid_search.fit.

- **XGBoost** – Teknik peningkatan gradien adalah teknik aditif (ensemble) yang membangun satu pohon pada satu waktu, belajar dari iterasi sebelumnya. 

Model terakhir yang dibuat pada proyek ini ialah *XGBoost*. Algoritma ini bekerja dengan cara menjalankan fungsi XGBClassifier() serta *hyperparameters* yang ditampung di dalam *grid search*. *GridSearch* akan melakukan validasi terhadap model dan juga *hyperparameters* masing-masing secara otomatis dan sistematis. Dalam algoritma ini, *Hyperparameters* yang digunakan ialah:
```
eta = [.1,.4,.7,1]
min_child_weight = [3,6,10]
max_depth = [.1,1,5,10]
```
Setelah *hyperparameters* didefinisikan, kemudian dipanggil pada variabel *grid*. Lalu model dilatih menggunakan grid_search.fit. Algortitma XGBoost ini menggunakan proses pra-filter dan berbasis histogram untuk menemukan nilai pemisah terbaik. Sehingga dapat memprediksi apakah seorang pelanggan akan melakukan churn atau tidak.

## Evaluation
Evaluasi yang dilakukan dalam proyek ini menggunakan *F1 Score metric*. *F1 Score metric* dapat diartikan sebagai rata-rata tertimbang dari presisi dan *recall*, dimana skor F1 mencapai nilai terbaiknya pada 1 dan skor terburuk pada 0. Kontribusi relatif presisi dan *recall* terhadap skor F1 adalah sama. Rumus untuk skor F1 ialah:
$F1 = 2 * {{(precision * recall)} \over (precision + recall)}$

F1 sangat relevan untuk masalah ini karena terdapat dampak bisnis yang jelas dalam pertukaran antara presisi dan recall. Metriks inilah yang digunakan untuk melakukan analisis ROI.

### Conclusion

Dari ketiga model tersebut, didapat hasil akurasi sebagai berikut: 
#### Result 
| Model               | Result |
|---------------------|--------|
| Logistic Regression | 0.85   |
| Random Forest       | 0.96   |
| XGBoost             | 0.97   |

Dari hasil tersebut kita dapat mengetahui bahwa model yang paling baik ialah dengan menggunakan *XGBoost*.
