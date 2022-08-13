from PIL import Image

from django.core.files.base import ContentFile
import io


def cropper(
    original_image, resize_coords: tuple, img_name: str, format: str = "JPEG"
) -> ContentFile:
    img_io = io.BytesIO()
    original_image = Image.open(original_image)
    original_image.thumbnail(resize_coords)
    # cropped_img = original_image.thumbnail(resize_coords)
    original_image.save(img_io, format=format, quality=100)
    img_content = ContentFile(img_io.getvalue(), img_name)
    return img_content
