# ==========================================================
# Module 07 Lab: functions.py
#
# SELF-ASSESSMENT Q1:
#   I did not find the Exercise 5 bugs on my own. AI (Claude) identified
#   all three: total = sale overwrote the total instead of adding to it,
#   the second for loop was missing a colon (SyntaxError), and the while
#   loop used <= so it ran one index past the end (IndexError). This tells
#   me I need to practice reading tracebacks and adding print() statements
#   myself before reaching for AI.
#
# SELF-ASSESSMENT Q2:
#   apply_discount takes a price and a customer tier ("gold", "silver",
#   "bronze", or anything else) and returns the price after the tier's
#   discount: 15%, 10%, 5%, or 0%. A colleague could use it from the name
#   and inputs alone without reading the body.
#
# AI DISCLOSURE (Q3):
#   AI used: Claude wrote the code for Exercises 1 to 6, found and fixed
#   the bugs in Exercise 5, and drafted these comments. I reviewed and ran
#   the file. Using AI this way shortcut my understanding more than it
#   built it.
# ==========================================================


# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':<8}${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]

# Bug 1: total = sale replaced the total each loop, so it only kept the last sale.
# Fix: use += to add each sale to the running total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2: the for loop was missing its colon, which is a SyntaxError.
# Fix: add the colon at the end of the for line.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: i <= len(sales) let i reach 5, but the last index is 4 (IndexError).
# Fix: use < so the loop stops at the last valid index.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
# Scope: the x inside double_it is a local variable that only exists while
# the function runs. Setting it to 999 does not touch the global x, so the
# global x stays 100 before and after the function call.
x = 100   # global variable

def double_it():
    x = 999   # local variable
    return x * 2

print(x)
print(double_it())
print(x)
