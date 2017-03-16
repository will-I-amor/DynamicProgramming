def billChange(alist,goal):
    #t = [1,2,5,10,20]
    #goal = 51
    n = len(alist)
    kong = []
    while (goal>0):
        mymax = 0
        for i in alist:
            if i<=goal:
                if mymax<i:
                    mymax = i
        goal = goal - mymax
        kong.append(mymax)
    print kong
    return kong

alist = [1,2,5,10,20]
goal = 53
t = billChange(alist,goal)
