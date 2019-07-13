
def is_armstrong_number(number):
    
    num_list = [int(x) for x in str(number)]
    count_list = len(num_list)
    power_list = [x**count_list for x in num_list]
    sum_power_list = sum(power_list)
    if sum_power_list == number:
        return True
    else:
        return False
        
