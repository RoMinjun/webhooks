#!/usr/bin/python3.9
import sys
import requests
from datetime import datetime

# URL of the endpoint
url = 'https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/'
params = {
    'key': '<steam api key>'
}
status_file = '/path/to/steam-server-status/status'
discord_webhook_url = '<discord webhook>'

def send_discord_alert(message, username):
    payload = {
        "content": message,
        "username": username
    }
    requests.post(discord_webhook_url, json=payload)

def read_last_status_code(file_path):
    try:
        with open(file_path, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 200  # Default to 200 if no file exists

def write_status_code(file_path, status_code):
    with open(file_path, 'w') as file:
        file.write(str(status_code))

def check_status_code():
    # Sending the GET request
    response = requests.get(url, params=params)

    # Get the current date and time
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # Check if the status code has changed from 200 to something else
    last_status_code = read_last_status_code(status_file)
    current_status_code = response.status_code

    if last_status_code == 200 and current_status_code != 200:
        # Status code has changed from 200 to something else
        message =  f"\n**[STEAM SERVER ERROR]**\n\t**Status Code**: **`{current_status_code}`**\n\t**Server status**: **`DOWN`**\n\t**Date/time**: {current_time}\n**Message**:\n\tSteam servers are down ***Nokie crying noises*** :NoOoOo:"
        send_discord_alert(message, "Steam Server Status by RoMinjun")
    elif last_status_code != 200 and current_status_code == 200:
        # Status code has returned to 200
        message = f"\n**[STEAM SERVER INFO]**\n\t**Status Code**: **`{current_status_code}`**\n\t**Server status**: **`UP`**\n\t**Date/time**: *`{current_time}`*\n**Message**:\n\tSteam servers are up again ***Happy Nokie Noises*** :widenokieHappy:"
        send_discord_alert(message, "Steam Server Status by RoMinjun")

    # Update the status code in the file
    write_status_code(status_file, current_status_code)

def maintenance_reminder(time_until_maintenance):
    if time_until_maintenance == "2 hours":
        message = f"\n**[STEAM MAINTENANCE REMINDER]**\n\t**When?:** **`in 2 hours`**\n**Message:**\n\tSteam servers are going down for scheduled maintenance in 2 hours :NoOoOo:"
    elif time_until_maintenance == "1 hour":
        message = f"\n**[STEAM MAINTENANCE REMINDER]**\n\t**When?:** **`in 1 hour`**\n**Message:**\n\tSteam servers are going down for scheduled maintenance in 1 hour :NoOoOo:"
    elif time_until_maintenance == "30 minutes":
        message = f"\n**[STEAM MAINTENANCE REMINDER]**\n\t**When?:** **`in 30 minutes`**\n**Message:**\n\tSteam servers are going down for scheduled maintenance in 30 minutes :NoOoOo:"
    send_discord_alert(message, "Steam Maintenance Reminder by RoMinjun")

if __name__ == "__main__":
    if '--check-status' in sys.argv:
        check_status_code()
    elif '--maintenance-reminder' in sys.argv:
        if 'two-hour' in sys.argv:
            maintenance_reminder("2 hours")
        elif 'one-hour' in sys.argv:
            maintenance_reminder("1 hour")
        elif 'thirty-minutes' in sys.argv:
            maintenance_reminder("30 minutes")
