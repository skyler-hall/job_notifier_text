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
    if "[" in line:
        job_lines.append(line)

print(len(job_lines))
print(job_lines[0])