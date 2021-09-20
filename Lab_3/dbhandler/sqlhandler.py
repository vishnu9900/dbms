import mysql.connector
class Mysqlhandler:
    
    
    def add_user():
        cnm=mysql.connector.connect(user='root',password="Mahindra@99",database= 'UserDB')
        cursor=cnm.cursor()

        query=("insert into user_data values('Vishnu',1,'2001-06-09')")
        
        cursor.execute(query)
        cnm.commit()

    def update_user():
        cnm=mysql.connector.connect(user='root',password="Mahindra@99",database= 'UserDB')
        cursor=cnm.cursor()

        query=("update user_data setphno=5 where name ='nikl'")

        cursor.execute(query)
        cnm.commit()


    def delete_user():
        cnm=sql.connector.connect(user='root',password="Mahindra@99",database='UserDB')
        cursor=cnm.cursor()

        query=("delete from user_data where name = 'Vishnu'")

        cursor.execute(query)
        cnm.commit()

    def display_users():
        cnm=mysql.connector.connect(user='root',password="Mahindra@99",database= 'UserDB')
        cursor=cnm.cursor()

        query=("select * FROM user_data")
        cursor.execute(query)            
