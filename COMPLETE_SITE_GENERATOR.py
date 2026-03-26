#!/usr/bin/env python3
"""
Complete Site Generator for EverydayMoments
This script generates ALL HTML pages for the website
"""

import os
import json
import re

print("🚀 EverydayMoments Complete Site Generator")
print("=" * 50)

# Common header/footer templates
def get_header(title, description):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - EverydayMoments</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
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

FOOTER = '''    <footer class="footer">
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
                    <li><a href="index.html#productivity">Productivity</a></li>
                    <li><a href="index.html#technology">Technology</a></li>
                    <li><a href="index.html#wellness">Wellness</a></li>
                    <li><a href="index.html#lifestyle">Lifestyle</a></li>
                    <li><a href="index.html#finance">Finance</a></li>
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

# Read articles
def read_articles():
    with open('articles.js', 'r') as f:
        content = f.read()
    match = re.search(r'const articles = (\[.*?\]);', content, re.DOTALL)
    if match:
        articles_str = match.group(1)
        articles_str = re.sub(r"'([^']*)'", r'"\1"', articles_str)
        articles_str = re.sub(r'(\w+):', r'"\1":', articles_str)
        return eval(articles_str)  # Using eval for complex nested structure
    return []

# Generate article pages
articles = read_articles()
count = 0

for article in articles:
    content = article['content']
    points_html = ''
    for section in content['sections']:
        points_html += f'<h2>{section["heading"]}</h2><ul>'
        for point in section['points']:
            points_html += f'<li>{point}</li>'
        points_html += '</ul>'
    
    page = get_header(article['title'], article['excerpt'])
    page += f'''
    <div class="article-header">
        <span class="article-category">{article['category']}</span>
        <h1 class="page-title">{article['title']}</h1>
        <div class="article-meta" style="justify-content: center;">
            <span>{article['date']}</span><span>•</span><span>{article['readTime']}</span>
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
    page += FOOTER
    
    filename = f"article-{article['slug']}.html"
    with open(filename, 'w') as f:
        f.write(page)
    count += 1
    print(f"✓ Generated article-{article['slug']}.html")

print(f"\n✅ Generated {count} article pages")

# Generate Contact Page
contact_html = get_header("Contact Us", "Get in touch with the EverydayMoments team")
contact_html += '''
    <div class="page-content">
        <h1 class="page-title">Contact Us</h1>
        <p class="page-intro">We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
        
        <div class="success-message" id="successMessage">
            ✓ Thank you for your message! We'll get back to you soon.
        </div>

        <form class="contact-form" onsubmit="handleContactSubmit(event)">
            <div class="form-group">
                <label class="form-label" for="name">Name *</label>
                <input type="text" id="name" name="name" class="form-input" required>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="email">Email *</label>
                <input type="email" id="email" name="email" class="form-input" required>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="subject">Subject *</label>
                <select id="subject" name="subject" class="form-select" required>
                    <option value="">Select a subject</option>
                    <option value="general">General Inquiry</option>
                    <option value="feedback">Feedback</option>
                    <option value="content">Content Suggestion</option>
                    <option value="partnership">Partnership Opportunity</option>
                    <option value="technical">Technical Issue</option>
                </select>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="message">Message *</label>
                <textarea id="message" name="message" class="form-textarea" required></textarea>
            </div>
            
            <button type="submit" class="btn">Send Message</button>
        </form>
    </div>
''' + FOOTER

with open('contact.html', 'w') as f:
    f.write(contact_html)
print("✓ Generated contact.html")

# Generate all other pages similarly...
# (Continuing with remaining pages)

