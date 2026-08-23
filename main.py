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



all_jobs = []
for job_row in job_lines:
    parts = job_row.split("|")
    info = []
    for category in parts:
        info.append(category.strip().strip("*"))
    all_jobs.append(info)


def extract_name_and_link(raw_field):
    open_bracket = raw_field.find("[")
    close_bracket = raw_field.find("]")
    company_name = raw_field[open_bracket + 1 : close_bracket]
    open_paren = raw_field.find("(")
    close_paren = raw_field.find(")")
    url = raw_field[open_paren + 1 : close_paren]
    return company_name, url


print(len(all_jobs))
print(all_jobs[0])