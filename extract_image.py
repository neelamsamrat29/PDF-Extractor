from PIL import Image
import io
import fitz  
import os

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    images_info = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image_filename = f"{output_folder}/page{page_num + 1}_image{img_index + 1}.png"
            image.save(image_filename)
            images_info.append(image_filename)

    return images_info

if __name__ == "__main__":
    pdf_path = "D:\pdf_project\imo_sample.pdf"
    output_folder = "extracted_images"
    images = extract_images_from_pdf(pdf_path, output_folder)

    print("Image extraction complete!")
    print(f"Extracted {len(images)} images.")
