import numpy as np

from PIL import Image, ImageDraw
from lang_sam import LangSAM

model = LangSAM()
image_pil = Image.open("./fish.jpg").convert("RGB")
text_prompt = "All yellow tailed fish"
masks, boxes, phrases, logits = model.predict(image_pil, text_prompt)
print(masks, boxes)
combined = image_pil.convert('RGBA')
print("Number of fish:", len(masks))
for mask in masks:
    mask_numpy = mask.numpy().astype(np.uint8)
    overlay = Image.new('RGBA', image_pil.size, (0, 255, 0, 0))  # 緑色のオーバーレイを初期化
    draw = ImageDraw.Draw(overlay)
    width, height = image_pil.size
    for y in range(height):
        for x in range(width):
            if mask_numpy[y, x]:
                draw.point((x, y), fill=(0, 255, 0, 128))
    combined = Image.alpha_composite(combined, overlay)

combined.save("fish_result.png")
