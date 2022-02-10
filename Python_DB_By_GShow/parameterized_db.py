# Parameterized in mysql:
# A parameterized query is query that is used for the format or pyformat parameterization 
# style for parameters and the parameter values supplied at execution.
# These executed with MYSQLCursor can use the '%s' and %(key)s format style.
# '%s' is used as format style in the sql query, while using tuple parameters.
# '%(key)s' is used as format style in the sql query, while using the dictionay parameters.

# sql 1.0.0

# example with '%s' as tuple format.

# sql = "insert into stundet(sid, name, roll_no, fees) values(%s, %s, %s, %s)"
# cusrsor = con.cursor()
# cursor.execute(sql, (1,'abhi',101,5000))

# or:

# sql = "insert into stundet(sid, name, roll_no, fees) values(%s, %s, %s, %s)"
# cusrsor = con.cursor()
# records = [
        #     (4, 'Sumit kumar', '104', '5000'),
        #     (5, 'Jitu', '105', '4000'),
        #     (6, 'Monu', '106', '6000'),
        # ]
# cursor.executemany(sql, records)

# sql 1.0.1

# example with '%(key)s' as dictionary format.

# sql = "insert into stundet(sid, name, roll_no, fees) values(%(sid)s, %(name)s, %(roll_no)s, %(fees)s)"
# cusrsor = con.cursor()
# cursor.execute(sql, {'sid': 1, 'name': 'abhi', 'roll_no': 101, 'fees':5000})

# or:

# sql = "insert into stundet(sid, name, roll_no, fees) values(%s, %s, %s, %s)"
# cusrsor = con.cursor()
# records = {'sid': 1, 'name': 'abhi', 'roll_no': 101, 'fees':5000}
# cursor.execute(sql, records)
