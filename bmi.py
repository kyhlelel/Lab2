def calculate_bmi(height, weight):
    
    bmi = weight / height**2
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(bmi))
    if bmi<18.5 :
        print("Under weight")
        return -1
    elif 18.5<=bmi<25.0 :
        print("Normal weight")
        return 0
    else :  
        print("Overweight")
        return 1
     
    
calculate_bmi(weight=74, height=1.73)

