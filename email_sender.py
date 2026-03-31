import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Lokesh Yadav'
email['to'] = 'Lokeshyad109@gmail.com'
email['subject'] = 'You won 100000 dollars!'

email.set_content('I am a Python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('#email','#pass')
    smtp.send_message()
    print('All good boss')