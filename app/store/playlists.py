from app.db.userdata import PlaylistTable
from app.lib.playlistlib import get_first_4_images
from app.models.playlist import Playlist
from app.store.tracks import TrackStore


class PlaylistEntry:
    def __init__(self, playlist: Playlist) -> None:
        self.playlist = playlist
        self.trackhashes: list[str] = playlist.trackhashes
        self.playlist.clear_lists()

        if not playlist.has_image:
            self.playlist.images = get_first_4_images(
                TrackStore.get_tracks_by_trackhashes(self.trackhashes)
            )


class PlaylistStore:
    playlistmap: dict[str, PlaylistEntry] = {}

    @classmethod
    def load_playlists(cls):
        """
        Loads all playlists into the store.
        """
        cls.playlistmap = {str(p.id): PlaylistEntry(p) for p in PlaylistTable.get_all()}
        print(cls.playlistmap)

    @classmethod
    def get_playlist_tracks(cls, playlist_id: str, start: int, limit: int):
        """
        Returns the trackhashes for a playlist.
        """

        entry = cls.playlistmap.get(playlist_id)
        if entry is None:
            return []

        return TrackStore.get_tracks_by_trackhashes(
            entry.trackhashes[start : start + limit]
        )

    @classmethod
    def get_flat_list(cls):
        return [p.playlist for p in cls.playlistmap.values()]

    @classmethod
    def add_playlist(cls, playlist: Playlist):
        cls.playlistmap[str(playlist.id)] = PlaylistEntry(playlist)