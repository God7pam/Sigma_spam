from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("⚡ᏨᎾᎷᎷᎯᏁᎠᏕ⚡", data="help_back")
    ],
    [
        Button.url("⚡ᏕᏬᏢᏢᎾᏒᎿ⚡ ", "https://t.me/sigma_addiction"),
        Button.url("⚡ᏨᎻᎯᏁᏁᎬᏝ⚡", "https://t.me/sigma_addiction")
        
    ],
    [
        Button.url("⚡ᏒᎬᏢᎾ⚡", "https://t.me/sigma_addiction")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"⚡MɎ ØWNɆɌ⚡: [ϚįƓ♏Ⱥ ҠįՌҠ](https://t.me/sigma_addiction)**\n\n"
        TEXT += f" ⚡ɈȺVȺ VɆɌSƗØN⚡ `FT9.78`\n"
        TEXT += f" ⚡ĦŦMŁ VɆɌSƗØN⚡  `89.GT.90`\n"
        TEXT += f"⚡ɃØŦ VɆɌSƗØN⚡  `{__version__}`\n`90.HT"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/d76990b1e2de0bbf2bc1e.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
