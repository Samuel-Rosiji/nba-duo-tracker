from nba_api.stats.endpoints import leaguedashlineups
from db import insert_lineups

def fetch_two_man_lineups():
    print("Fetching two-man lineup data for 2025-26 season...")
    
    data = leaguedashlineups.LeagueDashLineups(
        group_quantity=2,
        season='2025-26',
        season_type_all_star='Regular Season',
        per_mode_detailed='Totals',
        measure_type_detailed_defense='Base',
        timeout=60
    )
    
    df = data.get_data_frames()[0]
    print(f"Got {len(df)} rows")
    insert_lineups(df)
    return df     

if __name__ == "__main__":
    fetch_two_man_lineups()