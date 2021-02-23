import sqlite3
from sqlite3 import Error
import csv

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    database = r"python_sqlite.db"
    sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS questions (
                                        id integer PRIMARY KEY,
                                        question_type text NOT NULL,
                                        question text NOT NULL
                                    ); """

    sql_create_answers_table = """CREATE TABLE IF NOT EXISTS answers(
                                        id integer PRIMARY KEY,
                                        answer text,
                                        question_id integer NOT NULL,
                                        FOREIGN KEY (question_id) REFERENCES questions (id)
                                    );"""

    sql_create_answerkey_table = """CREATE TABLE IF NOT EXISTS answerkey(
                                        question_id integer NOT NULL,
                                        answer_id integer NOT NULL,
                                        FOREIGN KEY (question_id) REFERENCES questions (id),
                                        FOREIGN KEY (answer_id) REFERENCES answers (id),
                                        PRIMARY KEY (question_id, answer_id)
                                    );"""

    # create a database connection
    conn = create_connection(database)
    c = conn.cursor()
    # create tables
    if conn is not None:
        # create questions table in database
        create_table(conn, sql_create_questions_table)
        # create answers table in database
        create_table(conn, sql_create_answers_table)
        create_table(conn, sql_create_answerkey_table)
    else:
        print("Error! cannot create the database connection.")

    # insert data from csv file to the tables in the database.
    with open('question_bank.csv', 'r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin)  # comma is default delimiter
        # q_to_db = [(i["TYPE"], i[" Question"]) for i in dr]
        # q_to_ans = [(i[" Correct Answer"], i[" Option1"], i[" Option2"], i[" Option3"]) for i in dr]
        for i in dr:
            c.execute("INSERT INTO questions(question_type,question) VALUES(?, ?)", (i["TYPE"], i[" Question"]))
            q_id = c.lastrowid
            c.execute("INSERT INTO answers(answer,question_id) VALUES(?, ?)", (i[" Correct Answer"], q_id))
            a_id = c.lastrowid
            c.execute("INSERT INTO answers(answer,question_id) VALUES(?, ?)", (i[" Option1"], q_id))
            c.execute("INSERT INTO answers(answer,question_id) VALUES(?, ?)", (i[" Option2"], q_id))
            c.execute("INSERT INTO answers(answer,question_id) VALUES(?, ?)", (i[" Option3"], q_id))
            c.execute("INSERT INTO answerkey(question_id,answer_id) VALUES(?, ?)", (q_id, a_id))

    conn.commit()
    conn.close()