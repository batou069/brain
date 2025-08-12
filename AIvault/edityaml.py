#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path


def update_yaml_related(file_path):
    try:
        # Read the file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if file has YAML frontmatter
        if not content.startswith("---"):
            print(f"Skipping {file_path}: No YAML frontmatter")
            return

        # Split content into YAML and body
        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"Skipping {file_path}: Invalid YAML structure")
            return

        yaml_content = parts[1]
        body = parts[2]

        # Check for both related formats
        # Format 1: related: [item1, item2, ...]
        related_match_list = re.search(
            r"^related:\s*\[(.*?)\]\s*$", yaml_content, re.MULTILINE
        )
        # Format 2: related:\n  - item1\n  - item2\n ...
        related_match_yaml = re.search(
            r"^related:\s*$(?:\n\s*-\s*[^\n]+)*", yaml_content, re.MULTILINE
        )

        related_items = []
        if related_match_list:
            # Handle list format
            related_items = [
                item.strip()
                for item in related_match_list.group(1).split(",")
                if item.strip()
            ]
        elif related_match_yaml:
            # Handle YAML list format
            related_lines = related_match_yaml.group(0).split("\n")[
                1:
            ]  # Skip the 'related:' line
            related_items = [
                re.sub(r"^\s*-\s*", "", line).strip()
                for line in related_lines
                if line.strip()
            ]

        if not related_items:
            print(f"Skipping {file_path}: No related field or empty")
            return

        # Create new related field format
        new_related = "related:\n" + "\n".join(
            f'  - "[[{item}]]"' for item in related_items
        )

        # Replace old related field
        if related_match_list:
            new_yaml = re.sub(
                r"^related:\s*\[.*?\]\s*$",
                new_related,
                yaml_content,
                flags=re.MULTILINE,
            )
        else:  # related_match_yaml
            new_yaml = re.sub(
                r"^related:\s*$(?:\n\s*-\s*[^\n]+)*",
                new_related,
                yaml_content,
                flags=re.MULTILINE,
            )

        # Combine new content
        new_content = f"---{new_yaml}---{body}"

        # Create backup
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        shutil.copy2(file_path, backup_path)

        # Write updated content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path} (backup created at {backup_path})")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def main():
    # Specify your directory here
    directory = input("Enter the directory path containing Markdown files: ").strip()
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        return

    # Process all .md files
    for file_path in Path(directory).rglob("*.md"):
        update_yaml_related(file_path)


if __name__ == "__main__":
    main()
