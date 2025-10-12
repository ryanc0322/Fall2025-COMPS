
import random
import csv
import sys

# Basic Purchase Simulator
# Author: Jamal Omosun (modified)

QUALITY = ["poor", "mediocre", "good", "excellent"]


def read_items(filename):
    items = []
    categories = []
    prices = []
    try:
        with open(filename, newline='') as fh:
            reader = csv.reader(fh)
            headers = next(reader, None)
            for row in reader:
                if len(row) < 3:
                    continue
                categories.append(row[0].strip())
                items.append(row[1].strip())
                try:
                    prices.append(float(row[2]))
                except ValueError:
                    prices.append(0.0)
    except FileNotFoundError:
        print(f"Could not find {filename}. Exiting.")
        sys.exit(1)
    return items, categories, prices


def prompt_float(prompt, allow_zero=False):
    while True:
        val = input(prompt).strip()
        try:
            f = float(val)
            if f < 0 or (not allow_zero and f == 0):
                print("Enter a positive number.")
                continue
            return f
        except ValueError:
            print("Please enter a valid number.")


def prompt_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ('y', 'yes'):
            return True
        if ans in ('n', 'no'):
            return False
        print("Please answer 'y' or 'n'.")


def format_money(x):
    return f"${x:,.2f}"


def main():
    print("Basic Purchase Simulator")

    name = input("What's your name? ").strip() or "Shopper"
    balance = prompt_float("Enter your current balance: ")

    filename = "purchaseItems.csv"
    items, categories, prices = read_items(filename)
    if not items:
        print("No items found in catalog. Exiting.")
        return

    # Active payment plans: each entry is dict {"remaining": int, "install": float, "source": str}
    active_plans = []

    print(f"Welcome, {name}. Starting balance: {format_money(balance)}")

    while True:
        print("\nCurrent balance:", format_money(balance))

        # Choose a random item
        idx = random.randrange(len(items))
        item_name = items[idx]
        category = categories[idx]
        base_price = prices[idx]
        quality = random.choice(QUALITY)

        # Calculate surcharge from active plans that still have installments remaining
        surcharge = sum(p['install'] for p in active_plans if p['remaining'] > 0)
        total_price = round(base_price + surcharge, 2)

        print(f"Offer: {item_name} ({quality}) in {category} for {format_money(base_price)}")
        if surcharge > 0:
            print(f"  + {format_money(surcharge)} in installment charges from active payment plans")
        print(f"  -> TOTAL charge if purchased now: {format_money(total_price)}")

        buy = prompt_yes_no("Do you want to buy this item?")
        if not buy:
            cont = prompt_yes_no("Do you want to continue shopping?")
            if not cont:
                print("Thanks for visiting. Goodbye.")
                break
            else:
                continue

        # Ensure balance sufficient, allow deposits until user cancels
        while balance < total_price:
            print(f"Insufficient funds. You have {format_money(balance)}, need {format_money(total_price)}.")
            add = input("Enter amount to deposit or 'c' to cancel purchase: ").strip().lower()
            if add == 'c':
                print("Purchase cancelled.")
                break
            try:
                amt = float(add)
                if amt <= 0:
                    print("Enter a positive amount to deposit.")
                    continue
                balance += amt
                print(f"Deposited {format_money(amt)}. New balance: {format_money(balance)}")
            except ValueError:
                print("Enter a valid number or 'c'.")
        else:
            # This block runs if while condition is False (i.e., balance >= total_price)
            # Deduct total_price
            balance = round(balance - total_price, 2)
            print(f"Purchased {item_name} for {format_money(total_price)}. New balance: {format_money(balance)}")

            # Apply installment decrements for plans that were charged this purchase
            for plan in active_plans:
                if plan['remaining'] > 0:
                    plan['remaining'] -= 1
            # Remove finished plans
            active_plans = [p for p in active_plans if p['remaining'] > 0]

            # Offer a payment plan for expensive items (> $35)
            if base_price > 35:
                want_plan = prompt_yes_no(f"This item is over $35. Offer payment plan spreading a 30% increased cost over the next 3 purchases? ")
                if want_plan:
                    extra_total = round(base_price * 0.30, 2)
                    per_install = round(extra_total / 3, 2)
                    # To ensure total extra sums to extra_total, adjust last installment
                    installs = [per_install, per_install, extra_total - 2 * per_install]
                    # Create plan entries where the per-installment will be applied across the next 3 purchases
                    for amt in installs:
                        active_plans.append({"remaining": 1, "install": amt, "source": item_name})
                    # But this representation applies each as a single-install plan over next 3 purchases; to keep tracking
                    # We instead want a plan that ticks down 3 times; convert to single plan that will charge "per_install" three times
                    # We'll simplify by creating one plan object with remaining=3 and install=round(extra_total/3,2)
                    # (Replace what we just appended)
                    active_plans = [p for p in active_plans if p.get('source') != item_name]
                    active_plans.append({"remaining": 3, "install": round(extra_total / 3, 2), "source": item_name})
                    print(f"Payment plan added: extra {format_money(extra_total)} spread as {format_money(round(extra_total/3,2))} over the next 3 purchases.")

            # After each purchase, prompt user to optionally add funds
            if prompt_yes_no("Would you like to deposit additional funds into your balance?"):
                dep = prompt_float("Enter amount to deposit: ", allow_zero=False)
                balance = round(balance + dep, 2)
                print(f"New balance: {format_money(balance)}")

        # End of purchase handling

    # End while


if __name__ == '__main__':
    main()



