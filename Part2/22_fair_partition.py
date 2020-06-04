listA = list()
listB = list()


def partition(ratings):
    global listA
    global listB

    ratings = [n for n in ratings if n > 0]
    ratings.sort(reverse=True)
    listA = []
    listB = []

    for n in ratings:
        insert_number(n)
    rebalance()
    redistribute()

    print(sum(listA))
    print(sum(listB))

    return (listA, listB)


def insert_number(number):
    global listA
    global listB

    if((not listA) or (len(listA) < len(listB)) or (listB and (len(listA) == len(listB)) and listA[-1] <= listB[-1])):
        listA.append(number)
    else:
        listB.append(number)


def get_bigger():
    global listA
    global listB

    sumA = sum(listA)
    sumB = sum(listB)
    
    bigger = []
    smaller = []
    if(sumA > sumB):
        bigger = listA
        smaller = listB
    else:
        bigger = listB
        smaller = listA

    return (bigger, smaller)

def redistribute():
    bigger, smaller = get_bigger()
    diff = sum(bigger) - sum(smaller)
    if(diff == 0):
        return

    maxEl = 0
    lIndex = -1
    for i in range(len(bigger)):
      if(bigger[i] < diff and bigger[i] > maxEl):
        maxEl = bigger[i]
        lIndex = i

    if(lIndex < 0):
      return

    smaller.append(bigger[lIndex])
    del bigger[lIndex]
    redistribute()

def rebalance():
    while (True):
        bigger, smaller = get_bigger()
        diff = sum(bigger) - sum(smaller)
        if(diff == 0):
          return

        maxElDiff = 0
        elDiffIndex = -1

        for i in range(len(bigger)):
            a = bigger[i]
            b = 0 if i >= len(smaller) else smaller[i]
            elDiff = 0 if b > a else a - b
            if(elDiff < diff and elDiff > maxElDiff):
                maxElDiff = elDiff
                elDiffIndex = i

        if(elDiffIndex < 0):
            break

        if(len(smaller) > elDiffIndex):
            smaller[elDiffIndex], bigger[elDiffIndex] = bigger[elDiffIndex], smaller[elDiffIndex]
        else:
            smaller.append(bigger[elDiffIndex])
            del bigger[elDiffIndex]


partition([92, 88, 82, 73, 70, 44, 43, 42, 21, 7])
partition([87, 81, 76, 62, 33, 32, 18, 17, 5, 2])
