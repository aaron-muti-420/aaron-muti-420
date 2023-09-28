import requests

# Replace 'your_api_key' with your Wakatime API key
api_key = 'waka_56b7b9cf-c4e8-454a-851f-27e0aac739b7'

# Make a request to Wakatime's API to fetch statistics
response = requests.get(f'https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={api_key}')

# Parse the response and extract relevant statistics
data = response.json()
total_coding_time = data['data']['total_seconds']

# Update the README file with the statistics
with open('README.md', 'a') as readme:
    readme.write(f'Total Coding Time (Last 7 Days): {total_coding_time / 3600:.2f} hours\n')
