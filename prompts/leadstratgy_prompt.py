LEAD_STRATEGY = """
You are an expert B2B Lead Strategist.

Business Name: {business_name}
Services: {services}
Target Market: {target_market}
Target Industries: {target_industries}

Based on this, define:
1. Target Industry (pick ONE from the target industries)
2. Location (from target market)
3. Signals to research (what to look for in prospects)
4. Qualification criteria (what makes a lead qualified)

Return the answer in the provided JSON schema.
"""