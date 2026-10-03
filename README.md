# ⚡ Code2LLM Context CLI

Pack your entire codebase into a single, LLM-ready Markdown file in one second. 

Are you tired of manually copying and pasting dozens of files into ChatGPT, Claude, or Gemini? **Code2LLM** crawls your project, strictly obeys your `.gitignore`, and copies perfectly formatted context directly to your clipboard.

## 🚀 Quick Start

```bash
# Install globally directly from GitHub
pip install git+https://github.com/OladapoSalami/codebase-context-cli.git

# Run it in any directory (automatically copies to clipboard!)
code2llm . -c
```

## ✨ Features
* **Zero Config:** Just run it. It automatically reads your existing .gitignore.

* **Clipboard Integration:** Bypass file creation entirely with the -c flag.

* **Smart Skipping:** Automatically ignores binary files, images, and compiled code.

* **Beautiful UI:** Powered by Rich for a clean terminal experience.

## 🛠️ Usage Options
```bash
# Standard run (creates llm_context.md)
code2llm .

# Specify a custom output file
code2llm . -o my_project_context.md

# Copy output to clipboard and skip opening files
code2llm . -c
```

---
*Maintained by Oladapo Salami*