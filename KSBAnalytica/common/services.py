import os

import cloudinary
from cloudinary import uploader
from decouple import config

from KSBAnalytica import settings

# Configure Cloudinary with .env variables
cloudinary.config(
    cloud_name=config('CLOUDINARY_NAME'),
    api_key=config('CLOUDINARY_KEY'),
    api_secret=config('CLOUDINARY_SECRET'),
)

file_name = "fin_management_1.png"
file_path = os.path.join(settings.STATICFILES_DIRS[0], "images", file_name)

# Example: Upload an image
response = cloudinary.uploader.upload(file_path)
print(response['secure_url'])