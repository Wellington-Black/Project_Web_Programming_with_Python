from flask import Flask, render_template

from controllers.attendance_controller import attendances_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(attendances_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

