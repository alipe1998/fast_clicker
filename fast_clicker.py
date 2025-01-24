#!/usr/bin/env python3

from pytz import timezone
from datetime import datetime, timedelta
import time
import pyautogui
import argparse
from termcolor import colored

def fast_clicking_at_time(target_time: str, target_timezone: str = "US/Central"):
    """
    A script that automates a single mouse click at the specified time.

    Parameters:
        target_time (str): Time in HH:MM:SS format to execute the click.
        target_timezone (str): Timezone of the target time (default is 'US/Central').
    """
    tz = timezone(target_timezone)
    current_time = datetime.now(tz)

    # Parse target time and make it timezone-aware
    target_time_naive = datetime.strptime(target_time, "%H:%M:%S")
    target_datetime = tz.localize(
        datetime.combine(current_time.date(), target_time_naive.time())
    )

    # Adjust to the next day if the target time is in the past
    if target_datetime <= current_time:
        target_datetime += timedelta(days=1)

    print(colored(f"Scheduled to click at {target_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')}.", "green"))
    less_than_10 = False

    try:
        while True:
            current_time = datetime.now(tz)
            remaining_time = (target_datetime - current_time).total_seconds()

            if remaining_time <= 0:
                pyautogui.click()
                formatted_time = f"{current_time.strftime('%H:%M:%S')}.{current_time.microsecond:06d} {current_time.strftime('%Z')}"
                print(colored(f"Clicked at {formatted_time}.", "blue"))
                break

            if remaining_time > 60:
                sleep_time = 15
                print(colored(f"Time remaining: {remaining_time:.2f} seconds. Sleeping for {sleep_time} seconds.", "yellow"))
            elif 30 < remaining_time <= 60:
                sleep_time = 5
                print(colored(f"Time remaining: {remaining_time:.2f} seconds. Sleeping for {sleep_time} seconds.", "yellow"))
            elif 5 < remaining_time <= 30:
                print(colored(f"T-Minus: {remaining_time:.2f}", "green"))
                sleep_time = 1
            elif 2 < remaining_time <= 5:
                if not less_than_10:
                    print(colored(f"Less Than 5 Seconds! All Clicking Systems Preparing to Fire!", "green"))
                    less_than_10 = True
                sleep_time = 0.5
            else:
                sleep_time = 0.0001

            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print(colored("Script interrupted by user.", "red"))

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(
        description=colored("Schedule a mouse click at a specific time.", "cyan"),
        epilog=colored("Example usage: python fast_clicking_script.py --time 12:30:00 --timezone US/Eastern", "yellow")
    )
    parser.add_argument("--time", required=True, help=colored("Target time to click in HH:MM:SS format.", "magenta"))
    parser.add_argument(
        "--timezone",
        default="US/Central",
        help=colored("Timezone of the target time (default is 'US/Central').", "magenta")
    )

    args = parser.parse_args()

    try:
        fast_clicking_at_time(args.time, args.timezone)
        print(f"Log Results of Test Here: https://forms.gle/is6uwhx3sQ95ExrZ7")
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
    