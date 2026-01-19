import re
import sys
import os
import unicodedata

EXCEPTION_ORDER = ["Index", "Overview", "Misc Notes"]


def normalize_title(title: str) -> str:
    """Normalize markdown title to a GitHub-like anchor slug.

    Strategy:
    - Unicode-normalize (NFKD) and lowercase
    - Convert whitespace to single hyphen
    - Remove all characters except a-z, 0-9 and hyphen
    - Leave consecutive hyphens intact (so "<->" -> "---")
    - Strip leading/trailing hyphens
    """
    if not title:
        return ""

    # Normalize unicode and lowercase
    s = unicodedata.normalize("NFKD", title).lower().strip()

    # Replace any run of whitespace with a single hyphen
    s = re.sub(r"\s+", "-", s)

    # Remove characters except ASCII letters, digits and hyphen
    s = re.sub(r"[^a-z0-9\-]", "", s)

    # Strip leading/trailing hyphens
    s = s.strip("-")

    return s


def capitalize_list_items(md_text):
    """Capitalize the first character of each list item (all levels) if it's a letter."""
    def repl(match):
        prefix, content = match.groups()
        if content and content[0].isalpha():
            content = content[0].upper() + content[1:]
        return prefix + content

    pattern = re.compile(r"(^\s*[-*+]\s+)(.+)$", re.MULTILINE)
    return pattern.sub(repl, md_text)


def extract_sections(md_text):
    """Extract level-2 sections (## ...) as top-level sections.

    Each extracted section contains the entire block from the level-2 header
    up to (but not including) the next level-2 header. This preserves any
    level-3 headers (### ...) and all notes inside the block.
    """
    pattern = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(md_text))

    sections = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.start()
        end = matches[i+1].start() if i+1 < len(matches) else len(md_text)
        section_text = md_text[start:end].rstrip('\n')
        # Capitalize list items inside this section (including nested bullets)
        section_text = capitalize_list_items(section_text)
        sections[title] = section_text

    return sections


def sort_section_titles(titles):
    """Sort with exceptions at the top in defined order, rest alphabetically."""
    rest = sorted([t for t in titles if t not in EXCEPTION_ORDER], key=str.lower)
    return [t for t in EXCEPTION_ORDER if t in titles] + rest


def update_index_section(index_text, sections, sorted_titles):
    """Rebuild the Index section with nested level-3 subheaders.

    For each level-2 title, we look inside its section text for any level-3
    headers (lines starting with "### ") and emit them as nested list items
    in the index.
    """
    index_lines = ["## Index", ""]
    for title in sorted_titles:
        anchor = normalize_title(title)
        index_lines.append(f"- [{title}](#{anchor})")
        # find level-3 headers inside this section
        section_text = sections.get(title, "")
        sub_matches = re.findall(r"^###\s+(.+?)\s*$", section_text, re.MULTILINE)
        for sub in sub_matches:
            sub_anchor = normalize_title(sub)
            index_lines.append(f"  - [{sub}](#{sub_anchor})")
    return "\n".join(index_lines)


def rebuild_markdown(original_text, sorted_titles, sections):
    """Rebuild the full markdown content using the ordered sections.

    We preserve any content before the first level-2 heading as header_content.
    Each level-2 section block (which already contains any level-3 content)
    is appended in the desired order.
    """
    first_match = re.search(r"^##\s", original_text, re.MULTILINE)
    if first_match:
        first_section_start = first_match.start()
        header_content = original_text[:first_section_start].rstrip()
    else:
        header_content = original_text.rstrip()

    rebuilt_sections = [sections[title] for title in sorted_titles]

    return header_content + "\n\n" + "\n\n".join(rebuilt_sections) + "\n"


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        md_text = f.read()

    sections = extract_sections(md_text)

    if "Index" not in sections:
        print(f"No Index section found in {filepath}. Skipping.")
        return

    sorted_titles = sort_section_titles(list(sections.keys()))

    # Update Index content to reflect new order (Index is itself a section)
    sections["Index"] = update_index_section(sections["Index"], sections, sorted_titles)

    # Rebuild the markdown file
    new_md = rebuild_markdown(md_text, sorted_titles, sections)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_md)

    print(f"Markdown file '{filepath}' sorted successfully.")


def main(path):
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith(".md"):
                    process_file(os.path.join(root, file))
    elif os.path.isfile(path) and path.lower().endswith(".md"):
        process_file(path)
    else:
        print("Provided path is neither a markdown file nor a directory containing markdown files.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_md_sections.py <markdown_file_or_directory>")
    else:
        main(sys.argv[1])
