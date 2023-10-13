import os
import requests

api_key = os.getenv('waka_56b7b9cf-c4e8-454a-851f-27e0aac739b7')  # Use an environment variable for the API key

if api_key:
    try:
        # Make a request to Wakatime's API to fetch statistics
        response = requests.get(f'https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={api_key}')
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        # Parse the response and extract relevant statistics
        data = response.json()
        total_coding_time = data['data']['total_seconds']

        # Update the README file with the statistics
        with open('README.md', 'a') as readme:
            readme.write(f'Total Coding Time (Last 7 Days): {total_coding_time / 3600:.2f} hours\n')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
else:
    print("Wakatime API key not found. Please set the WAKATIME_API_KEY environment variable.")
