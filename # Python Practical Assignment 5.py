# Python Practical Assignment
# Topic: List and Tuple


# 1. Create a list of 5 Spotify song IDs
playlist_ids = [101, 205, 310, 415, 520]

print("1. Playlist IDs:", playlist_ids)


# 2. Add two more song IDs using append() and extend()

# append() adds one item
playlist_ids.append(625)

# extend() adds multiple items
playlist_ids.extend([730])

print("2. Updated Playlist IDs:", playlist_ids)


# 3. Remove the last played song using pop()

removed_id = playlist_ids.pop()

print("3. Removed Song ID:", removed_id)
print("   Remaining Playlist:", playlist_ids)


# 4. Create a tuple of Instagram filter names

insta_filters = ("Clarendon", "Juno", "Lark", "Valencia")

print("4. Instagram Filters:", insta_filters)

# Tuples are immutable, so changing an item gives an error.
# Uncomment the next line to see the error:
# insta_filters[0] = "Vintage"

# Error:
# TypeError: 'tuple' object does not support item assignment


# 5. List vs Tuple scenario

zomato_orders = ["Pizza", "Burger", "Biryani", "Pasta"]
ipl_teams = ("CSK", "MI", "RCB", "KKR", "GT")

# Zomato orders should use a LIST because orders can be added,
# removed, or changed.
#
# IPL team names should use a TUPLE because the fixed team names
# should not be changed accidentally.

print("5. Zomato Orders (List):", zomato_orders)
print("   IPL Teams (Tuple):", ipl_teams)