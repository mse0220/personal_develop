principal = 1000
rate      = 0.05
numyers   = 5
years     = 1
while years <= numyers:
    principal = principal * (1 + rate)
    # print(years , principal)
    # print("%3d %0.2f" %(years, principal))
    # print(format(years,"3d"),format(principal,"0.2f"))
    print("{0:3d} {1:0.2f}".format(years, principal))
    years += 1