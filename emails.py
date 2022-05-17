import content
import datetime
import ssl
import smtplib
from email.message import EmailMessage

class Email:
    def __init__(self):
        self.contents = {"quote": {"include": True, "content": content.getRandomQuote()},
                        "wiki": {"include": True, "content": content.getWikiArticle()}}

        self.recipients_list = ['xyz@ymail.com', 'abc@email.com']

        self.creds = {
            'email': 'xyz@gmail.com',
            'password': 'XXXXXXXX'
        }

    def formatEmail(self):
        text = f'\n\n--------- Daily Digest for {datetime.date.today().strftime("%d %b %Y")} ---------\n\n'

        if self.contents["quote"]["include"] and self.contents["quote"]["content"]:
            text += "** Quote of the Day **\n\n"
            text += f'"{self.contents["quote"]["content"]["quote"]}" \n \t\t\t - {self.contents["quote"]["content"]["author"]} in {self.contents["quote"]["content"]["book"]}\n\n\n'

        if self.contents["wiki"]["include"] and self.contents["wiki"]["content"]:
            text += "** Wiki of the Day **\n\n"
            text += f'"{self.contents["wiki"]["content"]["title"]}" \n "{self.contents["wiki"]["content"]["extract"]}" \n Read more at: {self.contents["wiki"]["content"]["url"]}\n\n'

        return text

    def sendEmail(self):
        msg = EmailMessage()
        msg['Subject'] = f'Daily Digest for {datetime.date.today().strftime("%d %b %Y")}'
        msg['From'] = self.creds['email']
        msg['To'] = ', '.join(self.recipients_list)

        msgBody = self.formatEmail()
        msg.set_content(msgBody)
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(self.creds['email'], self.creds['password'])
            server.send_message(msg)

if __name__ == "__main__":
    email = Email()
    emailText = Email.formatEmail(email)

    with open('message.txt', 'w', encoding='utf-8') as f:
        f.write(emailText)

    print('Sending test email...')
    email.sendEmail()