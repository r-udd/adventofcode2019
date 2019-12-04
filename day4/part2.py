no = "240920"
count = 0
while int(no) <= 789857:
    double = 0
    for i in range(5):
        if int(no[i]) > int(no[i+1]):
            #no = no[:i+1] + no[i] + no[i+2:]
            no = str(int(no) + 1)
            break
        if no[i] == no[i+1]:
            if i == 0 and no[i] != no[i+2]:
                double += 1
            elif i in range(1,4) and no[i] != no[i+2] and no[i-1] != no[i]:
                double += 1
            elif i == 4 and no[i-1] != no[i]:
                double += 1

            
    else: 
        if double >= 1:
            count += 1
        no = str(int(no) + 1)

print(count)