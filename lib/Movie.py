class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        self.reviews = []
        self.reviewers = []
        Movie.all.append(self)


    # title property getter/setter methods
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 0 < len(title):
            self._title = title
        else:
            raise Exception('Title must be a string greater than 0 characters!')

    def average_rating(self):
        sum = 0
        for rating in self.reviews:
            sum += rating

        return sum / len(self.reviews)

    @classmethod
    def highest_rated(cls):
        max = 0
        best_movie = None

        for movie in cls.all:
            current = movie.average_rating()
            if current > max:
                max = current
                best_movie = movie
        
        return best_movie
    
    # ***Extra method, returns a list of movie ratings for a given movie instance
    def get_all_reviews(self):
        return [review.rating for review in self.reviews]
    
    # ***Extra method, returns a list of usernames of reviewers for a given movie instance
    def get_all_reviewers(self):
        return [reviewer.username for reviewer in self.reviewers]
