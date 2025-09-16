**Nama** : Faishal Khoiriansyah Wicaksono
**NPM** : 2406436335

Football Shop

Live (PWS): https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id/  

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery memungkinkan backend menyediakan data yang terstruktur ke berbagai client (web frontend, aplikasi mobile, layanan lain/third-party). Manfaat utamanya:

    Interoperabilitas: banyak bahasa dan platform bisa mem-parsing JSON/XML sehingga backend bisa melayani banyak client berbeda.

    Separation of concerns: backend bertanggung jawab menyediakan data; tampilan (UI) dikembangkan terpisah.

    Skalabilitas & integrasi: memudahkan integrasi antar-service (microservices) dan pihak ketiga (mis. payment gateway, analytics).

    Efisiensi: format ringan (JSON) mengurangi transfer data dan parsing lebih cepat untuk aplikasi web/mobile.

    Reusability: satu API endpoint bisa dipakai oleh banyak client (web, mobile, script automatisasi).

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
JSON
    Lebih ringkas (kurang verbose).
    Mudah dipetakan ke struktur data native (object/array) di JavaScript dan banyak bahasa lainnya.
    Parsing biasanya lebih cepat dan lebih sedikit overhead.
    Lebih cocok untuk RESTful APIs modern dan aplikasi web/mobile.

XML
    Lebih verbose, tapi mendukung fitur seperti attributes, namespaces, dan validasi via XSD.
    Masih digunakan di beberapa domain enterprise, SOAP, atau ketika skema dan validasi ketat diperlukan.

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
form.is_valid() menjalankan proses validasi form secara keseluruhan:

    Memanggil pembersihan (cleaning) tiap field (to_python, validate, run_validators).
    Memanggil Form.clean() / ModelForm.clean() untuk validasi yang bersifat cross-field.
    Mengisi form.cleaned_data jika valid, atau form.errors jika ada kesalahan.
    Mengembalikan True jika semua validasi lolos, False jika ada error.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

{% csrf_token %} memasukkan token unik ke form yang dicocokkan dengan token pada sesi/cookie (dikelola oleh CsrfViewMiddleware).
Token ini memastikan request POST berasal dari halaman/asal yang sah (same origin), bukan request dari situs lain.
Jika tidak menambahkan csrf_token:

Django akan menolak request POST (biasanya 403) ketika CsrfViewMiddleware aktif.
Kalau middleware dinonaktifkan atau pengaturan salah, form tanpa CSRF dapat dimanfaatkan penyerang untuk Cross-Site Request Forgery (CSRF):
    Contoh serangan: penyerang menaruh form tersembunyi di situsnya yang mengirim POST ke endpoint kamu (mis. POST /change-email/) — kalau korban sedang login di situs kamu, browser akan mengirim cookie sesi, dan tanpa token server tidak bisa membedakan apakah request berasal dari user atau dari penyerang → penyerang melakukan aksi atas nama korban (transfer, ubah data, dsb).
CSRF token mencegah eksploitasi ini karena penyerang tidak bisa membaca atau menebak token yang tersimpan di sesi korban (Same-Origin Policy mencegah akses).

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Menambahkan Model
    Membuat model Product di main/models.py dengan field beragam

2. Membuat Form
    Menambahkan file main/forms.py:

3. Membuat Views

    Menambahkan 3 view utama

4. Menambahkan URL Routing

    Mengupdate main/urls.py:


5. Membuat Template

    main.html → menampilkan list produk dengan tombol Add (redirect ke create-product) dan tombol Detail untuk setiap produk.
    create_product.html → berisi form dengan {% csrf_token %}.
    product_detail.html → menampilkan detail satu produk.

5. Testing di Browser

    Menjalankan server
    Mengakses:
    http://127.0.0.1:8000/ → melihat semua produk.
    http://127.0.0.1:8000/create-product/ → menambahkan produk baru.
    http://127.0.0.1:8000/product/<id>/ → melihat detail produk.

6. Testing Data Delivery dengan Postman

    Melakukan GET request ke:
    http://127.0.0.1:8000/json/
    http://127.0.0.1:8000/xml/
    http://127.0.0.1:8000/json/<id>/
    http://127.0.0.1:8000/xml/<id>/


**Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
Tambahkan lebih banyak contoh troubleshooting

![alt text](<Screenshot 2025-09-16 at 23.31.41.png>)
![alt text](<Screenshot 2025-09-16 at 23.32.04.png>)
![alt text](<Screenshot 2025-09-16 at 23.43.44.png>)
![alt text](<Screenshot 2025-09-16 at 23.44.11.png>)