import smtplib

def send_emails(emails, schedule, forecast):
    # Connect to the smtp server
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

    # Start TLS encryption
    server.starttls()

    # Login
    passw = raw_input('Enter your password:')
    from_email = 'phjag@yahoo.com'
    server.login(from_email, passw)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Circus!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += 'The schedule is:\n' + schedule + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email,to_email, message)
        print('Sending email to', to_email)

