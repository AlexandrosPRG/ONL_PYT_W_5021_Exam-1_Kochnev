from flask import Flask, request, render_template_string
import psycopg2

# CREATE DATABASE exam1

app = Flask(__name__)

# HTML form
form_html = '''
    <h2>Register Reader</h2>
    {% if error %}<p style="color:red">{{ error }}</p>{% endif %}
    <form method="post">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br><br>
        <input type="submit" value="Register">
    </form>
'''

# Připojení k databázi
def connect_db():
    return psycopg2.connect(
        user="postgres",
        host="localhost",
        password="admin12345",
        port=5553,
        database="exam1"
    )

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        # Validace vstupu
        if not name:
            return render_template_string(form_html, error="Name cannot be empty.")
        if "@" not in email:
            return render_template_string(form_html, error="Email must contain '@'.")

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO Readers (name, email)
                VALUES (%s, %s)
            """, (name, email))
            conn.commit()
            cur.close()
            conn.close()
            return f"<h3>Reader {name} registered successfully.</h3>"
        except Exception as e:
            return render_template_string(form_html, error="Database error: " + str(e))

    # GET metod
    return render_template_string(form_html, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5553)
