def is_right_angled(a, b, c):
    lst = [a, b, c]
    lst.sort()

    if lst[2]**2 == (lst[0]**2 + lst[1]**2):
        print("Is Right Angled")
    else:
        print("Is Not Right Angled")

s1 = int(input("Enter first side: "))
s2 = int(input("Enter second side: "))
s3 = int(input("Enter third side: "))

is_right_angled(s1, s2, s3)