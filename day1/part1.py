i = '''hcpjssql4kjhbcqzkvr2fivebpllzqbkhg
4threethreegctxg3dmbm1
1lxk2hfmcgxtmps89mdvkl
''' 

j = i.split()
ans = 0 
for k in j:
    ans2 = 0
    z = k[::-1]
    for l in k:       
        if  l.isnumeric():
            ans2 = 10 * int(l)
            break

    for l in z:       
        if  l.isnumeric():
            ans2 += int(l)
            break    
    ans += ans2
print(ans)