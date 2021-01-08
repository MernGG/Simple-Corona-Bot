import discord
import time

from colorama import Fore, init
from selenium import webdriver
from discord.ext import commands
from discord.utils import find

title = f"""

                                         ██████╗  ██████╗ ███╗   ██╗ █████╗     
                                         ██╔══██╗██╔═══██╗████╗  ██║██╔══██╗    
                                         ██████╔╝██║   ██║██╔██╗ ██║███████║    
                                         ██╔══██╗██║   ██║██║╚██╗██║██╔══██║    
                                         ██║  ██║╚██████╔╝██║ ╚████║██║  ██║    
                                         ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝    
                                                {Fore.YELLOW}Covid{Fore.RESET} is Taking Over!!
                                               Bot By MernGG on github                                   

"""

token = ''
prefix = 'c.'
bot = commands.Bot(command_prefix=prefix, description="CORONA!!!")
bot.remove_command("help")

rona = webdriver.ChromeOptions()
rona.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
rona.add_argument('--disable-extensions')
rona.add_argument('--profile-directory=Default')
rona.add_argument("--incognito")
rona.add_argument("--disable-plugins-discovery");
rona.add_argument('headless');
rona.add_argument("--mute-audio");
driver = webdriver.Chrome('chromedriver.exe', options=rona)
driver.get('https://www.worldometers.info/coronavirus/')

cases = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span').text
deaths = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span').text
recovered = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[7]/div/span').text
active = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[1]').text
closed = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[10]/div/div[2]/div/div[1]/div[1]').text
deathrate = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[10]/div/div[2]/div/div[1]/div[3]/div[2]/strong').text
mild_c = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[1]/span').text
crit_c = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[3]/div[2]/span').text

def start():
    print(title)
    time.sleep(5)
    print("Bot is Ready! ")
    bot.run(token)



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Developed by MernGG", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    print(f"Logged in as {bot.user}")


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}! I have come here to inform you about Covid19!'.format(guild.name))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def corona(ctx):
    embed = discord.Embed(title='CoronaStats', color=0xffee00)
    embed.add_field(name='Cases:', value=cases, inline=False)
    embed.add_field(name='Deaths:', value=deaths, inline=False)
    embed.add_field(name='Deathrate:', value=deathrate + '%', inline=False)
    embed.add_field(name='Recovered:', value=recovered, inline=False)
    embed.add_field(name='Active Cases:', value=active, inline=False)
    embed.add_field(name='Closed Cases:', value=closed, inline=False)
    embed.add_field(name='Mild Active Cases:', value=mild_c, inline=False)
    embed.add_field(name='Critical Active Cases:', value=crit_c, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='List of Commands', color=0xffee00)
    embed.add_field(name='Help: ', value=f'{prefix}help', inline=False)
    embed.add_field(name='CoronaStats: ', value=f'{prefix}corona', inline=False)
    embed.add_field(name='Credits: ', value=f'{prefix}credits/ {prefix}creds', inline=False)
    await ctx.send(embed=embed)


@bot.command(aliases=['creds'])
async def credits(ctx):
    embed = discord.Embed(title='Credits', color=0xffee00)
    embed.add_field(name='Developer: ', value=f'MernGG', inline=False)
    embed.add_field(name='Twitch: ', value=f'twitch.tv/MernGG', inline=False)
    embed.add_field(name='Github: ', value=f'github.com/MernGG', inline=False)
    await ctx.send(embed=embed)


if __name__ == '__main__':
    init()
    start()
