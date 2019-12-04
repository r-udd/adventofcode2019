no = "240920"
count = 0
while int(no) <= 789857:
    double = False
    for i in range(5):
        if int(no[i]) > int(no[i+1]):
            #no = no[:i+1] + no[i] + no[i+2:]
            no = str(int(no) + 1)
            break
        if no[i] == no[i+1]:
            double = True
    else: 
        if double:
            count += 1
        no = str(int(no) + 1)

print(count)