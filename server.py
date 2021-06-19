from flask_app import app
from flask_app.controllers import display_ctrl, login_ctrl



if __name__ == "__main__":
    app.run(debug=True)