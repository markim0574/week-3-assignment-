def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount percentage must be non-negative.")
    # Call the function
    final_price = calculate_discount(price, discount_percent)
    # Display result
    print("Final Price: ", final_price)
except ValueError as e:
    print("Invalid input:", e)
