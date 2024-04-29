"""Functions for retrieving data
"""

import pandas as pd

def get_champ_data() -> pd.DataFrame:
    """Loads each tournament CSV and concatenates them
    """
    champ_list = [
        '2015_Worlds_LOL.csv',
        '2016_Worlds_LOL.csv',
        '2017_Worlds_LOL.csv',
        '2018_Worlds_LOL.csv',
        '2019_Worlds_LOL.csv',
        '2020_Worlds_LOL.csv',
        '2021_Worlds_LOL.csv',
        '2022_Worlds_LOL.csv',
        '2023_Worlds_LOL.csv',

    ]
    champ_data = [pd.read_csv(m) for m in champ_list]
    champs = pd.concat(
        champ_data,
        ignore_index=True
    )
    return champs

def get_top_data() -> pd.DataFrame:
    """Loads the CSV containing top lane data
    """
    return pd.read_csv('Top_Lane_Data.csv')

def get_picks_data() -> pd.DataFrame:
    """Loads the CSV containing champions picked
    """
    return pd.read_csv('picks_and_wins.csv')

def get_name_data() -> pd.DataFrame:
    """Loads the CSV containing champion names 
    """
    return pd.read_csv('champs.csv')

