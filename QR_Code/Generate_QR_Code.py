import qrcode
from PIL import Image
import os
import sys


class QRCode:
    def __init__(self, info, pic_path, logo_path):
        self.url = info
        self.pic_path = pic_path
        self.logo = logo_path

    def generate_qrcode(self):
        """
        生成中间带logo的二维码
        需要安装qrcode, PIL库
        @参数 string: 二维码字符串
        @参数 path: 生成的二维码保存路径
        @参数 logo: logo文件路径
        @return: None
        """
        qr = qrcode.QRCode(
            # 25*25     二维码的版本号，每一个版本号对应一个尺寸，这里尺寸不是图片的大小而的是二维码长宽被分成的份数
            version=2,
            # 纠错容量，指二维码不完整时可以正常识别出原信息的概率（ERROR_CORRECT_H的纠错率最高）
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            # 生成图片的像素
            box_size=8,
            # 二维码边框宽度
            border=1,
        )
        # string为想要打开的链接
        qr.add_data(self.url)
        # 用make()方法生成图片
        qr.make(fit=True)
        # 得到二维码对象，并可以通过修改fill_color、back_color参数来调整小格子颜色和背景色
        img = qr.make_image(fill_color='black', back_color='white')
        # 将图片转换为RGBA格式
        img = img.convert("RGBA")
        if self.logo and os.path.exists(self.logo):
            try:
                icon = Image.open(self.logo)
                # img_w、img_h是二维码的尺寸
                img_w, img_h = img.size
            except Exception as e:
                print(e)
                sys.exit(1)
            factor = 4
            size_w = int(img_w / factor)
            size_h = int(img_h / factor)

            # icon_W、icon_h是logo原始的尺寸
            icon_w, icon_h = icon.size
            # size_W、size_h是二维码尺寸的1/factor
            if icon_w > size_w:
                icon_w = size_w
            if icon_h > size_h:
                icon_h = size_h
            # antialias是平滑处理
            # icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
            icon = icon.resize((icon_w, icon_h), Image.Resampling.LANCZOS)
            # 保证二维码大小不超过二维码大小的1/factor

            # 计算logo在二维码中的相对位置
            w = int((img_w - icon_w) / 2)
            h = int((img_h - icon_h) / 2)
            icon = icon.convert("RGBA")
            # 根据相对位置w、h将logo放到二维码图片上，所以说实际是logo并不是二维码的一部分，会遮挡二维码的一部分，不能太大，否则无法识别
            img.paste(icon, (w, h), icon)
        img.save(self.pic_path)
        # 调用系统命令打开图片
        # xdg - open(opens a file or URL in the user's preferred application)
        # os.system('xdg-open %s' %(path)) #这是Linux系统的命令
        # windows 下打开文件
        os.startfile(self.pic_path)
