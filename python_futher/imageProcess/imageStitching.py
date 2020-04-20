from PIL import Image

def stitch():
    im_list = [Image.open('1.jpg'),Image.open('2.jpg')]

    # 图像尺寸
    width, height = im_list[1].size
    # 图片转化为相同的尺寸
    im_list[0] = im_list[0].resize((width, height))

    # 创建空白长图
    result = Image.new(im_list[0].mode, (width * 2, height))

    # 拼接
    for i, im in enumerate(im_list):
        result.paste(im, box=(i * width, 0))

    # 保存图片
    result.save('result_stitch.jpg')


if __name__ == '__main__':
    stitch()