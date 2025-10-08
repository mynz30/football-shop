function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
  
    if (!toastComponent) return;
  
    // Reset warna & ikon
    toastComponent.classList.remove(
      'bg-red-50', 'border-red-500', 'text-red-600',
      'bg-green-50', 'border-green-500', 'text-green-600',
      'bg-white', 'border-gray-300', 'text-gray-800'
    );
    toastIcon.textContent = '';
  
    // Style & ikon berdasarkan tipe
    if (type === 'success') {
      toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-700');
      toastComponent.style.border = '1px solid #22c55e';
      toastIcon.textContent = '✅';
    } else if (type === 'error') {
      toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
      toastComponent.style.border = '1px solid #ef4444';
      toastIcon.textContent = '❌';
    } else if (type === 'warning') {
      toastComponent.classList.add('bg-yellow-50', 'border-yellow-500', 'text-yellow-700');
      toastComponent.style.border = '1px solid #eab308';
      toastIcon.textContent = '⚠️';
    } else {
      toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
      toastComponent.style.border = '1px solid #d1d5db';
      toastIcon.textContent = 'ℹ️';
    }
  
    // Ganti isi toast
    toastTitle.textContent = title || "Juventus Store Indonesia";
    toastMessage.textContent = message || "Notifikasi dari Football Shop";
  
    // Tampilkan animasi masuk
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');
  
    // Sembunyikan setelah durasi tertentu
    setTimeout(() => {
      toastComponent.classList.remove('opacity-100', 'translate-y-0');
      toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
  }
  