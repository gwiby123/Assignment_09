#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# GByron, 2022-Mar-23, Downloaded Code for Assignment Use
# GByron, 2022-Mar-28, Downloaded and began code additions/alterations
# GByron, 2022-Mar-29, Finished code additions/alterations
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        cdId, cdTitle, cdArtist = CDInfo 
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, cdTitle, cdArtist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        while True:
            try:
                cd_idx = int(cd_idx)
            except:
                print('Please input an integer!')
                break
            try:
                cdId = ''
                for row in table:
                    if row.cdId == cd_idx:
                        cdId = row
                if cdId == '':
                    raise Exception('This CD ID doesn\'t exist the database!')
            except:
                break
           
            
    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        trkId, trkTitle, trkLength = track_info
        try:
            trkId = int(trkId)
        except:
            raise Exception('ID must be an integer!')
        row = DC.row(trkId, trkTitle, trkLength)
        cd.add_track(row)

