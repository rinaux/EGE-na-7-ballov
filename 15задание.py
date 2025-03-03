for A in range(1, 1000):
    for x in range(1, 1000):
        if (x%24==0) and (not(x%18==0) or (x%A==0)):
            break
    else:
        print(A)
