from app import app

from flask_sqlalchemy import SQLAlchemy


# DB init
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    person_id        = db.Column(db.Integer, nullable=False, primary_key=True)
    username         = db.Column(db.String(50), nullable=False)
    is_online        = db.Column(db.Boolean, default=False, nullable=False)
    last_online_at   = db.Column(db.DateTime(), nullable=False)
    last_login_at    = db.Column(db.DateTime(), nullable=False)
    photo_url        = db.Column(db.String(2000))
    default_language = db.Column(db.String(50))
    default_bio      = db.Column(db.String(2000))
    steam_id         = db.Column(db.String(50))
    discord_id       = db.Column(db.String(50))
    device_id        = db.Column(db.String(50))
    email_login      = db.Column(db.String(200))
    email_password   = db.Column(db.String(200))

    def __repr__(self):
        return f"User: {self.username}"


class CoreData(db.Model):
    __tablename__ = 'core_data'

    core_data_id       = db.Column(db.Integer, nullable=False, primary_key=True)
    data_updated_at    = db.Column(db.DateTime(), nullable=False)
    need_to_be_updated = db.Column(db.Boolean, default=True, nullable=False)
    app_username       = db.Column(db.String(50))
    language           = db.Column(db.String(50))
    bio                = db.Column(db.String(2000))

    def __repr__(self):
        return f"CoreData: {self.app_username}"


class ForniteAppData(db.Model):
    __tablename__ = 'fornite_app_data'

    app_data_id    = db.Column(db.Integer, nullable=False, primary_key=True)
    person_id      = db.Column(db.Integer, db.ForeignKey('user.person_id'), nullable=False)
    core_data_id   = db.Column(db.Integer, db.ForeignKey('core_data.core_data_id'), nullable=False)
    server         = db.Column(db.String(50))
    hero           = db.Column(db.String(50))
    video_clip_url = db.Column(db.String(2000))

    def __repr__(self):
        return f"ForniteAppData: {self.hero}"


class ForniteGameData(db.Model):
    __tablename__ = 'fornite_game_data'

    game_data_id     = db.Column(db.Integer, nullable=False, primary_key=True)
    app_data_id      = db.Column(db.Integer, db.ForeignKey('fornite_app_data.app_data_id'), nullable=False)
    hours_played     = db.Column(db.Numeric(10, 2))
    winpercentage    = db.Column(db.Numeric(10, 2))
    battlepass_level = db.Column(db.String(200))
    daily_hours      = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f"ForniteGameData: {self.game_data_id}"


class CsgoAppData(db.Model):
    __tablename__ = 'сsgo_app_data'

    app_data_id    = db.Column(db.Integer, nullable=False, primary_key=True)
    person_id      = db.Column(db.Integer, db.ForeignKey('user.person_id'), nullable=False)
    core_data_id   = db.Column(db.Integer, db.ForeignKey('core_data.core_data_id'), nullable=False)
    server         = db.Column(db.String(50))
    map            = db.Column(db.String(50))
    position       = db.Column(db.String(50))
    video_clip_url = db.Column(db.String(2000))

    def __repr__(self):
        return f"CsgoAppData: {self.app_data_id}"


class CsgoGameData(db.Model):
    __tablename__ = 'сsgo_game_data'

    game_data_id     = db.Column(db.Integer, nullable=False, primary_key=True)
    app_data_id      = db.Column(db.Integer, db.ForeignKey('сsgo_app_data.app_data_id'), nullable=False)
    hours_played     = db.Column(db.Numeric(10, 2))
    kill_per_round   = db.Column(db.Numeric(10, 2))
    total_kills      = db.Column(db.Numeric(10, 2))
    kill_death_ratio = db.Column(db.Numeric(10, 2))
    game_nickname    = db.Column(db.String(50))

    def __repr__(self):
        return f"CsgoGameData: {self.app_data_id}"

"""
User service

[x] User
[x] [PK] person_id int NOT NULL
[x] username varchar(50) NOT NULL
[x] is_online boolean NOT NULL DEFAULT FALSE
[x] last_online_at date NOT NULL
[x] last_login_at date NOT NULL
[x] photo_url varchar(2000)
[x] default_language varchar(50)
[x] default_bio varchar(2000)
[x] steam_id varchar(50)
[x] discord_id varchar(50)
[x] device_id varchar(50)
[x] email_login varchar(200)
[x] email_password varchar(200)

[x] CoreData
[x] [PK] core_data_id int NOT NULL
[x] data_updated_at date NOT NULL
[x] need_to_be_updated boolean NOT NULL DEFAULT TRUE
[x] app_username varchar(50)
[x] language varchar(50)
[x] bio varchar(2000)

[x] ForniteAppData
[x] [PK] app_data_id int NOT NULL
[x] [FK1] person_id int NOT NULL
[x] [FK2] core_data_id int NOT NULL
[x] server varchar(50)
[x] hero varchar(50)
[x] video_clip_url varchar(2000)

[x] ForniteGameData
[x] [PK] game_data_id int NOT NULL
[x] [FK1] app_data_id int NOT NULL
[x] hours_played decimal
[x] winpercentage decimal
[x] battlepass_level varchar(200)
[x] daily_hours decimal

[x] CsgoAppData
[x] [PK] app_data_id NOT NULL
[x] [FK1] person_id int NOT NULL
[x] [FK2] core_data_id NOT NULL
[x] server varchar(50)
[x] map varchar(50)
[x] position varchar(50)
[x] video_clip_url varchar(2000)

[x] CsgoGameData
[x] [PK] game_data_id int NOT NULL
[x] [FK1] app_data_id int NOT NULL
[x] hours_played decimal
[x] kill_per_round decimal
[x] total_kills decimal
[x] kill_death_ratio decimal
[x] game_nickname varchar(50)

=============================================

Team service

Team
[PK] team_id int NOT NULL
name varchar(50) NOT NULL
created_at date NOT NULL
updated_at date NOT NULL
game: enum("FORNITE", "CSGO") NOT NULL
photo_url varchar(2000)
last_played_at date

TeamMember
[PK] member_id int NOT NULL
[FK1] team_id int NOT NULL
person_id int NOT NULL
photo_url varchar(2000)
is_online boolean DEFAULT FALSE
discord_key varchar(200)

=============================================

Game service

PlayerMetadataCsgo
[PK] metadata_id int NOT NULL
person_id int NOT NULL
steam_id varchar(50) NOT NULL
steam_apikey varchar(200)
requests_per_day int NOT NULL DEFAULT 0

PlayerMetadataFornite
[PK] metadata_id int NOT NULL
person_id int NOT NULL
epic_account_key varchar(200) NOT NULL
requests_per_day int NOT NULL DEFAULT 0

GameDictionaryValue
[PK] dictionary_value_id int NOT NULL
key varchar(200) NOT NULL
value text
[FK1] dictionary_id int NOT NULL

GameDictionary
[PK] dictionary_id int NOT NULL
game enum("FORNITE", "CSGO") NOT NULL
dictionary_name varchar(200) NOT NULL
"""
