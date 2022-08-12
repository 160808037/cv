import mysql.connector
import pandas as pd
import streamlit as st

# Connect to server
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="160808037A",
    database="monkey")

# Get a cursor

# Execute a query
mycursor = conn.cursor()

# mycursor.execute("SELECT * FROM Employee WHERE Branch_id = 2;")
mycursor.execute("SELECT * FROM Employee WHERE Branch_id = 2;")

# iterate over the result
for row in mycursor:
    print(row)
query1 = pd.read_sql('SELECT * FROM Employee;' , conn)
st.header('Employees table')
query1
st.header('Distribution of the employees salary')
st.line_chart(query1.Salary)



for row in mycursor:
    print(row)
query5 = pd.read_sql('SELECT COUNT(Sex) AS TOTAL,Sex FROM Employee GROUP BY Sex;' , conn)
st.header('Distribution of the employees genders')
query5
st.bar_chart(query5.TOTAL)


for row in mycursor:
    print(row)
query2 = pd.read_sql('SELECT * FROM Employee WHERE Branch_id = 2;' , conn)
st.header('Employees with branch id 2')
query2
for row in mycursor:
    print(row)
query3 = pd.read_sql('SELECT * FROM Client;' , conn)
st.header('Clients table')
query3



for row in mycursor:
    print(row)
query0 = pd.read_sql('SELECT SUM(Total_Sales), Emp_Id FROM Works_With GROUP BY Emp_id;' , conn)
query0
st.header('Employees with the most sales to clients')
st.bar_chart(query0)



# we close the cursor and conn both
# mycursor.close()
# conn.close()

