import requests

url = "https://remoteok.com/api"
response = requests.get(url)
jobs = response.json()

for job in jobs[1:100]:
    title = job.get("position", "")
    company = job.get("company", "")

    for key in job.keys():
        value = str(job.get(key, "")).lower()

        if "python" in value or "ai" in value:
            job_line = f"{title} - {company}\n"

            try:
                with open("python_jobs.txt", "r", encoding="utf-8") as file:
                    existing_jobs = file.read()
            except FileNotFoundError:
                existing_jobs = ""

            if job_line not in existing_jobs:
                with open("python_jobs.txt", "a", encoding="utf-8") as file:
                    file.write(job_line)

                print(f"New match saved: {title} - {company}")
            else:
                print(f"Already exists: {title} - {company}")

            break