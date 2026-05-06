# Contributing

This project is a Python command-line generator for Obsidian Markdown notes. Keep
changes small, easy to regenerate, and aligned with the existing source layout.

## Coding Style

- Use Python 3 syntax and the standard library where it is enough.
- Keep modules focused: STIX retrieval and parsing belongs in `src/stix_parser.py`,
  Markdown and canvas output belongs in `src/markdown_generator.py`, note scanning
  belongs in `src/markdown_reader.py`, and Obsidian view setup belongs in
  `src/view.py`.
- Prefer explicit names over abbreviations. Existing ATT&CK terms such as
  `technique`, `mitigation`, `tactic`, `group`, and `software` should stay visible
  in variable and method names.
- Keep generated Markdown structure in `res/templates/` whenever possible. Use
  Python code to prepare structured data for templates, not to assemble large
  Markdown documents inline.
- Preserve Obsidian link behavior. Internal ATT&CK links should use wiki-link
  syntax and stable vault-relative paths below `kb/mitre/attack`.
- Normalize generated filenames and tags consistently. Reuse
  `MarkdownGenerator.note_filename`, `MarkdownGenerator.note_link`, and
  `MarkdownGenerator.tag` instead of duplicating path or tag logic.
- Use UTF-8 when reading or writing generated Markdown, canvas, JSON, or STIX
  files.
- Use `loguru.logger` for user-visible CLI progress and errors. Avoid raw
  `print()` calls outside narrow note-editing utilities.
- Keep comments useful and brief. Add comments for non-obvious ATT&CK, STIX, or
  Obsidian behavior, not for ordinary Python control flow.
- Do not hand-edit generated vault notes for source changes. Change the parser,
  generator, templates, or configuration and regenerate the vault output.

## Formatting

There is no enforced formatter configuration in this repository yet. Follow the
style already present in the codebase:

- Four-space indentation.
- Line lengths that remain readable in a terminal.
- Imports grouped by third-party, standard library, then local project imports
  when touching a file.
- Double quotes or single quotes are both acceptable; prefer consistency within
  the file being edited.
- Keep public methods grouped by behavior so parser, generator, and model classes
  are easy to scan.

If a formatter such as Black or Ruff is introduced later, add its configuration to
the repository and update this guide in the same change.

## Validation

Run these checks before submitting a code change:

```
python3 -m py_compile run.py src/*.py
python run.py --help
```

For parser or template changes, also generate a vault and inspect the diff:

```
python run.py -o vault
git diff -- README.md CONTRIBUTING.md src res config.yml
```

Network access is required when the generator downloads ATT&CK STIX data from the
default MITRE source. To test without network access, set `repository-url` in
`config.yml` to a local STIX JSON bundle.

## Generated Files

The `vault/` directory contains generated or example Obsidian content. Avoid
mixing source changes with unrelated Obsidian workspace changes such as
`.obsidian/workspace.json`.

When generated output changes are intentional, call that out in the change
description and include the source change that produced it.
