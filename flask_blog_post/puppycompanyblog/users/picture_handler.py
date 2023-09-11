import os
from PIL import Image
from flask import current_app

def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename

    # Check if the file has an allowed extension (e.g., jpg, png)
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}  # Add more if needed
    ext_type = filename.split('.')[-1].lower()
    if ext_type not in allowed_extensions:
        raise ValueError("Invalid file extension")

    storage_filename = f"{username}.{ext_type}"
    filepath = os.path.join(current_app.root_path, 'static', 'profile_pics', storage_filename)

    # Resize the image
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)

    # Save the image
    pic.save(filepath)

    return storage_filename
