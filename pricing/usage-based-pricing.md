# Usage-Based Pricing for AI Products

Usage-based pricing charges customers in proportion to their consumption of your AI product. This page covers the mechanics, tradeoffs, and implementation details specific to AI products.

## Unit selection

Choose a unit that directly represents value delivered to the buyer:

| AI product type | Appropriate unit |
|---|---|
| Transcription | Per audio minute |
| Document processing | Per page or per document |
| Text classification | Per record or per API call |
| Language model completion | Per token or per request |
| Image generation | Per image or per generation |
| Data enrichment | Per record enriched |

Avoid units that feel arbitrary to the buyer. If the buyer cannot connect the unit to value, billing feels opaque.

## Cost modeling for usage-based pricing

Before setting a per-unit price, calculate your cost per unit:

1. Measure the average LLM or API cost per unit in production
2. Add compute and infrastructure overhead allocated per unit
3. Add human review cost if spot-checking is part of the service
4. Add a support and operations overhead allocation
5. Apply target margin (typically 60–80% for software products)

If your cost per unit is $0.02 and you target 70% gross margin:
Price per unit = $0.02 / (1 - 0.70) = $0.067, rounded to $0.07/unit

## Volume tiers and committed use discounts

Most usage-based pricing includes volume discounts:
- Pay-as-you-go (no commitment): standard per-unit rate
- Prepaid bundle (commit to 10,000 units): 15–25% discount
- Annual commitment (commit to 100,000+ units): 30–40% discount

Volume tiers reward high-usage customers and create revenue predictability. They also encourage buyers to estimate their usage upfront.

## Spending limits and notifications

Always implement:
- Spending alerts when a customer reaches a defined threshold
- Hard or soft spending limits to prevent invoice shock
- Real-time usage dashboards so customers can track consumption

Surprise invoices — even justified ones — damage trust and create churn. Buyers should always know what they are spending.

## Minimum monthly charges

Consider a minimum monthly charge (e.g., $15–$50/month regardless of usage) to:
- Cover infrastructure costs for low-usage customers
- Establish a billing relationship before the customer becomes active
- Reduce the administrative overhead of billing very small amounts

## Metering infrastructure

Usage-based billing requires metering infrastructure. Common approaches:
- Stripe Metered Billing for SaaS products
- Custom metering with usage events sent to billing systems
- Third-party platforms (Orb, Lago, Metronome) for complex usage models

Choose metering infrastructure before launch — retrofitting it to an existing product is difficult.

Pricing is a hypothesis. Usage-based prices should be reviewed quarterly based on observed cost per unit and customer usage patterns.
