class Song:
    def __init__(self, title):
        self.__title = title
        self.__next_song = None

    def get_title(self):
        """
        Simple getter for the title
        Returns:
          self.__title: string, title of the song
        """
        return self.__title

    def set_title(self, title):
        """
        Simple setter for the title, performs title casing before returning title
        Returns:
          self.__title: string, properly cased song title
        """
        titleCased = title.title()
        self.__title = titleCased

    def get_next_song(self):
        """
        Simple getter for the next song
        Returns:
          self.__next_song: string, title of the song
        """
        return self.__next_song

    def set_next_song(self, next_song):
        """
        Setter function for the next song object.
        Returns:
          self.__next_song:   str, next song name
        """
        self.__next_song = next_song

    def __str__(self):
        """ Simple __str__ dunder for object address output"""
        return f"{self.__title}"

    def __repr__(self):
        """ Simple ___repr___ dunder for useful output"""
        return f"{self.__title} -> {self.__next_song}"
