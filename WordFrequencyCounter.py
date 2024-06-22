def freq_counter(lst):
    dic={}
    special_chr=[",",".","/","\"","\'","{","}","(",")"]
    for el in lst:
        if el in special_chr:
            pass
        else:
            if el in dic.keys():
                dic[el]+=1
            else:
                dic[el]=1
    key_lst=dic.keys()
    print("Frequency of each word:-")
    for ky in key_lst:
        print(f"{ky} : {dic[ky]}")


text=input("Enter a sentence or a para:")
lst=text.split()
freq_counter(lst)