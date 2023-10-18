def find():

    A = list(map(int,input('Enter a list: ').split()))

    element = int(input('Enter an element: '))
    print(A)

    for x in range(len(A)):

        if A[x] == element:

            print (A[x-1])
            print (A[x+1])

    return A


find()