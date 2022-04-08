import math
notes = [200,100,50,20,10,5]
def calc(num,notes):
    noteCount = []
    for note in notes:
        if num >= note:
            count = math.floor(num/note)
            noteCount.append(count)
            num -= count*note
    c = -1
    for n in notes:
        c+=1
        print(str(noteCount[c]) + " " + str(n))
while(True):
    calc(int(input("fiyat giriniz")), notes)
  
