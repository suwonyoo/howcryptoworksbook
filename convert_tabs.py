#!/usr/bin/env python3
"""
Convert GitBook tab syntax to MkDocs Material tab syntax.

GitBook format:
{% tabs %}
{% tab title="English" %}
Content
{% endtab %}
{% tab title="한국어" %}
Content
{% endtab %}
{% endtabs %}

MkDocs Material format:
=== "English"

    Content

=== "한국어"

    Content
"""

import os
import re
from pathlib import Path

def convert_tabs(content):
    """Convert GitBook tabs to MkDocs Material tabs."""

    # Pattern to match the entire tabs block
    def replace_tabs_block(match):
        full_block = match.group(0)

        # Extract individual tab sections
        tab_pattern = r'{%\s*tab\s+title="([^"]+)"\s*%}(.*?){%\s*endtab\s*%}'
        tabs = re.findall(tab_pattern, full_block, re.DOTALL)

        result = []
        for title, tab_content in tabs:
            # Clean up the content - remove leading/trailing whitespace from each line
            lines = tab_content.strip().split('\n')
            # Indent all lines with 4 spaces
            indented_lines = ['    ' + line if line.strip() else '' for line in lines]
            indented_content = '\n'.join(indented_lines)

            # Create MkDocs tab syntax
            result.append(f'=== "{title}"\n\n{indented_content}')

        return '\n\n'.join(result)

    # Pattern to match entire tabs blocks
    tabs_block_pattern = r'{%\s*tabs\s*%}(.*?){%\s*endtabs\s*%}'
    converted = re.sub(tabs_block_pattern, replace_tabs_block, content, flags=re.DOTALL)

    return converted

def convert_file(file_path):
    """Convert a single markdown file."""
    print(f"Converting {file_path}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    converted = convert_tabs(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted)

    print(f"  ✓ Converted {file_path}")

def main():
    """Convert all markdown files in gitbook directory."""
    gitbook_dir = Path('/Users/yoo/howcryptoworksbook/gitbook')

    # Find all markdown files
    md_files = list(gitbook_dir.glob('**/*.md'))

    print(f"Found {len(md_files)} markdown files to convert\n")

    for md_file in md_files:
        convert_file(md_file)

    print(f"\n✓ Conversion complete! Converted {len(md_files)} files.")

if __name__ == '__main__':
    main()
