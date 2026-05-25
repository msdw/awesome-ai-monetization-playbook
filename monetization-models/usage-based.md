# Usage-Based Pricing

## Overview

Usage-based pricing charges customers in proportion to their consumption. Units can be API calls, tokens processed, documents analyzed, records enriched, pages converted, or any other measurable output. Revenue scales directly with customer activity.

This model aligns provider cost with customer value. When a customer gets more value, they pay more. When they use less, they pay less. This alignment makes adoption easier because buyers can start small before committing to higher spend.

Usage-based pricing requires metering infrastructure, real-time cost tracking, and careful margin management. It is not suitable for early-stage builders who cannot yet predict usage patterns.

## Best For

- AI API products serving developers or technical teams
- Document processing services (OCR, extraction, classification)
- AI translation, summarization, or transcription at scale
- Data enrichment pipelines processing large contact or product datasets
- AI image generation or media processing tools
- Any workflow where value is clearly proportional to volume

## Pricing Structure

Common unit types and observed market ranges:

- Per API call: $0.001–$0.05 per request
- Per token (LLM): $0.50–$15.00 per million tokens (varies widely by model)
- Per document: $0.01–$0.50 per document depending on complexity
- Per record: $0.005–$0.10 per enriched record
- Per page: $0.01–$0.05 per processed page

Most usage-based products include a monthly minimum charge or a free tier with hard limits to establish a billing relationship.

Pricing hypotheses should be validated against actual cost per unit. Margin must be positive after LLM/API costs, hosting, and support.

## Pros & Cons

**Pros**
- Low barrier for new customers to try the product
- Revenue grows naturally with customer usage
- Pricing feels fair to customers who have variable workloads
- Customers with high volume can become significant revenue sources

**Cons**
- Revenue is unpredictable and can spike or drop sharply
- Requires metering infrastructure, billing systems, and usage dashboards
- Customers may churn when their project ends rather than staying for the next one
- Negative margin is possible if LLM costs are not modeled carefully

## Real-World Examples

- **OpenAI API** — per-token pricing for language model access
- **AWS Textract** — per-page pricing for document text extraction
- **Deepgram** — per-minute pricing for speech transcription
- **Replicate** — per-second or per-run pricing for AI model inference
- **AssemblyAI** — per-audio-minute pricing for transcription and analysis

These examples are publicly known and illustrative. Verify current pricing directly before making business decisions.

## How to Implement

1. Define the measurable unit of value your product delivers
2. Model your cost per unit precisely — include LLM API, compute, storage, and support overhead
3. Set a price per unit that maintains a target margin (typically 60–80% for software)
4. Build or integrate usage metering (Stripe Metered Billing, AWS Billing, or custom)
5. Create a usage dashboard so customers can track their consumption in real time
6. Set spending limits or alerts to prevent surprise invoices that damage trust
7. Design a pricing page with a calculator that helps customers estimate monthly cost
8. Consider a free tier with a hard monthly cap to enable self-service trials

## Common Mistakes

- Setting per-unit prices without modeling actual API costs — can create negative margins
- No spending caps for customers — large unexpected invoices damage trust and create churn
- No usage visibility for customers — opacity creates anxiety and support tickets
- Treating high-usage customers as pure profit — high-volume customers often need more support
- Not tracking cohort retention — usage-based models can hide early-stage churn
- Underpricing to acquire customers and failing to raise prices later
