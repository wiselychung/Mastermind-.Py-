import random


def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    list3 = list(dict.fromkeys(list3))
    return list3


def print_instruc():
    print("**INSTRUCTIONS** ")
    print("")
    print("The codebreaker attempts to guess the pattern in both order and color within 10 turns")
    print("Each guess is made by placing a row of code pegs on the decoding board.")
    print("Once placed, the codemaker provides feedback by placing black and white pegs")
    print("black pegs denoting correct position and color, while white pegs denotes correct color but wrong position")
    print("Colors: ")
    print("")
    print("R - red, G - green, Y - yellow")
    print("B - blue, V - violet, P - pink")
    print("")


pegs = ["R", "G", "Y", "B", "V", "P"]       # pegs array list
checker = ["BL", "WH"]                      # checker array list
i = 1                                       # while loop iteration
bcheck = 0                                  # correct color && correct position
wcheck = 0                                  # correct color but wrong position

Question = pegs[random.randint(0, 5)]
Question1 = pegs[random.randint(0, 5)]
Question2 = pegs[random.randint(0, 5)]
Question3 = pegs[random.randint(0, 5)]

print_instruc()

Q = [Question, Question1, Question2, Question3]
# print(Q)

print("[x]   [x]   [x]   [x]")

while i != 11:
    ans, ans1, ans2, ans3 = input("Enter guess " + str(i) + ": ").split()
    if ans.upper() != Question or ans1.upper() != Question1 or ans2.upper() != Question2 or ans3.upper() != Question3:
        A = [ans.upper(), ans1.upper(), ans2.upper(), ans3.upper()]
        i += 1
        wcheck = len(intersection(A, Q))
        if A[0] == Q[0]:
            bcheck += 1
            wcheck -= 1
        if A[1] == Q[1]:
            bcheck += 1
            wcheck -= 1
        if A[2] == Q[2]:
            bcheck += 1
            wcheck -= 1
        if A[3] == Q[3]:
            bcheck += 1
            wcheck -= 1
        if wcheck < 0:
            wcheck = 0
        print("white pegs: " + str(wcheck) + " black pegs: " + str(bcheck))
        bcheck = 0
        wcheck = 0
        if i == 11 and A != Q:
            print("You Lose")

    elif ans.upper() == Question and ans1.upper() == Question1 and ans2.upper() == Question2 and ans3.upper() == Question3:
        print("You win")
        i = 11
