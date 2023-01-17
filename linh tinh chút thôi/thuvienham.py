def tudien(vb):
    vb=vb.replace('trả về ','return ')
    vb=vb.replace('trong khi ','while ')
    vb=vb.replace('nhập tất cả','import *')
    vb=vb.replace('nhập ', 'import ')
    vb=vb.replace('mở','open')
    vb=vb.replace('từ ','from ')
    vb=vb.replace('đóng','close')
    vb=vb.replace(' trong ',' in ')
    vb=vb.replace('hoặc nếu ', 'elif ')
    vb=vb.replace('nếu không thì','else')
    vb=vb.replace('nếu ','if ')
    vb=vb.replace('duyệt ','for ')
    vb=vb.replace('dừng lặp','break')
    vb=vb.replace('lớp ','class ')
    vb=vb.replace('công tắc', 'switch')
    vb=vb.replace('tiếp tục','continue')
    vb=vb.replace('căn','math.sqrt')
    vb=vb.replace('đúng','True')
    vb=vb.replace('sai','False')
    vb=vb.replace(' và ',' and ')
    vb=vb.replace(' hoặc ',' or ')
    vb=vb.replace('in ra ','print')
    vb=vb.replace('thêm vào','.append')
    vb=vb.replace('chuỗi','range')
    vb=vb.replace('thư viện toán','math')
    vb=vb.replace('là', '=')
    vb=vb.replace('bằng', '=')
    vb=vb.replace('không là', '!=')
    vb=vb.replace('thì', '')
    return vb

def linhtinh(ds):
    list=[]
    for i in ds:
        i=inraxnlan(i)
        for j in i:
            list.append(j)
    ds=[]
    for i in list:
        i=ll(i)
        for j in i:
            ds.append(j)
    return ds

def xoadautiengviet(vanban):  
    S=''
    bt=False
    for s in vanban:
        if bt==False and s=="'":
            bt=True
        elif bt==True and s=="'":
            bt=False
        if bt==False:
            def sub(l,x,s):
                for i in l:
                    if i==s:
                        return x
                return s
            s = sub('áàảãạăắằẳẵặâấầẩẫậ', 'a', s)
            s = sub('ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ', 'A', s)
            s = sub('éèẻẽẹêếềểễệ', 'e', s)
            s = sub('ÉÈẺẼẸÊẾỀỂỄỆ', 'E', s)
            s = sub('óòỏõọôốồổỗộơớờởỡợ', 'o', s)
            s = sub('ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ', 'O', s)
            s = sub('íìỉĩị', 'i', s)
            s = sub('ÍÌỈĨỊ', 'I', s)
            s = sub('úùủũụưứừửữự', 'u', s)
            s = sub('ÚÙỦŨỤƯỨỪỬỮỰ', 'U', s)
            s = sub('ýỳỷỹỵ', 'y', s)
            s = sub('ÝỲỶỸỴ', 'Y', s)
            s = sub('đ', 'd', s)
            s = sub('Đ', 'D', s)
            S=S+s
        elif bt==True:
            S=S+s
        
    return S

def xoakhoangtrong(vanban):
    s=''
    for i in vanban:
        if i!=' ':
            s=s+i
    return s
  
def themhc(vb):
    dem=0
    daura=''
    t=False
    for i in vb:
        dem=dem+1
        if dem<=len(vb):
            daura=daura+i
        if i=='(':
            t=True
    if t:
        vb=vb+':'+'\n'
    else:
        vb=vb+'()'+':'+'\n'
    return vb   

def xoadau(ds):
    list=[]
    for i in ds:
        i=tudien(i)
        i=sulyrange(i)
        i=sulywhile(i)
        xoadau=xoadautiengviet(i)
        list.append(xoadau)
    return list

def xoacomment(list):
    daura=[]
    for i in list:
        vb=''
        for j in i:
            if j=='#':
                vb=vb+'\n'
                break
            vb=vb+j
        daura.append(vb)
    return daura

def xoakhoangcach(list):
    daura=[]
    for i in list:
        test=False
        if i.count(' ')!=len(i)-1:
            test=True
        if i!='\n' and test==True:
            daura.append(i)
    return daura

