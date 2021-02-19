import the random generator library
import random
#create random name stream
names = ["tonya","william", "samuel", "matt", "johnny", "cage", "lucas","will","jake","mary","olivia", "mike","rice","indigo","justin","blake", "red","black","lucas","tran","alex","judy","alex","violet","singh","khan","daniella","bruce","kent","leon"]
max_employees = 10
#create a random first and last name duo
def random_name():
    return f"{random.choice(names)} {random.choice(names)}"
def random_salary():
    return random.random() * 10000 + 1000
class employee:
    def __init__(self):
        self.name = random_name()
        self.salary = random_salary()
    def __str__(self):
        return "This employees name is " + self.name + "\nThis employees salary is $"+ str(self.salary)+"\n"

def find_2nd_highest( arr):
    max = arr[0]
    sec_max = arr[0]
    min = arr[0]
    #although this formula seems a little bit wasteful, it actually computes in 2n, which is approximately O(n), when compared to a quicksort or
    #mergesort method, this would perform a little bit better. NOTE, this only works because we know we are searching for 2nd highest, in a scenerio
    #where we want to find nth index, merge or quick sort would be alot better because they have a computational speed of O(nlogn).
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    sec_max = min
    for i in arr:
    
        if i > sec_max and i < max:
            sec_max = i
    return sec_max
        
if __name__ == "__main__":
    emp_arr = []
    emp_salary = []
    for i in range(max_employees):
        emp = employee()
        emp_arr.append(emp)
        print(emp)
        emp_salary.append(emp.salary)
    sec_max = find_2nd_highest( emp_salary)
    print(sec_max)
        
    