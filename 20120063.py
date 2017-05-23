def rule1(빙고) :
    for x in range(0,5) :
        if (빙고[x][0]+빙고[x][1]+빙고[x][2]+빙고[x][3]+빙고[x][4]) == 5:
            return True; return False

def rule2(빙고):
    for x in range(0,5) :
        if (빙고[0][x]+빙고[1][x]+빙고[2][x]+빙고[3][x]+빙고[4][x]) == 5:
            return True; return False

def rule3(빙고):
    count1 = 0
    for x in range(0,5) :
        if 빙고[x][x] == 1:
            count1 = count1 + 1 
    if count1 == 5 :
        return True

    count1 = 0
    for x in range(0,5):
        if 빙고[x][4-x] == 1:
            count1 = count1 + 1
    if count1 == 5 :
        return True; return False

def rule4(빙고):
    if (빙고[0][0] and 빙고[0][4] and 빙고[4][0] and 빙고[4][4]) == 1:
        return True; return False    

row = 5
col = 5

빙고2 = []
빙고 = []

T = int(input())
for t in range(0,T):

    빙고2 = []
    빙고 = []

    for i in range(0, row):
        row_input = input().split()
        row_input = [int(j) for j in row_input]
        빙고2.append(row_input)

        if i == 2 :
            빙고.append([0,0,1,0,0])
        else :
            빙고.append([0]*5)
            
    input_numbers = input().split()
    input_numbers = [int(j) for j in input_numbers]

    count_of_input = 0
    for number in input_numbers:

        count_of_input = count_of_input + 1

        for x in range(0,5):
            for y in range(0,5):
                if number == 빙고2[x][y]:
                    빙고[x][y] = 1
                
        if rule1(빙고) == True:
            print(count_of_input)
            break

        if rule2(빙고) == True:
            print(count_of_input)
            break


        if rule3(빙고) ==True:
            print(count_of_input)
            break

        if rule4(빙고) == True:
            print(count_of_input)
            break
