# HandyTools

This repository contains a collection of utility scripts. The primary tool is `pdf_tool.py`, which offers basic PDF manipulation features similar to those found in professional PDF editors.

## Features
- Merge multiple PDF files into one
- Split a PDF into individual pages
- Rotate pages within a PDF
- Extract text from a PDF

These operations are implemented using the `PyPDF2` library. Make sure to install it before using the tool:

```bash
pip install PyPDF2
```

## Usage
Run the script with Python and the desired subcommand:

```bash
python pdf_tool.py merge file1.pdf file2.pdf -o output.pdf
python pdf_tool.py split input.pdf -o pages/
python pdf_tool.py rotate input.pdf 90 -o rotated.pdf
python pdf_tool.py extract input.pdf -o text.txt
```

Each subcommand provides `--help` for more options.
