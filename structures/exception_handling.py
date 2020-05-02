a = [1,2,3]

try:
    a = 6
    b = 10
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ("Value of b = ", b)
    # raising error
    raise NameError('Not found')
except (ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")
else:
    print('final')