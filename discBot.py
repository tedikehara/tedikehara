
# testing python bot for discord

import os
import time
import discord as ds


token = 'OTA3NzAzMjkwNTY3OTkxMzI2.YYrCkA.vPIxuEjV8M3Og2mC5eG8Ghr0GrI'   #bot token for discord
channel_id = 907708927871950878
ip_list = ['169.63.179.247']
timeout = 10

client = ds.Client()



@client.event
async def on_ready():
    pings_channel = client.get_channel(channel_id)

    while True:
        for ip in ip_list:
            response = os.popen(f"ping {ip}").read()
            if not ("Received = 4" in response):                              # host is down do this
                await pings_channel.send(f"DOWN {ip} Ping Unsuccessful, HELP ME!!!")

        time.sleep(timeout)

    

client.run(token)


