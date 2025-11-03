
import random
import csv
import sys

# Basic Purchase Simulator
# Author: Jamal Omosun 26'

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

def prompt_end_shopping():
    # Returns True if the user wants to end shopping
    return prompt_yes_no("Do you want to end the shopping experience now?")


def format_money(x):
    return f"${x:,.2f}"

def get_user_info():
    name = input("What's your name? ").strip()
    balance = prompt_float("Enter your current balance: ")
    return name, balance

def choose_item(items, categories, prices):
    idx = random.randrange(len(items))
    return {
        "name": items[idx],
        "category": categories[idx],
        "base_price": prices[idx],
        "quality": random.choice(QUALITY),
    }


def display_offer(item, surcharge, total):
    print(f"Offer: {item['name']} ({item['quality']}) in {item['category']} for {format_money(item['base_price'])}")
    if surcharge > 0:
        print(f"  + {format_money(surcharge)} in installment charges from active payment plans")
    print(f"  -> TOTAL charge if purchased now: {format_money(total)}")


def apply_purchase(balance, total_price, active_plans):
    # Deduct total price
    balance = round(balance - total_price, 2)
    print(f"Purchased item for {format_money(total_price)}. New balance: {format_money(balance)}")
    # Decrement remaining installments and remove finished plans
    for plan in active_plans:
        if plan.get('remaining', 0) > 0:
            plan['remaining'] -= 1
    active_plans = [p for p in active_plans if p.get('remaining', 0) > 0]
    return balance, active_plans


def create_payment_plan_if_offered(item_name, base_price, active_plans):
    if base_price <= 35:
        return active_plans
    want_plan = prompt_yes_no(f"This item is over $35. Offer payment plan spreading a 30% increased cost over the next 3 purchases? ")
    if not want_plan:
        return active_plans
    extra_total = round(base_price * 0.30, 2)
    per_install = round(extra_total / 3, 2)
    # Use one plan object with remaining=3 and install equal to per_install (last cent differences ignored)
    active_plans.append({"remaining": 3, "install": round(extra_total / 3, 2), "source": item_name})
    print(f"Payment plan added: extra {format_money(extra_total)} spread as {format_money(round(extra_total/3,2))} over the next 3 purchases.")
    return active_plans


def post_purchase_deposit(balance):
    if prompt_yes_no("Would you like to deposit additional funds into your balance?"):
        dep = prompt_float("Enter amount to deposit: ", allow_zero=False)
        balance = round(balance + dep, 2)
        print(f"New balance: {format_money(balance)}")
    return balance

def calculate_surcharge(active_plans):
    return sum(p['install'] for p in active_plans if p['remaining'] > 0)

def ensure_funds(balance, total_price):
    while balance < total_price:
        print(f"Insufficient funds. You have {format_money(balance)}, need {format_money(total_price)}.")
        add = input("Enter amount to deposit or 'c' to cancel purchase: ").strip().lower()
        if add == 'c':
            print("Purchase cancelled.")
            return balance, False
        try:
            amt = float(add)
            if amt <= 0:
                print("Enter a positive amount to deposit.")
                continue
            balance += amt
            print(f"Deposited {format_money(amt)}. New balance: {format_money(balance)}")
        except ValueError:
            print("Enter a valid number or 'c'.")
    return balance, True


def main():
    print("Basic Purchase Simulator")

    name, balance = get_user_info()
    items, categories, prices = read_items("purchaseItems.csv")
    active_plans = []
    while True:
        item = choose_item(items, categories, prices)
        surcharge = calculate_surcharge(active_plans)
        total = round(item["base_price"] + surcharge, 2)
        display_offer(item, surcharge, total)
        if not prompt_yes_no("Buy?"):
            if prompt_end_shopping():
                print("Thank you for visiting the shop!")
                break
            continue
        balance, proceed = ensure_funds(balance, total)
        if not proceed:
            continue
        balance, active_plans = apply_purchase(balance, total, active_plans)
        active_plans = create_payment_plan_if_offered(item["name"], item["base_price"], active_plans)
        balance = post_purchase_deposit(balance)




if __name__ == '__main__':
    main()



