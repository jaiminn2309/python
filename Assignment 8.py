# 1. Print 5 favorite food delivery apps using a for loop
apps = ["Zomato", "Swiggy", "Eatsure", "Blinkit", "Zepto"]

print("1. Favorite Food Delivery Apps:")
for app in apps:
    print(app)
print("-" * 40)


# 2. Find the first day crossing 10,000 steps using a while loop
step_counts = [4500, 7800, 9200, 11500, 8900, 12000, 6000]

day_index = 0
while day_index < len(step_counts):
    if step_counts[day_index] > 10000:
        print(f"2. Crossed 10,000 steps on Day {day_index + 1} ({step_counts[day_index]} steps)")
        break
    day_index += 1
print("-" * 40)


# 3. Print IPL team names longer than 6 characters using continue
def filter_ipl_teams(teams):
    print("3. IPL Teams with names longer than 6 characters:")
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)

ipl_teams = ["MI", "CSK", "RCB", "Kolkata Knight Riders", "Rajasthan Royals", "GT", "Sunrisers Hyderabad"]
filter_ipl_teams(ipl_teams)
print("-" * 40)


# 4. Print song positions and durations using enumerate
song_durations = [210, 185, 240, 195, 300]

print("4. Spotify Song Durations:")
for index, duration in enumerate(song_durations, start=1):
    print(f"Song {index}: {duration} seconds")
print("-" * 40)


# 5. Shopping cart total calculator using break and continue
cart_prices = [350, 0, 450, 1200, 800, 150]

running_total = 0
for price in cart_prices:
    if price == 0:
        continue  # Skip out-of-stock items
    
    if running_total + price > 2000:
        break  # Stop adding if running total crosses ₹2000
    
    running_total += price

print(f"5. Final Shopping Cart Total: ₹{running_total}")