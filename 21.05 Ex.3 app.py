
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
participants = []

@app.route('/event_register', methods=['GET', 'POST'])
def event_register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        time = request.form.get('time')

        if not name or not email or not time:
            error = 'Please fill in all fields.'
            return render_template('event_register.html', error=error)

        participants.append({'name': name, 'email': email, 'time': time})
        return redirect(url_for('show_participants'))

    return render_template('event_register.html')

@app.route('/participants')
def show_participants():
    return render_template('participants.html', participants=participants)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