def tukhoa(vb):
    tukhoa=['def','class ','while ','for ','if ','else','elif ','switch ','default ','import ','from ','in ','return ',' ?','trả về ','trong khi ', 'trong ','nếu ', 'hoặc nếu ', ' nếu không thì','duyệt ','dừng lặp', 'lớp','công tắc']
    daura=[]
    for i in tukhoa:
        daura.append(i in vb)
    return any(daura)

def switch(list):
    return list

def xacdinhham(list):
    kc={}
    dem1=-1
    for i in list:
        dem1=dem1+1
        dem2=0
        for j in i:
            if j!=' ':
                break
            dem2=dem2+1
        kc[dem1]=dem2
    daura=[]
    k=-1
    vitri=0
    mangswitch=[]
    for vb in list:
        ct=False
        if k<len(kc)-2:
            k=k+1
            if 'switch ' in vb:
                vitri=k
                ct=True
            if kc[k]>kc[vitri] and vitri!=0 or ct == True:
                mangswitch.append(vb)
                continue
            if vitri!=0:
                dsswitch=switch(mangswitch)
                mangswitch=[]
                vitri=0
                for i in dsswitch:
                    daura.append(i)
            dk1=tukhoa(vb)
            if kc[k+1]-kc[k]==4 and dk1==False:
                vb=vb.strip()
                vb=xoakhoangtrong(vb)
                vb=themhc(vb)
                vb=kc[k]*' '+'def '+vb
        daura.append(vb)
    return daura
            
def dkt(vb):
    dem=0
    for i in vb:
        if i==' ':
            dem=dem+1
        else:
            break
    return dem

def noivb(vb):
    dr=''
    for i in vb:
        if i!=' ':
            dr=dr+i
    return dr

def noichu(list):
    daura=[]
    for i in list:
        i=sulyfor(i)
        i=sulyif(i)
        if 'class' in i:
            kt=dkt(i)
            i=i.lstrip('class')
            s=''
            for j in i:
                if j!=' ':
                    s=s+j
            s=kt*' '+'class '+s
            i=s
        if tukhoa(i):
            daura.append(i)
        else:
            s=''
            kt=dkt(i)
            bt=False
            for j in i:
                if bt==False and j=="'":
                    bt=True
                elif bt==True and j=="'":
                    bt=False
                if j!=' ' and bt==False:
                    s=s+j
                elif bt==True:
                    s=s+j
            s=kt*' '+s
            daura.append(s)
    return daura

def themhaicham(list):
    daura=[]
    for i in list:
        tukhoa=['class ','while ','for ','if ','else','elif ']
        dr=[]
        for j in tukhoa:
            dr.append(j in i)
        test = any(dr)
        if test:
            i=i.rstrip('\n')
            i=i.rstrip()
            i=i+':'+'\n'
        daura.append(i)
    return daura

def sosanh(list):
    daura=[]
    for i in list:
        tukhoa=['while ','if ','elif ']
        dr=[]
        for j in tukhoa:
            dr.append(j in i)
        test = any(dr)
        s=''
        for p in i:
            if p=='=' and test:
                p='=='
            s=s+p
        s=dbang(s)
        daura.append(s)
    return daura

def dbang(vb):
    a=''
    for i in vb:
        if '=' in vb and ' ?' in vb:
            if i=='=':
                i='=='
            if i=='?':
                i=''
        a=a+i
    return a

def slclass(mang):
    list=mang
    dem=-1
    for vb in list:
        dem=dem+1
        s1=''
        s3=''
        if 'class ' in vb:
            for i in vb:
                if i=='(' or i==':':
                    break
                else:
                    s1=s1+i
            s1=s1.lstrip()
            s1=s1.lstrip('class')
        if dem<len(list)-1:
            if 'def ' in list[dem+1]:
                s2=list[dem+1]
                for i in s2:
                    if i=='(' or i==':':
                        break
                    else:
                        s3=s3+i
                s3=s3.lstrip()
                s3=s3.lstrip('def')
        if s1==s3 and s3!='':
            kt=dkt(list[dem+1])
            congtac=False
            vanban=''
            for m in list[dem+1]:
                if m=='(' or m==':':
                    congtac= True

                if congtac==True:
                    vanban=vanban+m
            r=kt*' '+'def __init__ '+vanban
            list[dem+1]=r
    return list
            
