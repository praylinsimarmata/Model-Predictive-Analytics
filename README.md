# Proyek Pertama : Predictive Analytics

## Domain Proyek
Seorang manager di bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya. Mereka akan sangat menghargai jika seseorang dapat memprediksi untuk mereka pelanggan mana yang dapat mereka harapkan untuk berhenti sehingga mereka dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, dan pada akhirnya mencapai laba atas investasi yang positif bagi bank.

## Business Understanding

### Problem Statements
Seorang manager di bank merasa terganggu dengan semakin banyaknya nasabah yang meninggalkan layanan kartu kreditnya. Mereka akan sangat menghargai jika seseorang dapat memprediksi untuk mereka pelanggan mana yang dapat mereka harapkan untuk berhenti sehingga mereka dapat secara proaktif mengintervensi dan menawarkan layanan dan produk untuk mempertahankan pelanggan, dan pada akhirnya mencapai laba atas investasi yang positif bagi bank.

### Project Summary
- Membangun model klasifikasi untuk memprediksi churn nasabah kartu kredit suatu bank.
- Klasifikasi yang dilakukan menggunakan Optimized Linear Regression, Random Forest, and XGBoost.
- Melakukan analisis ROI dengan mempertimbangkan customer lifetime value (LTV), nilai dari false positives/negatives, dan nilai dari dan intervensi untuk mempertahankan pelanggan.

## Data Understanding
- Dataset diperoleh dari Kaggle:: https://www.kaggle.com/sakshigoyal7/credit-card-customers
- Dataset ini terdiri dari 10.000 pelanggan dengan 21 fitur, diantaranya: customer age, salary, marital_status, credit card limit, credit card category, dll. Data menggambarkan perilaku pelanggan selama 12 bulan terakhir.

### Exploratory Data Analysis
#### Correlation heatmap:
![images] (https://drive.google.com/file/d/11u-dY3Z4Y2tP8zGAgNUNyEqrsaZRdAP6/view?usp=share_link)

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
