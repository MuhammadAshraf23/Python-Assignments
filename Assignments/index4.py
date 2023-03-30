a=input('Enter the discounted Selling Price:')
discountedsellingprice=float(a)
b=input('Enter the discounted Percentage:')
discountedpercentage=float(b)
odiscountedpercentage=100-discountedpercentage
originalsellingprice=100*discountedsellingprice/odiscountedpercentage
print('The Original Selling Price is: %.2f' %(originalsellingprice))
