from PIL import Image, ImageDraw, ImageFont

def make_custom_image(text="Hello!", path="output.png", size=(400,400)):
    img = Image.new("RGB", size, (255,255,255))
    draw = ImageDraw.Draw(img)
    rect = [(50,50), (size[0]-50, size[1]-50)]
    draw.rectangle(rect, fill=(200,200,255), outline=(0,0,0))

    try:
        font = ImageFont.truetype("arial.ttf", size=40)
    except IOError:
        font = ImageFont.load_default()

    # Measure text bounding box
    x0, y0, x1, y1 = draw.textbbox((0,0), text, font=font)
    w, h = x1 - x0, y1 - y0

    # Center the text
    pos = ((size[0]-w)//2, (size[1]-h)//2)
    draw.text(pos, text, fill=(0,0,0), font=font)

    img.save(path)
    print(f"✨ Saved to {path}")

if __name__ == "__main__":
    make_custom_image("shrushti here!", "my_image.png")
