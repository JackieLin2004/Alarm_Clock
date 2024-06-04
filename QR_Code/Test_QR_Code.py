import QR_Code.Generate_QR_Code as qr

# 二维码的链接
# info = "http://www.sei.ynu.edu.cn/"
# info = "http://wzzzzz.gnway.cc:11679/"
# info = "https://www.et.ynu.edu.cn/appdd/uploads/20221120011/2/alarm_clock.html"
info = "http://43.140.36.10/#/ClockPage"
# 生成的图片保存文件
pic_path = "QR_Code.png"
# logo的文件名
logo_path = r"./logo.png"
# 调用函数
qrcode = qr.QRCode(info, pic_path, logo_path)
qrcode.generate_qrcode()
