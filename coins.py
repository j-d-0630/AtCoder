def price_calc(a,b,c):
    price_list = []
    for i in range(0,a+1):
        for j in range(0,b+1):
            for k in range(0,c+1):
                price = i*500 + j*100 + k*50
                price_list.append(price)
    
    return price_list


def count(price_list,X):
    count = 0
    for price in price_list:
        if price == X:
            count += 1
    
    return count



A = int(input())
B = int(input())
C = int(input())
X = int(input())

price_list = price_calc(A,B,C)
ans = count(price_list,X)
print(ans)