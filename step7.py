import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail I'd"])

        writer.writerow(info_list)

if __name__ == '__main__':     #this the the main() function of the program! the code will strat from the 1st line of the main function
    
    condition = True
    student_num = 1

    while(condition):
        student_info = input("\nEnter student information of student #{} in the following format - Name  Age  Contact_number  E-mail_id: ".format(student_num))
        
        student_info_list = student_info.split(' ')

        print("\n The entered information is :- \n Name: {}\n Age:{}\n Contact number: {}\n E-mail id: {}\n"
                .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("\nEnter (yes/no) if you want to enter information for another student: ")
            
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
            else:
                print("\nPlease rewrite your information!")
                choice_func(condition_check)

        elif choice_check == "no":
            print("\nPlease re - enter the values!")

        else:
                print("\nPlease rewrite your information!")