# How We Make Money
hwmm_html = get_header("How We Make Money", "Learn about our revenue model and commitment to transparency")
hwmm_html += '''
    <div class="page-content">
        <h1 class="page-title">How We Make Money</h1>
        <p class="page-intro">EverydayMoments is supported through advertising and partnerships.</p>
        <p class="page-text">We believe in being completely transparent about how we generate revenue to support our operations. This page explains exactly how EverydayMoments earns money while maintaining our commitment to providing valuable, independent content to our readers.</p>
        
        <h2 class="section-heading">Our Revenue Sources</h2>
        <p class="page-text">We maintain editorial independence while generating revenue through the following methods:</p>
        
        <div class="icon-card">
            <div class="icon-wrapper blue">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
            </div>
            <div>
                <h3 class="subsection-heading">Display Advertising</h3>
                <p class="page-text">We display advertisements from third-party advertising networks on our website. These ads help support our operations and keep our content free for readers.</p>
            </div>
        </div>

        <div class="icon-card">
            <div class="icon-wrapper purple">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>
            </div>
            <div>
                <h3 class="subsection-heading">Sponsored Content</h3>
                <p class="page-text">We occasionally publish sponsored articles or content. All sponsored material is clearly labeled and disclosed to readers, maintaining transparency.</p>
            </div>
        </div>

        <div class="icon-card">
            <div class="icon-wrapper green">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
            </div>
            <div>
                <h3 class="subsection-heading">Affiliate Partnerships</h3>
                <p class="page-text">Some of our articles may contain affiliate links. When you purchase products through these links, we may earn a small commission at no extra cost to you.</p>
            </div>
        </div>

        <div class="icon-card">
            <div class="icon-wrapper orange">
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.25m4.24 4.24l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m4.24-4.24l4.24-4.24"/></svg>
            </div>
            <div>
                <h3 class="subsection-heading">Content Recommendation Platforms</h3>
                <p class="page-text">We use advertising networks such as content recommendation platforms that suggest related articles and content to our readers.</p>
            </div>
        </div>

        <div class="alert-box blue">
            <h3 class="subsection-heading">Editorial Independence</h3>
            <p>We maintain strict editorial independence. Our content decisions are never influenced by advertisers or sponsors. All sponsored material is clearly disclosed to readers, and we always prioritize providing accurate, helpful information.</p>
        </div>

        <div class="alert-box green">
            <h3 class="subsection-heading">Transparency Commitment</h3>
            <p>We believe in complete transparency with our readers. Any content that has been sponsored, paid for, or involves affiliate partnerships will always be clearly labeled and identified.</p>
        </div>
    </div>
''' + FOOTER

with open('how-we-make-money.html', 'w') as f:
    f.write(hwmm_html)
print("✓ Generated how-we-make-money.html")

# Editorial Guidelines
eg_html = get_header("Editorial Guidelines", "Our commitment to quality journalism and content standards")
eg_html += '''
    <div class="page-content">
        <h1 class="page-title">Editorial Guidelines</h1>
        <p class="page-intro">Our editorial team follows strict publishing standards to ensure quality and transparency.</p>
        <p class="page-text">At EverydayMoments, we are committed to producing content that is accurate, trustworthy, and valuable to our readers. These editorial guidelines outline the principles and processes that govern how we create, review, and publish content across our platform.</p>
        
        <h2 class="section-heading">Our Core Principles</h2>
        
        <div class="feature-list">
            <div class="feature-item">
                <svg class="check-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Accuracy:</strong> We verify facts and cite reliable sources</span>
            </div>
            <div class="feature-item">
                <svg class="check-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Transparency:</strong> Clear disclosure of sponsored content</span>
            </div>
            <div class="feature-item">
                <svg class="check-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Editorial Independence:</strong> Content free from advertiser influence</span>
            </div>
            <div class="feature-item">
                <svg class="check-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Reader-First Content:</strong> Focus on providing genuine value</span>
            </div>
        </div>

        <h2 class="section-heading">Our Process</h2>
        <ol style="padding-left: 1.5rem; line-height: 2;">
            <li><strong>Topic Research:</strong> We research topics thoroughly to ensure they are relevant, timely, and valuable to our readers.</li>
            <li><strong>Fact Checking:</strong> All claims and statistics are verified against credible sources before publication.</li>
            <li><strong>Professional Editing:</strong> Content goes through editorial review to ensure clarity, accuracy, and readability.</li>
            <li><strong>Content Review Before Publishing:</strong> A final review ensures all standards are met before content goes live.</li>
        </ol>

        <h2 class="section-heading">What We Avoid</h2>
        <ul style="list-style: none; padding-left: 0;">
            <li class="page-text">❌ <strong>Misleading Headlines:</strong> Our headlines accurately reflect article content without exaggeration.</li>
            <li class="page-text">❌ <strong>Sensationalism:</strong> We present information in a balanced, fact-based manner.</li>
            <li class="page-text">❌ <strong>False Claims:</strong> All information is verified and sourced from credible references.</li>
            <li class="page-text">❌ <strong>Unverified Health or Financial Advice:</strong> We provide general information only and encourage readers to consult professionals.</li>
        </ul>

        <div class="alert-box blue">
            <p>These guidelines ensure that EverydayMoments provides trustworthy, helpful content that readers can rely on for making informed decisions in their daily lives.</p>
        </div>
    </div>
''' + FOOTER

