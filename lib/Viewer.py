class Viewer:

    all_viewers = []
    
    def __init__(self, username):
        self.username = username
        self.reviews = []
        self.reviewed_movies = []
        Viewer.all_viewers.append(self.username)

    # username property getter/setter methods
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            if username not in Viewer.all_viewers:
                self._username = username
            else:
                raise Exception('Username not available! Please choose a different username.')
        else:
            raise Exception('Username must be a string between 6 and 16 characters!')


    def reviewed_movie(self, movie):
        if movie not in self.reviewed_movies:
            return False
        else:
            return True

    def rate_movie(self, movie, rating):
        from lib.Review import Review
        if not self.reviewed_movie(movie):
            Review(self, movie, rating)
        else:
            for review in self.reviews:
                if review.movie == movie:
                    review.rating = rating

    # ***Extra method, returns a list of reviews done by a given Viewer instance
    def get_all_reviews(self):
        return [review for review in self.reviews]
    
    # ***Extra method, returns a list of movies reviewed by a given Viewer instance
    def get_all_movies(self):
        return [movie.title for movie in self.reviewed_movies]