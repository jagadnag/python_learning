import cs_weather
import cs_emails

def get_emails():
    # Reading the emails from the file
    emails = {}
    try:
        email_file = open('email.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except IOError as err:
        print(err)

    return emails

def get_schedule():
    # Reading our schedule from a file
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except IOError as err:
        print(err)

    return schedule

def main():
    emails = get_emails()

    schedule = get_schedule()

    forecast = cs_weather.get_weather_forecast()

    cs_emails.send_emails(emails, schedule, forecast)

main()
