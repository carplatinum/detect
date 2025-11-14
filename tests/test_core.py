import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image as PILImage


@pytest.fixture
def create_test_image_file():
    file = BytesIO()
    image = PILImage.new('RGB', (10, 10), color='red')
    image.save(file, 'JPEG')
    file.name = 'test.jpg'
    file.seek(0)
    return SimpleUploadedFile(file.name, file.read(), content_type='image/jpeg')


@pytest.mark.django_db
def test_create_image_model(create_test_image_file):
    from core.models import Image
    img = Image.objects.create(
        original_image=create_test_image_file,
        text_original="Hello",
        text_translated="[translate:Привет]"
    )
    assert img.text_original == "Hello"
    assert img.text_translated == "[translate:Привет]"
    assert img.translated_image.name is None


@pytest.fixture
def _user():
    from users.models import CustomUser
    return CustomUser.objects.create_user(username='testuser', password='testpass123')


@pytest.fixture
def api_client(_user):
    from rest_framework.test import APIClient
    client = APIClient()
    client.force_authenticate(user=_user)
    return client


@pytest.mark.django_db
def test_upload_image_and_start_task(api_client, create_test_image_file):
    from django.urls import reverse
    from core.models import Image
    url = reverse("image-list")
    data = {
        "original_image": create_test_image_file,
        "text_original": "Пример оригинального текста"
    }
    response = api_client.post(url, data, format='multipart')
    print(response.data)
    assert response.status_code == 201
    assert "task_id" in response.data
    img_id = response.data["id"]
    image = Image.objects.get(id=img_id)
    assert image.original_image.name.endswith(".jpg")


@pytest.mark.django_db
def test_get_task_status(api_client):
    from django.urls import reverse
    url_task = reverse("image-task-status", kwargs={"task_id": "fake-task-id"})
    response = api_client.get(url_task)
    assert response.status_code == 200
    assert "status" in response.data


@pytest.mark.django_db
def test_user_auth_creation_and_jwt_token():
    from users.models import CustomUser
    from django.urls import reverse
    from rest_framework.test import APIClient
    user = CustomUser.objects.create_user(username="authuser", password="authpass123")
    assert user is not None
    client = APIClient()
    url = reverse("token_obtain_pair")
    response = client.post(url, {"username": "authuser", "password": "authpass123"})
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
