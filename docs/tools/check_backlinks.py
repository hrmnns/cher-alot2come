import os
import re
import sys
from pathlib import Path

DOCS_DIR = Path("docs")
BACKLINK_SECTION = "## Weiterführende Dokumente"

# Markdown-Link: [Text](pfad.md)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def find_backlink_section(lines):
    """
    Findet die Zeilennummer der Backlink-Sektion.
    Gibt None zurück, wenn sie nicht existiert.
    """
    for idx, line in enumerate(lines):
        if line.strip() == BACKLINK_SECTION:
            return idx
    return None


def extract_links_from_section(lines, start_index):
    """
    Extrahiert alle Links unterhalb der Backlink-Sektion.
    Die Sektion endet bei der nächsten Überschrift oder Dokumentende.
    """
    links = []
    for line in lines[start_index + 1:]:
        # Ende der Sektion
        if line.startswith("#"):
            break
        match = LINK_PATTERN.search(line)
        if match:
            links.append(match.group(2))  # nur den Pfad zurückgeben
    return links


def file_exists(path_str):
    """
    Prüft, ob der Pfad relativ zum docs-Verzeichnis existiert.
    """
    path = DOCS_DIR / path_str
    return path.exists()


def check_file(md_file):
    """
    Prüft eine einzelne Markdown-Datei.
    Gibt eine Liste von Fehlermeldungen zurück.
    """
    errors = []
    lines = md_file.read_text(encoding="utf-8").splitlines()

    section_index = find_backlink_section(lines)

    if section_index is None:
        errors.append("Backlink-Sektion fehlt")
        return errors

    links = extract_links_from_section(lines, section_index)

    if not links:
        errors.append("Backlink-Sektion enthält keine Links")
        return errors

    for link in links:
        if not file_exists(link):
            errors.append(f"Broken Link: {link}")

    return errors


def main():
    all_errors = {}
    md_files = sorted(DOCS_DIR.rglob("*.md"))

    print(f"Scanning {len(md_files)} Markdown-Dateien...\n")

    for md_file in md_files:
        rel = md_file.relative_to(DOCS_DIR)
        errors = check_file(md_file)

        if errors:
            all_errors[str(rel)] = errors

    # Ausgabe
    if all_errors:
        print("=== FEHLER ===")
        for file, errors in all_errors.items():
            print(f"\n[ERROR] {file}")
            for err in errors:
                print(f"  - {err}")

        print("\nSummary:")
        print(f"  {len(all_errors)} Dateien mit Fehlern")
        print("Exit-Code: 1")
        sys.exit(1)

    else:
        print("Alle Dateien sind in Ordnung.")
        print("Exit-Code: 0")
        sys.exit(0)


if __name__ == "__main__":
    main()
