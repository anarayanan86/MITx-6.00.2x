# Problem 3
#  Bookmark this page
# Problem 3
# 20.0/20.0 points (graded)
# You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each
# tuple has the following elements:
# name: the first element, representing the song name (non-empty string)
# song_length: the second, element representing the song duration (float >= 0)
# song_size: the third, element representing the size on disk (float >= 0)

# You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take
# up more than a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).

# You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on
# disk, return an empty list. If there is enough space for this song, add it to the playlist.

# For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You
# do this until you cannot fit any more songs on the disk.

# Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the
# first element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and
# different durations.

# You may not mutate any of the arguments.

# For example,
# If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2, the function will
# return ['Roar','Wannabe','Timber']
# If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11, the function will return
# ['Roar','Wannabe']

# Paste your entire function (including the definition) in the box. Do not import anything. Do not leave any debugging print statements.


# Paste your code here
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
    else:
        return playlist
    song_list_copy_ascending = sorted(songs, key = lambda x: x[2])
    song_list_copy_ascending.remove(songs[0])
    space_remain = max_size - songs[0][2]
    for i in song_list_copy_ascending:
        if i[2] <= space_remain:
            playlist.append(i[0])
            space_remain -= i[2]
        else:
            break
    return playlist
    
# Correct
