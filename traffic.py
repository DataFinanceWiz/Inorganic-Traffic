import random
import time
import requests

# Set number of bot visits
num_visits = 10

# Set time delay between visits
delay = 0.5

# Set list of possible user agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393']

# Set list of possible referrers
referrers = ['https://google.com', 'https://bing.com', 'https://yahoo.com', 'https://duckduckgo.com', 'https://ask.com']

# Set list of possible IP addresses
ips = ['211.124.178.164', '156.81.249.188', '98.45.207.55', '27.217.137.49', '189.40.42.121', '56.253.67.137', '76.2.115.148', '92.31.5.66', '173.62.114.242', '180.152.51.8']

# Set target website
website = 'https://libregenie.com'

# Loop through number of visits
for i in range(num_visits):
  # Choose random user agent, referrer, and IP address
  user_agent = random.choice(user_agents)
  referrer = random.choice(referrers)
  ip = random.choice(ips)

  # Send visit to website
  requests.get(website, headers={'User-Agent': user_agent, 'Referrer': referrer}, allow_redirects=False, proxies={'http': ip})

  # Delay before next visit
  time.sleep(delay)

print('Bot traffic generation complete!')