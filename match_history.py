from nba_api.stats.endpoints import LeagueGameFinder

# Set the LeagueID to NBA (1)
league_id = "00"

# Retrieve all NBA games for the current season
game_finder = LeagueGameFinder(league_id_nullable=league_id)
games = game_finder.get_data_frames()[0]

# Filter relevant columns for stats and outcomes
stats_and_outcomes = games[
    [
        "GAME_DATE",
        "TEAM_NAME",
        "PTS",
        "AST",
        "REB",
        "TOV",
        "FG_PCT",
        "FG3A",
        "FGA",
        "PF",
        "BLK",
        "WL",
    ]
]

# Replace "W" with 1 and "L" with 0 in the WL column
stats_and_outcomes["WL"] = stats_and_outcomes["WL"].replace({"W": 1, "L": 0})

# Replace non-finite values (NA or inf) with a default value
stats_and_outcomes["WL"].fillna(-1, inplace=True)

# Convert WL column to integers
stats_and_outcomes["WL"] = stats_and_outcomes["WL"].astype(int)

# Save the statistics and outcomes as a CSV file
stats_and_outcomes.to_csv("./visualization/nba_stats.csv", index=False)

print(stats_and_outcomes)
