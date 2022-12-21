import pyodbc


def Table():
    connect = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL"
                             " Server};SERVER=LAPTOP-G1C1N8VG;"
                             "DATABASE=Game;"
                             "Trusted_Connection=yes")
    # query = "CREATE TABLE English_Questions(ID int primary key, Question varchar(200), True varchar(60)," \
    #         "False varchar(60), Answer varchar(50)) "
    # cursor = connect.cursor()
    # cursor.execute(query)
    # connect.commit()


Table()


def Question_input():
    connect = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL"
                             " Server};SERVER=LAPTOP-G1C1N8VG;"
                             "DATABASE=Game;"
                             "Trusted_Connection=yes")

    cursor = connect.cursor()
    ID = (input("ID Number:"))
    Question1 = input("Question?:")
    A = input("Option A:")
    B = input("Option B:")
    C = input("Option C:")
    D = input("Option D:")
    Answer = input("The Answer is:")
    cursor.execute("INSERT Maths_Questions(ID,Question,A,B,C,D,Answer)"
                   "VALUES(?,?,?,?,?,?,?)", (ID, Question1, A, B, C, D, Answer))
    connect.commit()


Question_input()
