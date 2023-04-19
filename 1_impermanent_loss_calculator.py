# Author: CryptoLead at https://www.cryptolead.xyz
# Date: 2023-04-17
# Message: Hey there fellow coders! If you found my code helpful and want to show your support, consider buying me a coffee or two. Your donations help me keep improving the code and creating more awesome stuff for the community. Thanks for your support!
# Donation: cryptolead.eth or 0xa2c35DA418f52ed89Ba18d51DbA314EB1dc396d0

from math import sqrt

# Input parameters
initial_token_a_price = 100
initial_token_b_price = 1
initial_token_a_quantity = 1

final_token_a_price = 200
final_token_b_price = 1

# Impermanent loss calculation, based on 2 fomulas
# 1) Equal value of LP token-pair: after change in price, both assets must be equal in value (price * quantity)
# 2) Constant product formula: after change in price, quantities of A and B in the pool remains constant, regardless of the changes in their individual prices

# Find initial quantity of token b; and initial product of token a and token b
initial_price_ratio = initial_token_a_price / initial_token_b_price
initial_token_b_quantity = (
    initial_token_a_price * initial_token_a_quantity
) / initial_token_b_price
k = initial_token_a_quantity * initial_token_b_quantity

print("Price of Token A at time_1:", initial_token_a_price)
print("Quantity of Token A at time_1:", initial_token_a_quantity)
print(
    "Total value of Token A in LP pool at time_1:",
    initial_token_a_price * initial_token_a_quantity,
)
print()
print("Price of Token B at time_1:", initial_token_b_price)
print("Quantity of Token B at time_1:", initial_token_b_quantity)
print(
    "Total value of Token B in LP pool at time_1:",
    initial_token_b_price * initial_token_b_quantity,
)
print()
print("Price tatio at time_1:", initial_price_ratio)
print(
    "Total value of both tokens in LP pool at time_1:",
    (initial_token_a_price * initial_token_a_quantity)
    + (initial_token_b_price * initial_token_b_quantity),
)
print("Constant K in constant product formula:", k)

# (quantity of token a) * (quantity of token b) = k
# (price ratio of token a) = (quantity of token b)/(quantity of token a)
# Derivation using the above two formulas:
# 1.1) (quantity of token a) = k/(quantity of token b)
# 1.2) Because, (quantity of token b) = (price ratio of token a) * (quantitfy of token a)
# 1.3) Thus, (quantity of token a) = k/((price ratio of token a) * (quantitfy of token a))
# 1.4) (quantity of token a)^2 = k/(price ratio of token a)
# 1.5) Finally, (quantity of token a) = sqrt(k/(price ratio of token a))

# 2.1) (quantity of token b) = k/(quantity of token a)
# 2.2) Because, (quantity of token b) = (price ratio of token a) * (quantitfy of token a)
# 2.3) Thus, (quantity of token b)^2 = (price ratio of token a) * (quantitfy of token a) * k/(quantity of token a)
# 2.4) Finally, (quantity of token b) = sqrt(k*(price ratio of token a))

# Factor into the change in price
initial_token_a_quantity_check = sqrt(k / initial_price_ratio)
initial_token_b_quantity_check = sqrt(k * initial_price_ratio)

assert initial_token_a_quantity == initial_token_a_quantity_check
assert initial_token_b_quantity == initial_token_b_quantity_check

final_price_ratio = final_token_a_price / final_token_b_price
final_token_a_quantity = sqrt(k / final_price_ratio)
final_token_b_quantity = sqrt(k * final_price_ratio)

print()
print("Price of Token A at time_2:", final_token_a_price)
print("Quantity of Token A at time_2:", final_token_a_quantity)
print(
    "Total value of Token A in LP pool at time_2:",
    final_token_a_price * final_token_a_quantity,
)
print()
print("Price of Token B at time_2:", final_token_b_price)
print("Quantity of Token B at time_2:", final_token_b_quantity)
print(
    "Total value of Token B in LP pool at time_2:",
    final_token_b_price * final_token_b_quantity,
)
print()
print("Price tatio at time_2:", final_price_ratio)
print(
    "Total value of both tokens in LP pool at time_2:",
    (final_token_a_price * final_token_a_quantity)
    + (final_token_b_price * final_token_b_quantity),
)
print("Constant K in constant product formula:", k)


# Option 1 - impermanent loss calculation
# Subtract the total LP pool value for hodling the original tokens with new prices by the total LP pool value from providing LP
impermanant_loss_in_value = (
    (final_token_a_price) * (final_token_a_quantity)
    + (final_token_b_price) * (final_token_b_quantity)
) - (
    (final_token_a_price) * (initial_token_a_quantity)
    + (final_token_b_price) * (initial_token_b_quantity)
)
impermanent_loss_in_percent = impermanant_loss_in_value / (
    (final_token_a_price) * (initial_token_a_quantity)
    + (final_token_b_price) * (initial_token_b_quantity)
)

print()
print("Impermanent loss in value:", impermanant_loss_in_value)
print("Impermanent loss in percent:", impermanent_loss_in_percent)


# Option 2 - impermanent loss calculation
# Once you have the change in price ratio, you can plug it into this formula and compute IL directly
def impermanent_loss_calculator(initial_token_price, final_token_price):
    price_ratio = final_token_price / initial_token_price
    return (2 * sqrt(price_ratio)) / (1 + price_ratio) - 1


print()
print(
    "Impermanent loss in percent:",
    impermanent_loss_calculator(initial_token_a_price, final_token_a_price),
)

