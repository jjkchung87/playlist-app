"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                    primary_key=True
                   )
    name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)
    
    description = db.Column(db.Text)

    playlistsongs = db.relationship('PlaylistSong', backref='playlists')

    songs = db.relationship('Song', secondary='playlistsongs', backref='playlists')
                            

    def __repr__(self):
        """Better representation of Playlist object"""
        return f'<Playlist: {self.id} {self.name}>'
    


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                   primary_key=True)
    
    title = db.Column(db.Text,
                      nullable=False)
    
    artist = db.Column(db.Text,
                      nullable=False)

    playlistsongs = db.relationship('PlaylistSong', backref='songs')


    def __repr__(self):
        """better representation of Song objects"""
        return f'<Song {self.id} {self.title} {self.artist}>'


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlistsongs"

    id = db.Column(db.Integer,
                   primary_key=True)
    
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists.id', ondelete="cascade")
                            )

    song_id = db.Column(db.Integer,
                            db.ForeignKey('songs.id', ondelete="cascade")
                            )
    
    def __repr__(self):
        """Better representation of PlaylistSong objects"""
        return f'<PlaylistSong {self.id} {self.playlist_id} {self.song_id}>'




# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
