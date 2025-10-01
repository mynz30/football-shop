**Nama** : Faishal Khoiriansyah Wicaksono
**NPM** : 2406436335

Football Shop

Live (PWS): https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id/  


## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS punya aturan prioritas (specificity). Urutannya:
1. **Inline style** (paling tinggi).
2. **ID selector** (`#id`).
3. **Class, pseudo-class, dan attribute selector** (`.class`, `:hover`, `[type=text]`).
4. **Element selector** (`div`, `p`, `h1`).
Kalau ada bentrok, yang lebih spesifik dan muncul paling terakhir akan dipakai.

---

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?  
Responsive design penting karena bikin tampilan web nyaman di berbagai ukuran layar (HP, tablet, laptop).  
- **Contoh yang sudah responsive**: Instagram → tampilan tetap rapi dan enak dilihat baik di HP maupun desktop.  
- **Contoh yang belum responsive**: Website lama sekolah/kampus → biasanya kalau dibuka di HP harus zoom in/out, layout jadi berantakan.  

---

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!  
- **Margin**: Jarak luar antar elemen.  
- **Border**: Garis tepi elemen.  
- **Padding**: Jarak dalam antara konten dengan border.  

Contoh implementasi di CSS:
```css
div {
  margin: 20px;   /* jarak luar */
  border: 2px solid black;  /* garis tepi */
  padding: 15px;  /* jarak dalam */
}


## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox: Cocok buat ngatur elemen dalam satu arah (row/column). Biasanya dipakai untuk navbar, card, atau alignment sederhana.

Grid Layout: Cocok untuk layout dua dimensi (baris dan kolom). Biasanya dipakai buat dashboard, galeri foto, atau layout kompleks.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!

Mulai dengan bikin struktur HTML dasar.

Tambahin CSS buat margin, border, dan padding sesuai kebutuhan.

Pakai selector dengan prioritas yang tepat (ID/Class/Element).

Implementasi responsive design pakai media query (@media).

Gunakan Flexbox untuk layout searah (misalnya card product).

Pakai Grid kalau layout lebih kompleks.

Tes di berbagai device biar tampilannya konsisten.