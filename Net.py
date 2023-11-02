import pymysql

# Replace with your database connection information
host = "your-rds-endpoint.rds.amazonaws.com"
user = "admin"
database = "vehicleTelematicsDB"
password = "Admintelematics123#"

try:
    # Establish a connection to the database
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    print("Connected to the database successfully")

    # Close the database connection
    connection.close()
except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")
