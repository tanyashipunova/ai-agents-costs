# Cost calculation for the model with four AI-agents adding a button to a web-site.

from decimal import Decimal

base_context = 50000
total_input_tokens = 120000
total_output_tokens = 6700
price_in_per_m = 3.0
price_out_per_m = 15.0

# Price to Decimal for financial accuracy
p_in_million = Decimal(str(price_in_per_m))
p_out_million = Decimal(str(price_out_per_m))

cost_in = (Decimal(total_input_tokens) / Decimal("1000000")) * p_in_million
cost_out = (Decimal(total_output_tokens) / Decimal("1000000")) * p_out_million
total_cost = cost_in + cost_out

print(f"Total session cost: ${total_cost:.4f}") # $0.4605
