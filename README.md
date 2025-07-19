
# AI Match Rule Generator

This tool intelligently suggests match rules for record deduplication using embeddings and GenAI. It is tailored for Informatica MDM, Customer 360, and other master data systems.

## 🚀 Project Overview
Defining matching rules manually can be error-prone and time-consuming. This AI-powered solution analyzes your dataset and proposes optimal match configurations (e.g., field importance, fuzzy logic, and weights) using LLMs and statistical similarity.

## 🔧 Features
- Accepts structured CSV input (Customer/Party data)
- Suggests matching strategies: exact, fuzzy, weighted
- Uses LLM prompts to auto-generate match rule logic
- Output ready to be used in MDM or IDMC pipelines

## 📊 Input Format
- CSV with fields: CustomerID, Name, Email, Phone, Address, etc.

## 🧠 Technologies Used
- Python, Pandas
- OpenAI API (or use dummy mode with local logic)
- Faker for test data generation
- Streamlit (optional UI for demo)

## 🛠 Setup

```bash
pip install -r requirements.txt
python generate_rules.py
```

## 📤 Output
- JSON file with suggested match rules
- Explanation of field matching logic

## 💡 Example

| Field     | Rule Type | Weight | Notes                    |
|-----------|-----------|--------|--------------------------|
| Name      | Fuzzy     | 0.4    | Use Levenshtein distance |
| Email     | Exact     | 0.3    | Case-insensitive match   |
| Phone     | Exact     | 0.2    | Strip special characters |
| Address   | Fuzzy     | 0.1    | Token-based matching     |

---

> Built with ❤️ by Vaishnavi Sohani — AI-Powered Data Integration Lead
