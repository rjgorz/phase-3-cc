class Review:
    # ***Review class is the linking factor between Movie and Viewer***
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer  # instance of Viewer
        self.movie = movie    # instance of Movie
        self.rating = rating

        # call all adder methods to link up relationships
        self.add_viewer_to_movie()
        self.add_movie_to_viewer()
        self.add_review_to_movie()
        self.add_review_to_viewer()

    # rating property getter/setter methods
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception('Rating must be an integer between 1 and 5!')

    # viewer property getter/setter methods
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        from lib.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception('Viewer must be an instance of the Viewer class!')

    # movie property getter/setter methods
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from lib.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception('Movie must be an instance of the Movie class!')
        
    # adder methods to build relationships between classes
    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)

    def add_review_to_movie(self):
        self._movie.reviews.append(self)

    def add_movie_to_viewer(self):
       if self._movie not in self._viewer.reviewed_movies:
           self._viewer.reviewed_movies.append(self._movie)

    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)