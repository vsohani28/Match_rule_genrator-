
import pandas as pd
import json

# Load dataset
df = pd.read_csv("sample_data.csv")

# Define simple rule logic
rules = []
for col in df.columns:
    rule = {"field": col}
    if "id" in col.lower():
        rule.update({"rule": "Exact", "weight": 0.0, "notes": "Unique identifier"})
    elif "name" in col.lower():
        rule.update({"rule": "Fuzzy", "weight": 0.4, "notes": "Use Levenshtein distance"})
    elif "email" in col.lower():
        rule.update({"rule": "Exact", "weight": 0.3, "notes": "Case-insensitive match"})
    elif "phone" in col.lower():
        rule.update({"rule": "Exact", "weight": 0.2, "notes": "Strip special characters"})
    elif "address" in col.lower():
        rule.update({"rule": "Fuzzy", "weight": 0.1, "notes": "Token-based match"})
    else:
        rule.update({"rule": "Custom", "weight": 0.1, "notes": "Review manually"})
    rules.append(rule)

# Save rules
with open("match_rules.json", "w") as f:
    json.dump(rules, f, indent=4)

print("✅ Match rules generated and saved to match_rules.json")
