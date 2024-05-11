import QR_Code.Generate_QR_Code as qr

# 二维码的链接
info = "http://www.sei.ynu.edu.cn/"
# 生成的图片保存文件
pic_path = "QR_Code.png"
# logo的文件名
logo_path = r"./logo.png"
# 调用函数
qrcode = qr.QRCode(info, pic_path, logo_path)
qrcode.generate_qrcode()
