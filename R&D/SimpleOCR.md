1-  Install Tesseract-OCR
2- Convert Image to text with tesseract:
```python
import pytesseract
from PIL import Image

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(image)
        return text

# Example usage
image_path = 'image.jpg'
result = ocr(image_path)
print(result)
```

3- run with python:
```shell
python tesseract.py
```