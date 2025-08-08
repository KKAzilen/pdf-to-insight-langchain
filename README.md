# PDF to Insight with LangChain

Extract insights from PDFs using LangChain and OpenAI in just 3 files.  

This project is built for real-world enterprise use cases—like HR policies, vendor contracts, and compliance documents—where quick access to summarized information creates business value.

---

## Setup Instructions

1. Clone this repository  
2. Install required packages:

```bash
pip install langchain openai pypdf
```

3. Set your OpenAI API key in `extractor.py`:

```python
os.environ["OPENAI_API_KEY"] = "your-key"
```

4. Run the script:

```bash
python extractor.py
```

---

## Files Overview

| File           | Description                                                     |
|----------------|-----------------------------------------------------------------|
| `extractor.py` | Core logic to load PDF, chunk it, and extract insight via OpenAI |
| `sample.pdf`   | Sample enterprise document for testing                          |
| `README.md`    | You’re here — setup, usage, and service links                   |

---

## Enterprise Use Cases

- HR document summarization (e.g., onboarding policies)
- Vendor contract triage and comparison
- Compliance document insight extraction
- Internal knowledge base automation

---

## Related Resources from Azilen

- 🔗 [AI Agent Development Services →](https://www.azilen.com/ai-agents-development-services/)  
  *Explore how we build autonomous AI agents tailored for enterprise workflows.*

- 🧠 [AI Agents in HRTech](https://www.azilen.com/blog/ai-agents-in-hr-tech/)  
  *Discover 10 most-asked questions on AI Agents in HRTech, from use cases and cost to build timelines, real examples, and where to start.*

---  

## Note

This is a guide/demo repository. You must replace `"your-openai-api-key"` in `extractor.py` with your own OpenAI API key to run the script.

---

Built by the AI Engineering team at [Azilen Technologies](https://www.azilen.com)
