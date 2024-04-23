
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    print("Temperature list: ", numlist)
    sort_temperature(numlist)
    resultmin, resultmax = find_min_max(numlist)
    print("Lowest temparature: ", resultmin)
    print("Highest temperature: ", resultmax)
    #calc_median_temp()
    
    average_temp = calc_average(numlist)
    print("This is your average temperature: ", average_temp)

#def calc_median_temp():

def find_min_max(numlist3):
    minval = min(numlist3)
    maxval = max(numlist3)
    return minval, maxval
      
def sort_temperature(numlist2):
    numlist2.sort()
    print("Ascending list: ", numlist2)
    return
    
def display_main_menu():
    print("Enter temperature SEPARATED BY COMMAS (e.g. 5, 67, 32)")
    
def calc_average(numlist1):
    total_temp = sum(numlist1)
    average_temp = total_temp / len(numlist1)
    return average_temp
    
def get_user_input():
    n_string = input("Enter here: ")
    n_list =  n_string.split(",") 
    numlist = [float(x) for x in n_list]
    return numlist 

if __name__ == "__main__":
    main()