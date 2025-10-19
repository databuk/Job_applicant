from classifier import OllamaClient
from scraper import get_jobs
from email_sender import send_email


    
def main():
    llm = OllamaClient()
    jobs  = get_jobs()
    for job in jobs:
        if job["job_details"] == "yes":
            email = llm.extract_email(job["extract_email"])
            job_details = job["job_details"]
            application_letter = llm.generate_email(job_details)
            #email = "researchforme2023@gmail.com"
            recipient = email if email != "none" else "irinyenikanibukun@gmail.com"
            send_email(recipient, application_letter)
if __name__ == "__main__":
    main()