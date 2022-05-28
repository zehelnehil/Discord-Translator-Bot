import discord
import keys
import supported_languages as langs
from discord.ext import commands
import translators as translator


client = discord.Client()
client = commands.Bot(command_prefix="!")
is_client_running = False


@client.event
async def on_ready():
    global is_client_running

    if not is_client_running:
        is_client_running = True
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="!ts-help"))
        print(f"{int(round(client.latency * 1000))} ms")
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        await message.channel.trigger_typing()

    await client.process_commands(message)


@client.command(aliases=['ts', 'ts-google'])
async def translate_default(ctx, lang_target, *args):
    user_msg = ' '.join(args)
    if lang_target in langs.list_of_supported_langs_google:
        if args:
            try:
                translated_msg = translator.google(user_msg, to_language=lang_target)
                await ctx.send(translated_msg)
                print(f"New request from: {ctx.message.author}, id: {ctx.message.author.id}, using: Google {user_msg}")
            except Exception as error:
                await ctx.send(f"Hey {ctx.message.author.mention} slow down a bit, Google is not too fast or they are offline for now. Try again later or use `!ts-help` to see more translate services available.")
                print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Google {lang_target}, user args: {user_msg}\nError: {error}")
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} you need to provide a phrase to translate. Use `!ts-help` to get more help.")
    else:
        error_msg = discord.Embed(title=f"Sorry, Google don't support {lang_target} yet.", color=638712)
        error_msg.add_field(name=f"Bot usage example", value=f"`!ts ja Hello`", inline=False)
        error_msg.add_field(name=f"List of supported languages by Google. Use `!ts-help` to get more help", value=langs.list_of_supported_langs_google, inline=False)
        await ctx.send(embed=error_msg)
        print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Google {lang_target}, user args: {user_msg}\nError: {error}")


@client.command(aliases=['ts-deepl'])
async def translate_deepl(ctx, lang_target, *args):
    user_msg = ' '.join(args)
    if lang_target in langs.list_of_supported_langs_deepl:
        if args:
            try:
                translated_msg = translator.deepl(user_msg, to_language=lang_target)
                await ctx.send(translated_msg)
                print(f"New request from: {ctx.message.author}, id: {ctx.message.author.id}, usign: Deepl {user_msg}")
            except Exception as error:
                await ctx.send(f"Hey {ctx.message.author.mention} slow down a bit, Deepl is not too fast or they are offline for now. Try again later or use `!ts-help` to see more translate services available.")
                print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Deepl {lang_target}, user args: {user_msg}\nError: {error}")
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} you need to provide a phrase to translate. Use `!ts-help` to get more help.")
    else:
        error_msg_deepl = discord.Embed(title=f"Sorry, Deepl don't support {lang_target} yet.", color=638712)
        error_msg_deepl.add_field(name=f"Bot usage example", value=f"`!ts-deepl ja Hello`", inline=False)
        error_msg_deepl.add_field(name=f"List of supported languages by Deepl. Use `!ts-help` to get more help", value=langs.list_of_supported_langs_deepl, inline=False)
        await ctx.send(embed=error_msg_deepl)


@client.command(aliases=['ts-bing'])
async def translate_bing(ctx, lang_target, *args):
    user_msg = ' '.join(args)
    if lang_target in langs.list_of_supported_langs_bing:
        if args:
            try:
                translated_msg = translator.bing(user_msg, to_language=lang_target)
                await ctx.send(translated_msg)
                print(f"New request from: {ctx.message.author}, id: {ctx.message.author.id}, usign: Bing {user_msg}")
            except Exception as error:
                await ctx.send(f"Hey {ctx.message.author.mention} slow down a bit, Bing is not too fast or they are offline for now. Try again later or use `!ts-help` to see more translate services available.")
                print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Bing {lang_target}, user args: {user_msg}\nError: {error}")
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} you need to provide a phrase to translate. Use `!ts-help` to get more help.")
    else:
        error_msg_bing = discord.Embed(title=f"Sorry, Bing don't support {lang_target} yet.", color=638712)
        error_msg_bing.add_field(name=f"Bot usage example", value=f"`!ts-bing ja Hello`", inline=False)
        error_msg_bing.add_field(name=f"List of supported languages by Bing. Use `!ts-help` to get more help", value=langs.list_of_supported_langs_bing, inline=False)
        await ctx.send(embed=error_msg_bing)


