from employee import Employee

def test_give_default_raise():
    employee = Employee('alonso', 'camarena', 50000)
    employee.give_raise()
    assert employee.annual_salary == 55000, f"Error: Expected 55000 but got {employee.annual_salary}"

def test_give_custom_raise():
    employee = Employee('alonso', 'camarena', 50000)
    employee.give_raise(10000)
    assert employee.annual_salary == 60000, f"Error: Expected 55000 but got {employee.annual_salary}"

