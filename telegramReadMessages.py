import asyncio
import pytz
import telethon
from datetime import datetime
from telethon import TelegramClient, events

# Replace the values below with your own API ID, API hash and phone number.
api_id = ''
api_hash = ''
phone_number = '+'

client = TelegramClient('session_name', api_id, api_hash)

async def handle_messages():
    async for dialog in client.iter_dialogs():
        if dialog.unread_count > 0:
            entity = dialog.entity
            if isinstance(entity, telethon.tl.types.User):
                continue
            if entity.title not in ["Insane Traders - Options (Monthly Income Plan)","Small Account Challenge", "FYT COMMUNITY","Mr.Scalper Personal Trade Group"]:
                continue
            async for message in client.iter_messages(entity, limit=1):
                # Convert message timestamp to IST timezone
                ist = pytz.timezone('Asia/Kolkata')
                timestamp = message.date.astimezone(ist)

                # Format the message
                message_str = f'{timestamp.date()} {timestamp.strftime("%H:%M:%S")} (IST) - {entity.title}: {message.message}'

                print(message_str)

async def main():
    while True:
        async with client:
            await handle_messages()
        await asyncio.sleep(5) # wait for 5 seconds before checking for new messages again

if __name__ == '__main__':
    asyncio.run(main())
