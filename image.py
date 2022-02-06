from PIL import Image, ImageFilter

with Image.open('./assets/img/zen_rocks.jpg') as img:
    img.thumbnail((400, 200))
    img.save('./assets/img_resize/zen_image.jpg')
    print(img.size)