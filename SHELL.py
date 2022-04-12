# Сортировка Шелла - сортировкой с уменьшением инкремента

def shellSort(alist):
    shag = len(alist) // 2
    while shag > 0:

      for str in range(shag):
        gapInsert(alist,str,shag)

      print("При шаге приращения  ",shag,
                                   "список такой: ",alist)

      shag = shag // 2

def gapInsert(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        val = alist[i]
        pos = i

        while pos>=gap and alist[pos-gap]>val:
            alist[pos]=alist[pos-gap]
            pos = pos-gap

        alist[pos]=val

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print("После сортировки: ", alist)