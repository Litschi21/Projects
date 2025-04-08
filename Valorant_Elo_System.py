import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class MatchData:
    kills: int
    deaths: int
    won: bool
    agent: str
    timestamp: datetime
    agent_role: str

class ValorantTracker:
    def __init__(self):
        self.agent_roles = {
            "phoenix": "duelist", "jett": "duelist", "raze": "duelist", "reyna": "duelist", "yoru": "duelist", "neon": "duelist",
            "sova": "initiators", "breach": "initiators", "skye": "initiators", "kayo": "initiators", "fade": "initiators", "gekko": "initiators",
            "brimstone": "controller", "viper": "controller", "omen": "controller", "astra": "controller", "harbor": "controller",
            "killjoy": "sentinel", "cypher": "sentinel", "sage": "sentinel", "chamber": "sentinel", "deadlock": "sentinel"
        }

    def get_agent_role(self, agent):
        return self.agent_roles.get(agent.lower(), "unknown")

    def input_match(self):
        """Get match data through manual input"""
        print("\nEnter match details:")
        agent = input("Agent played: ").lower()
        if agent not in self.agent_roles:
            print('Invalid agent. Try again.')
            ValorantTracker.input_match(self)
        kills = int(input("Number of kills: "))
        if kills < 0:
            print('Invalid Number. Try again.')
            ValorantTracker.input_match(self)
        deaths = int(input("Number of deaths: "))
        if deaths < 0:
            print('Invalid Number. Try again.')
            ValorantTracker.input_match(self)
        won = input("Did you win? (y/n): ").lower() == 'y'
        
        return MatchData(
            kills=kills,
            deaths=deaths,
            won=won,
            agent=agent,
            agent_role=self.get_agent_role(agent),
            timestamp=datetime.now()
        )

    def save_match_history(self, matches, filename="match_history.json"):
        """Save matches to a JSON file"""
        match_list = []
        for match in matches:
            match_list.append({
                "kills": match.kills,
                "deaths": match.deaths,
                "won": match.won,
                "agent": match.agent,
                "agent_role": match.agent_role,
                "timestamp": match.timestamp.isoformat()
            })
            
        with open(filename, 'w') as f:
            json.dump(match_list, f, indent=4)

def calculate_elo(rating, match_data, k_factor=25):
    """Calculate new Elo based on your system"""
    score = 1 if match_data.won else 0
    
    role_multipliers = {
        'duelist': 1.2,
        'initiators': 1.1,
        'controller': 1.0,
        'sentinel': 0.9
    }

    role_mult = role_multipliers.get(match_data.agent_role, 1.0)

    # Calculate K/D ratio
    if match_data.deaths == 0:
        kd_ratio = match_data.kills * 2
    else:
        kd_ratio = match_data.kills / match_data.deaths

    # Determine performance factor based on role and K/D
    if match_data.agent_role in ['duelist', 'initiators']:
        if kd_ratio < 1.0:
            performance_factor = 0.8 * role_mult
        elif kd_ratio >= 1.0 and kd_ratio < 2.0:
            performance_factor = 1.0 * role_mult
        else:
            performance_factor = 1.2 * role_mult
    else:  # controller or sentinel
        if kd_ratio < 0.7:
            performance_factor = 0.8 * role_mult
        elif kd_ratio >= 0.7 and kd_ratio < 1.5:
            performance_factor = 1.0 * role_mult
        else:
            performance_factor = 1.1 * role_mult
    
    # Calculate rating change
    if score == 1:
        rating_change = k_factor * performance_factor
    else:
        rating_change = -(k_factor * 0.5 * performance_factor)
    
    return round(rating + rating_change, 2)

def main():
    current_elo = float(input("Enter current Elo rating: "))
    k_factor = float(input("Enter K-factor (25 for high rank, 50 for low rank): "))
    num_matches = int(input("How many matches would you like to input? "))
    
    tracker = ValorantTracker()
    matches = []
    
    try:
        # Input matches manually
        for i in range(num_matches):
            print(f"\nMatch {i+1}/{num_matches}")
            match = tracker.input_match()
            matches.append(match)
            
            # Calculate and display Elo change
            new_elo = calculate_elo(current_elo, match, k_factor)
            print(f"\nMatch as {match.agent} ({match.agent_role})")
            print(f"K/D: {match.kills}/{match.deaths}")
            print(f"Result: {'Won' if match.won else 'Lost'}")
            print(f"Elo change: {current_elo} → {new_elo} ({new_elo - current_elo:+.2f})")
            current_elo = new_elo
            
        # Save match history
        tracker.save_match_history(matches)
        print(f"\nMatch history saved to match_history.json")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# p1 =  # Player 1
# score =  # 0 = loss, 1 = win
# kills = 
# deaths = 
# char_group = 'duelist'

# print(new_elo(p1, score, kills, deaths, char_group))

# My Stats
# Current Elo: 1193.5
# Peak Elo: 1229.5
# Lowest Elo: 937
# Char: Killjoy (Sentinel)

# TenZ's Stats
# Current Elo: 2869
# Peak Elo: 2884
# Lowest Elo: 1000
# Char: Jett (Duelist)

# Friend Stats
# Elo: 
# Peak Elo: 
# Char:  (Duelist)
