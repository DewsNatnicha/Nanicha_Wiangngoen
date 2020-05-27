from datetime import date 
loop = 1
fdata = open("d:\\Dew_python\\DewMaLha.txt","w")
while loop <= 5:
    Name,Nickname,Birth,Province,School,tel = input("Name : Nickname : Date of Birth : Province : School : Tel ::: ").split(':')
    fdata.write('%s,%s,%s,%s,%s,%s\n'%(Name,Nickname,Birth,Province,School,tel))
    loop += 1
fdata.close()

def Show():
    fdata = open("d:\\Dew_python\\DewMaLha.txt","r")
    print("-----------------------------------------------------------------------------------------------------------")
    print("No.\tName\t\tNickname\t   Date of Birth\tAge\t    Province\t  School \t tel")
    print("-----------------------------------------------------------------------------------------------------------")
    count = 1
    while True:
        information = fdata.readline().split(',')
        if information[0] == "":
            break
        Birth = information[2]
        year = Birth[-4:len(Birth)]
        daynow = date.today().strftime('%Y')
        age = int(daynow)-int(year)
        print('{0:<10}'.format(str(count)),end="")
        print('{0[0]:<15}{0[1]:<20}{0[2]:<20}'.format(information),end="")
        print('{0:<10}'.format(str(age)),end="")
        print('{0[3]:<15}{0[4]:<12}{0[5]:<10}'.format(information),end="")
        count += 1
        print()
    print("-----------------------------------------------------------------------------------------------------------")
    fdata.close()
Show()
