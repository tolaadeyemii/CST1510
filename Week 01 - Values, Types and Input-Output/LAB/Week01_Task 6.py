weeks_per_year = 52
total_weeks = weeks_per_year * 3
savings = 10 * total_weeks
savings += 20 * weeks_per_year
savings -= 0.50 * (total_weeks // 2)
print(f"Final savings after 3 years: £{savings:.2f}")
