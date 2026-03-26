#!/bin/bash

echo "=========================================="
echo "  EverydayMoments Quick Start Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "   Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"
echo ""

# Generate all pages
echo "📄 Generating all HTML pages..."
python3 COMPLETE_SITE_GENERATOR.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "  ✅ SUCCESS!"
    echo "=========================================="
    echo ""
    echo "Your website is ready!"
    echo ""
    echo "📁 Files created:"
    echo "   - 18 article pages"
    echo "   - 6 main pages"
    echo "   - 4 legal pages"
    echo ""
    echo "🌐 Opening website in browser..."
    echo ""
    
    # Open in default browser
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open index.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open index.html
    elif [[ "$OSTYPE" == "msys" ]]; then
        # Windows Git Bash
        start index.html
    fi
    
    echo "✅ Website opened in your browser!"
    echo ""
    echo "Next steps:"
    echo "1. Browse your website"
    echo "2. Customize content as needed"
    echo "3. Deploy to hosting provider"
    echo ""
    echo "Happy publishing! 🚀"
else
    echo ""
    echo "❌ Error generating pages"
    echo "   Please run manually: python3 COMPLETE_SITE_GENERATOR.py"
    exit 1
fi
