from discord.ext import commands
import json
import discord
import aiohttp
import random
import xml.etree.ElementTree
try:
    from imgurpython import ImgurClient
except:
    ImgurClient = False


class Images:
    """Image related commands."""

    def __init__(self, bot):
        self.bot = bot
        self.tmp_config = json.loads(str(open('./options/config.js').read()))
        self.config = self.tmp_config['config']
        self.imgur = ImgurClient(self.config['giphy-id'], self.config['giphy-secret'])
        self.emojiUnicode = self.tmp_config['unicode']
        self.exchange = self.tmp_config['exchange']
        self.channels = self.tmp_config['channels']
        self.emojiUnicode = self.tmp_config['unicode']
        self.owner_list = self.config['owner-id']


    @commands.command(pass_context=True, no_pm=True)
    async def gif(self, ctx, *keywords):
        """Retrieves a random gif from a giphy search"""
        if keywords:
            keywords = "+".join(keywords)
        else:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='sigh.. **`{}help gif`**'.format(self.config['prefix']),
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, self.emojiUnicode['error'])
            return
        await self.bot.send_typing(ctx.message.channel)
        url = ("http://api.giphy.com/v1/gifs/random?&api_key={}&tag={}"
               "".format(self.config['giphy-api-key'], keywords))

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                source = await response.json(encoding='utf8')

        source = json.dumps(source)
        result = json.loads(str(source))

        if response.status == 200:
            if result["data"]:
                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description='{}'.format(''),
                                      colour=0xf20006)
                embed.set_image(url=result["data"]["image_original_url"])
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['succes'])
            else:
                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description='{}'.format('No results found.'),
                                      colour=0xf20006)
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['warning'])
        else:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='{}'.format('Error contacting the API'),
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, self.emojiUnicode['error'])


    @commands.command(pass_context=True)
    async def credits(self, ctx):
        """Give credit to a user"""
        embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                              description='\n:ok_hand:  :laughing:\n  :telephone_receiver::shirt::call_me:\n         :jeans:        :fire:',
                              colour=0xf20006)
        last_message = await self.bot.say(embed=embed)
        await self.bot.add_reaction(last_message, self.emojiUnicode['succes'])


    @commands.command(pass_context=True)
    async def rule34(self, ctx, *, content=None):
        """
        Shows graphical content NSFW.
        Rule#34 : If it exists there is porn of it. If not, start uploading.
        Works only in channels with nsfw in the name.
        """

        if 'nsfw' not in str(ctx.message.channel.name).lower():
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='You do not have the permission to use this command outside a NSFW channel.',
                                  colour=0xf20006)
            await self.bot.say(embed=embed)
            return

        if content == None:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='Maybe you should considering using `{}help rule34` instead'.format(self.config['prefix']),
                                  colour=0xf20006)
            await self.bot.say(embed=embed)

        else:
            link = 'http://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=100&tags=' + content
            url = link.replace(' ', '_').replace('+', ' ')
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    source = await response.read()

            root = xml.etree.ElementTree.fromstring(source)
            image = root[random.randint(0, len(root) - 1)].attrib['file_url']

            try:
                if image.endswith(".webm"):
                    embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                          description='Naughty boy grrrr tiger :tiger:',
                                          colour=0xf20006)
                    last_message = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(last_message, self.emojiUnicode['warning'])
                    await self.bot.say(embed=embed)
                    return

                if image.endswith(".png"):
                    pass

                if image.endswith(".jpg"):
                    pass

                if image.endswith(".jpeg"):
                    pass

                if image.endswith(".gif"):
                    pass


                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      colour=0xf20006)
                embed.set_image(url=image)
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['succes'])
                return
            except ValueError:
                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description='{}'.format('No results found.'),
                                      colour=0xf20006)
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['warning'])
                return
            except Exception as e:
                a = await self.bot.say(image)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])
        return


    @commands.command(pass_context=True, hidden=True)
    async def dict(self, ctx, *keywords):
        """
        Look something up in the UrbanDictionary.
        Use this command with a search keyword.
        """

        if keywords == None:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='Did you tried `{}help dict` yet?'.format(self.config['prefix']),
                                  colour=0xf20006)
            a = await self.bot.say(embed=embed)
            await self.bot.add_reaction(a, self.emojiUnicode['error'])
        if keywords:
            keywords = "%20".join(keywords)
            url = 'http://api.urbandictionary.com/v0/define?term={}'.format(keywords)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    source = await response.json(encoding='utf8')

            source = json.dumps(source)
            result = json.loads(str(source), indent=2)
            print(result)
            await self.bot.say('Check your console\nThe Url was\n```\n{}\n```'.format(url))
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  colour=0xf20006)
            embed.add_field(name='Json', value='```result```', inline=False)

            a = await self.bot.say(embed=embed)
            await self.bot.add_reaction(a, self.emojiUnicode['succes'])


def setup(bot):
    if ImgurClient is False:
        raise RuntimeError("You need the imgurpython module to use this.\n"
                           "pip3 install imgurpython")

    bot.add_cog(Images(bot))