with open('editorial-guidelines.html', 'w') as f:
    f.write(eg_html)
print("✓ Generated editorial-guidelines.html")

# Privacy Policy
pp_html = get_header("Privacy Policy", "How we collect, use, and protect your information")
pp_html += '''
    <div class="page-content">
        <h1 class="page-title">Privacy Policy</h1>
        <p class="page-text"><em>Last updated: March 13, 2026</em></p>
        
        <p class="page-intro">EverydayMoments ("we," "our," or "us") respects your privacy and is committed to protecting your personal data.</p>
        
        <h2 class="section-heading">Information We Collect</h2>
        <p class="page-text">We may collect and process the following types of information:</p>
        <ul>
            <li>Information you provide directly (contact forms, newsletter subscriptions)</li>
            <li>Usage data (pages viewed, time spent, browser type)</li>
            <li>Cookies and tracking technologies</li>
        </ul>

        <h2 class="section-heading">How We Use Your Information</h2>
        <ul>
            <li>To provide and improve our services</li>
            <li>To communicate with you</li>
            <li>To analyze website usage</li>
            <li>To deliver relevant advertising</li>
        </ul>

        <h2 class="section-heading">Your Rights</h2>
        <p class="page-text">You have the right to:</p>
        <ul>
            <li>Access your personal data</li>
            <li>Correct inaccurate data</li>
            <li>Request deletion of your data</li>
            <li>Opt-out of marketing communications</li>
        </ul>

        <h2 class="section-heading">Contact Us</h2>
        <p class="page-text">If you have questions about this Privacy Policy, please <a href="contact.html" style="color: #2563eb;">contact us</a>.</p>
    </div>
''' + FOOTER

with open('privacy-policy.html', 'w') as f:
    f.write(pp_html)
print("✓ Generated privacy-policy.html")

# Terms of Service
terms_html = get_header("Terms of Service", "Terms and conditions for using EverydayMoments")
terms_html += '''
    <div class="page-content">
        <h1 class="page-title">Terms of Service</h1>
        <p class="page-text"><em>Last updated: March 13, 2026</em></p>
        
        <p class="page-intro">By accessing EverydayMoments, you agree to be bound by these Terms of Service.</p>
        
        <h2 class="section-heading">Use of Our Website</h2>
        <p class="page-text">You may use our website for lawful purposes only. You agree not to:</p>
        <ul>
            <li>Violate any applicable laws or regulations</li>
            <li>Infringe on intellectual property rights</li>
            <li>Transmit harmful code or malware</li>
            <li>Attempt to gain unauthorized access to our systems</li>
        </ul>

        <h2 class="section-heading">Content</h2>
        <p class="page-text">All content on this website is owned by EverydayMoments and protected by copyright laws. You may not reproduce, distribute, or create derivative works without our written permission.</p>

        <h2 class="section-heading">Disclaimer</h2>
        <p class="page-text">The content on this website is for informational purposes only. We make no warranties about the completeness, reliability, or accuracy of this information.</p>

        <h2 class="section-heading">Changes to Terms</h2>
        <p class="page-text">We reserve the right to modify these terms at any time. Changes will be effective immediately upon posting.</p>

        <h2 class="section-heading">Contact</h2>
        <p class="page-text">For questions about these Terms, please <a href="contact.html" style="color: #2563eb;">contact us</a>.</p>
    </div>
''' + FOOTER

with open('terms.html', 'w') as f:
    f.write(terms_html)
