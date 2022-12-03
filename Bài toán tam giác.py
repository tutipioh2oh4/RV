import math

#Ham kiem tra tam giac:
def kiem_tra_tam_giac(TD):
    # Toa do cac dinh tam giac ABC
    A = TD[0:2]
    B = TD[2:4]
    C = TD[4:6]
    # Toa do cac canh cua tam giac ABC
    AB = [float(B[0]) - float(A[0]), float(B[1]) - float(A[1])]
    BC = [float(C[0]) - float(B[0]), float(C[1]) - float(B[1])]
    CA = [float(A[0]) - float(C[0]), float(A[1]) - float(C[1])]
    try:
        if (AB[0]/((-1)*CA[0])) !=  (AB[1]/((-1)*CA[1])):
            return True
        else:
            return False
    except:
        return False


#Ham tinh do dai cac canh:
def goc_canh_tamgiac(AB,BC,CA):
    import math
    a=list()
    canhAB= round(math.sqrt(AB[0]*AB[0]+AB[1]*AB[1]),2)
    canhBC= round(math.sqrt(BC[0]*BC[0]+BC[1]*BC[1]),2)
    canhCA= round(math.sqrt(CA[0]*CA[0]+CA[1]*CA[1]),2)
    a.append(canhAB)
    a.append(canhBC)
    a.append(canhCA)

    cosA=(AB[0]*(-1)*CA[0]+AB[1]*(-1)*CA[1])/(math.sqrt(pow(AB[0],2)+pow(AB[1],2))*math.sqrt(pow(CA[0],2)+pow(CA[1],2)))
    gocA= round(math.degrees(math.acos(cosA)),2)
    a.append(gocA)

    cosB =(BC[0]*(-1)*AB[0]+BC[1]*(-1)*AB[1])/(math.sqrt(pow(BC[0],2)+pow(BC[1],2))*math.sqrt(pow(AB[0],2)+pow(AB[1],2)))
    gocB = round(math.degrees(math.acos(cosB)),2)
    a.append(gocB)

    '''cosC =(CA[0]*(-1)*BC[0]+CA[1]*(-1)*BC[1])/(math.sqrt(pow(CA[0],2)+pow(CA[1],2))*math.sqrt(pow(BC[0],2)+pow(BC[1],2)))
    gocC = round(math.degrees(math.acos(cosC)),2)'''
    gocC= round(180-gocB-gocA,2)
    a.append(gocC)
    return a

#Ham xet tam giac
def xet_tamgiac(a):
    a= goc_canh_tamgiac(AB,BC,CA)
    if a[0]==a[1] and a[1]==a[2]:
        return("Tam giac ABC la tam giac deu")
    elif a[0]==a[1] or a[1]==a[2] or a[2]==a[0]:
        if a[3]==90:
            return("Tam giac ABC vuong can tai A")
        elif a[4]== 90:
            return("Tam giac ABC vuong can tai B")
        elif a[5]== 90:
            return("Tam giac ABC vuong can tai C")
        elif a[3]> 90:
            return("Tam giac ABC tu can tai A")
        elif a[4]> 90:
            return("Tam giac ABC tu can tai B")
        elif a[5]> 90:
            return("Tam giac ABC tu can tai C")
        else:
            return("Tam giac ABC la tam giac can")
    elif a[0]!=a[1] and a[1]!=a[2] and a[2]!=a[0]:
        if a[3] == 90:
            return("Tam giac ABC vuong tai A")
        elif a[4] == 90:
            return("Tam giac ABC vuong tai B")
        elif a[5] == 90:
            return("Tam giac ABC vuong tai C")
        elif a[3] > 90:
            return("Tam giac ABC tu tai A")
        elif a[4] > 90:
            return("Tam giac ABC tu tai B")
        elif a[5] > 90:
            return("Tam giac ABC tu tai C")
    else:
        return("Tam giac ABC la tam giac binh thuong")


