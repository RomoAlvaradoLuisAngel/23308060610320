from flask import Flask, render_template, url_for, request, redirect

app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/clasificar_macro')
def clasi():
    return render_template('clasificar_macro.html')


if __name__ == "__main__":
    app.run(debug=True)