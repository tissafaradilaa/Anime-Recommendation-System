# 🎌 Anime Recommendation System (Hybrid Recommendation)
Anime Recommendation System using Hybrid Filtering (Content-Based &amp; Collaborative Filtering) implemented with Python and Flask.

Proyek ini merupakan sistem rekomendasi anime yang dibangun menggunakan pendekatan **Hybrid Recommendation System**, yaitu dengan menggabungkan metode **Content-Based Filtering** dan **Collaborative Filtering**. Sistem ini bertujuan untuk membantu pengguna menemukan anime yang relevan berdasarkan preferensi konten maupun pola penilaian pengguna lain.

Sistem diimplementasikan dalam bentuk **aplikasi berbasis web** menggunakan framework **Flask**, sehingga dapat diakses melalui browser dan mendukung dua mode rekomendasi, yaitu mode berbasis anime dan mode berbasis pengguna (user-based).

---

## 🚀 Fitur Utama

- 🔍 **Mode Anime-Based Recommendation**  
  Memberikan rekomendasi anime berdasarkan kemiripan genre dari anime yang dipilih pengguna.

- 👤 **Mode User-Based Recommendation**  
  Memberikan rekomendasi anime berdasarkan riwayat rating dan kemiripan dengan pengguna lain.

- 🔄 **Hybrid Filtering**  
  Menggabungkan hasil content-based filtering dan collaborative filtering menggunakan teknik pembobotan.

- 🌐 **Web-Based Interface**  
  Antarmuka sederhana dan interaktif yang dibangun menggunakan HTML, CSS, dan Flask.

---

## 🧠 Metode yang Digunakan

1. **Content-Based Filtering**
   - Representasi genre anime menggunakan TF-IDF
   - Perhitungan kemiripan menggunakan cosine similarity

2. **Collaborative Filtering (User-Based)**
   - Pembentukan matriks user-item
   - Perhitungan kemiripan antar pengguna menggunakan cosine similarity

3. **Hybrid Recommendation**
   - Penggabungan skor content-based dan collaborative filtering dengan parameter bobot (alpha)

---

## 📊 Dataset

Dataset yang digunakan terdiri dari:
- **Anime Dataset**: informasi anime seperti ID, nama, dan genre
- **Rating Dataset**: data penilaian pengguna terhadap anime

Sebelum digunakan, dataset melalui tahap preprocessing, antara lain:
- Penanganan nilai genre kosong
- Penghapusan data rating tidak valid (rating = -1)

---

## 🛠️ Teknologi yang Digunakan

- Python
- Flask
- Pandas
- Scikit-learn
- HTML & CSS
