from Application import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(1024), nullable=False)
    email = db.Column(db.String(1024), nullable=False)
    password_hash = db.Column(db.String(2048), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_hash(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Fixtures(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Team_A = db.Column(db.String(100), nullable=False)
    Team_B = db.Column(db.String(100), nullable=False)
    team_a_playing_11 = db.Column(db.String(2048), nullable=False)
    team_b_playing_11 = db.Column(db.String(2048), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)
    venue = db.Column(db.String(500), nullable=False)
    runs_by_team_A = db.Column(db.String(500), nullable=False)
    runs_by_team_B = db.Column(db.String(500), nullable=False)
    outcome = db.Column(db.String(2048), nullable=False)
    player_of_match = db.Column(db.String(500), nullable=False)
    best_bowler = db.Column(db.String(500))
    Umpires = db.Column(db.String(500))
    third_umpire = db.Column(db.String(500))
    match_refree = db.Column(db.String(500))
    Toss = db.Column(db.String(500))
    player_of_series = db.Column(db.String(500))
    status = db.Column(db.String(100), nullable=False)


class Venue_Details(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    stadium = db.Column(db.String(500), nullable=False)
    capacity = db.Column(db.String(100), nullable=False)
    ends = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    floodlights = db.Column(db.String(100), nullable=False)
    home_to = db.Column(db.String(100), nullable=False)
    time_zone = db.Column(db.String(100), nullable=False)


class player_stats(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    test_matches = db.Column(db.String(100), nullable=False)
    odi_matches = db.Column(db.String(100), nullable=False)
    t20_matches = db.Column(db.String(100), nullable=False)


class Group_A(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    matches = db.Column(db.Integer(), nullable=False)
    won = db.Column(db.Integer(), nullable=False)
    loss = db.Column(db.Integer(), nullable=False)
    tied = db.Column(db.Integer(), nullable=False)
    points = db.Column(db.Integer(), nullable=False)
    NRR = db.Column(db.String(100), nullable=False)


class Group_B(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    matches = db.Column(db.Integer(), nullable=False)
    won = db.Column(db.Integer(), nullable=False)
    loss = db.Column(db.Integer(), nullable=False)
    tied = db.Column(db.Integer(), nullable=False)
    points = db.Column(db.Integer(), nullable=False)
    NRR = db.Column(db.String(100), nullable=False)


class Super_4(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    matches = db.Column(db.Integer(), nullable=False)
    won = db.Column(db.Integer(), nullable=False)
    loss = db.Column(db.Integer(), nullable=False)
    tied = db.Column(db.Integer(), nullable=False)
    points = db.Column(db.Integer(), nullable=False)
    NRR = db.Column(db.String(100), nullable=False)
