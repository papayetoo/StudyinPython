bin_str = bin(6)[2:]
combination_length = 2
for i in range(len(bin_str)-combination_length+1):
    print(i)
    bin_str = [x for x in bin_str]
    bin_str[i+1] = '1'
    print(bin_str)
    for j in range(i+1, len(bin_str)-1):
        bin_str[j], bin_str[j+1] = '0', '1'
        print(''.join(bin_str))
    bin_str[j+1] ='0'
    bin_str[i], bin_str[i+1] = '0', '1'