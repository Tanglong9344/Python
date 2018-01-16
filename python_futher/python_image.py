# python Image module
# url: http://www.pythonware.com/products/pil/
from PIL import Image, ImageDraw

print("Modes:", Image.MODES)
print("Version:", Image.VERSION)

# open a image
im = Image.open('image/im.png')

# show information of a image
print(" im.format:%s\n im.size:%s\n im.mode:%s\n" % (im.format, im.size, im.mode))

# show a image
# im.show()

# create a image
# 1.Image.new(mode,size)
# 2.Image.new(mode,size,color)
im_new = Image.new("RGBA", (600, 450), (155, 165, 0))
print(" im_new.format:%s\n im_new.size:%s\n im_new.mode:%s\n" % (im_new.format, im_new.size, im_new.mode))
# save a image
im_new.save('image/im_new.png', 'png')

# point operation-enhance each point of this image by multifing 1.5
im_out = im.point(lambda i: i*1.5)
im_out.save('image/im_out.png', 'png')

# crop a image
im_crop = im.crop((60, 30, 450, 420))
im_crop.save('image/im_crop.png', 'png')

# paste and union two images
im.save('image/im_1.png', 'png')
im_1 = Image.open('image/im_1.png')
im_1.paste(im_crop, (60, 30, 450, 420))

# channel spliit
r, g, b, a = im.split()
print(" r:%s\n g:%s\n b:%s\n a:%s\n" % (r, g, b, a))
# channel merge
im_merge = Image.merge("RGBA", (b, r, g, a))
im_merge.save('image/im_merge.png', 'png')

# image resize
im_resize = im.resize((128, 128))
im_resize.save('image/im_resize.png', 'png')

# image rotate-anticlockwize
im_rotate = im.rotate(-45)
im_rotate.save('image/im_rotate.png', 'png')
# image transpose(rotate)-anticlockwize
im_transpose = im.transpose(Image.ROTATE_270)
im_transpose.save('image/im_transpose.png', 'png')

# image transpose-left&right
im_lr = im.transpose(Image.FLIP_LEFT_RIGHT)
im_lr.save('image/im_lr.png', 'png')
# image transpose-top&bottom
im_tb = im.transpose(Image.FLIP_TOP_BOTTOM)
im_tb.save('image/im_tb.png', 'png')

# image type convert
im_type = im.convert("RGBA")
im_type.save('image/im_type.png', 'png')

# get pexel from a position
print("im.getpixel((4,4)):", im.getpixel((4, 4)))
# put pixel to a position
im.putpixel((4, 4), (255, 255, 255, 0))

# blend two images
# im_blend = Image.blend(im, im_new)
# im_blend.save('image/im_blend.png', 'png')
