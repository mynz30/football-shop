**Nama** : Faishal Khoiriansyah Wicaksono
**NPM** : 2406436335

Football Shop

Live (PWS): https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id/  


**Pertanyaan :**

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
1. Membuat repositori baru di GitHub khusus untuk Tugas 2, lalu clone ke lokal agar terpisah dari tutorial.

2. Membuat virtual environment dengan python -m venv env lalu aktivasi source env/bin/activate.

3. Install Django dan Gunicorn menggunakan pip install django gunicorn.

4. Membuat proyek Django dengan django-admin startproject football_shop ..

5. Membuat aplikasi main dengan python manage.py startapp main dan menambahkan 'main' ke INSTALLED_APPS di settings.py.

6. Mendefinisikan model Product di main/models.py dengan field seperti name, price, description, thumbnail, category, dan beberapa field tambahan opsional.

7. Melakukan migrasi database dengan python manage.py makemigrations dan python manage.py migrate.

8. Membuat view show_main di main/views.py yang menampilkan nama, kelas, dan nama aplikasi.

9. Membuat template main.html di folder main/templates/ untuk menampilkan context dari view.

10. Menambahkan routing di main/urls.py lalu meng-include ke football_shop/urls.py.

11. Menambahkan requirements.txt dengan pip freeze > requirements.txt dan membuat Procfile berisi web: gunicorn football_shop.wsgi.

12. Push ke GitHub menggunakan git push origin main.

13. Deploy ke PWS dengan menambahkan remote PWS lalu git push pws master.

14. Verifikasi aplikasi di PWS sudah berjalan dengan membuka link project.

15. Membuat README.md yang berisi link aplikasi PWS dan jawaban pertanyaan tugas.

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

    a. urls.py
        - Berfungsi sebagai pengarah (router) request dari client.
        - Setiap URL yang dikunjungi client diarahkan ke fungsi atau kelas di views.py.

    b. views.py
        - Menerima request dari urls.py dan memprosesnya.
        - Bisa mengambil data dari models.py dan menentukan template HTML mana yang digunakan untuk menampilkan hasil.

    c. models.py
        - Tempat menyimpan struktur data atau tabel database.
        - views.py menggunakan models.py untuk mengambil atau menyimpan data.

    d. Template HTML
        - Menyediakan tampilan untuk user.
        - Data yang dikirim dari views.py ditampilkan di sini sehingga client bisa melihat informasi yang diinginkan.

**3. Jelaskan peran settings.py dalam proyek Django!**

settings.py adalah berkas konfigurasi utama di proyek Django. Fungsinya seperti “pusat kontrol” untuk proyek, karena di sini kita mengatur berbagai hal penting, misalnya:

    Database – menentukan jenis database yang digunakan (misal SQLite, PostgreSQL) dan pengaturannya.

    Installed Apps – daftar aplikasi Django yang aktif di proyek.

    Template & Static Files – lokasi template HTML, CSS, JavaScript, gambar, dll.

    Security – pengaturan kunci rahasia (SECRET_KEY), debug mode, dan allowed hosts.

    Middleware & URL Config – daftar middleware dan file URL utama yang dipakai.

    Pengaturan Lain – bahasa, zona waktu, pengaturan email, logging, dll.

**4. Bagaimana cara kerja migrasi database di Django?**

    1. Membuat model, Kita mendefinisikan struktur data atau tabel di models.py.

    2. Membuat file migrasi, Django membaca perubahan di models.py dan membuat file migrasi menggunakan perintah: python manage.py makemigrations

    3. Menerapkan migrasi ke database. Setelah file migrasi dibuat, dijalankan perintah: python manage.py migrate
    Django mengeksekusi instruksi di file migrasi dan menyesuaikan struktur database sesuai model.

**5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Django sering dipilih sebagai framework awal karena mudah dipahami, lengkap, dan cepat digunakan. Dengan Django, kita bisa belajar konsep web development sekaligus praktik nyata tanpa harus membuat semuanya dari nol, karena sudah tersedia banyak fitur siap pakai, seperti autentikasi pengguna, manajemen database, dan antarmuka admin. Selain itu, Django menggunakan Python, yang dikenal sederhana dan mudah dipelajari, sehingga cocok untuk pemula yang ingin memahami logika pemrograman dan alur aplikasi web secara menyeluruh.

**6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
Materi Tutorial 1 disajikannya sangat baik, penjelasannya tetap enak diikuti. Bahasa yang digunakan jelas dan mudah dimengerti, sehingga walaupun hanya membaca, materi tetap gampang dipahami.