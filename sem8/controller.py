import view
import add_students
import add_perfomance


def button():
    lst_names = []
    lst_subj = []
    lst = []
    flag = True
    while flag == True:
        a = view.viewer()
        if a == 1:
            lst_names.append(add_students.st_name())
            # lst_subj.append(add_students.st_subjects())

        if a == 2:
            lst_subj.append(add_students.st_subjects())

        if a == 3:
            pass
        if a == 4:
            print(lst_names,lst_subj)
        if a == 5:
            flag = False



        

button()