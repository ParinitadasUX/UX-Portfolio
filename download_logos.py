#!/usr/bin/env python3
"""
Script to download software logos from the web
"""

import requests
import os
from urllib.parse import urlparse

# Create logos directory if it doesn't exist
os.makedirs('assets/img/logo', exist_ok=True)

# Software logos URLs (using CDN sources for better reliability)
logos = {
    'figma.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg',
    'sketch.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sketch/sketch-original.svg',
    'adobe-xd.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/xd/xd-plain.svg',
    'illustrator.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/illustrator/illustrator-plain.svg',
    'photoshop.png': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/photoshop/photoshop-plain.svg',
    'invision.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/invision.svg',
    'principle.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/principle.svg',
    'zeplin.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/zeplin.svg',
    'miro.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/miro.svg',
    'notion.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/notion.svg',
    'slack.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/slack.svg',
    'jira.png': 'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/jira.svg'
}

def download_logo(filename, url):
    """Download a logo from URL"""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        filepath = f'assets/img/logo/{filename}'
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"✓ Downloaded {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    print("Downloading software logos...")
    print("=" * 40)
    
    success_count = 0
    total_count = len(logos)
    
    for filename, url in logos.items():
        if download_logo(filename, url):
            success_count += 1
    
    print("=" * 40)
    print(f"Downloaded {success_count}/{total_count} logos successfully!")
    
    if success_count < total_count:
        print("\nSome logos failed to download. You can manually download them from:")
        print("- https://simpleicons.org/")
        print("- https://devicons.github.io/devicon/")
        print("- https://github.com/simple-icons/simple-icons")

if __name__ == "__main__":
    main()