def noichutrongdongcotukhoa(list):
    daura=[]
    for i in list:
        if 'return ' in i:
            kt=dkt(i)
            i=i.lstrip()
            i=i.lstrip('return')
            i=noivb(i)
            i=kt*' '+'return '+i
        # thêm vào các trường hợp
        daura.append(i)
    return daura

def sulyfor(vb):
    if 'for ' in vb and ' in ' in vb:
        vb=vb.replace(' in ','~in~')
        kc=dkt(vb)
        vb=vb.lstrip()
        vb=vb.lstrip('for ')
        dr=''
        for i in vb:
            if i!=' ':
                dr=dr+i
        dr=kc*' '+'for '+dr
        vb=dr.replace('~in~',' in ')
    return vb

def sulywhile(vb):
    if 'while ' in vb:
        vb=vb.replace('while ','while~')
        kc=dkt(vb)
        dr=''
        for i in vb:
            if i!=' ':
                dr=dr+i
        dr=kc*' '+dr
        vb=dr.replace('~',' ')
    return vb

def sulyif(vb):
    if 'if ' in vb:
        vb=vb.replace('if ','if~')
        kc=dkt(vb)
        dr=''
        for i in vb:
            if i!=' ':
                dr=dr+i
        dr=kc*' '+dr
        vb=dr.replace('~',' ')
    return vb

def sulyrange(vb):
    if 'range' in vb:
        a=vb.split('range')
        b=''
        l=a[1].lstrip()
        for i in l:
            if i!=')':
                b=b+i
            else:
                break
        b=b.lstrip('(')
        b=b.split(',')
        ss=vb.split(')')
        sss=ss[1]
        if len(b)==1:
            ch='range(1,'+b[0]+'+1'
            vb=a[0]+ch+')'+sss
        elif len(b)==2:
            ch='range('+b[0]+','+b[1]+'+1'
            vb=a[0]+ch+')'+sss
        else:
            print('???')
    return vb
        
def inraxnlan(vb):
    r=vb
    dr=[]
    kc=dkt(vb)
    if 'in ra ' in vb and 'lần' in vb:
        vb=vb.strip()
        vb=vb.lstrip('in ra ')
        vb=vb.rstrip('lần')
        vb=vb.split()
        try:
            n=int(vb[-1])
            s=''
            for i in vb:
                if i != vb[-1]:
                    s=s+i+' '
            s=s.strip()
            vb1=kc*' '+'for i in range('+str(n)+')\n'
            vb2=(kc+4)*' '+"print('"+s+"')\n"
            dr.append(vb1)
            dr.append(vb2)
            return dr
        except:
            dr.append(r)
            return dr
    elif 'in ra ' in vb and '(' not in vb:
        vb=vb.strip()
        vb=vb.lstrip('in ra')
        vb=vb.strip()
        vb=vb.strip("'")
        vb=vb.strip('"')
        vb=kc*' '+"print('"+vb+"')\n"
        dr.append(vb)
        return dr
    dr.append(r)
    return dr 
        
def ll(vb):
    r=vb
    dr=[]
    if 'lặp lại ' in vb and 'lần' in vb:
        vb=vb.rstrip()
        kc=dkt(vb)
        vb=vb.lstrip()
        vb=vb.lstrip('lặp lại ')
        vb=vb.rstrip('lần')
        vb=vb.split()
        try:
            n=int(vb[-1])
            if len(vb) == 1:
                r='for i in range('+str(n)+')\n'
                dr.append(r)
                return dr
            else:
                s=''
                for i in vb:
                    if i != vb[-1]:
                        s=s+i+' '
                s=s.strip()
                vb1=kc*' '+'for i in range('+str(n)+')\n'
                if '()' in s:
                    vb2=(kc+4)*' '+s+'\n'
                else:
                    vb2=(kc+4)*' '+s+'()\n'
                dr.append(vb1)
                dr.append(vb2)
                return dr
        except:
            dr.append(r)
            return dr
    dr.append(r)
    return dr 
    
