**Nama** : Faishal Khoiriansyah Wicaksono
**NPM** : 2406436335

Football Shop

Live (PWS): https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id/  

1) Apa itu Django `AuthenticationForm`?

`AuthenticationForm` adalah form bawaan Django untuk login menggunakan username dan password. Kelebihan:

* Terintegrasi dengan backend Django.
* Validasi kredensial dan user inactive otomatis.
* Mudah digunakan di template.

Kekurangan:

* Hanya mendukung username+password.
* Tidak ada 2FA atau captcha bawaan.
* Pesan error generik.

---

2) Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikannya?

* **Autentikasi**: memverifikasi identitas (Siapakah Anda?).
* **Otorisasi**: menentukan hak akses (Apa yang boleh dilakukan?).

Django:

* Autentikasi: `authenticate()`, `login()`, `request.user`
* Otorisasi: `user.has_perm()`, decorators `@login_required`, `@permission_required`

---

3) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

* **Cookies**: disimpan di browser, kapasitas kecil, bisa diubah user.
* **Session**: disimpan di server, lebih aman, bisa invalidasi paksa, perlu backend (DB/Redis).

---

4) Apakah penggunaan cookies aman secara default dalam pengembangan web? Risiko potensial dan bagaimana Django menanganinya.

* Tidak sepenuhnya aman secara default.
* Risiko: XSS, CSRF, session hijacking.
* Django membantu dengan: signed cookies, HttpOnly, CSRF middleware, Secure flag.

---

5) Jelaskan bagaimana cara mengimplementasikan checklist di atas secara step-by-step (bukan hanya mengikuti tutorial)

1. Pilih model user: default atau custom.
2. Konfigurasi session di `settings.py` dan keamanan cookie.
3. Buat login view menggunakan `AuthenticationForm`.
4. Atur permission & group.
5. Tambahkan rate-limit/lockout jika perlu.
6. Test flow login, permission, session.
7. Deployment: gunakan HTTPS, Redis (jika multiple instance), dan environment variables.


