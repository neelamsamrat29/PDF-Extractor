import json

def create_json_output(text_content, images_info):
    structured_data = []

    for i, text in enumerate(text_content):
        page_data = {
            "question": text.strip(),
            "images": images_info[i] if i < len(images_info) else "",
            "option_images": []  
        }
        structured_data.append(page_data)

    with open("output.json", "w") as json_file:
        json.dump(structured_data, json_file, indent=4)

    print("JSON file created successfully!")

if __name__ == "__main__":
    text_content = []  
    images_info = []   
    create_json_output(text_content, images_info)
