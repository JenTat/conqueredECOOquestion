'''
Question: Framing Squares

ICS3U: Python Part II
ECOO 2010 Boardwide

'''

sampleData = [[3, 3, 2, 4], [10, 12, 3, 6], [30, 10, 1, 4], [25, 35, 5, 0], [25, 25, 4, 8]]

for dataSet in sampleData:

    M = dataSet[0]
    N = dataSet[1]
    P = dataSet[2]
    Q = dataSet[3]

    for q in range(0, Q):
        print((2 * P + 2 * Q + N) * ("#"))

    for p in range(0, P):
        mat_w = "#" * Q
        print(mat_w + ((N + (P * 2)) * "+") + mat_w)
    
    for m in range(0, M):
        line = ""
        horizontal = "." * (N-1)
        rows = "." * (M - (M-1))
        plus_p = "+" * P
        line += mat_w
        line += plus_p
        line += horizontal
        line += rows
        line += plus_p
        line += mat_w
        print(line)

    for p in range(0, P):
        mat_w = "#" * Q
        print(mat_w + ((N + (P * 2)) * "+") + mat_w)

    for q in range(0, Q):
        print((2 * P + 2 * Q + N) * ("#"))
        
    #What is MNPQ?
    print(M, N, P, Q)
    print("\n\n")

    
