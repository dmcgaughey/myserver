from flask import Flask, render_template, send_from_directory, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def route(username=None):
    return render_template('index.html',name=username)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        # print (data)
        with open('database.txt',mode='a') as file:
            file.write(f"\n{data['name']}, {data['email']}, {data['subject']}, {data['message']}")
        return  redirect('thank-you.html') #,username=data['name'])
    return 'Something went wrong'

@app.route("/<string:page_name>")
def load_page(page_name):
    return render_template(page_name)


@app.route("/favicon.ico")
def icon():
    return send_from_directory('./static/favicon.ico')