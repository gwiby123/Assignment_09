#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# GByron, 2022-Mar-23, Downloaded Code for Assignment Use
# GByron, 2022-Mar-28, Downloaded and began code additions
# GByron, 2022-Mar-29, Finished code additions
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        trkId: (int) with Track position on CD / Album
        trkTitle: (str) with Track title
        trkLength: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    # -- Constructor -- #
    
    def __init__(self, trkId, trkTitle, trkLength):
        self.__trkId = trkId
        self.__trkTitle = trkTitle
        self.__trkLength = trkLength
    # -- Properties -- #
    
    # Track position
    @property
    def trkId(self):
        return self.__trkId
    
    @trkId.setter
    def trkId(self, value):
        if type(value) != int:
                raise Exception('Item needs to be an integer!')
                self.__trkId = value
        
    @property
    def trkTitle(self):
        return self.__title
    
    @trkTitle.setter
    def trkTitle(self, value):
        if type(value) == str:
            if value == '':
                raise Exception('You need to put information in!')
            self.__trkTitle = value
        else:
            raise Exception('Please input the correct information!')
        
    @property
    def trkLength(self):
         return self.lengths
     
    @trkLength.setter
    def trkLength(self, value):
         if type(value) == str:
             if value == '':
                 raise Exception('You need to put information in!')
             self.__trkLength = value
         else:
             raise Exception('Please input the correct information!')
             
    # -- Methods -- #
    def __str__(self):
        """Returns Track details as formatted string""" 
        return '{}, {}, {}'.format(self.__trkId, self.__trkTitle, self.__trkLength)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{}, {}, {}'.format(self.__trkId, self.__trkTitle, self.__trkLength)


class CD:
    """Stores data about a CD / Album:

    properties:
        cdID: (int) with CD  / Album ID
        cdTitle: (string) with the title of the CD / Album
        cdArtist: (string) with the artist of the CD / Album
        cdTracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """
    # -- Constructor -- #
    def __init__(self, cdID: int, cdTitle: str, cdArtist: str) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cdID = int(cdID)
            self.__cdTitle = str(cdTitle)
            self.__cdArtist = str(cdArtist)
            self.__tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cdID(self):
        return self.__cdID

    @cdID.setter
    def cdID(self, value):
        try:
            self.__cdID = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cdTitle(self):
        return self.__cdTitle

    @cdTitle.setter
    def cdTitle(self, value):
        try:
            self.__cdTitle = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cdArtist(self):
        return self.__cdArtist

    @cdArtist.setter
    def cdArtist(self, value):
        try:
            self.__cdArtist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cdID, self.cdTitle, self.cdArtist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cdID, self.cdTitle, self.cdArtist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        
        self.__tracks.append(track)
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        while True:
            try:
                track_id = int(track_id)
            except:
                print('Please input an integer!')
                break
            try: 
                if self.__tracks[(int(track_id)-1)] == None:
                    print('This track does not exist!')
                    break
                else:
                    del self.__tracks[(int(track_id)-1)]
                    print('The track was removed')
                    self.__sort_tracks
            except:
                break

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.trkId):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.trkId - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result



