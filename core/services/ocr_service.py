import pytesseract
from PIL import Image as PILImage


def extract_text_from_image(image_path):
    pil_image = PILImage.open(image_path)
    text = pytesseract.image_to_string(pil_image, lang='eng')
    return text
