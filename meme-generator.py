from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import os


def choose_image():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Choose an image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.webp"),
            ("All files", "*.*")
        ]
    )

    root.destroy()
    return file_path


def get_font(size):
    font_paths = [
        "C:/Windows/Fonts/impact.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Impact.ttf",
        "/Library/Fonts/Arial Bold.ttf"
    ]

    for path in font_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


def draw_meme_text(draw, image, text, y, font):
    # Find text size
    box = draw.textbbox((0, 0), text, font=font, stroke_width=0)

    text_width = box[2] - box[0]

    # Center text
    x = (image.width - text_width) // 2

    # White text with black outline
    draw.text(
        (x, y),
        text,
        font=font,
        fill="white",
        stroke_width=5,
        stroke_fill="black"
    )


def make_meme(image_path, top_text, bottom_text):
    image = Image.open(image_path).convert("RGB")

    # Resize large images
    max_width = 1200

    if image.width > max_width:
        ratio = max_width / image.width
        image = image.resize(
            (max_width, int(image.height * ratio))
        )

    draw = ImageDraw.Draw(image)

    font_size = max(30, image.width // 15)
    font = get_font(font_size)

    # Top text
    if top_text:
        draw_meme_text(
            draw,
            image,
            top_text.upper(),
            20,
            font
        )

    # Bottom text
    if bottom_text:
        box = draw.textbbox(
            (0, 0),
            bottom_text.upper(),
            font=font,
            stroke_width=0
        )

        text_height = box[3] - box[1]

        draw_meme_text(
            draw,
            image,
            bottom_text.upper(),
            image.height - text_height - 30,
            font
        )

    # Save
    output = "my_meme.jpg"
    image.save(output, quality=95)

    return output


# -----------------------------
# PROGRAM START
# -----------------------------

print("================================")
print("       MEME GENERATOR")
print("================================")

image_path = choose_image()

if not image_path:
    print("No image selected.")
    exit()

print("\nImage selected:", image_path)

top = input("\nEnter TOP text: ")
bottom = input("Enter BOTTOM text: ")

output = make_meme(
    image_path,
    top,
    bottom
)

print("\nMeme successfully created!")
print("Saved as:", output)
import os

print("Meme saved here:")
print(os.path.abspath("my_meme.jpg"))
