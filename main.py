import numpy as np

a = int(input(""))

b = []

c = []
for i in range(a):
    # N
    b.append(input(""))
    # H
    c.append(input(""))

out2 = []

for i in range(a):
    #     print("i=")
    #     print(i)
    bb = []
    bb3 = []
    bb2 = []
    bb4 = []
    k1 = int(b[i])
    #     print("k1=")
    #     print(k1)
    if (k1 % 2) == 0:
        out2.append(False)
    else:
        k2 = (k1 + 1) / 2
        #         print("k2=")
        #         print(k2)

        if k1 == 1:
            out2.append(k1 == np.array(c[i]))
        else:
            bb = np.array(range(int(k2))) + 1
            #             print(bb)
            bb3 = np.array(range(int(k2) - 1)) + 1
            #             print(bb3)
            bb2 = bb3[::-1]
            #             print(bb2)

            bb4 = np.concatenate((bb, bb2), axis=0)
            out2.append(np.array_equal(bb4, np.array([int(x) for x in c[i].split(' ')])))
#             print(bb4)
#             print(np.array([int(x) for x in  c[i].split(' ')]))
#             print(np.array(c[i].split(' ')))
#             print(np.array_equal(bb4,np.array([int(x) for x in  c[i].split(' ')])))


for i in range(a):
    if out2[i]:
        print("yes")
    else:
        print("no")
