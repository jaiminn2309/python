# 1. Create and print the initial Instagram followers dictionary
insta_followers = {
    "virat.kohli": 270000000,
    "prajakta_koli": 5000000,
    "techburner": 3500000,
    "ranveer.allahbadia": 3000000,
    "kusha_kapila": 3300000,
}
print("1. Initial Instagram Followers:")
print(insta_followers)
print()


# 2. Add, update, and delete entries from the dictionary
insta_followers["carryminati"] = 10000000  # Add new influencer
insta_followers["techburner"] = 3800000  # Update existing follower count
del insta_followers["kusha_kapila"]  # Delete an influencer

print("2. Updated Instagram Followers:")
print(insta_followers)
print()


# 3. Display Zomato food items costing more than ₹200
food_prices = {
    "Paneer Butter Masala": 280,
    "Garlic Naan": 60,
    "Chicken Biryani": 320,
    "Veg Momos": 150,
    "Butter Chicken": 350,
}

print("3. Food items costing more than ₹200:")
for item, price in food_prices.items():
    if price > 200:
        print(f"- {item}: ₹{price}")
print()


# 4. Find common users on Flipkart and Myntra using set intersection
flipkart_users = {"aarav99", "rohit_sharma", "priya_m", "sneha_k", "dev_g"}
myntra_users = {"priya_m", "ananya_r", "rohit_sharma", "kabir_s", "neha_p"}

common_users = flipkart_users.intersection(myntra_users)
print("4. Users with accounts on both platforms:")
print(common_users)
print()


# 5. Function to get unique artists across two Spotify playlists
def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1 | spotify_playlist2


# Example usage for Question 5:
playlist_a = {"Arijit Singh", "AR Rahman", "Shreya Ghoshal"}
playlist_b = {"AR Rahman", "Diljit Dosanjh", "Pritam"}

all_unique_artists = get_unique_artists(playlist_a, playlist_b)
print("5. Unique artists across both playlists:")
print(all_unique_artists)