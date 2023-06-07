# AI_DiabetesDiagnosis_Kel7

**Diabetes Diagnosis**

**Daftar Anggota**
  - 71210678 Setya Kristendy Cianjur <br />
  - 71210693 Dhea Angelina <br />
  - 71210725 Angelene Nadine

**Penjelasan singkat**
<br /> Aplikasi Artificial Intelligence (AI) yang kami buat adalah Diabetes Diagnosis. Aplikasi tersebut menggunakan data sekunder dari Kaggle. Eksplorasi data kami visualisasikan dalam bentuk Violin Plot dan Scatter Plot. Selanjutnya, aplikasi diimplementasikan menggunakan Model Klasifikasi dengan algoritma Logistic Regression. Model yang sudah jadi kami evaluasi menggunakan Confusion Matrix. 

**Eksplorasi Data**
8 Parameter/Feature - Input berupa numerik
  - Pregnancies = Jumlah Kehamilan <br />
  - Glucose = Glukosa <br />
  - Blood Pressure = Tekanan Darah <br />
  - Skin Thickness = Ketebalan Kulit <br />
  - Insulin <br />
  - Body Mass Index = Indeks Massa Tubuh (Indikator Tinggi Badan dan Berat badan Ideal) <br />
  - Diabetes Pedigree Function = Riwayat Penyakit Diabetes <br />
  - Age = Usia

1 Target - Output berupa numerik
  Outcome (Berupa 0 atau 1)
  0 adalah Tidak Diabetes dan 1 adalah Diabetes
  
**Modelling**
*Logistic Regression* <br />
Algoritma yang cocok digunakan untuk melakukan pemodelan antara variabel dependen biner (Outcome yang berupa 0 atau 1) dengan beberapa variabel independen (8 parameter) <br />
Dengan algoritma tersebut dihasilkan: 
- Area Under the Curve (AUC) = mengukur kemampuan prediksi untuk membedakan antara positif dan negatif = 0.818 <br />
- Classification Accuracy (CA) = mengukur sejauh mana prediksi benar atau tidak = 0.729
- F1 Score = mengukur rata-rata antara presisi dan recall = 0.803
- Precision = mengukur mana identifikasi positif benar atau belum = 0.752

*Confusion Matrix*
Model evaluasi ini memberikan gambaran tentang jumlah diagnosis yang benar dan salah. Confusion Matrix mencakup empat metrik evaluasi utama, yaitu:
- True Positive (TP) = actual 1, predicted 1 = diabetes dan didiagnosis diabetes = 34
- True Negative (TN) = actual 0, predicted 0 = tidak diabetes dan didiagnosis tidak diabetes = 106
- False Positive (FP) = actual 0, predicted 1 = tidak diabetes, tetapi didiagnosis diabetes = 17
- False Negative (FN) = actual 1, predicted 0 = diabetes, tetapi didiagnosis tidak diabetes = 35
