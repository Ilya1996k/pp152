n=0
k=0
for a1 in 'авиортф':
    for a2 in 'авиортф':
        for a3 in 'авиортф':
            for a4 in 'авиортф':
                for a5 in 'авиортф':
                    for a6 in 'авиортф':
                        for a7 in 'авиортф':
                            s=a1+a2+a3+a4+a5+a6+a7
                            n += 1
                            if n%2!=0 and 'трио' in s[1:-1]:
                                k+=1

print(k)
