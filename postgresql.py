import psycopg2


if __name__ == "__main__":
    uri = "postgresql://worker:secret@localhost:5432/superblog"
    with psycopg2.connect(uri) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """)
        cursor.execute("""
            INSERT INTO users (username, password, email)
            VALUES
                ('user1', 'password1', 'user1@example.com'),
                ('user2', 'password2', 'user2@example.com'),
                ('user3', 'password3', 'user3@example.com'),
                ('user4', 'password4', 'user4@example.com'),
                ('user5', 'password5', 'user5@example.com'),
                ('user6', 'password6', 'user6@example.com'),
                ('user7', 'password7', 'user7@example.com'),
                ('user8', 'password8', 'user8@example.com'),
                ('user9', 'password9', 'user9@example.com'),
                ('user10', 'password10', 'user10@example.com');
        """)
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)