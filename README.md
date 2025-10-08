**Nama** : Faishal Khoiriansyah Wicaksono
**NPM** : 2406436335

Football Shop

Live (PWS): https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id/  


=============== TUGAS 6 ===============
1. Apa perbedaan antara synchronous request dan asynchronous request?
Jawaban :
Synchronous request adalah jenis permintaan di mana browser akan menunggu respon dari server terlebih dahulu sebelum melanjutkan proses lainnya. Artinya, saat kita melakukan request, halaman akan berhenti sejenak (biasanya muncul loading) sampai server selesai memproses dan mengirimkan balasan. Cara ini cenderung lebih lambat karena setiap aksi yang dilakukan membutuhkan reload halaman.

Sedangkan asynchronous request (AJAX) memungkinkan browser untuk mengirim dan menerima data ke server di latar belakang tanpa perlu me-reload seluruh halaman. Jadi, pengguna tetap bisa berinteraksi dengan halaman (seperti scroll, mengetik, atau klik tombol lain) sambil data sedang diproses di belakang. Hasilnya kemudian akan ditampilkan secara dinamis menggunakan JavaScript.
Contohnya, ketika kita menambah produk di halaman katalog menggunakan AJAX, daftar produk langsung ter-update tanpa harus refresh halaman.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
Jawaban :
- Pengguna melakukan aksi di halaman web, misalnya klik tombol “Add Product” atau “Login”.
- JavaScript mengirimkan permintaan (request) ke server Django menggunakan metode seperti fetch() atau XMLHttpRequest(). Permintaan ini biasanya dikirim ke endpoint Django yang mengembalikan JSON sebagai respon.
- Django menerima request tersebut melalui fungsi view (misalnya add_product_ajax atau login_ajax), memproses datanya (misalnya menyimpan ke database atau memverifikasi user), lalu mengirimkan respon dalam format JSON.
- JavaScript di sisi klien menerima respon JSON dari server, kemudian mengupdate tampilan halaman secara dinamis tanpa reload.
Misalnya, data produk baru langsung muncul di grid produk, atau muncul notifikasi “Login berhasil”.

Dengan cara ini, interaksi antara pengguna dan server jadi lebih cepat, responsif, dan efisien.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Jawaban :
Menggunakan AJAX memiliki beberapa kelebihan dibandingkan cara render biasa yang harus me-reload halaman, di antaranya:
- Lebih cepat dan efisien
Hanya data yang dibutuhkan saja yang dikirim dan diterima, bukan seluruh halaman HTML.
-  Tampilan tidak perlu reload 
Pengguna bisa tetap berada di halaman yang sama tanpa kehilangan posisi scroll atau data input.
- Interaksi terasa lebih halus dan real-time
Contohnya, saat menambah produk, data langsung muncul tanpa harus klik refresh.
- Pengalaman pengguna lebih baik 
Pengguna merasa aplikasi lebih modern, interaktif, dan mirip seperti aplikasi native.
- Beban server lebih ringan 
Karena server hanya mengirimkan data JSON, bukan seluruh template HTML setiap kali ada permintaan.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Jawaban :
Walaupun AJAX membuat proses login dan register lebih cepat, keamanan tetap harus diperhatikan. Beberapa langkah yang perlu dilakukan antara lain:
- Gunakan CSRF Token (Cross-Site Request Forgery Protection)
Django sudah menyediakan sistem CSRF otomatis. Setiap request POST dari AJAX harus menyertakan token CSRF pada header. Ini mencegah serangan dari situs lain yang mencoba mengirimkan request palsu.
- Menggunakan HTTPS
Memastikan website berjalan menggunakan protokol HTTPS agar data sensitif seperti username dan password terenkripsi saat dikirim ke server.
- Validasi input di server
Semua data dari AJAX harus tetap diperiksa dan divalidasi di sisi Django. Tidak hanya bergantung pada validasi JavaScript di sisi klien, karena itu mudah dimanipulasi.
- Membatasi response informasi sensitif
Saat login gagal, server sebaiknya hanya mengirim pesan umum seperti “Username atau password salah”, bukan alasan detail yang bisa dimanfaatkan pihak luar.

Dengan cara-cara ini, fitur login dan register menggunakan AJAX tetap aman seperti form biasa yang menggunakan render template.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Jawaban :
Penggunaan AJAX memberikan pengaruh besar terhadap User Experience (UX) karena membuat interaksi di website terasa lebih cepat, dinamis, dan nyaman.
Beberapa pengaruh positifnya yaitu:
- Waktu respon lebih singkat
Pengguna tidak perlu menunggu reload halaman penuh setiap kali berinteraksi.
- Feedback langsung
Misalnya muncul toast notification “Produk berhasil ditambahkan” begitu user mengklik submit.
- Halaman tetap interaktif
Pengguna bisa menambah, mengedit, atau menghapus data tanpa keluar dari halaman utama.
- Fokus pengguna tidak terganggu
Karena halaman tidak berpindah, pengguna bisa tetap fokus pada konten yang sedang diakses.
- Terasa seperti aplikasi modern
Website menjadi lebih mirip aplikasi mobile yang responsif dan cepat.

Secara keseluruhan, AJAX membuat website terasa lebih user-friendly dan profesional, karena pengguna mendapat respon instan dari setiap aksi yang dilakukan.

referensi :
- tutorial 5 pbp
- W3Schools - How To Create a Snackbar / Toast
- youtube channel Lun Dev
- website mendix
- GeeksforGeeks - Handling Ajax in Django