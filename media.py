import webbrowser

class Movie():
  """Summary of class here.
  Attributes:
      title: Movie title.
      storyline: Description of the movie story.
      poster_image_url: Url of the movie poster.
      trailer_youtube_url: Url of the movie youtube trailer.
  """

  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)