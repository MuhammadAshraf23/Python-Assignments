a=input('Enter the original Selling Price:')
originalsellingprice=float(a)
b=input('Enter the discounted Selling Percentage:')
discountsellingpercentage=float(b)
discountsellingprice=originalsellingprice-(originalsellingprice*discountsellingpercentage/100)
print('The Discounted Selling Price is: %.2f' %(discountsellingprice))
