import argparse
from pathlib import Path

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    PdfReader = None
    PdfWriter = None


def merge_pdfs(input_files, output):
    if PdfReader is None:
        raise ImportError("PyPDF2 is required for PDF operations")
    writer = PdfWriter()
    for pdf_file in input_files:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)


def split_pdf(input_file, output_dir):
    if PdfReader is None:
        raise ImportError("PyPDF2 is required for PDF operations")
    reader = PdfReader(input_file)
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = Path(output_dir) / f"page_{i}.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)


def rotate_pdf(input_file, output_file, angle):
    if PdfReader is None:
        raise ImportError("PyPDF2 is required for PDF operations")
    reader = PdfReader(input_file)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)


def extract_text(input_file, output_file=None):
    if PdfReader is None:
        raise ImportError("PyPDF2 is required for PDF operations")
    reader = PdfReader(input_file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


def main():
    parser = argparse.ArgumentParser(description="PDF Utility Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    merge = subparsers.add_parser("merge", help="Merge PDF files")
    merge.add_argument("inputs", nargs="+", help="Input PDF files")
    merge.add_argument("-o", "--output", required=True, help="Output PDF file")

    split = subparsers.add_parser("split", help="Split PDF into pages")
    split.add_argument("input", help="Input PDF file")
    split.add_argument("-o", "--output-dir", required=True, help="Directory to store pages")

    rotate = subparsers.add_parser("rotate", help="Rotate pages in a PDF")
    rotate.add_argument("input", help="Input PDF file")
    rotate.add_argument("angle", type=int, help="Rotation angle (degrees)")
    rotate.add_argument("-o", "--output", required=True, help="Output PDF file")

    extract = subparsers.add_parser("extract", help="Extract text from PDF")
    extract.add_argument("input", help="Input PDF file")
    extract.add_argument("-o", "--output", help="Output text file")

    args = parser.parse_args()

    if args.command == "merge":
        merge_pdfs(args.inputs, args.output)
    elif args.command == "split":
        split_pdf(args.input, args.output_dir)
    elif args.command == "rotate":
        rotate_pdf(args.input, args.output, args.angle)
    elif args.command == "extract":
        extract_text(args.input, args.output)


if __name__ == "__main__":
    main()
