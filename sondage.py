# import discord
# import re
# from asyncio import sleep
# from discord.ext import commands
# from datetime import datetime
# from operator import itemgetter

# from utils.emojis import EMOJI_NUM, EMOJI_UTIL

# async def send_msg(ctx, client, props):
#     content = ""
#     for i in range(len(props)):
#         content += EMOJI_NUM[i] + " " + props[i] + "\n"

#     content += EMOJI_UTIL.get("crossmark") + " je suis nul et je peux pas venir"
#     embed = discord.Embed(
#         title="Sondage pour VJam!!!",
#         color=discord.Color.green(),
#         description=content
#     )
#     embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
#     sondage = await ctx.send(embed=embed)
#     for i in range(len(props)):
#         await sondage.add_reaction(EMOJI_NUM[i])

#     await sondage.add_reaction(EMOJI_UTIL.get("crossmark"))
#     await wait_for_reactions(ctx, sondage, client, props)

# async def wait_for_reactions(ctx, msg, client, props):
#     await sleep(3) # 86400 - 24 heures
#     cached_msg = discord.utils.get(client.cached_messages, id=msg.id)
#     react_l = []
#     for i in range(len(cached_msg.reactions)-1):
#         if (str(cached_msg.reactions[i]) == EMOJI_NUM[i]):
#             react_l.append((props[i], cached_msg.reactions[i].count-1))
#     react_l.append(("on est des nullos on annule", cached_msg.reactions[len(cached_msg.reactions)-1].count-1))
    
#     content = ""
#     for react in react_l:
#         content += str(react[0]) + " : " + str(react[1]) + "\n"
    
#     embed = discord.Embed(
#         title="Résultaaats",
#         color=discord.Color.green(),
#         description=content
#     )
#     embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)

#     await ctx.send(embed=embed)

#     # m = re.match("^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}_[0-9]{1,2}:[0-9]{1,2}$", str(max(react_l, key=itemgetter(1))))
#     # if (m != None):
#     #     try:
#     #         print(m)
#     #         # dt = datetime()
#     #         # await create_scheduled_event(ctx, dt)
#     #         pass
#     #     except:
#     #         pass

# async def create_scheduled_event(ctx, dt):
#     await ctx.guild.create_scheduled_event(name="VJam")
#     pass