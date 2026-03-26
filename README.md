# EverydayMoments - HTML/CSS/JS Version

This is the complete HTML, CSS, and JavaScript conversion of the EverydayMoments React application.

## Files Structure

```
public/
├── index.html              (Home page)
├── about.html              (About page) 
├── contact.html            (Contact page)
├── how-we-make-money.html  (Revenue disclosure)
├── editorial-guidelines.html (Editorial standards)
├── privacy-policy.html     (Privacy policy)
├── terms.html              (Terms of service)
├── disclaimer.html         (Legal disclaimer)
├── cookie-policy.html      (Cookie policy)
├── article-*.html          (18 article pages)
├── styles.css              (All styles)
├── script.js               (Main JavaScript)
├── articles.js             (Articles data)
├── generate-pages.py       (Page generator script)
└── README.md               (This file)
```

## Quick Start

1. Open `index.html` in your web browser
2. All pages are linked and navigation works
3. No server required - pure static HTML/CSS/JS

## Generating All Pages

To generate all the remaining HTML pages, run the Python script:

```bash
python3 generate-pages.py
```

This will create:
- All main pages (about, contact, etc.)
- All 18 article detail pages
- All legal pages

## Features

✅ Fully responsive design
✅ Mobile-friendly navigation
✅ Article browsing and detail pages
✅ Contact form with validation
✅ All legal pages included
✅ SEO-friendly HTML structure
✅ Professional styling
✅ No dependencies - pure HTML/CSS/JS

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Customization

### Update Styles
Edit `styles.css` to change colors, fonts, or layout.

### Update Content
Edit individual HTML files or modify `articles.js` for article content.

### Update Navigation
Edit the header section in each HTML file.

## File Sizes

- index.html: ~7 KB
- styles.css: ~15 KB
- script.js: ~2 KB
- articles.js: ~25 KB

## Performance

All pages are optimized for fast loading:
- Minimal CSS
- Lightweight JavaScript
- Optimized images from Unsplash
- No external dependencies (except Google Fonts for Playfair Display)

## Notes

- Images are loaded from Unsplash CDN
- Contact form submits are simulated (no backend)
- All pages follow the same consistent design
- Fully accessible HTML markup
