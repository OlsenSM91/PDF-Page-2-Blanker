import os
import sys
from tkinter import Tk, filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError

def select_directory():
    """Open a dialog to select a directory and return the path."""
    root = Tk()
    root.withdraw()  # Hide the main window
    root.attributes('-topmost', True)  # Bring the dialog to the front
    folder_selected = filedialog.askdirectory(title="Select Directory Containing PDF Files")
    root.destroy()
    return folder_selected

def add_blank_page_after_first(input_pdf_path, output_pdf_path):
    """Add a blank page after the first page of the PDF."""
    try:
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        if len(reader.pages) < 1:
            print(f"Skipping '{input_pdf_path}': PDF has no pages.")
            return

        # Add the first page (cover page)
        writer.add_page(reader.pages[0])

        # Create a blank page with the same size as the first page
        first_page = reader.pages[0]
        width = first_page.mediabox.width
        height = first_page.mediabox.height
        writer.add_blank_page(width=width, height=height)

        # Add the remaining pages
        for page_num in range(1, len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # Write the modified PDF to the output path
        with open(output_pdf_path, 'wb') as out_file:
            writer.write(out_file)

        print(f"Processed: '{input_pdf_path}' -> '{output_pdf_path}'")

    except PdfReadError as e:
        print(f"Error reading '{input_pdf_path}': {e}")
    except Exception as e:
        print(f"An error occurred while processing '{input_pdf_path}': {e}")

def process_pdfs(directory):
    """Process all PDF files in the given directory."""
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in '{directory}'.")
        return

    for pdf_file in pdf_files:
        input_path = os.path.join(directory, pdf_file)
        base_name, ext = os.path.splitext(pdf_file)
        output_file = f"{base_name}_modified{ext}"
        output_path = os.path.join(directory, output_file)

        add_blank_page_after_first(input_path, output_path)

    print("\nAll PDF files have been processed.")

def main():
    print("=== PDF Blank Page Inserter ===")
    directory = select_directory()

    if not directory:
        messagebox.showinfo("No Selection", "No directory selected. Exiting.")
        sys.exit()

    print(f"Selected Directory: {directory}\n")
    process_pdfs(directory)
    messagebox.showinfo("Completed", "All PDF files have been processed.")

if __name__ == "__main__":
    main()
