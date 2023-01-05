import boto3, json, os, time

default_minutes = 60
interval = 60 # seconds
def get_minutes():
  if os.path.exists('timer.json'):
     with open('timer.json') as f:
        data = json.load(f)
        minutes = data['minutes']
        return minutes
  else:
      return write_minutes(default_minutes)

def write_minutes(minutes):
      data = {'minutes': minutes}
      with open('timer.json', 'w') as f:
          f.write(json.dumps(data))
          return minutes

while (minutes := get_minutes()) > 0:
  print(minutes)
  minutes = minutes - 1
  write_minutes(minutes)
  time.sleep(interval)

write_minutes(default_minutes)
LAMBDA_URL = os.environ.get('LAMBDA_URL')
os.system(f'curl {LAMBDA_URL}/stop') # Stop the server
