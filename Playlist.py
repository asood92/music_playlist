from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    def add_song(self, title):
        """
        Function to instantiate and add a new Song object to the linked list. Loop performed
        to guarantee the song is being added to the end of the stack.
        Returns:
          None
        """
        current_song = self.__first_song
        new_song = Song(title)
        new_song.set_title(title)

        if current_song == None:
            self.__first_song = new_song
            return

        while current_song.get_next_song() != None:
            current_song = current_song.get_next_song()

        current_song.set_next_song(new_song)

    def find_song(self, title):
        """
        Search function iterates through the linked list until it reaches the end, searching for a
        user entered song.
        Returns:
          count: int,  representing the index of the song if found in the list
          -1:  int,  value representing to main that the song was not found
        """
        current_song = self.__first_song
        count = 0

        while current_song != None:

            if current_song.get_title() == title:
                return count

            else:
                count += 1
                current_song = current_song.get_next_song()

        return -1

    def remove_song(self, title):
        """
        Function to search and remove a user entered song object from the linked list and link the previous item to the found items next pointer.
        Returns:
          None
        """
        last_song = None
        current_song = self.__first_song
        foundFlag = False

        if current_song == None:
            return f"Empty playlist, can't remove a song from an empty playlist."

        while not foundFlag:
            if current_song.get_title() == title:
                foundFlag = True
            else:
                last_song = current_song
                current_song = current_song.get_next_song()
        if last_song == None:
            self.__first_song = current_song.get_next_song()
        else:
            last_song.set_next_song(current_song.get_next_song())

    def length(self):
        """
        Simple counter function to count the number of song objects in the linked list and return that value.
        Returns:
          count:  int,  representing the length of the linked list
        """
        current_song = self.__first_song
        count = 0

        if current_song == None:
            print("Empty list.")
            return 0

        while current_song.get_next_song() != None:
            current_song = current_song.get_next_song()
            count += 1

        return count + 1

    def print_songs(self):
        """
        Simple print function to iterate through and print the entire contents of the linked list.
        Returns:
          None
        """
        current_song = self.__first_song
        count = 0

        if current_song == None:
            print("Empty playlist, no songs.")
            return

        while current_song.get_next_song() != None:
            print(f"{count+1}.)  {current_song}")
            count += 1
            current_song = current_song.get_next_song()
        print(f"{count+1}.)  {current_song}")
