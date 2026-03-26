#!/usr/bin/env python3
"""
Quick Article Generator - Creates all 18 article pages
Run this script to generate all remaining article pages instantly
"""

# Article data (from articles.js)
articles_data = [
    {"slug": "morning-routines-improve-productivity", "title": "Morning Routines That Improve Productivity", "category": "Productivity", "date": "March 10, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1585693907431-69d82bdced6f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb3JuaW5nJTIwY29mZmVlJTIwcHJvZHVjdGl2aXR5JTIwd29ya3NwYWNlfGVufDF8fHx8MTc3MzM5Mzc5NHww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Morning routines play an important role in setting the tone for the day. Many successful professionals follow structured habits that help improve focus, productivity, and mental clarity.", "heading": "Key Morning Habits", "points": ["Hydrating after waking up", "Avoiding immediate phone use", "Planning the day ahead", "Light physical activity", "Mindfulness or meditation"], "why": "A structured routine helps reduce decision fatigue and improves mental energy throughout the day.", "conclusion": "Starting the day intentionally can improve productivity and overall well-being."},
    {"slug": "simple-lifestyle-changes-daily-life", "title": "Simple Lifestyle Changes That Improve Daily Life", "category": "Lifestyle", "date": "March 9, 2026", "readTime": "4 min read", "image": "https://images.unsplash.com/photo-1759398430338-8057876edf61?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtaW5pbWFsaXN0JTIwbGlmZXN0eWxlJTIwc2ltcGxlJTIwbGl2aW5nfGVufDF8fHx8MTc3MzM5Mzc5NXww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Small lifestyle adjustments can create significant positive impacts on your daily experience. These changes don't require major time investments or dramatic shifts in behavior.", "heading": "Simple Changes to Consider", "points": ["Setting specific sleep and wake times", "Preparing meals in advance", "Decluttering one space each week", "Taking short breaks during work", "Practicing gratitude journaling"], "why": "Consistency in small habits builds momentum and creates lasting behavioral change without overwhelming your schedule.", "conclusion": "Incremental improvements compound over time to create meaningful lifestyle enhancements."},
    {"slug": "technology-trends-everyday-life", "title": "Technology Trends Shaping Everyday Life", "category": "Technology", "date": "March 8, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1718866033984-c3ddab9af2a0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjB0ZWNobm9sb2d5JTIwZ2FkZ2V0cyUyMGhvbWV8ZW58MXx8fHwxNzczMzkzNzk1fDA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Technology continues to reshape how we live, work, and communicate. Understanding these trends helps us adapt and make informed decisions about which tools to adopt.", "heading": "Emerging Technology Trends", "points": ["AI-powered personal assistants", "Remote collaboration platforms", "Wearable health monitoring devices", "Smart home automation systems", "Cloud-based productivity tools"], "why": "These technologies streamline daily tasks, improve communication efficiency, and provide valuable insights into personal health and productivity.", "conclusion": "Staying informed about technology trends helps you leverage tools that genuinely improve your quality of life."},
    {"slug": "daily-wellness-tips-busy-people", "title": "Daily Wellness Tips for Busy People", "category": "Wellness", "date": "March 7, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1759476532819-e37ac3d05cff?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxoZWFsdGh5JTIwbGlmZXN0eWxlJTIwd2VsbG5lc3MlMjBleGVyY2lzZXxlbnwxfHx8fDE3NzMzOTM3OTR8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Maintaining wellness doesn't require hours of free time. Even busy schedules can accommodate simple practices that support physical and mental health.", "heading": "Quick Wellness Practices", "points": ["Five-minute stretching sessions", "Drinking water throughout the day", "Taking walking meetings", "Practicing deep breathing exercises", "Getting sunlight exposure"], "why": "Brief, consistent wellness practices reduce stress, improve focus, and support long-term health without disrupting your schedule.", "conclusion": "Small wellness investments throughout the day create sustainable health benefits."},
    {"slug": "digital-productivity-tools", "title": "Digital Productivity Tools Everyone Should Know", "category": "Productivity", "date": "March 6, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1760536928911-40831dacdbc3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxwcm9kdWN0aXZpdHklMjB0b29scyUyMGxhcHRvcCUyMHdvcmtzcGFjZXxlbnwxfHx8fDE3NzMzOTM3OTh8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "The right digital tools can significantly enhance productivity and organization. Here are practical applications that serve various needs in modern work and personal life.", "heading": "Essential Productivity Categories", "points": ["Task management and to-do lists", "Note-taking and knowledge management", "Time tracking and focus timers", "Calendar and scheduling tools", "Password managers and security"], "why": "These tools reduce mental load by organizing information, automating repetitive tasks, and keeping important data accessible.", "conclusion": "Choosing the right productivity tools based on your specific needs can streamline workflows and reduce daily friction."},
    {"slug": "smart-home-technology-trends", "title": "Smart Home Technology Trends", "category": "Technology", "date": "March 5, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1550959087-f655e48c2b8d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzbWFydCUyMGhvbWUlMjB0ZWNobm9sb2d5JTIwZGV2aWNlc3xlbnwxfHx8fDE3NzMzMTQ0MzN8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Smart home technology has become increasingly accessible and popular across American households. These devices offer convenience, energy efficiency, and enhanced security.", "heading": "Popular Smart Home Categories", "points": ["Smart thermostats and climate control", "Voice-activated assistants", "Security cameras and doorbell systems", "Smart lighting solutions", "Connected appliances"], "why": "Smart home devices provide remote control, automation capabilities, and data insights that improve comfort while potentially reducing energy costs.", "conclusion": "Starting with one or two key devices can help you understand smart home benefits before expanding your system."},
    {"slug": "everyday-budgeting-tips", "title": "Everyday Budgeting Tips", "category": "Finance", "date": "March 4, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1767423802472-f5fd07dfdb10?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxidWRnZXQlMjBwbGFubmluZyUyMGZpbmFuY2UlMjBtb25leXxlbnwxfHx8fDE3NzMzOTM3OTd8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Effective budgeting doesn't require complex spreadsheets or financial expertise. Simple strategies can help you understand spending patterns and make intentional money decisions.", "heading": "Practical Budgeting Approaches", "points": ["Tracking monthly expenses", "Setting spending categories", "Automating savings transfers", "Using the 50/30/20 budget rule", "Reviewing subscriptions regularly"], "why": "Understanding where money goes enables informed decisions and helps identify areas where spending can be optimized.", "conclusion": "Consistent budget awareness leads to better financial decision-making and reduced money-related stress."},
    {"slug": "work-from-home-productivity", "title": "Work-From-Home Productivity Tips", "category": "Productivity", "date": "March 3, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1626065838283-d338b7702fed?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxyZW1vdGUlMjB3b3JrJTIwaG9tZSUyMG9mZmljZXxlbnwxfHx8fDE3NzMzNDcyMzJ8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Remote work offers flexibility but requires intentional strategies to maintain productivity and work-life boundaries. These practices help create an effective home work environment.", "heading": "Remote Work Best Practices", "points": ["Designating a dedicated workspace", "Maintaining regular work hours", "Taking scheduled breaks", "Using video for important meetings", "Communicating availability clearly"], "why": "Clear boundaries and structured routines help separate work from personal time, preventing burnout and maintaining focus.", "conclusion": "Successful remote work requires intentional practices that support both productivity and well-being."},
    {"slug": "healthy-morning-habits", "title": "Healthy Morning Habits Backed by Experts", "category": "Wellness", "date": "March 2, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1607551748581-7ee851bf978b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtZWRpdGF0aW9uJTIwbWluZGZ1bG5lc3MlMjByZWxheGF0aW9ufGVufDF8fHx8MTc3MzM5Mzc5Nnww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Research supports specific morning habits that contribute to better mental and physical health. These evidence-based practices can be adapted to various lifestyles.", "heading": "Evidence-Based Morning Practices", "points": ["Exposure to natural morning light", "Protein-rich breakfast", "Morning movement or exercise", "Limiting early screen time", "Mindful breathing or meditation"], "why": "These habits support circadian rhythms, stabilize blood sugar, reduce stress hormones, and improve mental clarity.", "conclusion": "Incorporating even a few of these evidence-based practices can support overall health and daily energy levels."},
    {"slug": "remote-work-culture-trends", "title": "Trends in Remote Work Culture", "category": "Lifestyle", "date": "March 1, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1626065838283-d338b7702fed?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxyZW1vdGUlMjB3b3JrJTIwaG9tZSUyMG9mZmljZXxlbnwxfHx8fDE3NzMzNDcyMzJ8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Remote work has transformed from a temporary solution to a permanent workplace option for many Americans. Understanding these cultural shifts helps both employers and employees adapt.", "heading": "Emerging Remote Work Patterns", "points": ["Hybrid work models gaining popularity", "Asynchronous communication becoming standard", "Results-focused rather than hours-focused", "Digital nomad lifestyle increasing", "Virtual team building evolving"], "why": "These trends reflect a shift toward flexibility, autonomy, and work-life integration rather than traditional separation.", "conclusion": "Remote work culture continues to evolve, creating new opportunities and challenges for modern professionals."},
    {"slug": "social-media-trends", "title": "Social Media Trends Shaping Culture", "category": "Technology", "date": "February 28, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1770368787714-4e5a5ea557fd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzb2NpYWwlMjBtZWRpYSUyMHBob25lJTIwZGlnaXRhbHxlbnwxfHx8fDE3NzMzOTM3OTd8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Social media platforms continually shape communication patterns, cultural trends, and information consumption. Understanding these trends helps navigate the digital landscape.", "heading": "Current Social Media Patterns", "points": ["Short-form video content dominance", "Authentic and unpolished content preference", "Community-focused platforms growing", "Privacy-conscious user behavior", "Niche communities over mass audiences"], "why": "These trends reflect user desires for genuine connection, entertainment, and communities aligned with specific interests.", "conclusion": "Social media evolution reflects broader cultural shifts toward authenticity and meaningful digital interaction."},
    {"slug": "reduce-stress-daily", "title": "Simple Ways to Reduce Stress Daily", "category": "Wellness", "date": "February 27, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1607551748581-7ee851bf978b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtZWRpdGF0aW9uJTIwbWluZGZ1bG5lc3MlMjByZWxheGF0aW9ufGVufDF8fHx8MTc3MzM5Mzc5Nnww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Chronic stress affects both mental and physical health. Fortunately, simple daily practices can significantly reduce stress levels without requiring major lifestyle changes.", "heading": "Effective Stress Reduction Techniques", "points": ["Progressive muscle relaxation", "Time in nature or green spaces", "Limiting news and social media", "Regular physical movement", "Connecting with supportive people"], "why": "These practices activate the parasympathetic nervous system, reduce cortisol levels, and provide mental breaks from stressors.", "conclusion": "Consistent stress management practices build resilience and improve overall quality of life."},
    {"slug": "minimalist-lifestyle-trends", "title": "Minimalist Lifestyle Trends", "category": "Lifestyle", "date": "February 26, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1759398430338-8057876edf61?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtaW5pbWFsaXN0JTIwbGlmZXN0eWxlJTIwc2ltcGxlJTIwbGl2aW5nfGVufDF8fHx8MTc3MzM5Mzc5NXww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Minimalism has evolved from a niche philosophy to a mainstream lifestyle choice. More Americans are embracing intentional living and reducing excess.", "heading": "Key Minimalist Principles", "points": ["Intentional purchasing decisions", "Quality over quantity approach", "Decluttering physical spaces", "Digital minimalism practices", "Focus on experiences over possessions"], "why": "Minimalism reduces decision fatigue, financial stress, and environmental impact while often increasing life satisfaction.", "conclusion": "Minimalist principles can be adapted to personal values and circumstances, making it accessible to various lifestyles."},
    {"slug": "technology-gadgets-worth-watching", "title": "Technology Gadgets Worth Watching", "category": "Technology", "date": "February 25, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1718866033984-c3ddab9af2a0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjB0ZWNobm9sb2d5JTIwZ2FkZ2V0cyUyMGhvbWV8ZW58MXx8fHwxNzczMzkzNzk1fDA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "New technology gadgets continually enter the market, promising to improve various aspects of daily life. Here are devices generating significant interest.", "heading": "Notable Gadget Categories", "points": ["Advanced wearable health monitors", "Portable power solutions", "Next-generation earbuds and audio", "Smart displays and tablets", "Home automation controllers"], "why": "These gadgets address real needs around health tracking, connectivity, entertainment, and home management.", "conclusion": "Evaluating whether new gadgets genuinely improve your life helps avoid unnecessary technology accumulation."},
    {"slug": "smart-habits-better-focus", "title": "Smart Habits for Better Focus", "category": "Productivity", "date": "February 24, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1760536928911-40831dacdbc3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxwcm9kdWN0aXZpdHklMjB0b29scyUyMGxhcHRvcCUyMHdvcmtzcGFjZXxlbnwxfHx8fDE3NzMzOTM3OTh8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Maintaining focus has become increasingly challenging in our connected world. These evidence-based habits can help improve concentration and reduce distractions.", "heading": "Focus-Enhancing Practices", "points": ["Time-blocking specific tasks", "Eliminating notification interruptions", "Using focus music or white noise", "Taking regular movement breaks", "Single-tasking instead of multitasking"], "why": "These practices reduce cognitive switching costs, minimize external distractions, and support sustained attention.", "conclusion": "Building focus is a skill that improves with consistent practice and environmental design."},
    {"slug": "digital-wellness-tips", "title": "Digital Wellness Tips", "category": "Wellness", "date": "February 23, 2026", "readTime": "5 min read", "image": "https://images.unsplash.com/photo-1770368787714-4e5a5ea557fd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzb2NpYWwlMjBtZWRpYSUyMHBob25lJTIwZGlnaXRhbHxlbnwxfHx8fDE3NzMzOTM3OTd8MA&ixlib=rb-4.1.0&q=80&w=1080", "intro": "While technology provides many benefits, managing digital consumption supports mental health and well-being. These strategies help create a healthier relationship with devices.", "heading": "Digital Wellness Strategies", "points": ["Setting app time limits", "Creating phone-free zones", "Using grayscale mode", "Establishing digital curfews", "Regular digital detox periods"], "why": "Intentional technology use reduces anxiety, improves sleep quality, and creates space for offline activities and relationships.", "conclusion": "Digital wellness involves using technology purposefully rather than letting it control your attention and time."},
    {"slug": "daily-news-lifestyle-updates", "title": "Daily News & Lifestyle Updates", "category": "Lifestyle", "date": "February 22, 2026", "readTime": "4 min read", "image": "https://images.unsplash.com/photo-1759398430338-8057876edf61?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtaW5pbWFsaXN0JTIwbGlmZXN0eWxlJTIwc2ltcGxlJTIwbGl2aW5nfGVufDF8fHx8MTc3MzM5Mzc5NXww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Staying informed about lifestyle and cultural trends helps you make relevant decisions and understand societal shifts. Here are current noteworthy developments.", "heading": "Current Lifestyle Trends", "points": ["Sustainable living practices gaining traction", "Flexible work arrangements becoming standard", "Mental health awareness increasing", "Plant-based food options expanding", "Local community engagement growing"], "why": "These trends reflect evolving values around health, sustainability, work-life balance, and community connection.", "conclusion": "Understanding cultural shifts helps you make informed choices aligned with changing societal values."},
    {"slug": "trending-insights-modern-living", "title": "Trending Insights & Modern Living", "category": "Lifestyle", "date": "February 21, 2026", "readTime": "6 min read", "image": "https://images.unsplash.com/photo-1585693907431-69d82bdced6f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb3JuaW5nJTIwY29mZmVlJTIwcHJvZHVjdGl2aXR5JTIwd29ya3NwYWNlfGVufDF8fHx8MTc3MzM5Mzc5NHww&ixlib=rb-4.1.0&q=80&w=1080", "intro": "Modern living continues to evolve as technology, values, and priorities shift. These insights help make sense of emerging trends shaping daily life.", "heading": "Key Modern Living Patterns", "points": ["Prioritizing experiences over material goods", "Seeking work with personal meaning", "Embracing lifelong learning", "Valuing authenticity and transparency", "Building diverse social connections"], "why": "These patterns reflect a broader shift toward intentional living, personal growth, and authentic connection.", "conclusion": "Understanding these trends can help you make lifestyle choices aligned with contemporary values and personal goals."}
]

# HTML Template
def create_article_html(article):
    points_html = ''.join([f'<li>{point}</li>' for point in article['points']])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} - EverydayMoments</title>
    <meta name="description" content="{article['intro'][:150]}">
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

    <div class="article-header">
        <span class="article-category">{article['category']}</span>
        <h1 class="page-title">{article['title']}</h1>
        <div class="article-meta" style="justify-content: center;">
            <span>{article['date']}</span>
            <span>•</span>
            <span>{article['readTime']}</span>
        </div>
    </div>

    <img src="{article['image']}" alt="{article['title']}" class="article-detail-image" style="max-width: 56rem; margin: 0 auto; display: block; padding: 0 1rem;">

    <div class="article-body">
        <p class="page-text">{article['intro']}</p>
        
        <h2>{article['heading']}</h2>
        <ul>
            {points_html}
        </ul>
        
        <div class="why-it-works">
            <h3>Why It Works</h3>
            <p>{article['why']}</p>
        </div>
        
        <p class="page-text">{article['conclusion']}</p>
        
        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e5e7eb;">
            <a href="index.html" style="color: #2563eb; font-weight: 500;">&larr; Back to all articles</a>
        </div>
    </div>

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

# Generate all pages
print("🚀 Generating all 18 article pages...")
print("=" * 60)

for article in articles_data:
    filename = f"article-{article['slug']}.html"
    html = create_article_html(article)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Created {filename}")

print("=" * 60)
print(f"✅ SUCCESS! Generated all {len(articles_data)} article pages")
print("\nYour complete website is ready!")
print("\n📂 Files created:")
print("   - 18 article pages")
print("   - 3 legal pages (already created)")
print("   - Total: 21 pages + index.html + about.html = 27 pages")
print("\n🌐 Open index.html to view your website!")
