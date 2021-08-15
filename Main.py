import sqlite3
import names
import random
from utilities import generateEmail, getDate

count = 1
amount = 2001

conn = sqlite3.connect('employees.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS employees(ID INT, name VARCHAR(40), email VARCHAR(25), salary INT, gender VARCHAR(6), hire_date VARCHAR(10))')
conn.commit()


while count < amount:
    fullName = names.get_full_name()
    c.execute("SELECT * FROM employees")
    c.execute(f"INSERT INTO employees(ID, NAME, EMAIL, SALARY, GENDER, HIRE_DATE) VALUES({count}, \'{fullName}\', \'{generateEmail(fullName)}\', {random.randint(23000, 150000)}, \'{random.choice(['male', 'female'])}\', \'{getDate()}\')")
    count += 1
    conn.commit()

c.close()
conn.close()