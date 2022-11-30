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
- Melakukan analisis ROI dengan mempertimbangkan LTV atau lifetime value of a customer, nilai dari false positives/negatives, dan nilai dari dan intervensi untuk mempertahankan pelanggan.

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
#### Correlation heatmap:
![gambar](https://user-images.githubusercontent.com/99348807/202886627-e41b287a-15f3-4983-9f9e-7f99b1d8158d.jpg)

## Data Preparation / Data Preprocessing
- Mengatasi missing values
- Mengubah fitur kategorikal menjadi dummies
- Normalize/scale features menggunakan robust scaler untuk mempertahankan outlier relationships
- Membagi dataset menjadi training dan test dengan perbandingan 75/25 split
- Oversample minor class pada training set untuk menyeimbangkan kelas

## Modeling 
Pada proyek ini, digunakan 3 model yakni:
- Logistic Regression
- Random Forest
- XG Boost 

Di setiap model yang dibuat pada proyek ini menggunakan hyperparameters dan grid search untuk menemukan parameter terbaik yang digunakan akan pada modeling dalam machine learning.

Dari ketiga model tersebut, didapat hasil sebagai berikut: 
### Result 
- Logistic Regression: 0.85
- Random Forest: 0.96
- XGBoost: 0.97

## Evaluation
Untuk evaluasi pada proyek ini menggunakan **Confusion Matrix** dan **Classification Report.** Yang mana di dalam _confusion matrix_ terdapat nilai FP yang nantinya digunakan dalam perhitungan EvP.

## Summary
Sekarang, dapat dihitung nilai value per prediction (EvP) untuk membandingkan model xgboost dengan model logistic regression.

- False Positive (FP) = $100 (asumsi biaya penawaran insentif kepada pelanggan untuk mencegah churn)
- False Negative (FN) = $278.5 (nilai dari LTV atau lifetime value of a customer)

**EvP = FP * selisih FP % + FN * selisih FN %**

Untuk xgboost model
EvP = 100 * .104 + 278.5 * .014 = $14.6 penghematan per pelanggan.