#Ham tinh dien tich tam giac
def dien_tich(a):
    a= goc_canh_tamgiac(AB,BC,CA)
    p= (a[0]+a[1]+a[2])/2
    S=round(math.sqrt(p*(p-a[0])*(p-a[1])*(p-a[2])),2)
    return S


#Ham tinh duong cao tam giac
def duongcaotamgiac(S,a):
    S=dien_tich(a)
    a=goc_canh_tamgiac(AB,BC,CA)
    dc=list()
    dcA=round(S*2/a[2],2)
    dc.append(dcA)
    dcB=round(S*2/a[3],2)
    dc.append(dcB)
    dcC=round(S*2/a[1],2)
    dc.append(dcC)
    return dc


#Ham tinh toa do trong tam va truc tam cua tam giac
def tam_tamgiac(A,B,C):
    H=list()
    tt1= round((int(A[0])+int(B[0])+int(C[0]))/3,2)
    H.append(tt1)
    tt2= round((int(A[1])+int(B[1])+int(C[1]))/3,2)
    H.append(tt2)
    return H


#Ham tinh trung tuyen tam giac:
def trungtuyen_tamgiac(A,B,C,H):
    AH = [float(H[0]) - float(A[0]), float(H[1]) - float(A[1])]
    BH = [float(H[0]) - float(B[0]), float(H[1]) - float(B[1])]
    CH = [float(H[0]) - float(C[0]), float(H[1]) - float(C[1])]
    TT=list()
    ttA=  round(math.sqrt(pow(AH[0], 2) + pow(AH[1],2)),2)
    TT.append(ttA)
    ttB = round(math.sqrt(pow(BH[0], 2) + pow(BH[1],2)),2)
    TT.append(ttB)
    ttC = round(math.sqrt(pow(CH[0], 2) + pow(CH[1],2)),2)
    TT.append(ttC)
    return TT


#Ham giaima tam giac:
def giaima_tamgiac(TD):
    if kiem_tra_tam_giac(TD) is False:
        return("A, B, C khong hop thanh mot tam giac")
    else:
        print("A, B, C hop thanh mot tam giac")
        a=goc_canh_tamgiac(AB,BC,CA)
        print("Chieu dai canh AB: ",a[0])
        print("Chieu dai canh BC: ", a[1])
        print("Chieu dai canh BC: ", a[2])
        print("Goc A: ", a[3])
        print("Goc B: ", a[4])
        print("Goc C: ", a[5])
        print(xet_tamgiac(a))
        S=dien_tich(a)
        print("Dien tich cua tam giac ABC: ",S)
        dc=duongcaotamgiac(S,a)
        print("Do dai duong cao tu dinh A:",dc[0])
        print("Do dai duong cao tu dinh B:", dc[1])
        print("Do dai duong cao tu dinh C:", dc[2])
        H= tam_tamgiac(A,B,C)
        TT=trungtuyen_tamgiac(A,B,C,H)
        print("Khoang cach tu trong tam den diem A: ",TT[0])
        print("Khoang cach tu trong tam den diem B: ", TT[1])
        print("Khoang cach tu trong tam den diem C: ", TT[2])
        print("Toa do trong tam tam giac ABC: ", H)
TD = list()
KH=['Ax','Ay','Bx','By','Cx','Cy']
for i in range(0, 6):
    td = float(input("Mơi ban nhap vao toa do "+ KH[i]+': '))
    TD.append(td)
# Toa do cac dinh tam giac ABC
A = TD[0:2]
B = TD[2:4]
C = TD[4:6]
# Toa do cac canh cua tam giac ABC
AB = [float(B[0]) - float(A[0]), float(B[1]) - float(A[1])]
BC = [float(C[0]) - float(B[0]), float(C[1]) - float(B[1])]
CA = [float(A[0]) - float(C[0]), float(A[1]) - float(C[1])]
print(giaima_tamgiac(TD))







