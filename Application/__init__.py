from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__, template_folder='Templates', static_folder='static')
app.config['SECRET_KEY'] = "ceae6c9e3c539be973568828"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cricket_league.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



from Application.models import player_stats, Group_A, Group_B, Super_4, Fixtures, Venue_Details


class MyAdminView(ModelView):
    def is_accessible(self):
        if current_user.id == 1:
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('start.html'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.id == 1:
            return current_user.is_authenticated


admin = Admin(app, index_view=MyAdminIndexView())

admin.add_view(MyAdminView(player_stats, db.session))
admin.add_view(MyAdminView(Group_A, db.session))
admin.add_view(MyAdminView(Group_B, db.session))
admin.add_view(MyAdminView(Super_4, db.session))
admin.add_view(MyAdminView(Fixtures, db.session))
admin.add_view(MyAdminView(Venue_Details, db.session))

from Application import routes
