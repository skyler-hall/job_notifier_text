# Skyler's job scraper to text 8/20/26
import urllib.request
import json
import sqlite3
import smtplib
from email.message import EmailMessage
from pathlib import Path

simplify_url = "https://raw.githubusercontent.com/SimplifyJobs/New-Grad-Positions/dev/README.md"
jobright_url = "https://raw.githubusercontent.com/jobright-ai/2026-Business-Analyst-New-Grad/master/README.md"

job_board = urllib.request.urlopen(jobright_url)

data = job_board.read()

text = data.decode("utf-8")
lines = text.splitlines()
job_lines = []
for line in lines:
    if "[" in line and line.strip().startswith("|"):
        job_lines.append(line)

print(len(job_lines))
print(job_lines[0])

parts = job_lines[0].split("|")
info = []
for category in parts:
    info.append(category.strip().strip("*"))
print(info)

test = "[Marshall+Sterling](https://www.marshallsterling.com/)"
open_bracket = test.find("[")
close_bracket = test.find("]")
print(open_bracket)
print(close_bracket)

company_name = test[open_bracket + 1 : close_bracket]
print(company_name)

open_paren = test.find("(")
close_paren = test.find(")")
url = test[open_paren + 1 : close_paren]
print(url)