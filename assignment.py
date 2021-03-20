#High Peak Software Pvt.ltd
#Assignment Solution by DON CHRISTY MATHEW
 #open input file to read input
in_file =open("input.txt","r")
#open output file to write output
out_file = open("output.txt","w+")
products={}
out_list=[]
#reading the sample input file 
for f in in_file:
    Read_sample_price=f.index(":")
    print(f[Read_sample_price+1:].strip())
    print(f[:Read_sample_price])
    products[f[:Read_sample_price]]=f[Read_sample_price+1:].strip()
print(products) 
price_of_products=list(products.values())


price_of_products=[int(i)for i in price_of_products]
#sorted list in decsending order to get prices to be distributed in order
price_of_products.sort(reverse=True)
print(price_of_products)
#taking the inputs of employees details
num_of_employees=int(input("Enter number of employees: "))
leng=(len(price_of_products)-num_of_employees)

print(leng)

#finding minimum difference between highest and lowest
for i in range(leng):
    max_price=price_of_products[i]
    min_price=price_of_products[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        index_taken=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        index_taken=i

choosen_prices=price_of_products[index_taken:num_of_employees+index_taken]
#differnce between high and low price
diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

content=0
for key,value in products.items():
    price_of_products[content]
    print(value)
    if int(value)in choosen_prices and content<num_of_employees:
        str1=key+": "+value
        #preparing  list for output
        out_list.append(str1)
        content+=1
        print(str1)
#writing to output file
out_file.write("The goodies selected for employees distribution are : ")

out_file.write("\n")

for i in out_list:
    out_file.write(i)
    out_file.write("\n")
out_file.write("The difference between the chosen goodie with highest price and the lowest price is "+str(diff))

in_file.close()
out_file.close()
