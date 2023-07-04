from flask import Flask, render_template, request

app = Flask(__name__)

data = {}


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return f"Entry '{key}: {value}' created successfully!"
    return render_template('create.html')


@app.route('/read')
def read():
    return render_template('read.html', data=data)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
            return f"Entry '{key}' updated successfully!"
        else:
            return f"Entry '{key}' does not exist."
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return f"Entry '{key}' deleted successfully!"
        else:
            return f"Entry '{key}' does not exist."
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)