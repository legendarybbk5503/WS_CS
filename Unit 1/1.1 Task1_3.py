Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [ 5,  8,  3,  6]
Outlet3Sales = [10, 12, 15, 10]

total = []

for i in range(4):
    temp = 0
    temp += Outlet1Sales[i]
    temp += Outlet2Sales[i]
    temp += Outlet3Sales[i]
    total.append(temp)

for i in range(4):
    print(f"Total for quarter {i+1}: {total[i]}")