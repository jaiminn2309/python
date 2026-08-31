# Python String Methods Assignment

# 1. Convert to lowercase and replace dash with space
text = 'Flipkart-Sale2024'

result = text.lower().replace('-', ' ')

print("1. Output:", result)


# 2. Clean the product name
product_name = ' OnePlus Nord-CE 3 '

result = product_name.strip().upper().replace('-', ':')

print("2. Output:", result)


# 3. Split product code into parts
def split_product_code(product_code):
    return product_code.split('-')

code = 'ZOMATO-FOOD-2024'

print("3. Output:", split_product_code(code))


# 4. Extract "Premium" using string slicing
text = 'Spotify_Premium_Offer'

premium = text[8:15]

print("4. Output:", premium)


# 5. Format and print the message
product = 'Myntra Shirt'
price = 799.5

print(f"5. Output: Deal: {product} is available at ₹{price:.2f} only!")