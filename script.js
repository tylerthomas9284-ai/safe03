// Mobile menu toggle
function toggleMobileMenu() {
  const mobileMenu = document.getElementById('mobileMenu');
  mobileMenu.classList.toggle('active');
}

// Contact form handling
function handleContactSubmit(event) {
  event.preventDefault();
  
  const form = event.target;
  const submitBtn = form.querySelector('button[type="submit"]');
  const successMsg = document.getElementById('successMessage');
  
  // Disable submit button
  submitBtn.disabled = true;
  submitBtn.textContent = 'Sending...';
  
  // Simulate form submission
  setTimeout(() => {
    // Show success message
    successMsg.classList.add('show');
    
    // Reset form
    form.reset();
    
    // Re-enable button
    submitBtn.disabled = false;
    submitBtn.textContent = 'Send Message';
    
    // Hide success message after 5 seconds
    setTimeout(() => {
      successMsg.classList.remove('show');
    }, 5000);
  }, 1000);
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', function() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
});

// Article filtering (for potential future use)
function filterArticles(category) {
  const articleCards = document.querySelectorAll('.article-card');
  
  articleCards.forEach(card => {
    const cardCategory = card.dataset.category;
    
    if (category === 'all' || cardCategory === category) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

// Filter articles by category with smooth scroll
function filterByCategory(category) {
  const articleCards = document.querySelectorAll('.article-card');
  const articlesSection = document.getElementById('latest');
  let visibleCount = 0;
  
  articleCards.forEach(card => {
    const cardCategory = card.dataset.category;
    
    if (cardCategory === category) {
      card.style.display = 'flex';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });
  
  // Scroll to articles section
  if (articlesSection) {
    articlesSection.scrollIntoView({ behavior: 'smooth' });
  }
  
  // Update section title
  const sectionTitle = document.querySelector('#latest .section-title');
  if (sectionTitle) {
    sectionTitle.textContent = `${category} Articles (${visibleCount})`;
  }
}

// Show all articles
function showAllArticles() {
  const articleCards = document.querySelectorAll('.article-card');
  const articlesSection = document.getElementById('latest');
  
  articleCards.forEach(card => {
    card.style.display = 'flex';
  });
  
  // Update section title back to default
  const sectionTitle = document.querySelector('#latest .section-title');
  if (sectionTitle) {
    sectionTitle.textContent = 'Latest Stories';
  }
  
  // Scroll to articles section
  if (articlesSection) {
    articlesSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Back to top button
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Add scroll event listener for back to top button
window.addEventListener('scroll', function() {
  const backToTopBtn = document.getElementById('backToTop');
  if (backToTopBtn) {
    if (window.pageYOffset > 300) {
      backToTopBtn.style.display = 'block';
    } else {
      backToTopBtn.style.display = 'none';
    }
  }
});