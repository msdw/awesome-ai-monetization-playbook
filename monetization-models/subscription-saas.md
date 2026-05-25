# Subscription SaaS

## Overview

Subscription SaaS is a software delivery model where customers pay a recurring fee — monthly or annually — to access a hosted AI-powered product. The software runs on the provider's infrastructure, and access continues as long as the subscription is active.

This model is appropriate when the AI capability delivers ongoing, recurring value. If the value is a one-time setup or transformation, a project fee or productized service is usually a better fit. Subscription SaaS works when users return to the product regularly and get measurable benefit from each session.

## Best For

- AI writing assistants and copywriting tools
- AI analytics dashboards and reporting platforms
- AI scheduling, meeting, or productivity tools
- AI-powered SEO, monitoring, or keyword research platforms
- AI document review and contract analysis tools
- AI customer support or triage platforms

This model is best suited for indie builders and startup founders who can develop and maintain a hosted product, rather than consultants or freelancers who deliver services directly.

## Pricing Structure

Typical ranges observed in the AI SaaS market:

- Entry tier: $19–$49/month (individual users, limited usage)
- Professional tier: $79–$199/month (small teams, higher limits)
- Team or business tier: $299–$599/month (multiple seats, integrations)
- Enterprise: custom pricing with SLA, security, and procurement

Annual billing typically offers a 15–25% discount over monthly.

Pricing should reflect the value delivered to the buyer — time saved, cost avoided, or revenue generated — not the complexity of the underlying model.

Pricing is a hypothesis. Every tier should be tested with real buyers and adjusted based on observed conversion rates and churn patterns.

## Pros & Cons

**Pros**
- Predictable, recurring revenue improves financial planning
- Infrastructure scales better than human-delivered services
- Product improvements benefit all users simultaneously
- Acquisition cost can be recovered over a multi-month relationship

**Cons**
- Churn must be managed continuously — a 5% monthly churn rate will collapse revenue
- Requires significant upfront product development before any revenue
- Sales cycles can be long without a self-serve free trial
- LLM API costs must be accurately modeled into margin calculations

## Real-World Examples

- **Jasper** — AI writing tool with subscription pricing for marketers
- **Copy.ai** — AI copy generation with a free tier and paid tiers
- **Otter.ai** — AI meeting transcription sold as a monthly subscription
- **Notion AI** — AI features added as a subscription add-on to an existing product
- **Perplexity** — AI search with a free tier and a Pro subscription

These are publicly known companies used as illustrative references. Pricing details change and should be verified directly.

## How to Implement

1. Define the core recurring value the product delivers (what keeps users coming back)
2. Choose a narrow initial audience — one specific buyer type with a clear recurring problem
3. Build a minimum viable version focused on the one workflow that drives retention
4. Set up payment infrastructure (Stripe is standard) with monthly and annual billing
5. Implement usage metering if your costs are variable (token usage, API calls)
6. Create a free trial or limited free tier to reduce acquisition friction
7. Track monthly churn rate, activation rate, and LTV from day one
8. Model LLM API costs carefully before setting prices — margin can erode quickly at scale

## Common Mistakes

- Setting prices based on AI complexity rather than buyer value
- Offering unlimited usage without modeling API costs — this creates negative margins at scale
- Launching without a retention mechanism — acquisition without retention produces rapid churn
- Skipping a free trial, which increases the barrier to conversion for self-serve products
- Ignoring churn until it becomes a crisis — monitor churn weekly from the start
- Building enterprise features before validating with smaller buyers
- Treating the subscription model as inherently recurring — renewal must be earned, not assumed
