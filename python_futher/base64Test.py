import base64

image = 'image/im_type.png'
with open(image, 'rb') as f:
    image = f.read()
    image_base64 = str(base64.b64encode(image), encoding='utf-8')
    print("base64:",image_base64)