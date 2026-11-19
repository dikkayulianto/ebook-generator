import os
from PIL import Image, ImageDraw, ImageFont

def create_favicons():
    size = 512
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    # 1. Emerald Gradient Background in a Rounded Rectangle
    radius = 128
    # Draw vertical/diagonal gradient into mask
    for y in range(size):
        ratio = y / size
        # interpolate from #10b981 (16, 185, 129) to #047857 (4, 120, 87)
        r = int(16 * (1 - ratio) + 4 * ratio)
        g = int(185 * (1 - ratio) + 120 * ratio)
        b = int(129 * (1 - ratio) + 87 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # Mask to rounded rectangle
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), (size, size)], radius=radius, fill=255)
    im.putalpha(mask)

    draw = ImageDraw.Draw(im)
    # Subtle inner border
    draw.rounded_rectangle([(18, 18), (size-18, size-18)], radius=114, outline=(255, 255, 255, 50), width=4)

    # 2. Draw Book Graphic in Crisp White
    # Book left page & right page
    left_poly = [(256, 320), (205, 305), (85, 320), (85, 185), (205, 170), (256, 190)]
    right_poly = [(256, 320), (307, 305), (427, 320), (427, 185), (307, 170), (256, 190)]
    
    draw.polygon(left_poly, fill=(245, 248, 250, 255))
    draw.polygon(right_poly, fill=(255, 255, 255, 255))
    draw.polygon([(256, 190), (256, 310), (248, 298), (240, 310), (240, 190)], fill=(16, 185, 129, 255))

    # Decorative lines on pages
    for y_offset in [220, 250, 280]:
        draw.line([(125, y_offset), (215, y_offset+7)], fill=(203, 213, 225, 255), width=6)
        draw.line([(297, y_offset+7), (387, y_offset)], fill=(203, 213, 225, 255), width=6)

    # 3. Golden Sparkle / Star
    star_pts = [(375, 105), (385, 130), (410, 140), (385, 150), (375, 175), (365, 150), (340, 140), (365, 130)]
    draw.polygon(star_pts, fill=(251, 191, 36, 255))
    draw.ellipse([(320, 110), (334, 124)], fill=(253, 224, 71, 230))
    draw.ellipse([(416, 166), (426, 176)], fill=(253, 224, 71, 230))

    # 4. Text "BU GURU"
    try:
        font = ImageFont.truetype("arialbd.ttf", 64)
    except:
        font = ImageFont.load_default()

    # Draw centered text
    text = "BU GURU"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    tx = (size - tw) // 2
    draw.text((tx, 375), text, fill=(255, 255, 255, 255), font=font)

    # Save PNGs
    # 96x96
    im_96 = im.resize((96, 96), Image.Resampling.LANCZOS)
    im_96.save("public/favicon-96x96.png", "PNG")

    # Apple Touch Icon 180x180 (iOS doesn't need transparent corners, solid looks best)
    im_180 = im.resize((180, 180), Image.Resampling.LANCZOS)
    im_180.save("public/apple-touch-icon.png", "PNG")

    # Multi-resolution ICO (16, 32, 48, 64)
    im_64 = im.resize((64, 64), Image.Resampling.LANCZOS)
    im_48 = im.resize((48, 48), Image.Resampling.LANCZOS)
    im_32 = im.resize((32, 32), Image.Resampling.LANCZOS)
    im_16 = im.resize((16, 16), Image.Resampling.LANCZOS)
    
    im.save("public/favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("Favicons generated successfully!")

if __name__ == "__main__":
    create_favicons()
