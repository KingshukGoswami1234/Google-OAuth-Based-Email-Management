from email.mime.text import MIMEText
import base64

def send_mail(service, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(
        userId="me",
        body={'raw': raw}
    ).execute()

    print("Mail Sent Successfully.")


def delete_mail(service, msg_id):
    service.users().messages().trash(
        userId='me',
        id=msg_id
    ).execute()

    print("Mail Deleted.")