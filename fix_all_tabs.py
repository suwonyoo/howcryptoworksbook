#!/usr/bin/env python3
"""
Restructure all chapter files to have single English/Korean tab pair.
"""

import re
from pathlib import Path

def restructure_tabs(content):
    """Restructure content to have one English tab and one Korean tab."""

    # Extract all English sections
    english_sections = []
    korean_sections = []

    # Split by tabs
    parts = re.split(r'===\s+"(English|한국어)"\s*\n', content)

    # Skip the first part (before any tabs - usually just the title)
    title = parts[0].strip()

    # Process remaining parts (language, content, language, content, ...)
    for i in range(1, len(parts), 2):
        if i + 1 >= len(parts):
            break

        language = parts[i]
        section_content = parts[i + 1].strip()

        if language == "English":
            english_sections.append(section_content)
        else:  # 한국어
            korean_sections.append(section_content)

    # Reconstruct with single tab pair
    result = [title, '']

    if english_sections:
        result.append('=== "English"\n')
        for i, section in enumerate(english_sections):
            if i > 0:
                result.append('')  # Add blank line between sections
            # Indent each line with 4 spaces
            indented = '\n'.join('    ' + line if line.strip() else ''
                                for line in section.split('\n'))
            result.append(indented)

    if korean_sections:
        result.append('')
        result.append('=== "한국어"\n')
        for i, section in enumerate(korean_sections):
            if i > 0:
                result.append('')  # Add blank line between sections
            # Indent each line with 4 spaces
            indented = '\n'.join('    ' + line if line.strip() else ''
                                for line in section.split('\n'))
            result.append(indented)

    return '\n'.join(result)

def process_file(file_path):
    """Process a single markdown file."""
    print(f"Processing {file_path}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has tabs
    if '===' not in content:
        print(f"  ⊘ Skipping {file_path} (no tabs)")
        return

    restructured = restructure_tabs(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(restructured)

    print(f"  ✓ Restructured {file_path}")

def main():
    """Process all markdown files in gitbook directory."""
    gitbook_dir = Path('/Users/yoo/howcryptoworksbook/gitbook')

    # Find all chapter files
    chapter_files = list(gitbook_dir.glob('chapters/*.md'))

    # Also include preface (already done, but safe to re-run)
    preface = gitbook_dir / 'preface.md'
    if preface.exists():
        chapter_files.insert(0, preface)

    print(f"Found {len(chapter_files)} files to process\n")

    for file_path in chapter_files:
        process_file(file_path)

    print(f"\n✓ Restructuring complete! Processed {len(chapter_files)} files.")

if __name__ == '__main__':
    main()
