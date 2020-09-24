def gloves(ar, n):
    count = 0
    ar.sort()
    i = 0
    while i < (n-1):
        if (ar[i] == ar[i + 1]):
            count += 1
            i = i + 2
        else:
            i += 1
            
    return count


ar = [60, 20, 20, 10, 10, 30, 10, 30, 60, 10]
n= len(ar)
print(gloves(ar, n))


