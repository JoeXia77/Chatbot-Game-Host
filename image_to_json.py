import os
import json
import requests
from PIL import Image

def compress_image(image_path):
    with Image.open(image_path) as img:
        img_quality = 90
        img.save(image_path, quality=img_quality)

def image_to_text(image_path):
    api_key = 'K87549321588957'  # Replace with your OCR.space API key

    with open(image_path, 'rb') as f:
        image_data = f.read()

    url = 'https://api.ocr.space/parse/image'
    headers = {'apikey': api_key}
    files = {'file': ('image.png', image_data, 'image/png')}
    data = {
        'language': 'chs',  # Chinese Simplified
        'isOverlayRequired': False
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    response.raise_for_status()

    result = response.json()

    if 'ParsedResults' not in result:
        error_message = result.get('ErrorMessage', 'Unknown error')
        error_details = result.get('ErrorDetails', '')
        raise ValueError(f"OCR.space API error: {error_message} ({error_details})")

    chinese_text = result['ParsedResults'][0]['ParsedText']

    return chinese_text

def save_to_json(image_paths, results):
    json_file_name = os.path.splitext(os.path.basename(image_paths[0]))[0] + '.json'
    json_file_path = os.path.join(os.getcwd(), json_file_name)

    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump({"question": results[0], "truth": results[1]}, f, ensure_ascii=False, indent=4)

    print(f"JSON saved to {json_file_path}")

def main():
    image_paths = [
        r'./Story1-question.PNG',
        r'./Story1-truth.PNG'
    ]

    results = []

    for image_path in image_paths:
        # Check if the image size is larger than 1000KB
        if os.path.getsize(image_path) > 1000 * 1024:
            compress_image(image_path)

        recognized_text = image_to_text(image_path)
        results.append(recognized_text)

    save_to_json(image_paths, results)

if __name__ == "__main__":
    main()
