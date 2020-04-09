import base64

image = 'image/base64.jpg'
with open(image, 'rb') as f:
    image = f.read()
    print(image)
    image_base64 = base64.b64encode(image)
    print(str(image_base64,encoding='utf-8'))