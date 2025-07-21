import fitz  

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_content = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")  
        text_content.append(text)

    return text_content

if __name__ == "__main__":
    pdf_path = "D:\pdf_project\imo_sample.pdf"  
    text_content = extract_text_from_pdf(pdf_path)

    with open("extracted_text.txt", "w") as file:
        for page in text_content:
            file.write(page + "\n")
    print("Text extraction complete!")
