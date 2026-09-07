# 1. Calculate final price after applying a discount rate
def calculate_final_price(price, discount_rate):
    return price * (1 - discount_rate)


# 2. Get delivery charge based on city (default: Ahmedabad)
def get_delivery_charge(amount, city="Ahmedabad"):
    if city.lower() == "ahmedabad":
        return 0
    return 50


# 3. Format price string according to currency
def format_price(price, currency="INR"):
    if currency.upper() == "USD":
        return f"${price}"
    return f"₹{price}"


# 4. Apply 10% coupon discount if valid code is given
def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price * 0.90
    return price


# --- Example Test Calls ---
print("1. Final Price (Price 1000, 15% off):", calculate_final_price(1000, 0.15))
print("2. Delivery Charge (Ahmedabad):", get_delivery_charge(300))
print("2. Delivery Charge (Mumbai):", get_delivery_charge(300, "Mumbai"))
print("3. Formatted Price (INR):", format_price(500))
print("3. Formatted Price (USD):", format_price(500, "USD"))
print("4. Coupon ZOMATO10:", apply_coupon(500, "ZOMATO10"))
print("4. No Coupon:", apply_coupon(500))