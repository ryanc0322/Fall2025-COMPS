# import shoppingSimulator.py 
from shoppingSimulatorSol import *

def simulation():
    """
    Runs the shopping simulation.

    Steps:
    1. Greets the user and gets their name and initial balance.
    2. Loads product data from 'products.csv'.
    3. Enters a loop where:
        a. If balance is zero or negative, exits the loop.
        b. Applies  active payment plans to the balance.
        c. Offers a random product to the shopper.
        d. Applies a discount at random to the product price.
        e. Displays product details and current balance.
        f. Prompts the shopper to buy, see another product, or exit.
        g. If buying and price > $35, offers to create a payment plan.
        h. Updates balance and payment plans based on shopper actions.
        i. User continues shopping until they choose to exit or run out of funds.
    4. Thanks the user and displays their final balance upon exit.
    """

    print("------------------- Welcome to the Shopping Simulator! -------------------")

    # Shopper info, data loading, and initialize payment plans
    name = input("What's your name? ").strip()
    while True:
        balance_input = input("Enter your current balance: ").strip()
        try:
            balance = float(balance_input)
            if balance < 0:
                print("Invalid input. Balance can't be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Balance must be a number.")

    products, categories, prices = read_items("products.csv")
    payment_plans = []

    while True:

        # Check if balance is zero
        if balance <= 0:
            print("You have no money left! Please come back with more funds.")
            break

        # Apply active payment plans using the apply_payment_plans function
        if payment_plans:
            balance, payment_plans = apply_payment_plans(balance, payment_plans)
            total_payments_left = 0
            for plan in payment_plans:
                total_payments_left += plan['num_payments']
            # Print payment plan summary
            print(f"\n--- Payment Plans Applied ---")
            print(f"Remaining active plans: {len(payment_plans)}")
            print(f"Total payments left: {total_payments_left}")
            print(f"New balance: ${balance:.2f}")
            print("-----------------------------\n")

        # Offer a product using the offer_product function
        product = offer_product(products, categories, prices)
        # Apply discount using the discount function
        final_price, discount_flag = apply_discount(product['price'])
        # Display product details
        print(f"--------------------------- Product Offer ---------------------------")
        print(f"Offer: {product['name']} in {product['category']}")
        if discount_flag:
            print(f"DISCOUNT APPLIED! Original price: ${product['price']:.2f} -> Discounted price: ${final_price:.2f}")
        else:
            print(f"Price: ${final_price:.2f}")

        print(f"Your current balance: ${balance:.2f}")

        # Prompt shopper to buy, see another product, or exit
        while True:
            choice = input("Would you like to buy? (yes/no): ").strip().lower()
            if choice in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if choice == "yes":
            # Offer payment plan if price > $35
            if final_price > 35:
                while True:
                    plan_choice = input("This item qualifies for a payment plan! Set one up? (yes/no): ").strip().lower()
                    if plan_choice in ["yes", "no"]:
                        break
                    print("Please enter 'yes' or 'no'.")
                if plan_choice == "yes":
                    # Create payment plan using the create_payment_plan function
                    payment_plans = create_payment_plan(payment_plans, final_price)
                    plan = payment_plans[-1]
                    # Apply first payment using the apply_purchase function
                    balance = apply_purchase(balance, plan["payment_amount"])
                    print(f"Payment plan created: 3 payments of ${plan['payment_amount']:.2f}")
                else:
                    if balance >= final_price:
                        # Apply purchase using the apply_purchase function
                        balance = apply_purchase(balance, final_price)
                        print(f"Purchased {product['name']} for ${final_price:.2f}")
                    else:
                        print("Your balance is too low. Please come back with more funds.")
                        break
            else:
                if balance >= final_price:
                    # Apply purchase using the apply_purchase function
                    balance = apply_purchase(balance, final_price)
                    print(f"Purchased {product['name']} for ${final_price:.2f}")
                else:
                    print("Your balance is too low. Please come back with more funds.")
                    break

        elif choice == "no":
            while True:
                next_choice = input("Would you like to see a different product? (yes/no): ").strip().lower()
                if next_choice in ["yes", "no"]:
                    break
                print("Please enter 'yes' or 'no'.")
            if next_choice == "no":
                print(f"\nThank you for shopping, {name}! Final balance: ${balance:.2f}")
                break


def main():
    simulation()

if __name__ == "__main__":
    main()
