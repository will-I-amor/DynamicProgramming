def fibna(n):
    kong = [0,1]
    if n<2:
        return n
    else:
        for i in range(n):
            temp = kong[0]+kong[1]
            kong[0] = kong[1]
            kong[1]=temp
        return temp
    
p = fibna(5)
print p
