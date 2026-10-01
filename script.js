// ==========================================================================
// Interactive Navbar Logic
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  const mobileToggle = document.getElementById('mobile-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  const btnClickMe = document.getElementById('btn-click-me');
  const btnContact = document.getElementById('btn-contact');
  const toast = document.getElementById('toast');
  const toastTitle = document.getElementById('toast-title');
  const toastDesc = document.getElementById('toast-desc');

  let clickCount = 0;
  let toastTimeout = null;

  // Function to show animated toast notification
  function showToast(title, desc, icon = '✨') {
    toastTitle.textContent = title;
    toastDesc.textContent = desc;
    document.querySelector('.toast-icon').textContent = icon;
    
    toast.classList.add('show');
    
    if (toastTimeout) clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
      toast.classList.remove('show');
    }, 3200);
  }

  // 1. Mobile Menu Toggle
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileToggle.classList.toggle('active');
      navMenu.classList.toggle('open');
    });
  }

  // 2. Active Link Switching & Smooth navigation
  navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      navLinks.forEach((l) => l.classList.remove('active'));
      link.classList.add('active');

      // Close mobile menu on item click
      if (navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        mobileToggle.classList.remove('active');
      }
    });
  });

  // 3. "Click Me" button interaction
  if (btnClickMe) {
    btnClickMe.addEventListener('click', () => {
      clickCount++;
      // Subtle pulse scale
      btnClickMe.style.transform = 'scale(0.92)';
      setTimeout(() => {
        btnClickMe.style.transform = '';
      }, 150);

      showToast(
        'Click Me bosildi!',
        `Siz tugmani ${clickCount}-marta bosdingiz. Ajoyib!`,
        '🎉'
      );
    });
  }

  // 4. "Contact" button interaction
  if (btnContact) {
    btnContact.addEventListener('click', () => {
      showToast(
        'Contact bo\'limi',
        'Biz bilan bog\'lanish uchun taklif yuborildi!',
        '📬'
      );
    });
  }

  // 5. Scroll effect for header
  const header = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
});
