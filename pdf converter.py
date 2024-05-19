import os
import fitz  # PyMuPDF
from pdfminer.high_level import extract_text

def pdf_to_text(pdf_path, text_output_path):
    try:
        text = extract_text(pdf_path)
        with open(text_output_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Text extracted and saved to {text_output_path}")
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")

def pdf_to_images(pdf_path, images_output_folder):
    try:
        if not os.path.exists(images_output_folder):
            os.makedirs(images_output_folder)
        
        document = fitz.open(pdf_path)
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            pix = page.get_pixmap()
            image_path = os.path.join(images_output_folder, f'page_{page_num + 1}.png')
            pix.save(image_path)
            print(f"Page {page_num + 1} saved as {image_path}")
    except Exception as e:
        print(f"An error occurred while converting to images: {e}")

def main():
    print("PDF Conversion Tool")
    print("1. Convert PDF to Text")
    print("2. Convert PDF to Images")
    choice = input("Enter your choice (1/2): ")

    pdf_path = "C:\\Users\\Sivateja\\OneDrive\\Desktop\\CC.pdf"

    if choice == '1':
        text_output_path ="C:\\Users\\Sivateja\\OneDrive\\Desktop\\sample.txt"
        pdf_to_text(pdf_path, text_output_path)
    elif choice == '2':
        images_output_folder = input("Enter the folder path for the output images: ").strip()
        pdf_to_images(pdf_path, images_output_folder)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
