import requests
import os

YANDEX_API_KEY = os.getenv('YANDEX_API_KEY', '')


def translate_text(text, target_lang='ru'):
    if not YANDEX_API_KEY:
        raise Exception("YANDEX_API_KEY is not set in environment variables")
    url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    headers = {"Authorization": f"Api-Key {YANDEX_API_KEY}"}
    body = {
        "targetLanguageCode": target_lang,
        "texts": [text],
        "folderId": os.getenv("YANDEX_FOLDER_ID"),
    }
    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    translated = response.json()['translations'][0]['text']
    return translated
