
from Student import *
import sqlite3

class StudentManager(object):

    global results, con, cur
    con = sqlite3.connect("my_database.db")
    cur = con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS KIDS(NAME TEXT PRIMARY KEY,GENDER TEXT,AGE INTEGER,PARENT_NAME TEXT,"
                "TEL TEXT,ADDRESS TEXT,PAYMENT_INFO TEXT,TEACHER TEXT,MEMO TEXT)")
    con.commit()
    cur.execute("SELECT * FROM KIDS;")
    results = cur.fetchall()

    def __init__(self):
        self.student_list=[]

    def run(self):
        self.load_student()

        while True:
            self.show_menu()
            menu_number=int(input('Please input your choice:'))
            if menu_number==1:
                self.add_student()
            elif menu_number==2:
                self.del_student()
            elif menu_number==3:
                self.modify_student()
            elif menu_number==4:
                self.search_student()
            elif menu_number==5:
                self.show_allstudent()
            elif menu_number==6:
                self.save_student()
            elif menu_number==7:
                break
            else:
                print('You choose the wrong number,please try again..')
                continue
        cur.close()
        con.close()
        return

    @staticmethod
    def show_menu():
        print('Please choose from the following menu: ')
        print('1.Add a student')
        print('2.delete a student')
        print('3.Modify a student')
        print('4.Search a student information')
        print('5.print all students information')
        print('6.Save students information')
        print('7.Exit student managing system')

    def load_student(self):
        self.student_list = [Kid(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]) for i in results]
        return

    def add_student(self):
        name=input('please input kid name(format as first_name.last_name): ')
        gender=input('please input kid gender:')
        age=int(input('please input kid age: '))
        parent_name=input('please input kid parent name: ')
        tel=input('please input kid contacting number:')
        address=input('please input kid address:')
        payment_info=input('please input kid payment info:')
        teacher=input('please input kid teacher')
        memo=input('please input kid memo:')
        for i in self.student_list:
            if name==i.name:
                print('The kid is already existing!')
                return
        self.student_list.append(Kid(name,gender,age,parent_name,tel,address,payment_info,teacher,memo))
        print(f'Kid {name} has been added.')
        return



    def save_student(self):
        con.execute("delete from KIDS")
        con.commit()
        for i in self.student_list:
            con.execute("INSERT INTO KIDS(NAME,GENDER,AGE,PARENT_NAME,TEL,ADDRESS,PAYMENT_INFO,TEACHER,MEMO) "
                        "VALUES (?,?,?,?,?,?,?,?,?)",(i.name,i.gender,i.age,i.parent_name,i.tel,i.address,
                                                      i.payment_info,i.teacher,i.memo))
        con.commit()
        print("saving successful!")
        return



    def search_student(self):
        search_name=input('please input searching kid name:')
        for i in self.student_list:
            if i.name==search_name:
                print('name \t gender \t age \t parent_name \t tel \t address \t payment_info \t teacher \t memo')
                print(f'{i.name} \t {i.gender} \t {i.age} \t {i.parent_name} '
                      f'\t {i.tel} \t {i.address} \t {i.payment_info} \t {i.teacher} \t {i.memo}')
                return
        else:
            print('This kid does not exist!')
            return

    def del_student(self):
        del_name=input('please input the deleting kid name:')
        for i in self.student_list:
            if del_name==i.name:
                self.student_list.remove(i)
                print(f'Kid {del_name} has been deleted!')
                return
        else:
            print('This kid does not exist!')
            return


    def modify_student(self):

        modify_name=input('please input the modified kid name:')
        for i in self.student_list:
            if modify_name==i.name:
                i.name = input('please input kid name(format as first_name.last_name): ')
                i.gender = input('please input kid gender:')
                i.age = int(input('please input kid age: '))
                i.parent_name = input('please input kid parent name: ')
                i.tel = input('please input kid contacting number:')
                i.address = input('please input kid address:')
                i.payment_info = input('please input kid payment info:')
                i.teacher = input('please input kid teacher')
                i.memo = input('please input kid memo:')
                print(f'kid {modify_name} has been modified!')
                return
        else:
            print(f'kid {modify_name} does not exist!')
            return




    def show_allstudent(self):
        print('name \t gender \t age \t parent_name \t tel \t address \t payment_info \t teacher \t memo')
        for i in self.student_list:
            print(f'{i.name} \t {i.gender} \t {i.age} \t {i.parent_name} \t {i.tel} \t {i.address} \t {i.payment_info}'
                  f' \t {i.teacher} \t {i.memo}')






