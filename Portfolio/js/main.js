// main.js

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initScrollObserver();
  initStaggeredObserver();
  initCounters();
});

// Mobile Navigation Toggle
function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  
  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
      // Toggle display
      if (navLinks.style.display === 'flex') {
        navLinks.style.display = 'none';
      } else {
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.width = '100%';
        navLinks.style.background = 'rgba(11, 12, 14, 0.95)';
        navLinks.style.padding = '1rem 0';
        navLinks.style.borderBottom = '1px solid var(--border-color)';
      }
    });
  }
}

// Intersection Observer for scroll animations (fade-up)
function initScrollObserver() {
  const elements = document.querySelectorAll('.reveal');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Optional: stop observing once revealed
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  elements.forEach(el => observer.observe(el));
}

// Staggered reveals for lists and grids
function initStaggeredObserver() {
  const containers = document.querySelectorAll('.stagger-container');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const items = entry.target.querySelectorAll('.reveal-stagger');
        items.forEach((item, index) => {
          setTimeout(() => {
            item.classList.add('active');
          }, index * 150); // Stagger delay
        });
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1
  });
  
  containers.forEach(container => observer.observe(container));
}

// Animated Counters for "Why Me" Section
function initCounters() {
  const counters = document.querySelectorAll('.stat-number');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const targetNumber = parseInt(target.getAttribute('data-target'), 10);
        const suffix = target.getAttribute('data-suffix') || '';
        const duration = 2000; // ms
        
        let startTimestamp = null;
        const step = (timestamp) => {
          if (!startTimestamp) startTimestamp = timestamp;
          const progress = Math.min((timestamp - startTimestamp) / duration, 1);
          // Easing easeOutQuart
          const easeOut = 1 - Math.pow(1 - progress, 4);
          const currentNumber = Math.floor(easeOut * targetNumber);
          
          target.innerText = currentNumber + suffix;
          
          if (progress < 1) {
            window.requestAnimationFrame(step);
          } else {
            target.innerText = targetNumber + suffix;
          }
        };
        
        window.requestAnimationFrame(step);
        observer.unobserve(target);
      }
    });
  }, {
    threshold: 0.5
  });
  
  counters.forEach(counter => observer.observe(counter));
}

// Functions for modals can be added here if needed for Featured Case Studies
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}
