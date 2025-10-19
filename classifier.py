from openai import OpenAI
class OllamaClient:
    def __init__(self, model="llama3.2:1b"):
        self.client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        self.model =  model
    def classify_writing_job(self, job_text):
        prompt = [
            {"role": "system", "content": ("You are a classfier. Your job is to only respond with 'yes' or 'no'. \
                You will receive a job posting  topic. if the job posting is related to writing jobs ,\
                    respond with 'yes' otherwise respond with 'no'. Only 'yes' or 'no'. no explanation. only respond with \
                        either 'yes' or 'no'. not both. nothing else") }, 
            {"role": "user", "content": job_text}
            ]
        return self._query(prompt)
    def extract_email(self, text):
        extract_email_prompt = [
            {"role": "system", "content": ("You an an email extractor. Your job is to extract the email address of job of hiring position. \
                If the email address is the address to apply for job, respond with the email address. If the email address is not the address \
                    to apply for job, respond with 'none'. Only respond with the email address or 'None'. No stories. Nothing else.")},
            {"role": "user", "content": (f"Extract the email address from this text only if it the address to apply for job: {text}")}
        ]
        return self._query(extract_email_prompt)
    def generate_email(self, job_details):
        example_response = """
                Dear Hiring Manager,

                I am applying for the Data Scientist position at Axa. I hold strong skills in Python, SQL, and machine learning, with experience using tools such as Pandas, Scikit-learn, and Power BI. In my recent role at [Previous Company/Project], I developed predictive models that improved [specific metric] and provided actionable insights for decision-making.

                I am particularly drawn to Axa because of your focus on [specific company goal or project]. I am eager to apply my analytical skills and problem-solving abilities to help your team drive data-based innovation.
                Please find my resume attached. I look forward to the opportunity to discuss how I can contribute to your team.

                Best regards,
                Ibukun Irinyenikan
                08126572027 | irinyenikanibukun@gmail.com """
        prompt_application_letter = [
        {"role": "system", "content": ("You are a job seeker applying for a writing job.  Your task is to write a professional \
            and concise email application letter based on the job details provided. The letter should highlight your relevant skills, experience, \
                and enthusiasm for the position. It should be no more than 150 words. No preamble. Ony write what the hiring manager needs to see.")},
        {"role": "user", "content": (f"write a professional email application letter based on the following job description: {job_details} \
            conclude the letter with my name Ibukun Irinyenikan, phone number: 08126572027 and email address: irinyenikanibukun@gmail.com. \
                No preamble. Here is an example of a application letter: {example_response}")}
    ]
        return self._query(prompt_application_letter)
                    
    def _query(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
        )
        return response.choices[0].message.content.strip()
    
    
        
    
    