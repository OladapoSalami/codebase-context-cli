import os
from pathlib import Path
import pathspec

def load_ignore_rules(directory: Path) -> pathspec.PathSpec:
    """ loads .gitignore and adds default fallback ignores"""
    ignore_lines = ['.git/', '__pycache__/', 'venv/', 'node_modules/', '*.pyc', '.env']

    gitignore_path = directory / '.gitignore'
    if gitignore_path.exists():
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            ignore_lines.extend(f.readlines())

    return pathspec.PathSpec.from_lines('gitwildmatch', ignore_lines)

def generate_context(target_dir: str, output_file: str = "llm_context.md"):
    root = Path(target_dir).resolve()
    spec = load_ignore_rules(root)
    processed_files = 0

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(f"# Codebase Context: {root.name}\n\n")

        for filepath in root.rglob('*'):
            if filepath.is_file():
                # Convert path to standard forward slashes for pathspec
                rel_path = str(filepath.relative_to(root)).replace('\\', '/')

                if not spec.match_file(rel_path):
                    try:
                        # Read as text; if it fails, it's likely a binary file(images, compiled code)
                        content = filepath.read_text(encoding='utf-8')

                        # Determine markdown code block language by extension
                        ext = filepath.suffix.lstrip('.')

                        out.write(f"### File: '{rel_path}'\n")
                        out.write(f"'''{ext}\n{content}\n'''\n\n")
                        processed_files += 1
                    except UnicodeDecodeError:
                        pass # skips binary files silently

    return output_file, processed_files