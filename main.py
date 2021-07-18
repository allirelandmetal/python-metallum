import metallum


# Search bands matching term
bands = metallum.band_search('metallica')
# -> [<SearchResult: Metallica | Thrash Metal (early), Hard Rock/Heavy/Thrash Metal (later) | United States>]

bands[0].name
# -> 'Metallica'

# Fetch band page
band = bands[0].get()

# Get all albums
band.albums
# -> [<Album: No Life 'til Leather (Demo)>, <Album: Kill 'Em All (Full-length)>, ...]

# Get only full-length albums
full_length = band.albums.search(type=metallum.AlbumTypes.FULL_LENGTH)
# -> [<Album: Kill 'Em All (Full-length)>, <Album: Ride the Lightning (Full-length)>, <Album: Master of Puppets (Full-length)>, <Album: ...and Justice for All (Full-length)>, <Album: Metallica (Full-length)>, <Album: Load (Full-length)>, <Album: ReLoad (Full-length)>, <Album: Garage Inc. (Full-length)>, <Album: St. Anger (Full-length)>, <Album: Death Magnetic (Full-length)>, <Album: Hardwired... to Self-Destruct (Full-length)>]

album = full_length[2]
album.title
# -> 'Master of Puppets'

album.date
# -> datetime.datetime(1986, 3, 3, 0, 0)

# Get all tracks
album.tracks
# -> [<Track: Battery (313)>, <Track: Master of Puppets (516)p