# bot.py
import os
from discord.ext import commands
from dotenv import load_dotenv
from youtube_search import YoutubeSearch
import json
import requests

# Set up your tokens and bot

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
playlist = os.getenv('YOUTUBE_TOKEN')

bot = commands.Bot(command_prefix='!')

# bot commands

@bot.command(name='search_song', help='Searches for song on YouTube (put song name in quotes)')
async def song_search(ctx, song: str):
    print(song)
    results = YoutubeSearch(song, max_results=10).to_json()
    json_data = json.loads(results)
    if len(json_data['videos']) > 0:
        options = []
        for v in json_data['videos']:
            song = v['title'] + "\n\tLink: " + v['link'] + "\n\tID: " + v['id']
            options.append(song)
        await ctx.send("Here are your results:\n\n" + '\n'.join(options))
    else:
        await ctx.send("No Results")

@bot.command(name='post_song', help="Posts song to playlist based on song ID")
async def song_post(ctx, song_id: str):
    print("test")

# run bot

print("BOT RUNNING")
bot.run(token)