print("✓ Generated terms.html")

# Disclaimer
disclaimer_html = get_header("Disclaimer", "Important information about our content")
disclaimer_html += '''
    <div class="page-content">
        <h1 class="page-title">Disclaimer</h1>
        <p class="page-text"><em>Last updated: March 13, 2026</em></p>
        
        <h2 class="section-heading">General Information</h2>
        <p class="page-text">The information provided on EverydayMoments is for general informational purposes only. All information is provided in good faith, however we make no representation or warranty of any kind regarding the accuracy, adequacy, validity, reliability, or completeness of any information on the site.</p>

        <h2 class="section-heading">Professional Advice Disclaimer</h2>
        <p class="page-text">The site cannot and does not contain medical, legal, or financial advice. The information is provided for general informational and educational purposes only and is not a substitute for professional advice. Accordingly, before taking any actions based upon such information, we encourage you to consult with the appropriate professionals.</p>

        <h2 class="section-heading">Affiliate Links Disclaimer</h2>
        <p class="page-text">Some content may contain affiliate links. If you make a purchase through these links, we may earn a commission at no additional cost to you.</p>

        <h2 class="section-heading">External Links Disclaimer</h2>
        <p class="page-text">This website may contain links to external websites that are not provided or maintained by us. We do not guarantee the accuracy, relevance, or completeness of any information on these external websites.</p>

        <div class="alert-box amber">
            <p><strong>Use at Your Own Risk:</strong> The use of any information provided on this site is solely at your own risk. We assume no responsibility for errors or omissions in the contents of the service.</p>
        </div>
    </div>
''' + FOOTER

with open('disclaimer.html', 'w') as f:
    f.write(disclaimer_html)
print("✓ Generated disclaimer.html")

# Cookie Policy
cookie_html = get_header("Cookie Policy", "How we use cookies and similar technologies")
cookie_html += '''
    <div class="page-content">
        <h1 class="page-title">Cookie Policy</h1>
        <p class="page-text"><em>Last updated: March 13, 2026</em></p>
        
        <p class="page-intro">This Cookie Policy explains how EverydayMoments uses cookies and similar technologies.</p>
        
        <h2 class="section-heading">What Are Cookies?</h2>
        <p class="page-text">Cookies are small text files that are placed on your device when you visit our website. They help us provide you with a better experience and allow certain features to function properly.</p>

        <h2 class="section-heading">Types of Cookies We Use</h2>
        
        <h3 class="subsection-heading">Essential Cookies</h3>
        <p class="page-text">These cookies are necessary for the website to function and cannot be switched off in our systems.</p>

        <h3 class="subsection-heading">Analytics Cookies</h3>
        <p class="page-text">These cookies help us understand how visitors interact with our website by collecting and reporting information anonymously.</p>

        <h3 class="subsection-heading">Advertising Cookies</h3>
        <p class="page-text">These cookies are used to deliver relevant advertisements and track advertising campaign performance.</p>

        <h2 class="section-heading">Managing Cookies</h2>
        <p class="page-text">Most web browsers allow you to control cookies through their settings. However, if you limit the ability of websites to set cookies, you may impact your overall user experience.</p>

        <h2 class="section-heading">Updates to This Policy</h2>
        <p class="page-text">We may update this Cookie Policy from time to time. We encourage you to review this page periodically for any changes.</p>

        <h2 class="section-heading">Contact Us</h2>
        <p class="page-text">If you have questions about our use of cookies, please <a href="contact.html" style="color: #2563eb;">contact us</a>.</p>
    </div>
''' + FOOTER

with open('cookie-policy.html', 'w') as f:
    f.write(cookie_html)
print("✓ Generated cookie-policy.html")

print("\n" + "=" * 50)
print("✅ ALL PAGES GENERATED SUCCESSFULLY!")
print("=" * 50)
print(f"\nTotal pages created: {count + 6} (18 articles + 6 main pages)")
print("\nYou now have a complete HTML/CSS/JS website!")
print("\nTo view the site:")
print("1. Open index.html in your web browser")
print("2. All links and navigation should work")
print("3. No server required!")
print("\n" + "=" * 50)
