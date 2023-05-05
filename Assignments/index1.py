               # Q1 Write a program that prints a percentage marks of high school graduates by taking input of sum of their obtained marks and maximum marks.
a=input('Enter your Obtained Marks: ')
obtained=float(a)
b=input('Enter Your Maximum/Total Marks:')
totalmark=float(b)
percentage=obtained/totalmark*100
print("Your Percentage is: %.2f" % (percentage))
                    ############################QUESTION END#########################################

                              #Q2 Write a program that takes input of radius of circle and prints its circumference and area.
a=input('Enter the radius of Circle:')
r=float(a)
circumference=2*3.14*r
area=3.14*r**2
print('The Circumference of Circle is: %.2f' % (circumference))
print('The Area of the Circle is: %.2f' % (area)) 
                  ############################QUESTION END#########################################

                #Q3 Discounted selling price is to be calculated if original selling price and discount percentage is given. Write a program to 
#calculate and print discounted selling priceof the user given two inputs  1)Original selling price  2)Discounted selling price
a=input('Enter the original Selling Price:')
originalsellingprice=float(a)
b=input('Enter the discounted Selling Percentage:')
discountsellingpercentage=float(b)
discountsellingprice=originalsellingprice-(originalsellingprice*discountsellingpercentage/100)
print('The Discounted Selling Price is: %.2f' %(discountsellingprice))
                     ############################QUESTION END#########################################
  
                        #Q4 Write a program to calculate and print the original selling price if the discounted selling price and discount percentage is entered by the user.
a=input('Enter the discounted Selling Price:')
discountedsellingprice=float(a)
b=input('Enter the discounted Percentage:')
discountedpercentage=float(b)
odiscountedpercentage=100-discountedpercentage
originalsellingprice=100*discountedsellingprice/odiscountedpercentage
print('The Original Selling Price is: %.2f' %(originalsellingprice))
