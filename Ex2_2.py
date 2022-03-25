"""Practice using the Python interpreter as a calculator:"""

#The volume of a sphere whit radius r is (4/3)*(pi)*(r**3). What is the volume of a sphere with radius 5?
import math
(4/3)*math.pi*(5**3) #523.598775 is the volume of a sphere with radius 5

#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#Shipping costs $3 for the first copy and 75 cent for each additional copy.
#What is the total wholesale cost for 60 copies?

24.95 / 100 * 60 #$14.97 discounted price
(14.97 + 3) + (14.97 + 0.75) * 59 #945.45 is the total wholesale cost for 60 copies

#If i leave at 6:52 and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
#and 1 mile at easy pace again, what time do i get home for breakfat?

(8.15 * 2) + (7.12 * 3) #37:66 -> 38:06 i get home at 7:30:06
