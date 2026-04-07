from PIL import Image, ImageDraw, ImageFont
import os

# Create a professional placeholder image
width, height = 400, 400
background_color = "#1e3a8a"  # Dark blue
text_color = "#ffffff"  # White

# Create image
img = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(img)

# Add gradient effect by drawing colored rectangles
for i in range(height):
    ratio = i / height
    r = int(30 * (1 - ratio) + 59 * ratio)
    g = int(58 * (1 - ratio) + 130 * ratio)
    b = int(138 * (1 - ratio) + 201 * ratio)
    draw.rectangle([(0, i), (width, i+1)], fill=(r, g, b))

# Try to use a default font, fall back if not available
try:
    font = ImageFont.truetype("arial.ttf", 48)
    font_small = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Draw text
text = "Team Member"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_x = (width - text_width) // 2
draw.text((text_x, height // 2 - 40), text, fill=text_color, font=font)

# Save the image
os.makedirs('media/team', exist_ok=True)
img.save('media/team/bhakti_jokare.jpg', 'JPEG', quality=95)
print("✓ Image created successfully: media/team/bhakti_jokare.jpg")
