from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import subprocess
import sys
import pandas as pd
import os
import json
import glob

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 🔥 Track last generated report
last_report = {
    "excel": None,
    "pdf": None
}


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": {"High": 0, "Medium": 0, "Low": 0},
        "stride": {},
        "ai_threats": []
    })


# 🔥 Helper → Get latest file
def get_latest_file(pattern):
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getctime)


@app.post("/generate")
def generate(request: Request, ecu: str = Form(...), interface: str = Form(...)):

    result = subprocess.run(
        [sys.executable, "main.py", ecu, interface],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return JSONResponse({"error": result.stderr}, status_code=500)

    # 🔥 Get latest generated files
    excel_file = get_latest_file(f"tara_{ecu}_{interface}_*.xlsx")
    pdf_file = get_latest_file(f"tara_{ecu}_{interface}_*.pdf")

    if not excel_file:
        return JSONResponse({"error": "Excel not generated"}, status_code=500)

    # 🔥 Save last report
    last_report["excel"] = excel_file
    last_report["pdf"] = pdf_file

    df = pd.read_excel(excel_file, sheet_name="TARA Results")

    summary = df["Risk Level"].value_counts().to_dict()
    summary.setdefault("High", 0)
    summary.setdefault("Medium", 0)
    summary.setdefault("Low", 0)

    stride = df["STRIDE"].value_counts().to_dict()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "stride": stride,
        "ai_threats": []
    })


@app.post("/ai_analyze")
def ai_analyze(request: Request, ecu: str = Form(...), interface: str = Form(...)):

    from ai_engine import generate_ai_threats

    with open("asset_library.json") as f:
        asset_library = json.load(f)

    assets = asset_library.get(ecu, [])

    if not assets:
        return JSONResponse({"error": f"No assets found for ECU: {ecu}"}, status_code=400)

    try:
        result = generate_ai_threats(ecu, interface, assets)
        threats = result.get("threats", [])
    except Exception as e:
        print(f"AI ERROR: {str(e)}")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "summary": {"High": 0, "Medium": 0, "Low": 0},
            "stride": {},
            "ai_threats": [],
            "error": str(e)
        })

    # 🔥 Run standard TARA also
    subprocess.run(
        [sys.executable, "main.py", ecu, interface],
        capture_output=True,
        text=True
    )

    # 🔥 Get latest files
    excel_file = get_latest_file(f"tara_{ecu}_{interface}_*.xlsx")
    pdf_file = get_latest_file(f"tara_{ecu}_{interface}_*.pdf")

    last_report["excel"] = excel_file
    last_report["pdf"] = pdf_file

    df = pd.read_excel(excel_file, sheet_name="TARA Results")

    summary = df["Risk Level"].value_counts().to_dict()
    summary.setdefault("High", 0)
    summary.setdefault("Medium", 0)
    summary.setdefault("Low", 0)

    stride = df["STRIDE"].value_counts().to_dict()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "stride": stride,
        "ai_threats": threats
    })


@app.get("/download_excel")
def download_excel():
    if not last_report["excel"]:
        return JSONResponse({"error": "Generate report first"}, status_code=400)

    return FileResponse(
        last_report["excel"],
        filename=os.path.basename(last_report["excel"])
    )


@app.get("/download_pdf")
def download_pdf():
    if not last_report["pdf"]:
        return JSONResponse({"error": "Generate report first"}, status_code=400)

    return FileResponse(
        last_report["pdf"],
        filename=os.path.basename(last_report["pdf"])
    )