import os
import pathlib
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF opener so Pillow can handle HEIC images
register_heif_opener()

# Define input and output folders
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
OUTPUT_FORMAT = "png"  # Change to desired format (".jpg", ".jpeg", ".png", ".webp", ".heic")

# Create folders if they don’t exist
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Only process HEIC files
SUPPORTED_FORMATS = (".heic",)


def convert_image(input_path, output_format):
    """Convert an HEIC image to the specified format."""
    output_path = os.path.join(OUTPUT_FOLDER, f"{pathlib.Path(input_path).stem}.{output_format}")

    try:
        # Open HEIC image with Pillow
        image = Image.open(input_path)

        # Convert and save image
        if output_format == "jpg":
            image = image.convert("RGB")  # JPG doesn’t support transparency
        image.save(output_path, format=output_format.upper())

        print(f"Converted {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error converting {input_path}: {e}")


# Process only HEIC images in the input folder
for file in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, file)
    if file.lower().endswith(SUPPORTED_FORMATS):
        convert_image(file_path, OUTPUT_FORMAT)

