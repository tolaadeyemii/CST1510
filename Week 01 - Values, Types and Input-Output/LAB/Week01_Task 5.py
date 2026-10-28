s1_episodes = 10
s1_seconds_per_ep = (45 * 60) + 35
total_s1_seconds = s1_episodes * s1_seconds_per_ep

s2_5_seasons = 4
s2_5_episodes = s2_5_seasons * 10
s2_5_seconds_per_ep = (35 * 60) + 15
total_s2_5_seconds = s2_5_episodes * s2_5_seconds_per_ep

total_seconds = total_s1_seconds + total_s2_5_seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")