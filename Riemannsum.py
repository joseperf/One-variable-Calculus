
#Function definition
def f(x):
    return (1 - x**2) ** 0.5 # Function

#Inputs
lower = 0
upper = 1
subinterval1 = 100
subinterval2 = 1000
subinterval3 = 10000

#Calculating area
def Riemannsum(a,b,n):
    deltax = (b-a)/n
    area = 0
    while a < b:
        area =  area + (f(a) * deltax)
        a = a + deltax
    return area

#Outputs
area = Riemannsum(lower,upper,subinterval1)
print("For 100 interval size, area = :", area)
area = Riemannsum(lower,upper,subinterval2)
print("For 1000 interval size, area = :", area)
area = Riemannsum(lower,upper,subinterval3)
print("For 10000 interval size, area = :", area)




