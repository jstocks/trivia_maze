import sqlite3


def get_question_count(database):
    try:
        conn = sqlite3.connect(database)
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM questions")
        count = c.fetchone()[0]
        # print(count)
        c.close()
        return count

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if conn:
            conn.close()
            # print("The Sqlite connection is closed")

def getallquestions(database):
    try:
        conn = sqlite3.connect(database)
        # to access the individual items of a row by position or keyword value.
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM questions")
        rows = c.fetchall()
        for row in rows:
            print(row["question"])
        c.close()
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if conn:
            conn.close()
            # print("The Sqlite connection is closed")

def get_q_a(database, val):
    try:
        conn = sqlite3.connect(database)
        # to access the individual items of a row by position or keyword value.
        # conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT id, question_type, question FROM questions where id=?", (val,))
        q = c.fetchone()[1:]
        c.execute("SELECT id, answer FROM answers where question_id=?", (val,))
        a = c.fetchall()
        c.execute("SELECT answer_id FROM answerkey where question_id=?", (val,))
        result = c.fetchone()[0]
        for ans in a:
            if ans[0] == result:
                correct_ans = ans[1]
        options = [elem[1] for elem in a]
        c.close()
        return [q, correct_ans, options]
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if conn:
            conn.close()
            # print("The Sqlite connection is closed")

if __name__ == '__main__':
    database = r"python_sqlite.db"
    # getallquestions(database)
    # print(get_question_count(database))
    q = get_q_a(database, 66)
    print("q: ", q)
<<<<<<< HEAD
=======
    # print(q[0], q[1], q[2])
>>>>>>> master
