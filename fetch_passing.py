from nba_api.stats.endpoints import playerdashptpass
import pandas as pd
from db import insert_passing

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def fetch_player_passing():
    print("Fetching passing data for the 25-26 season")

    data = playerdashptpass.PlayerDashPtPass(
        team_id = 1610612743, 
        player_id= 203999,
        season = '2025-26',
        season_type_all_star='Regular Season',
        timeout= 60
    )

    
    murray_id = 1627750

    passes_made = data.get_data_frames()[0]
    print(f"Got {len(passes_made)} rows")
    print(passes_made.columns.tolist())
    print(passes_made.head(1))

    passes_received = data.get_data_frames()[1]
    print(f"Got {len(passes_received)} rows")
    print(passes_received.columns.tolist())
    print(passes_received.head(1))

    murray_passes_made = passes_made[passes_made['PASS_TEAMMATE_PLAYER_ID'] == murray_id]
    murray_passes_received = passes_received[passes_received['PASS_TEAMMATE_PLAYER_ID'] == murray_id]

    print(murray_passes_made)
    print(murray_passes_received)
    insert_passing(murray_passes_made, murray_passes_received)

    return murray_passes_made, murray_passes_received


if __name__ == "__main__":
    fetch_player_passing()


