# Automated Code Correction

An AI-powered debugging framework that detects, explains, and corrects errors in Python programs using large language models (LLMs). This modular system leverages LangChain and LangGraph to streamline the debugging workflow.

##  Features

- Automated error detection and correction
- Integration with LLMs (Gemini)
- Custom tools for analyzing code defects
- Modular, maintainable structure
- Batch processing of buggy programs

## Repository Structure

| File / Folder       | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `main.py`           | Entry point for running the correction workflow on individual programs     |
| `agents.py`         | Defines LLM-based agents responsible for analyzing and fixing code          |
| `workflow.py`       | Coordinates the interaction between tools and agents using LangGraph       |
| `config.py`         | Sets up API keys, constants like defect types, and program lists            |
| `fetchers.py`       | Retrieves buggy code and related metadata                                   |
| `save.py`           | Saves fixed code and logging output to appropriate directories              |
| `utils.py`          | Utility functions shared across the modules                                |
| `process_all.py`    | Script to apply correction logic to a batch of programs                    |
| `fixed_programs/`   | Contains output from the correction process                                |
| `requirements.txt`  | Python dependencies required to run the project                            |
| `docs/Overview.pdf` | Full project report or documentation in PDF format                         |

## 📄 Full Documentation

For the complete explanation of the system architecture, design choices, and evaluation, see the (https://drive.google.com/file/d/1MFFHXjg3rHmcgKSBSwgjt3ulb5QZdJ6Z/view?usp=sharing).

## 🛠️ Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/hafsah-006/Automated-Code-Correction.git
   cd Automated-Code-Correction
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Configure your environment**
Set your API keys (e.g., Gemini) via environment variables or .env file, as expected by config.py.
4. **Run the correction pipeline**
   ```bash
   python main.py
5. **To Batch Process Programs**
   ```bash
   python process_all.py


