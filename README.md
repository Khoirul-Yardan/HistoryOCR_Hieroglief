
# 📜 HistoryOCR_Hieroglief

**HistoryOCR_Hieroglief** adalah proyek berbasis OCR (Optical Character Recognition) yang dirancang untuk mengenali dan menerjemahkan simbol-simbol *Hieroglif Mesir Kuno*. Proyek ini bertujuan sebagai media edukatif dan eksploratif dalam memahami peradaban kuno melalui teknologi AI modern.

![Hieroglyph Example](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Hieroglyphs_from_the_tomb_of_Seti_I.png/800px-Hieroglyphs_from_the_tomb_of_Seti_I.png)

catatan : masih dalam tahap pengembangan lebih lanjut

## ✨ Fitur

- 🔍 Deteksi simbol hieroglif dari gambar atau dokumen.
- 🧠 Penerjemahan simbol ke dalam teks latin / bahasa modern.
- 🖼️ Mendukung input dari gambar berformat JPG, PNG, dll.
- 📚 Basis data simbol hieroglif yang dapat diperluas.
- 🌐 Tampilan antarmuka sederhana dan user-friendly (opsional: berbasis web / GUI lokal).

## 🧰 Teknologi yang Digunakan

- `Python` 3.x
- `OpenCV` untuk deteksi gambar
- `Tesseract OCR` (jika digunakan)
- `NumPy`, `Pandas`
- `Tkinter` / `Streamlit` (jika ada tampilan UI)
- Dataset Hieroglif (custom / open-source)

## 🚀 Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/Khoirul-Yardan/HistoryOCR_Hieroglief.git
cd HistoryOCR_Hieroglief
```

### 2. Instalasi Library
Gunakan `pip` untuk menginstall semua dependensi:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Program
Jika berbasis CLI:
```bash
python main.py
```

Jika berbasis web:
```bash
streamlit run app.py
```

## 📁 Struktur Folder

```
HistoryOCR_Hieroglief/
│
├── data/                  # Dataset hieroglif
├── images/                # Contoh gambar input
├── model/                 # Model deteksi atau klasifikasi
├── src/                   # Source code utama
│   └── ocr.py             # Logika OCR
│   └── translator.py      # Penerjemah simbol
├── app.py                 # Antarmuka web (opsional)
├── requirements.txt       # Daftar dependensi
└── README.md              # Dokumentasi proyek
```

## 🧪 Contoh Gambar Input

| Gambar Asli | Hasil OCR |
|-------------|------------|
| ![ex](images/sample1.png) | 𓂀 𓂋 𓆣 |

> Catatan: Gambar hanya contoh, gunakan koleksi dataset hieroglif untuk pengujian lebih lanjut.

## 🤝 Kontribusi

Kontribusi sangat terbuka! Jika kamu ingin menambahkan fitur, memperbaiki bug, atau mengembangkan UI:

1. Fork repositori ini
2. Buat branch: `git checkout -b fitur-baru`
3. Commit perubahan: `git commit -m 'Tambah fitur baru'`
4. Push ke branch: `git push origin fitur-baru`
5. Buat pull request

## 📝 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).  
Bebas digunakan, dimodifikasi, dan disebarkan untuk tujuan apapun dengan tetap menyertakan atribusi.

## 📬 Kontak

Jika kamu memiliki pertanyaan atau ingin bekerja sama:

- GitHub: [Khoirul-Yardan](https://github.com/Khoirul-Yardan)
- Email: _tambahkan email jika ingin_

---

> Proyek ini dibuat untuk tujuan edukasi dan eksplorasi teknologi OCR dalam konteks sejarah dan budaya kuno. Mari kita jelajahi masa lalu dengan teknologi masa kini!
