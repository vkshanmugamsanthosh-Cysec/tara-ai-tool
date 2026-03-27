\# AI-Powered Automotive TARA Tool



An automated Threat Analysis \& Risk Assessment (TARA) platform aligned with \*\*ISO/SAE 21434\*\* and \*\*UNECE R155/R156\*\*.



\## Features



\- Automated asset identification with CIA property mapping

\- STRIDE-based threat generation per asset

\- Impact scoring — Safety, Financial, Operational, Privacy (ISO/SAE 21434 Clause 15)

\- Attack feasibility calculation (HEAVENS-inspired)

\- Cybersecurity Goal (CSG) and Requirement (CSR) auto-generation

\- AI-powered threat scenarios using Claude API

\- Excel report — TARA Results + ISO Standards reference sheet

\- PDF report export

\- Web dashboard with risk summary and STRIDE distribution chart



\## Tech Stack



\- Python 3.11

\- FastAPI + Jinja2 (web backend)

\- Claude AI API (threat intelligence)

\- pandas + openpyxl (Excel generation)

\- ReportLab (PDF generation)

\- Chart.js (dashboard charts)



\## Supported ECUs



ESCL, BMS, TCU, ADAS, Gateway, Infotainment



\## Supported Interfaces



CAN, OTA, Bluetooth



\## Installation



1\. Clone the repository

&nbsp;  git clone https://github.com/yourusername/tara-ai-tool.git

&nbsp;  cd tara-ai-tool



2\. Create virtual environment with Python 3.11

&nbsp;  py -3.11 -m venv venv

&nbsp;  venv\\Scripts\\activate



3\. Install dependencies

&nbsp;  pip install -r requirements.txt



4\. Add your API key

&nbsp;  Create a .env file and add:

&nbsp;  ANTHROPIC\_API\_KEY=your-key-here



5\. Run the server

&nbsp;  python -m uvicorn api:app --port 8001



6\. Open browser

&nbsp;  http://127.0.0.1:8001



\## Usage



1\. Select ECU and Interface from the dashboard

2\. Click Generate TARA for standard ISO 21434 analysis

3\. Click AI Analyze for AI-powered threat scenarios

4\. Download Excel or PDF report



\## Standards Alignment



\- ISO/SAE 21434 — Cybersecurity Engineering

\- UNECE R155 — Cyber Security Management System

\- STRIDE — Threat Modeling Methodology

\- HEAVENS — Attack Feasibility Assessment



\## Author



Santhosh S — Automotive Cybersecurity Engineer

LinkedIn: linkedin.com/in/santhosh-shanmugamsanthosh

