from Application import app, db
from Application.forms import Login, Register
from Application.models import User, player_stats, Group_B, Group_A, Super_4, Venue_Details, Fixtures
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user


@app.route('/', methods=['GET', 'POST'])
def start():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        login = Login()
        register = Register()

        if login.sign_in.data and login.validate():
            attempted_user = User.query.filter_by(username=login.username.data).first()
            if attempted_user and attempted_user.check_password_hash(attempted_password=login.password.data):
                login_user(attempted_user)
                flash("Logged In Successfully")
                return redirect(url_for('home'))
            else:
                flash("Invalid Username or Password")

        if request.method == 'POST':
            if register.sign_up.data and register.validate():
                print(register.sign_up.data and register.validate())
                add_user = User(username=register.username.data, name=register.name.data,
                                email=register.email.data, password=register.password1.data)
                db.session.add(add_user)
                db.session.commit()
                user = User.query.filter_by(username=register.username.data).first()
                login_user(user)
                flash('User Register Successfully')
                return redirect(url_for('home'))

        if register.errors != {}:
            for error_message in register.errors.values():
                flash(error_message)

        return render_template('start.html', login=login, register=register)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        group_a = Group_A.query.all()
        group_b = Group_B.query.all()
        super_4 = Super_4.query.all()
        match = Fixtures.query.all()
        return render_template('home.html', group_a=group_a, group_b=group_b, super_4=super_4, match=match)
    else:
        flash("Please Login To Continue....")


@app.route('/home/<team_name>', methods=['GET', 'POST'])
def team_profile(team_name):
    if current_user.is_authenticated:
        player = player_stats.query.filter_by(country=team_name).all()
        title = team_name
        return render_template('team.html', player=player, title=title)
    else:
        flash("Please Login To Continue....")


@app.route('/home/<team_name>/<player_name>', methods=['GET', 'POST'])
def player_profile(team_name, player_name):
    if current_user.is_authenticated:
        player = player_stats.query.filter_by(country=team_name).filter_by(name=player_name).first()
        title = f'{team_name}-{player_name}'
        return render_template('player.html', title=title, player=player)
    else:
        flash("Please Login To Continue....")


@app.route('/stadium/<name>', methods=['GET', 'POST'])
def stadium(name):
    if current_user.is_authenticated:
        venue = Venue_Details.query.filter_by(stadium=name).first()
        title = name
        return render_template('stadium.html', title=title, venue=venue)
    else:
        flash("Please Login To Continue....")


@app.route('/<match_id>/<team_a> vs <team_b>')
def match_summary(team_a, team_b, match_id):
    if current_user.is_authenticated:
        title = f'{team_a} vs {team_b}'
        details = Fixtures.query.filter_by(id=match_id).filter_by(Team_A=team_a).filter_by(Team_B=team_b).first()
        return render_template('match_summary.html', title=title, details=details)
    else:
        flash("Please Login To Continue....")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('start'))
