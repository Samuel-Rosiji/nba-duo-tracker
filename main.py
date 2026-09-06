import time

from db import db
from db import get_top_duos
from db import insert_passing
from fetch import fetch_two_man_lineups
from fetch_passing import fetch_player_passing


def main():
    try:
        fetch_two_man_lineups()
        db["passes"].drop()
        for doc in get_top_duos(limit=50):
            group_arr =  doc['GROUP_ID'].split("-")
            team = doc['TEAM_ID']
            player_1 =  int(group_arr[1])
            teammate_2 = int(group_arr[2])
            passes_made, passes_received = fetch_player_passing(player_1, team, teammate_2)
            if passes_made is not None:
                insert_passing(passes_made, passes_received)
            time.sleep(1)

    except Exception as e:
            print(f"Failed for player {player_id}: {e}")
            return None, None




if __name__ == "__main__":
    main()