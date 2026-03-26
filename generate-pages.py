#!/usr/bin/env python3
"""
Generate all HTML pages for EverydayMoments website
Run this script to create all pages automatically
"""

import json
import re

# Header template
HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - EverydayMoments</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-content">
            <a href="index.html" class="logo">EverydayMoments</a>
            
            <nav class="nav-desktop">
                <a href="index.html">Home</a>
                <a href="about.html">About</a>
                <a href="contact.html">Contact</a>
                <a href="how-we-make-money.html">How We Make Money</a>
                <a href="editorial-guidelines.html">Editorial Guidelines</a>
            </nav>
            
            <button class="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Toggle menu">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                </svg>
            </button>
        </div>
        
        <nav class="mobile-menu" id="mobileMenu">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="how-we-make-money.html">How We Make Money</a>
            <a href="editorial-guidelines.html">Editorial Guidelines</a>
        </nav>
    </header>
'''

# Footer template
FOOTER = '''    <!-- Footer -->
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>Company</h3>
                <ul>
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="how-we-make-money.html">How We Make Money</a></li>
                    <li><a href="editorial-guidelines.html">Editorial Guidelines</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Legal</h3>
                <ul>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms of Service</a></li>
                    <li><a href="disclaimer.html">Disclaimer</a></li>
                    <li><a href="cookie-policy.html">Cookie Policy</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Categories</h3>
                <ul>
                    <li><a href="#productivity">Productivity</a></li>
                    <li><a href="#technology">Technology</a></li>
                    <li><a href="#wellness">Wellness</a></li>
                    <li><a href="#lifestyle">Lifestyle</a></li>
                    <li><a href="#finance">Finance</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Follow Us</h3>
                <ul>
                    <li><a href="#facebook">Facebook</a></li>
                    <li><a href="#twitter">Twitter</a></li>
                    <li><a href="#instagram">Instagram</a></li>
                    <li><a href="#linkedin">LinkedIn</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 EverydayMoments. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

def create_page(title, description, content):
    """Create a complete HTML page"""
    return HEADER.format(title=title, description=description) + content + FOOTER

# Read articles from articles.js file
def read_articles():
    """Read articles from the JavaScript file"""
    with open('articles.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the articles array from JavaScript
    match = re.search(r'const articles = (\[.*?\]);', content, re.DOTALL)
    if match:
        articles_json = match.group(1)
        # Replace JavaScript single quotes with double quotes for JSON
        articles_json = articles_json.replace("'", '"')
        return json.loads(articles_json)
    return []

def generate_article_page(article):
    """Generate an individual article page"""
    content = article['content']
    
    # Build points list
    points_html = ''
    for section in content['sections']:
        points_html += f'<h2>{section["heading"]}</h2><ul>'
        for point in section['points']:
            points_html += f'<li>{point}</li>'
        points_html += '</ul>'
    
    page_content = f'''
    <div class="article-header">
        <span class="article-category">{article['category']}</span>
        <h1 class="page-title">{article['title']}</h1>
        <div class="article-meta" style="justify-content: center;">
            <span>{article['date']}</span>
            <span>•</span>
            <span>{article['readTime']}</span>
        </div>
    </div>

    <img src="{article['imageUrl']}" alt="{article['title']}" class="article-detail-image" style="max-width: 56rem; margin: 0 auto; display: block; padding: 0 1rem;">

    <div class="article-body">
        <p class="page-text">{content['introduction']}</p>
        
        {points_html}
        
        <div class="why-it-works">
            <h3>Why It Works</h3>
            <p>{content['whyItWorks']}</p>
        </div>
        
        <p class="page-text">{content['conclusion']}</p>
        
        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e5e7eb;">
            <a href="index.html" style="color: #2563eb; font-weight: 500;">&larr; Back to all articles</a>
        </div>
    </div>
    '''
    
    return create_page(article['title'], article['excerpt'], page_content)

# Create all article pages
try:
    articles = read_articles()
    print(f"Found {len(articles)} articles")
    
    for article in articles:
        filename = f"article-{article['slug']}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(generate_article_page(article))
        print(f"✓ Created {filename}")
    
    print("\n✅ All article pages generated successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\nNext, create the remaining static pages manually or use the templates below.")
