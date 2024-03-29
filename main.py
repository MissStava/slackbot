import os
from slack import RTMClient

@RTMClient.run_on(event="message")
def say_hello(**payload):
  data = payload['data']
  print(data)
  print("")
  web_client = payload['web_client']

  if 'Hello' in data['text']:
    channel_id = data['channel']
    thread_ts = data['ts']
    user = data['user']

    web_client.chat_postMessage(
      channel=channel_id,
      text=f"Hi <@{user}>!",
      thread_ts=thread_ts
    )

slack_token = os.environ["SLACK_TOKEN"]
rtm_client = RTMClient(token=slack_token,proxy="http://127.0.0.1:3128")
rtm_client.start()
