from PIL import Image, ImageDraw, ImageFont
import os


def overlay_translated_text(original_image_path, translated_text):
    image = Image.open(original_image_path).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font_path = os.getenv("FONT_PATH", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    font = ImageFont.truetype(font_path, 20)

    # Пример простого наложения текста (в левом верхнем углу)
    draw.text((10, 10), translated_text, font=font, fill=(255, 0, 0, 255))

    combined = Image.alpha_composite(image, overlay)
    output_path = original_image_path.replace("original_images", "translated_images")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    combined.convert("RGB").save(output_path, "JPEG")

    # Возвращаем путь относительно MEDIA_ROOT
    relative_path = output_path.split('media/')[-1]
    return relative_path
