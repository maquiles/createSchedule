teams8 = ["1", "2", "3", "4", "5", "6", "7", "8"]
teams6 = ["1", "2", "3", "4", "5", "6"]

def create_schedule(list):
    
    s = []
    
    if len(list) % 2 == 1: list = list + ["BYE"]
    
    for i in range(len(list)-1):
        
        mid = len(list) / 2
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()
        
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]
        
        list.insert(1, list.pop())
    
    return s

def main():
    x = 1
    y = 1

    print "8 TEAMS"
    for round in create_schedule(teams8):
        print "week ", x
        for match in round:
            print match[0] + " - " + match[1]
        x+=1
        print
    print "6 TEAMS"
    for round in create_schedule(teams6):
        print "week ", y
        for match in round:
            print match[0] + " - " + match[1]
        y+=1
        print


if __name__ == "__main__":
    main()