@client.command(aliases=['ts-itranslate'])
async def translate_itranslate(ctx, lang_target, *args):
    user_msg = ' '.join(args)
    if lang_target in langs.list_of_supported_langs_itranslate:
        if args:
            try:
                translated_msg = translator.itranslate(user_msg, to_language=lang_target)
                await ctx.send(translated_msg)
                print(f"New request from: {ctx.message.author}, id: {ctx.message.author.id}, usign: Itranslate {user_msg}")
            except Exception as error:
                await ctx.send(f"Hey {ctx.message.author.mention} slow down a bit, Itranslate is not too fast or they are offline for now. Try again later or use `!ts-help` to see more translate services available.")
                print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Itranslate {lang_target}, user args: {user_msg}\nError: {error}")
        else:
            await ctx.send(f"Hey {ctx.message.author.mention} you need to provide a phrase to translate. Use `!ts-help` to get more help.")
    else:
        error_msg_itranslate = discord.Embed(title=f"Sorry, Itranslate don't support {lang_target} yet.", color=638712)
        error_msg_itranslate.add_field(name=f"Bot usage example", value=f"`!ts-itranslate ja Hello`", inline=False)
        error_msg_itranslate.add_field(name=f"List of supported languages by Itranslate. Use `!ts-help` to get more help", value=langs.list_of_supported_langs_itranslate, inline=False)
        await ctx.send(embed=error_msg_itranslate)


@client.command(aliases=['ts-reverso'])
async def translate_reverso(ctx, lang_from, lang_target, *args):
    user_msg = ' '.join(args)
    if lang_target in langs.list_of_supported_langs_reverso and lang_from in langs.list_of_supported_langs_reverso:
        if lang_from != lang_target:
            if args:
                try:
                    translated_msg = translator.reverso(user_msg, to_language=lang_target, from_language=lang_from)
                    await ctx.send(translated_msg)
                    print(f"New request from: {ctx.message.author}, id: {ctx.message.author.id}, usign: Reverso {user_msg}")           
                except Exception as error:
                    await ctx.send(f"Hey {ctx.message.author.mention} slow down a bit, Reverso is not too fast. Try again later or use `!ts-help` to see more translate services available.")
                    print(f"New request returned error from: {ctx.message.author}, id: {ctx.message.author.id}, lang target: Reverso {lang_target}, user args: {user_msg}\nError: {error}")
            else:
                await ctx.send(f"Hey {ctx.message.author.mention} you need to provide a phrase to translate. Use `!ts-help` to get more help.")
        else:
            await ctx.send(user_msg)
    else:
        error_msg_reverso = discord.Embed(title=f"Sorry, Reverso don't support {lang_target} or {lang_from} yet.", color=638712)
        error_msg_reverso.add_field(name=f"Bot usage example", value=f"`!ts-reverso en ja Hello`", inline=False)
        error_msg_reverso.add_field(name=f"List of supported languages by Reverso. Use `!ts-help` to get more help", value=langs.list_of_supported_langs_reverso, inline=False)
        await ctx.send(embed=error_msg_reverso)


@client.command(aliases=['ts-ping'])
async def ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f"{ctx.message.author.mention} Pong!  `{int(ping)}ms`")


@client.command(aliases=['ts-support'])
async def translate_support(ctx):
    await ctx.send(f"Talk with my creator <@757738778633961592>")


@client.command(aliases=['ts-help'])
async def translate_help(ctx):
    help_msg = discord.Embed(title=f"Translate bot help", color=638712)
    help_msg.add_field(name=f"Bot usage examples", value=f"`!ts ja Hello\n!ts-deepl en Ciao\n!ts-bing pt Bonjour\n!ts-itranslate fr-CA Hi\n!ts-reverso pt pl Olá`", inline=False)
    help_msg.add_field(name=f"List of supported languages by Google", value=langs.list_of_supported_langs_google, inline=False)
    help_msg.add_field(name=f"List of supported languages by Deepl", value=langs.list_of_supported_langs_deepl, inline=False)
    help_msg.add_field(name=f"List of supported languages by Bing", value=langs.list_of_supported_langs_bing, inline=False)
    help_msg.add_field(name=f"List of supported languages by Itranslate", value=langs.list_of_supported_langs_itranslate, inline=False)
    help_msg.add_field(name=f"List of supported languages by Reverso", value=langs.list_of_supported_langs_reverso, inline=False)
    help_msg.add_field(name=f"Usage of Reverso", value=f"When you are using Reverso you need to specify the language are coming from. For example `!ts-reverso en pt Got it!`", inline=False)
    help_msg.add_field(name=f"More commands", value=f"`!ts-ping\n!ts-support`", inline=False)
    await ctx.send(embed=help_msg)


if __name__ == '__main__':
    client.run(keys.TOKEN)