def ferr(vb):
    vb=vb.split()
    dem=0
    for i in vb:
        dem=dem+1
        if i=='line':
            x=vb[dem].rstrip(',')
            return int(x)-1
    return '???'

def err(sl,er,tiengviet):
    ct=False
    hang=0
    for i in er:
        if ct==False:
            i=sulitrichdan(sl,i,hang)
            i=dsl(i,tiengviet)
            print(i)
        else:
            if tiengviet==True:
                print('  Lỗi tại dòng',hang+1)
            print('->  '+sl[hang].strip('\n'))
        if 'line' in i and 'File' in i:
            ct =True
            hang=ferr(i)
        else:
            ct=False
                
def dsl(vb,tiengviet):
    
    if vb=='SyntaxError: invalid syntax' and tiengviet==True:
        vb='SyntaxError: invalid syntax\nLỗi cú pháp: cú pháp không hợp lệ'
    if 'NameError: name' in vb and 'is not defined' in vb and tiengviet==True:
        a=vb.replace('NameError: name ','Lỗi Tên: tên ')
        a=a.replace(' is not defined',' không được xác định')
        a=a.replace('Did you mean','Ý bạn là')
        vb=vb+'\n'+a
    if vb=='ZeroDivisionError: division by zero' and tiengviet==True:
        vb='ZeroDivisionError: division by zero'+'\nLỗi chia không: chia cho số không'
    if 'SyntaxError: unterminated string literal' in vb and tiengviet==True:
        vb=vb+'\nLỗi cú pháp: chuỗi ký tự chưa kết thúc'
    if 'ModuleNotFoundError: No module named' in vb and tiengviet==True:
        a=vb.replace('ModuleNotFoundError: No module named','Lỗi không tìm thấy mô-đun: Không có mô-đun có tên')
        vb=vb+'\n'+a
    if 'SyntaxError: Missing parentheses' in vb and tiengviet==True:
        vb=vb+'\nLỗi cú pháp: Thiếu dấu ngoặc đơn'
    if vb=='IndexError: list index out of range' and tiengviet==True:
        vb=vb+'\nLỗi chỉ mục: danh sách chỉ mục nằm ngoài phạm vi'
    if vb=='IndentationError: unexpected indent' and tiengviet==True:
        vb=vb+'\nLỗi ghi chú: thụt lề không mong muốn'
    
    return vb

def dstt(vb):
    ds=['+', '-', '*', '%','=', '/','==','!=','<','>','(',')',','] 
    for i in ds:
        if vb == i:
            return True
    return False

def tachbien(vb):
    dr=[]
    s=''
    for i in vb:
        if dstt(i)==True:
            dr.append(s)
            s=''
            continue
        s=s+i
    dr.append(s)
    return dr

def sulitrichdan(sl,vb,hang):
    dem=0
    if 'Error' in vb and "'" in vb:
        ct=False
        s=''
        x=xoadautiengviet(sl[hang])
        x=noivb(x)
        for i in vb:
            if i=="'" and ct == True:
                ct=False
                dem=dem+1
                continue
            if ct==True:
                s=s+i
            if i=="'" and ct == False and dem<1:
                ct=True
        x=tachbien(x.strip('\n'))
        vbx=tachbien(sl[hang].strip('\n'))
        dem=-1
        for i in x:
            dem=dem+1
            if i==s:
                kq=vbx[dem]
                vb=vb.replace(s, kq)
        return vb
    else:
        return vb
    
def kiemtratiengviet(list):
    for i in list:
        kiemtra=danhsachtukhoa(i)
        if kiemtra==True:
            return True
    return False

def danhsachtukhoa(vb):
    ds=['trả về ','trong khi ','nhập tất cả','nhập ','mở','từ ','đóng',' trong ','hoặc nếu ','nếu không thì','nếu ','duyệt ','dừng lặp','lớp ','công tắc','tiếp tục','căn','đúng','sai',' và ',' hoặc ','in ra ','thêm vào','chuỗi','thư viện toán','là','bằng','không là','thì']
    for i in ds:
        if i in vb:
            return True
    return False

