def adding():

    A = list(map(int,input('Enter a list: ').split()))

    print(A)

    for x in range(len(A)):

        if x % 2!=0:

            A.append(A[x])

    print(A)

    return A

adding()