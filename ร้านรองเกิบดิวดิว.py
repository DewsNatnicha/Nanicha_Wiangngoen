Shopping = list()

def Store():
  print("---------------------\nร้านรองเกิบ ดิวดิ่วดิ้วดิ๊วดิ๋ว\n---------------------")
  print('[1]NIKE\n[2]ADIDAS\n[3]FILA\n[4]แสดงรายการสินค้า\n[5]ไม่รับสินค้าแล้วค่ะ')
  Select = input('\nกรุณาเลือกยี่ห้อ: ')
  if Select == '1': F1()
  elif Select == '2': F2()
  elif Select == '3': F3()
  elif Select == '4': Shop()
  elif Select == '5': exit()
  else: Store()

def F1():
  print("\n--------------\nNIKE\n--------------")
  print('[1]Nike P-6000\n[2]Nike Air Max 200\n[3]Nike in season TR9')
  S = input("\nเลือกรุ่น: ")
  if S == '1': F1Price(1)
  elif S == '2': F1Price(2)
  elif S == '3': F1Price(3)
  else: print("\nกรุณาเลือกใหม่ค่ะ") ; F1()

def F1Price(n):
  if n == 1:
    print("Nike P-6000  ราคา 3600 บาท  ส่วนลด 10%")
    Shopping.append(['Nike P-6000','3600','10%',str(3600*(90/100))])
    Store()
  elif n == 2:
    print("Nike Air Max 200  ราคา 2400 บาท  ส่วนลด 10%")
    Shopping.append(['Nike Air Max 200','2400','10%',str(2400*(90/100))])
    Store()
  elif n == 3:
    print("Nike in season TR9  ราคา 2700 บาท  ส่วนลด 10%")
    Shopping.append(['Nike in season TR9','2700','10%',str(2700*(90/100))])
    Store()
  else : print("ขออภัยค่ะ ทางร้านไม่มีสินค้า") ; F2()

def F2():
  print("\n--------------\nADIDAS\n--------------")
  print('[1] Adidas PULSEBOOST HD M\n[2] Adidas ULTRABOOST 19\n[3] Adidas LXCON 94')
  S = input("\nเลือกรุ่น: ")
  if S == '1': F2Price(1)
  elif S == '2': F2Price(2)
  elif S == '3': F2Price(3)
  else: print("\nกรุณาเลือกใหม่ค่ะ") ; F2()

def F2Price(n):
  if n == 1:
    print("Adidas PULSEBOOST HD M  ราคา 5000 บาท  ส่วนลด 30%")
    Shopping.append(['Adidas PULSEBOOST HD M ','5000','30%',str(5000*(70/100))])
    Store()
  elif n == 2:
    print("Adidas ULTRABOOST 19 V1 ราคา 7300 บาท ส่วนลด 30%")
    Shopping.append(['Adidas ULTRABOOST 19','7300','30%',str(7300*(70/100))])
    Store()
  elif n == 3:
    print("Adidas LXCON 94 V1  ราคา 6000 บาท  ส่วนลด 30%")
    Shopping.append(['Adidas LXCON 94','6000','30%',str(6000*(70/100))])
    Store()
  else : print("ขออภัยค่ะ ทางร้านไม่มีสินค้า") ; F2()
    
def F3():
  print("\n--------------\nFILA\n--------------")
  print('[1]FILA FA181546\n[2]FILA Ray CB Low\n[3]FILA Welly Indoor Court')
  S = input("\nเลือกรุ่น: ")
  if S == '1': F3Price(1)
  elif S == '2': F3Price(2)
  elif S == '3': F3Price(3)
  else: print("\nกรุณาเลือกใหม่ค่ะ") ; F3()

def F3Price(n):
  if n == 1:
    print("FILA FA181546  ราคา 1290 บาท  ส่วนลด 20%")
    Shopping.append(['FILA FA181546','1290','20%',str(1290*(80/100))])
    Store()
  elif n == 2:
    print("FILA Ray CB Low  ราคา 2691 บาท  ส่วนลด 20%")
    Shopping.append(['FILA Ray CB Low','2691','20%',str(2691*(80/100))])
    Store()
  elif n == 3:
    print("FILA Welly Indoor Court ราคา 1290 บาท  ส่วนลด 20%")
    Shopping.append(['FILA Welly Indoor Court','1290','20%',str(1290*(80/100))])
    Store()
  else : print("ขออภัยค่ะ ทางร้านไม่มีสินค้า") ; F3()

def Shop():
  AP = 0 
  print("\n-------------------------------------------------------------------------------------------------")
  print("รุ่นรองเท้า                      ราคา                         ส่วนลด                          จ่ายจริง")
  print("-------------------------------------------------------------------------------------------------")
  for i in Shopping :
    for k in i :
      print(k.ljust(30),end="")
    print()
  for i in range(len(Shopping)): AP = AP + float(Shopping[i][3])
  print("-------------------------------------------------------------------------------------------------")
  print("รวมเป็นเงิน                                                                                   %d"%AP)
  
Store()