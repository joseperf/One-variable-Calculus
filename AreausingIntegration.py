from scipy.integrate import quad

# Function definition
def f(x):
    return (1 - x**2) ** 0.5 # Function

print ("Area is :",quad(f,0,1)[0])
