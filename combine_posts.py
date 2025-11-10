#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script zum Kombinieren von Posts aus Unterordnern
"""
import os
import re
from pathlib import Path
from collections import defaultdict

POSTS_DIR = Path('docs/_posts')

def extract_content(file_path):
    """Extrahiert den Content aus einer Markdown-Datei (ohne Front Matter)"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Entferne Front Matter (zwischen ---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content.strip()

def combine_posts_for_date(date_dir):
    """Kombiniert alle Posts in einem Datums-Ordner"""
    date_str = date_dir.name

    # Sammle alle .md Dateien
    post_files = sorted(date_dir.glob('*.md'))

    if not post_files:
        return

    # Lese alle Posts
    combined_parts = []
    for post_file in post_files:
        content = extract_content(post_file)
        if content:
            combined_parts.append(content)

    if not combined_parts:
        return

    # Kombiniere mit doppelten Zeilenumbrüchen
    combined_content = '\n\n'.join(combined_parts)

    # Erstelle kombinierte Datei
    output_file = POSTS_DIR / f"{date_str}-daily-news.md"

    front_matter = f"""---
title: Daily News Digest - {date_str}
date: {date_str}
layout: post
---

"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(front_matter + combined_content + '\n')

    print(f"Erstellt: {output_file.name} ({len(post_files)} Posts kombiniert)")

# Haupt-Logik
if __name__ == '__main__':
    # Finde alle Datums-Ordner
    date_dirs = [d for d in POSTS_DIR.iterdir() if d.is_dir() and re.match(r'\d{4}-\d{2}-\d{2}', d.name)]

    for date_dir in sorted(date_dirs):
        combine_posts_for_date(date_dir)

    print(f"\nFertig! {len(date_dirs)} kombinierte Posts erstellt.")

