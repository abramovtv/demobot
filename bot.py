from telethon import TelegramClient, events
import openai, asyncio


tg_client = TelegramClient("bot", int("TG_API_ID"), "TG_API_HASH"))
openai_client = openai.AsyncOpenAI(api_key="OPENAI_API_KEY")

@tg_client.on(events.NewMessage)
async def handler(event):
    response = await openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Если сообщение содержит вопрос про автомобили, на который ты можешь даль хороший ответ, дай его, иначе ответь словом нет\n{event.text}"}]
    )
    if "нет" not in response.choices[0].message.content.lower():
        await event.reply(response.choices[0].message.content)

async def main():
    await tg_client.start(bot_token="TG_BOT_TOKEN")
    await tg_client.run_until_disconnected()

asyncio.run(main())
