class Video:
    def __init__(self, video_id, title, video_link, views_count, likes_count):
        self.video_id = video_id
        self.title = title
        self.video_link = video_link
        self.views_count = views_count
        self.likes_count = likes_count


class PLVideo(Video):
    def __init__(self, video_id, title, video_link, views_count, likes_count, playlist_id):
        super().__init__(video_id, title, video_link, views_count, likes_count)
        self.playlist_id = playlist_id

