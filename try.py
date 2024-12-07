import asyncio
import websockets

# Replace with your ssid
SSID = r'42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"968fbe28a99f8fcbc5bb10ba3e9bf173\";s:10:\"ip_address\";s:12:\"98.97.79.202\";s:10:\"user_agent\";s:111:\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1733449881;}448be3b75e1e6d7969b7fd792682d23e","isDemo":1,"uid":79658638,"platform":2}]'
URL = "wss://https://pocketoption.com/en/cabinet/"

async def connect():
    async with websockets.connect(URL) as websocket:
        # Authenticate
        await websocket.send(SSID)
        print("Authentication Sent!")

        # Listen for responses
        async for message in websocket:
            print("Received:", message)

asyncio.run(connect())