import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user_signin.html')

@app.route('/signup')
def signup():
    return render_template('user_signup.html')

@app.route('/signup_reg', methods=['POST'])
def signup_reg():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Here, you can insert the data into your database (as shown in the previous response)
        # Example: insert_user(username, email, password)

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='chestxpertise.cef8hjcpzbou.us-east-2.rds.amazonaws.com',
            user='admin',
            password='ChestXPertise?',
            database='ChestXP'
        )

        create_table_query = create_table_sql = '''
        CREATE TABLE IF NOT EXISTS user_signup (
            user_id INTEGER PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        );
        '''

        cursor = connection.cursor()

        check_table_query = f"SHOW TABLES LIKE '{'user_signup'}'"

        cursor.execute(check_table_query)

        result=cursor.fetchone()

        if not result:
            cursor.execute(create_table_query)

        insert_query = "INSERT INTO user_signup (username, email, password) VALUES (%s, %s, %s)"

        values=(username,email,password)

        cursor.execute(insert_query,values)
    
        # Close the database connection when done
        cursor.close()
        connection.close()


        # For simplicity, let's just print the data for demonstration
        print(f"Username: {username}, Email: {email}, Password: {password}")

        # You can redirect the user to a success page or perform other actions here

    return "Sign-up successful!"

if __name__ == '__main__':
    app.run(debug=True)
