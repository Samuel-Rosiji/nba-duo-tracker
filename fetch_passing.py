from nba_api.stats.endpoints import playerdashptpass


def fetch_player_passing():
    print("Fetching passing data for the 25-26 season")

    data = playerdashptpass.PlayerDashPtPass(
        team_id = 1610612743, 
        player_id= 203999,
        season = '2025-26',
        season_type_all_star='Regular Season',
        timeout= 60
    )

    passes_made = data.get_data_frames()[0]
    print(f"Got {len(passes_made)} rows")
    print(passes_made.columns.tolist())
    print(passes_made.head(5))

    passes_received = data.get_data_frames()[1]
    print(f"Got {len(passes_received)} rows")
    print(passes_received.columns.tolist())
    print(passes_received.head(5))

    return passes_made, passes_received


if __name__ == "__main__":
    fetch_player_passing()


