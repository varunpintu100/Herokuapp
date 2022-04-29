import sqlite3

from flask_restful import Resource,reqparse


class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        #this query selects all the fields with the username that we pass in 
        query = "SELECT * FROM users WHERE username=?"
        
        #data we pass must always be in the form of a tuple and , is for sure as we need to specify that we are passing in the tuple
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        #this verifies that the row has some value
        if row:
            #we have used cls(*row) as that assigns the values respectively instead of cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None
            
        connection.close()
        
        return user
    
    @classmethod
    def find_by_id(cls,user_id):
        #this is used to create a connection for the database
        connection = sqlite3.connect('data.db')
        
        #this is for the cursor connection
        cursor = connection.cursor()
        
        #this is the query used to select the data we require
        query = "SELECT * FROM users WHERE id=?"
        
        #this is used to store the data when executed with the requirement
        result = cursor.execute(query,(user_id,))
        
        #this fetches the first row
        row = result.fetchone()
        
        #this is used to check that we wont return any empty data
        if row:
            user = cls(*row)
        
        else:
            user = None
        
        return user
        
        
class UserRegister(Resource):
    parser = reqparse.RequestParser()
        
    #this parser will parse through json of the request and make sure that the field is present
    parser.add_argument('username',type=str,required=True,help="This field cannot be blank")
        
    #this parser will parse through json of the request and make sure that the field is present
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")
    
    def post(self):
        
        #this is used to get the parsed arguments to one place 
        data = UserRegister.parser.parse_args()
        
        #we will use the function already present in user class
        if User.find_by_username(data['username']):
            return {"message":"A user with the uesrname already exists."},400
        
        connection = sqlite3.connect('data.db')
        
        cursor = connection.cursor()
        
        #this query is used to get the data and if data exists them it returns 1 and if no then 0
        #find_query = "SELECT EXISTS(SELECT * from users WHERE username=?)"
        

        query = 'INSERT INTO users VALUES(NULL,?,?)'
        
        cursor.execute(query,(data['username'],data['password'],))
        
        connection.commit()
        
        connection.close()
        
        return {"message" : "User created sucessfully"},201
        
        
        
        