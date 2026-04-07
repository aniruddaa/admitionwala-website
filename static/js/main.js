// Main JavaScript with jQuery for WebStudio

jQuery(document).ready(function($) {
    
    // === MOBILE MENU FUNCTIONALITY ===
    $('#mobile-menu-btn').on('click', function() {
        $('#mobile-menu').slideToggle(300);
    });
    
    // Close mobile menu when clicking on a link
    $('#mobile-menu a').on('click', function() {
        $('#mobile-menu').slideUp(300);
    });
    
    // === NAVBAR SCROLL EFFECT ===
    $(window).on('scroll', function() {
        if($(this).scrollTop() > 50) {
            $('nav').addClass('scrolled');
        } else {
            $('nav').removeClass('scrolled');
        }
    });
    
    // === SMOOTH SCROLL FOR ANCHOR LINKS ===
    $(document).on('click', 'a[href^="#"]', function(e) {
        e.preventDefault();
        const target = $(this.getAttribute('href'));
        if(target.length) {
            $('html, body').stop().animate({
                scrollTop: target.offset().top - 80
            }, 1000);
        }
    });
    
    // === ANIMATION ON SCROLL ===
    function animateOnScroll() {
        $('.service-card, .article-card, .value-card, .team-member, .portfolio-item').each(function() {
            const elementOffset = $(this).offset().top;
            const windowScroll = $(window).scrollTop() + $(window).height();
            
            if(windowScroll > elementOffset + 100) {
                $(this).css({
                    'animation': 'fadeIn 0.8s ease-out forwards'
                });
            }
        });
    }
    
    $(window).on('scroll', animateOnScroll);
    animateOnScroll(); // Run on page load
    
    // === PORTFOLIO FILTER ===
    $('.filter-btn').on('click', function() {
        const filter = $(this).data('filter');
        
        // Update active button
        $('.filter-btn').removeClass('active');
        $(this).addClass('active');
        
        // Filter items
        if(filter === 'all') {
            $('.portfolio-item').fadeIn(300);
        } else {
            $('.portfolio-item').fadeOut(300);
            $('.portfolio-item[data-category="' + filter + '"]').fadeIn(300);
        }
    });
    
    // === STATS COUNTER ANIMATION ===
    let statsAnimated = false;
    
    function animateStats() {
        if(statsAnimated) return;
        
        const statsOffset = $('.stat-number').first().offset().top;
        const windowScroll = $(window).scrollTop() + $(window).height();
        
        if(windowScroll > statsOffset) {
            statsAnimated = true;
            
            $('.stat-number').each(function() {
                const $this = $(this);
                const target = parseInt($this.data('target'));
                let current = 0;
                const increment = target / 40;
                
                const counter = setInterval(function() {
                    current += increment;
                    if(current >= target) {
                        $this.text(target);
                        clearInterval(counter);
                    } else {
                        $this.text(Math.floor(current));
                    }
                }, 50);
            });
        }
    }
    
    $(window).on('scroll', animateStats);
    
    // === CONTACT FORM HANDLING ===
    $('#contact-form').on('submit', function(e) {
        e.preventDefault();
        
        const form = $(this);
        const name = $('#name').val();
        const email = $('#email').val();
        const message = $('#message').val();
        const csrfToken = $('[name="csrfmiddlewaretoken"]').val();
        
        // Disable submit button
        const submitBtn = form.find('button[type="submit"]');
        const originalText = submitBtn.html();
        submitBtn.prop('disabled', true).html('<i class="fas fa-spinner fa-spin mr-2"></i>Sending...');
        
        $.ajax({
            url: $('#contact-form').attr('action') || '/api/submit-contact/',
            type: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': csrfToken
            },
            data: JSON.stringify({
                name: name,
                email: email,
                message: message
            }),
            success: function(response) {
                // Show success message
                $('#contact-form')[0].reset();
                $('#success-message').removeClass('hidden').addClass('message-box');
                $('#error-message').addClass('hidden');
                
                // Re-enable submit button
                submitBtn.prop('disabled', false).html(originalText);
                
                // Auto-hide success message after 5 seconds
                setTimeout(function() {
                    $('#success-message').fadeOut(300);
                }, 5000);
            },
            error: function(response) {
                let errorText = 'Something went wrong. Please try again.';
                
                if(response.responseJSON && response.responseJSON.message) {
                    errorText = response.responseJSON.message;
                }
                
                $('#error-text').text(errorText);
                $('#error-message').removeClass('hidden').addClass('message-box');
                $('#success-message').addClass('hidden');
                
                // Re-enable submit button
                submitBtn.prop('disabled', false).html(originalText);
                
                // Auto-hide error message after 5 seconds
                setTimeout(function() {
                    $('#error-message').fadeOut(300);
                }, 5000);
            }
        });
    });
    
    // === FORM INPUT FOCUS EFFECTS ===
    $('input, textarea').on('focus', function() {
        $(this).parent().find('label').css('color', '#2563eb');
    });
    
    $('input, textarea').on('blur', function() {
        $(this).parent().find('label').css('color', '');
    });
    
    // === PARALLAX EFFECT ===
    $(window).on('scroll', function() {
        const scrollPos = $(window).scrollTop();
        
        // Apply parallax to hero section
        if(scrollPos < $(window).height()) {
            $('.hero-section').css('transform', 'translateY(' + (scrollPos * 0.5) + 'px)');
        }
    });
    
    // === LOAD MORE FUNCTIONALITY ===
    let currentPage = 1;
    const itemsPerPage = 9;
    
    // Add feature: load more items on button click
    $(document).on('click', '.load-more-btn', function() {
        const btn = $(this);
        btn.prop('disabled', true).html('<i class="fas fa-spinner fa-spin mr-2"></i>Loading...');
        
        // Simulate loading more items
        setTimeout(function() {
            btn.prop('disabled', false).html('Load More Projects');
            // In a real scenario, this would fetch more items via AJAX
        }, 1000);
    });
    
    // === DARK MODE TOGGLE (Optional) ===
    // Uncomment to enable dark mode
    /*
    $('#dark-mode-toggle').on('click', function() {
        $('body').toggleClass('dark-mode');
        localStorage.setItem('darkMode', $('body').hasClass('dark-mode'));
    });
    
    // Restore dark mode preference
    if(localStorage.getItem('darkMode') === 'true') {
        $('body').addClass('dark-mode');
    }
    */
    
    // === KEYBOARD NAVIGATION ===
    $(document).on('keydown', function(e) {
        // Close mobile menu on ESC
        if(e.keyCode === 27) {
            $('#mobile-menu').slideUp(300);
        }
    });
    
    // === LAZY LOADING IMAGES ===
    if('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img.lazy').forEach(img => imageObserver.observe(img));
    }
    
    // === SCROLL TO TOP BUTTON ===
    // Add scroll to top button functionality
    $(window).on('scroll', function() {
        if($(this).scrollTop() > 300) {
            $('#scroll-to-top').fadeIn(300);
        } else {
            $('#scroll-to-top').fadeOut(300);
        }
    });
    
    $(document).on('click', '#scroll-to-top', function(e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, 'slow');
    });
    
    // === PAGE TRANSITION ANIMATIONS ===
    // Add fade-in animation to page load
    $('body').css('opacity', '0').animate({ opacity: 1 }, 300);
    
});

// === UTILITY FUNCTIONS ===

// Function to check if element is in viewport
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to format date
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString('en-US', options);
}

// Function to debounce
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Function to throttle
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
