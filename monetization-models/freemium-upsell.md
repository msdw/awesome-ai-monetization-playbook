# Freemium and Upsell

## Overview

Freemium is a distribution strategy where a product is offered free with usage limits or feature restrictions, and users can upgrade to a paid tier for more capacity, features, or integrations. It is not a standalone monetization model — it is a conversion funnel that leads to subscription or usage-based revenue.

AI-powered freemium products are common because the marginal cost of serving additional free users is relatively low (especially for lightweight AI features), and free usage creates habit before the upgrade ask.

Freemium works best when the product has strong individual utility, generates habit quickly, and has a clear paid tier that delivers meaningfully more value than the free tier.

## Best For

- AI productivity tools with individual and team usage patterns
- AI writing, summarization, or research tools
- AI scheduling or meeting intelligence tools
- AI developer tools and code assistants
- AI image or media generation tools with daily creation limits

## Pricing Structure

Typical freemium tier structures for AI products:

- Free tier: limited usage (e.g., 50 requests/month, 5 documents, 1 project)
- Pro tier: $12–$40/month per user (higher limits, priority access, integrations)
- Team tier: $30–$80/user/month (collaboration, admin controls, shared workspaces)
- Enterprise: custom pricing with SSO, compliance, SLA, and volume pricing

Conversion from free to paid typically ranges from 2–8% for consumer tools and 5–15% for B2B tools with strong team utility. These are observed ranges from publicly discussed SaaS benchmarks.

The free tier cost must be sustainable. LLM inference costs for free users can destroy margins if the free tier is too generous.

## Pros & Cons

**Pros**
- Lower acquisition friction — users try before buying
- Word-of-mouth distribution through free users who recommend the product
- Can build a large user base that converts to paid over time

**Cons**
- Free users cost money in infrastructure and support
- Conversion rates are typically low — the product must work at scale with many non-paying users
- Poorly designed free tier limits can create frustration rather than upgrade motivation
- Pricing the upgrade value incorrectly leads to low conversion

## Real-World Examples

- **Notion** — free plan with usage limits, paid plans with team features
- **Grammarly** — free grammar checking, paid AI writing assistance
- **Otter.ai** — free transcription minutes per month, paid tiers for more
- **GitHub Copilot** — individual free tier introduced alongside team subscriptions
- **Perplexity** — free search tier, Pro tier with more capable models

These are publicly known products used as illustrative references.

## How to Implement

1. Define what free users get and model the cost per free user before launching
2. Design the free tier to create habit and show value without fully satisfying power users
3. Set paid tier limits at thresholds where engaged users naturally run out of free capacity
4. Build clear in-product upgrade prompts at the moment users hit free tier limits
5. Track activation rate (users who reach the "aha moment") before tracking conversion rate
6. Measure the cost per free user monthly — adjust free tier generosity if costs are unsustainable
7. Experiment with the paid tier price — freemium conversion is highly sensitive to price
8. Create a team tier with collaboration features to drive B2B expansion revenue

## Common Mistakes

- Making the free tier too generous — users never need to upgrade
- Making the free tier too restrictive — users leave before experiencing value
- Not modeling free user infrastructure cost — can create unsustainable unit economics
- No clear upgrade path from within the product
- Treating freemium as a complete business model rather than a conversion funnel
- Not tracking why users do not convert — conversion is improved by understanding objections
