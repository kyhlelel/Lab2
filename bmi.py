def calculate_bmi(height, weight):
    
    bmi = weight / height**2
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(bmi))
    if bmi<18.5 :
        print("Under weight")
    elif 18.5<=bmi<25.0 :
        print("Normal weight")
    else :  
        print("Overweight")
     
    
calculate_bmi(weight=57, height=1.73)

