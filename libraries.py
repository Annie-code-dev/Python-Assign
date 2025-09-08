import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # 1. Prompt the user for an image URL
    url = input("Enter the image URL: ").strip()

    # 2. Create 'Fetched_Images' directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # 3. Fetch the image from the URL
        response = requests.get(url, timeout=10)  # timeout avoids hanging forever
        response.raise_for_status()  # Raise an error for HTTP issues (404, 403, etc.)

        # 4. Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename is empty, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # 5. Save the image in binary mode
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully fetched and saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        # 6. Handle errors respectfully
        print(f"⚠️ Unable to fetch the image. Reason: {e}")

if __name__ == "__main__":
    fetch_image()
