from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App! Go to /register to register."

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get data from form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        # You can add validation or save data here
        
        # For now, we are just sending the username to the success page
        return render_template('success.html', name=username)

    # If GET request, return the registration form
    return render_template('v2.html')

if __name__ == '__main__':
    app.run(debug=True)