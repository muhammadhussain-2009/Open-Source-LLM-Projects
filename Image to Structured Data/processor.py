import base64
import instructor
from mistralai import Mistral
from PIL import Image
import io

def process_and_encode_image(image_file, max_size=(2048, 2048)):
    """Resizes image to fit API limits and converts to base64."""
    img = Image.open(image_file)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG", quality=90)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def extract_structured_data(image_file, schema_model, api_key: str):
    """Send the image to Mistral Large 3 and return data validated against the given schema."""
    client = instructor.from_mistral(Mistral(api_key=api_key))
    base64_image = process_and_encode_image(image_file)

    # The chat completions API expects messages with string content. Embed the
    # image as a data URL in the text content so the SDK accepts the message type.
    user_content = (
        "Extract all items found in this image into the requested structure.\n"
        f"Image: data:image/jpeg;base64,{base64_image}"
    )

    return client.chat.completions.create(
        model="mistral-large-latest",
        response_model=schema_model,
        max_retries=1,  # Set retries to 1 to avoid hitting rate limits on errors
        messages=[{"role": "user", "content": user_content}],
    )