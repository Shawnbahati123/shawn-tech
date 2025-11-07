import os, random, numpy as np
from PIL import Image, ImageDraw

OUT = 'backend/ai_engine/training/synthetic'
os.makedirs(OUT, exist_ok=True)

def gen_image(has_cash=True, idx=0):
    img = Image.new('RGB', (224,224), color=(255,255,255))
    d = ImageDraw.Draw(img)
    if has_cash:
        # draw simple green rectangle to simulate cash
        d.rectangle([60,80,160,140], fill=(34,139,34))
    img.save(os.path.join(OUT, f"img_{'cash' if has_cash else 'nocash'}_{idx}.png"))

def generate(n=100):
    for i in range(n):
        gen_image(True, i)
        gen_image(False, i)

if __name__ == '__main__':
    generate(50)
    print('Synthetic images generated in', OUT)
