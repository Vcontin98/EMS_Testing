from employee_management import Employee, Manager, Supervisor 

#instanciating our Classes
employee = Employee("hello","bye")
employee2 = Employee("bye","bye")
employee3 = Employee("test","bye")
employee4 = Employee("shawn","micheal")
manager = Manager("bobby","lee")
supervisor = Supervisor("sinc","cake")

#testing add employee method
manager.add_employee(employee)
manager.add_employee(employee2)
manager.add_employee(employee3)
#supervisor add employee since it inherits from 
supervisor.add_employee(employee4)

#testing if employee show 
print(manager.show_employees())
print(supervisor.show_employees())

#test removing method
manager.remove_employee("hellob@codingtemple.com")
supervisor.remove_employee("shawnm@codingtemple.com")
print(manager.show_employees())

#Testing get email method
employee.create_post()

#testing grab employee email
print(employee.get_employee_by_email("hellob@codingtemple.com"))

# manager cant post fix
manager.create_post()
supervisor.create_post()






