# Hospital Assist Agent 🏥🤖

**Hospital Assist Agent** is an interactive assistant for hospital workflows — designed to help staff and patients with triage, appointment handling, patient information lookup, and clinician support using modern LLM tools and local interfaces.

---

## ✨ Highlights

- **Quick setup** with a virtual environment and `requirements.txt` ✅
- Built using **Streamlit** for a friendly web UI
- Integrates with **LangChain / LangGraph** and other LLM tooling for flexible agent workflows 💬
- Notebook demo included: `AnindaMy_langgraph.ipynb`

---

## 🔧 Features

- Symptom intake & triage guidance (configurable rules)
- Appointment scheduling and reminders
- Quick patient lookup and context-aware responses
- Extensible architecture for adding hospital-specific modules

> Note: Feature list is a starting point — customize to match your actual implementation.

---

## 🚀 Quickstart (Windows)

1. Clone the repo

```powershell
git clone <your-repo-url>
cd hospital_assist_agent
```

2. Create and activate the venv (the workspace includes `agenvenv` already if you prefer)

```powershell
python -m venv .\agenvenv
.\agenvenv\Scripts\activate
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

4. Run the app

```powershell
streamlit run app.py
```

Open the Streamlit URL in your browser (usually `http://localhost:8501`).

---

## ⚙️ Configuration

- Add API keys / secrets as environment variables (example names):
  - `GOOGLE_API_KEY` or provider key you use
  - `OPENAI_API_KEY` (if applicable)
- Configure any DB, email or calendar integrations in your project config (use `.env` or platform secrets)

> For local testing, store keys in a `.env` file and load them with `python-dotenv`.

---

## 🧪 Notebooks & Demos

- `AnindaMy_langgraph.ipynb` — demo notebook exploring LangGraph integrations and example prompts.

---

## 🛠️ Development

- Follow Python best practices and add unit tests where applicable
- Keep the `requirements.txt` updated when adding new packages

### Recommended commands

```powershell
# Run tests (if you add pytest)
pytest

# Linting
flake8 .
```

---

## 🤝 Contributing

- Feel free to open issues or PRs
- Add clear descriptions, tests, and update this `README.md` when adding features

---

## 📜 License

This project is currently unlicensed — add a `LICENSE` file (e.g., **MIT**) to make it open source.

---

## 📞 Contact

For questions or help: open an issue on GitHub or contact the repository owner.

---

Made with ❤️ — adapt and expand to suit your hospital's workflows.
