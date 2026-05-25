# Cost-Plus Pricing

Cost-plus pricing sets a price by adding a target margin to the fully loaded cost of delivery. It is not the recommended primary approach for AI services, but it is a useful sanity check to ensure your prices are above the cost floor.

## How to calculate cost-plus pricing

For a service, identify all delivery costs:

| Cost Component | Example |
|---|---|
| LLM API cost | $0.50 per document processed |
| Infrastructure | $2/month allocated per client |
| Human review time | 2 hours at $60/hour = $120/delivery |
| Client communication | 1 hour/month at $60/hour = $60 |
| Tools and software | $15/month allocated per client |
| **Total cost** | **$197.50/delivery** |

Apply a target margin:
- 50% gross margin: price = $197.50 / (1 - 0.50) = $395
- 60% gross margin: price = $197.50 / (1 - 0.60) = $494
- 70% gross margin: price = $197.50 / (1 - 0.70) = $659

## When cost-plus pricing is useful

Cost-plus pricing is useful as a floor check:
- It tells you the minimum price to avoid losing money
- It helps identify if your costs are too high for your target price
- It reveals where cost reduction would most improve margins

## When cost-plus pricing is not sufficient

Cost-plus pricing as the sole pricing method has significant problems:
- It underprices when buyer value is much higher than delivery cost
- It ignores competitive context and buyer willingness to pay
- AI efficiency gains should benefit the provider, not automatically reduce prices
- It does not account for the value of repeatability — your 10th delivery should cost less than your first, but the buyer's value does not change

## Use cost-plus as a floor, value-based as the target

The recommended approach is to calculate your cost floor using cost-plus pricing, and then set your actual price based on buyer value. If the value-based price is significantly above your cost floor, that is margin and business sustainability — not a problem to fix by lowering the price.

## LLM cost modeling tips

LLM API costs change frequently and vary significantly by model and provider. Model your costs conservatively:
- Use the cost of the model you plan to deploy, not the cheapest available alternative
- Include retry costs and failed calls — not every API call succeeds
- Model peak usage, not average usage, to avoid surprises
- Track actual LLM costs per client per month and compare to estimates
