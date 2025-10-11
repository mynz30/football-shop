function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  if (!toastComponent) return;

  // Hentikan animasi jika sedang berjalan
  clearTimeout(toastComponent.hideTimeout);

  // Reset style dan visibility
  toastComponent.classList.remove(
    'bg-red-50', 'border-red-500', 'text-red-600',
    'bg-green-50', 'border-green-500', 'text-green-700',
    'bg-yellow-50', 'border-yellow-500', 'text-yellow-700',
    'bg-white', 'border-gray-300', 'text-gray-800',
    'opacity-0', 'translate-y-10', 'hidden'
  );

  // Set ikon & warna berdasarkan tipe notifikasi
  switch (type) {
    case 'success':
      toastIcon.textContent = '✅';
      toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-700');
      toastComponent.style.border = '1px solid #22c55e';
      break;
    case 'error':
      toastIcon.textContent = '❌';
      toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
      toastComponent.style.border = '1px solid #ef4444';
      break;
    case 'warning':
      toastIcon.textContent = '⚠️';
      toastComponent.classList.add('bg-yellow-50', 'border-yellow-500', 'text-yellow-700');
      toastComponent.style.border = '1px solid #eab308';
      break;
    default:
      toastIcon.textContent = 'ℹ️';
      toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
      toastComponent.style.border = '1px solid #d1d5db';
  }

  // Set isi teks toast
  toastTitle.textContent = title || "Juventus Store Indonesia";
  toastMessage.textContent = message || "Pesan dari sistem";

  // Tampilkan toast (dengan animasi masuk)
  toastComponent.classList.remove('hidden');
  toastComponent.classList.add('opacity-100', 'translate-y-0');
  toastComponent.style.transition = 'all 0.3s ease';

  // Sembunyikan toast setelah durasi tertentu
  toastComponent.hideTimeout = setTimeout(() => {
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-10');

    // Sembunyikan setelah animasi keluar selesai
    setTimeout(() => {
      toastComponent.classList.add('hidden');
    }, 300);
  }, duration);
}
