from celery import shared_task
from .models import Image
from .services.ocr_service import extract_text_from_image
from .services.translation_service import translate_text
from .services.image_overlay_service import overlay_translated_text


@shared_task
def process_image_task(image_id):
    image = Image.objects.get(id=image_id)
    original_path = image.original_image.path

    extracted_text = extract_text_from_image(original_path)
    image.text_original = extracted_text

    translated_text = translate_text(extracted_text, target_lang='ru')
    image.text_translated = translated_text

    result_path = overlay_translated_text(original_path, translated_text)
    image.translated_image.name = result_path
    image.save()
