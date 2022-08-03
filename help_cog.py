import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self. bot = bot

        self.help_message = """
```
Comandos gerais de música:

>help = Mostra todos os comandos possíveis.
>p <palavra-chave> = Procura a música no youtube e a reproduz no canal de voz.
>q = Mostra as músicas atuais da fila.
>skip = Pula a música atual.
>clear = Para a música atual e limpa a fila.
>leave = Expulsa o bot do canal de voz.
>pause = Pausa a música atual, ou retoma a música se já estiver pausada.
>resume = Retoma a música atual.

```
    """
        self.text_channel_text = []
    
    
    @commands.command(name="help", help="Mostra todos os comandos possíveis.")
    async def help(self, ctx):
        await ctx.send(self.help_message)
        