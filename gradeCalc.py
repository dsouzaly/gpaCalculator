import math;
"What grade do I currently have"
def gpa2(grade):
    if grade >= 85:
        gpa = "4.0"
    elif grade >= 80:
        gpa = "3.7"
    elif grade >= 77:
        gpa = '3.3'
    elif grade >=  73:
        gpa = '3.0'
    elif grade >=  70:
        gpa = '2.7'
    elif grade >= 67:
        gpa = '2.3'
    elif grade >= 63:
        gpa = '2.0'
    elif grade >= 60:
        gpa = '1.7'
    elif grade >= 57:
        gpa = '1.3'
    elif grade >= 57:
        gpa = '1.0'
    elif grade >= 50:
        gpa = '.7'
    else:
        gpa = 'Step your damn game up'    
    return gpa

def tell_me():
    current_grade = 0
    total_weight = 0
    more = 'y'
    gpa = 0
    
    while more != 'n':
        mark = float(input("Input your mark: "))
        out_of = float(input("Input total marks: "))
        grade = mark/out_of
        weight = float(input("Input the weight (percent): "))
        more = input("more (y/n): ")
        current_grade += grade*weight
        total_weight += weight
    current_grade = round(current_grade,2)
    total_weight = round(total_weight,2)
    gpa = gpa2(round(100*current_grade/total_weight))

    
    print("Your current gpa: " + gpa)
    print("Your current percent: " + str(round(100*current_grade/total_weight,2)))
    print("You have earned " + str(current_grade) + "/" + str(total_weight) + " of the marks awarded.")
  
    best_grade = 100 - total_weight + current_grade
    gpa = gpa2(best_grade)
    
    print("your best possible percent: " + str(best_grade))
    print("your best possible gpa: " + gpa)

    more = 'y'
    while more != 'n':
        mark = float(input("What do you want in the course (percent): "))
        avg = round(100*(mark - current_grade)/(100-total_weight),2)
        print("You need to get a " + str(avg) + "% from now on")
        more = input("more (y/n)")
        
tell_me()
