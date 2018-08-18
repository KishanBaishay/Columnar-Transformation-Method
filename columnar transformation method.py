# Encryption using Columnar Transformation Method
plain_text=input("Enter the plain text:")
keyword=input("Enter the keyword:")
list1=[]
list2=[]
plain_text=plain_text.replace(' ','')
list1=list(plain_text)

length=len(list1)
len_keyword=len(keyword)

cols=len_keyword                    # Finding rows and columns
rows=0
for j in range(1,len_keyword+1):
    if (cols*j)>=length:
        rows=j
        break
    
diff=(rows*cols)-length

for i in range(diff):               # Addition of refernce element 'x'
    list1.append('x')

list3=[]
keyword=keyword.lower()
for i in range(len_keyword):
    list3.append(ord(keyword[i]))

position=[]
for i in range(len_keyword):        # Finding of index of smallest element in keyword
    element=min(list3)
    for j in range(len_keyword):
        if list3[j]==element:
            break
    position.append(j)
    list3[j]=130

final_list=[]
for i in range(cols):               # Encrypting phase
    k=position[i]
    for j in range(rows):
        final_list.append(list1[k])
        k=k+len_keyword
        
cipher_text=('').join(final_list)
print("Cipher Text is :",cipher_text)


# Decryption for above gained Cipher Text
list4=list(cipher_text)
list5=[]
for i in range(rows*cols):
    list5.append(i)
p=0

for i in range(cols):        # Decrypting phase
    k=position[i]
    for j in range(rows):
        m=list4[p]
        list5[k]=m
        p=p+1
        k=k+cols
   
cnt=list5.count('x')

for i in range(cnt):                # Removing 'x' which is add as the reference
    if 'x' in list5:
        list5.remove('x')

plain_text=('').join(list5)
print("Plain Text is : ",plain_text) 



    
