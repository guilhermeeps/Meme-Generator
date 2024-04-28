from flask import Flask, render_template
import requests, mysql.connector

mydb = mysql.connector.connect (
    host='172.17.0.2',
    user='teste',
    password='teste',
    database='Memegeneratordb',
)

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url).json();
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    image_url = response["url"]
    
    # SQL command to insert data on db
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO memes (image_url) VALUES ('{image_url}')"
    my_cursor.execute(sql)
    mydb.commit()

    return meme_large, subreddit


def display_meme_table():
    # Commands to catch all data from the database
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM memes')
    memes_table = my_cursor.fetchall()

    # Generate HTML table
    html_table = "<table border='1'><tr><th>ID</th><th>Meme Image</th><th>Created At</th></tr>"
    for row in memes_table:
        html_table += "<tr>"
        for col in row:
            html_table += "<td>{}</td>".format(col)
        html_table += "</tr>"
    html_table += "</table>"

    return html_table


@app.route("/")
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


@app.route("/history")
def history():
    html_table = display_meme_table()
    return render_template("history.html", html_table=html_table)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)