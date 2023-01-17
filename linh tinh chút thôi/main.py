# Thiết kế ngôn ngữ lập trình
import subprocess, os
from thuvienham import *
# hiển thị đầu ra
htdr=False
# đọc code là biết
a = open ('dauvao.txt','r',encoding='utf8')
list=a.readlines()
a.close()

# kiểm tra tiếng việt
tiengviet=kiemtratiengviet(list)
# sao lưu văn bản
sl=list
# xóa comment khoảng cách
list=xoacomment(list)
#list=xoakhoangcach(list)
list=linhtinh(list)
# xóa dấu tiếng việt
list=xoadau(list)
# xác định các hàm, dịch switch. chưa code được cái switch đâu
list=xacdinhham(list)
# nối chữ ví dụ: a y e ->aye
list=noichu(list)
# thêm : 
list=themhaicham(list)
# sử lí dấu toán tử so sách
list=sosanh(list)
# sử lí class. chưa là được gì nhiều đâu
list=slclass(list)
# nối chữ
list=noichutrongdongcotukhoa(list)
# ghi dữ liệu ra
b=open('daura.py','w',encoding='utf8')
for i in list:
    b.write(i)   
b.close()


# chạy file đầu ra .py với trình bao. đâu ra được lưu vào a.stdout lỗi được lưu vào a.stderr
a=subprocess.run(['python', 'daura.py'],capture_output=True,encoding='utf-8')
outp=a.stdout.strip()
er=a.stderr.strip()
if len(outp)!=0:
    print(outp)
er=er.split('\n')
err(sl,er,tiengviet)
if len(er)>1:
    print()
if htdr ==False:
    os.remove('daura.py')

