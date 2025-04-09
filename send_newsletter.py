import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load environment variables from .env
load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
if not SENDGRID_API_KEY:
    raise ValueError("SENDGRID_API_KEY environment variable is not set.")

# Create the email message
with open('D:/Academics/Projects/Research Agent/newsletter_agent_new/logs/2025-01-08_03-00-38_newsletter_task.html', 'r') as file:
    html_content = file.read()

message = Mail(
    from_email='11n44sourjeshmukherjee@gmail.com',
    to_emails='sourjesh.ece.iiitk@gmail.com',
    subject='Trial Newsletter',
    html_content=html_content
)

# Send the email
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print("Status Code:", response.status_code)
    print("Response Body:", response.body)
    print("Response Headers:", response.headers)
except Exception as e:
    print("Error:", str(e))
