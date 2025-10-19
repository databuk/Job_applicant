from dotenv import load_dotenv
import os
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
EDGE_DRIVER_PATH = r"C:\Users\Ibk\Downloads\edge_driver\msedgedriver.exe"