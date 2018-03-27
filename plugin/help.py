import discord
from discord.ext import commands
import json
import datetime
import asyncio
import xml
from dependency import fuzzy
import re

try:
    from plugin.database import Database
except Exception as e:
    pass


tmp_config = json.loads(str(open('./options/config.js').read()))
config = tmp_config['config']
owner_list = config['owner-id']


class Help:
    def __init__(self, bot):
        self.bot = bot
        bot_version = 'V0.7'
        self.version = bot_version
        self.tmp_config = json.loads(str(open('./options/config.js').read()))
        self.config = self.tmp_config['config']
        self.emojiUnicode = self.tmp_config['unicode']
        self.exchange = self.tmp_config['exchange']
        self.botzillaChannels = self.tmp_config['channels']
        self.owner_list = self.config['owner-id']

        self.emoji_start = '\u23ee'
        self.emoji_five_back = '\u23ea'
        self.emoji_oneback = '\u25c0'
        self.emoji_oneahead = '\u25b6'
        self.emoji_five_ahead = '\u23e9'
        self.emoji_end = '\u23ed'
        self.emoji_start_txt = '⏮'
        self.emoji_five_back_txt = '⏪'
        self.emoji_oneback_txt = '◀'
        self.emoji_oneahead_txt = '▶'
        self.emoji_five_ahead_txt = '⏩'
        self.emoji_end_txt = '⏭'

        try:
            self.database = Database(self.bot)
            self.database_file_found = True
        except Exception as e:
            print('Help: Database files not found - {}'.format(e.args))
            pass

    @commands.command(pass_context=True)
    async def help(self, ctx, command: str = None):
        """
        Show this message
        """
        print(f'{datetime.date.today()} {datetime.datetime.now()} - {ctx.message.author} ran command !!help <{command}> in -- Channel: {ctx.message.channel.name} Guild: {ctx.message.server.name}')
        self.message = ctx.message

        def get_command_by_name():
            self.database.cur.execute("select * from botzilla.help;")
            command_object = self.database.cur.fetchall()
            self.database.cur.execute("ROLLBACK;")
            command_names = [i[0] for i in command_object]
            return command_names

        def get_commands_by_cog(cog_name):
            self.database.cur.execute("select * from botzilla.help where cog = '{}';".format(cog_name))
            command_object = self.database.cur.fetchall()
            self.database.cur.execute("ROLLBACK;")
            return command_object

        def get_short_desc(command_object):
            command_desc = command_object[2]
            split_lines = command_desc.splitlines(keepends=True)
            list_desc = [i.strip() for i in split_lines if i != '\n']
            try:
                short_desc = f'{list_desc[0]}\n{list_desc[1]}'
            except Exception as e:
                short_desc = list_desc[0]
            return short_desc

        async def wait_for_reaction(message):
            while True:
                reaction = await self.bot.wait_for_reaction([self.emoji_start, self.emoji_five_back, self.emoji_oneback, self.emoji_oneahead, self.emoji_five_ahead, self.emoji_end], message=message, timeout=120)
                if ctx.message.author.id == reaction.user.id:
                    try:
                        await self.bot.remove_reaction(emoji=reaction.reaction.emoji, member=ctx.message.author, message=message)
                    except Exception as e:
                        print(e.args)
                    break
                else:
                    try:
                        await self.bot.remove_reaction(emoji=reaction.reaction.emoji, member=reaction.user, message=message)
                    except Exception as e:
                        print(e.args)
            return reaction

        def create_new_page(cog:str):
            # print('New_page Function')
            data = get_commands_by_cog(cog)
            data = sorted(data)
            pages = []
            new_page = discord.Embed(title=f'Help for {ctx.message.author.display_name}',
                                     description=f'**Category:** ***`{cog}`***',
                                     colour=0xf20006)
            for item in data:
                new_page.add_field(name=f"-- {self.config['prefix']}{item[0]}\n\n",
                                value=f'***`{get_short_desc(item)}`***\n**Name:** ***`{item[0]}`***',
                                inline=False)
                pages.append(new_page)
            # print('DONE New_page Function')
            return pages

        def generate_pages():
            # print('generate_pages Function')
            all = []
            # print('all')
            all.append(create_new_page('Games'))
            # print('Games DONE')
            all.append(create_new_page('GameStats'))
            # print('GameStats DONE')
            all.append(create_new_page('Fun'))
            # print('Fun DONE')
            all.append(create_new_page('Music'))
             #print('Music DONE')
            all.append(create_new_page('Utils'))
            # print('Utils DONE')
            all.append(create_new_page('Images'))
            # print('Images DONE')
            all.append(create_new_page('Exchange'))
            # print('Exchange DONE')

            paginator = {}
            page_number = 0
            for item in all:
                page_number += 1
                paginator[str(page_number)] = item
            # print('DONE generate_pages Function')
            return paginator

        #test

        if command is None:
            # print('Function loaded in')

            # Pages
            page0 = discord.Embed(title=f'Help for: {ctx.message.author.display_name}',
                                  description='This command is under construction and may not work correctly\n\n'
                                              'If you are stuck this console is for you.\nNavigate around with the **`emoji\'s`** underneath.\n\n`{0}`: First page\n`{1}`: Five pages back\n`{2}`: One page back\n`{3}`: Next page\n`{4}`: Skip next five pages\n`{5}`: Last page\n\nIf you like to retrieve more information about a command.\nSimply add any command name behind **`{6}help`**\nFor example: Their is a command called **`battleship`**.\nIt\'s a game what you can play in discord.\nFor more information on how to play battleship use **`{6}help battleship`**\n\nIf this console is **`2`** minutes inactive it will shutdown'.format(
                                      self.emoji_start_txt, self.emoji_five_back_txt, self.emoji_oneback_txt, self.emoji_oneahead_txt, self.emoji_five_ahead_txt, self.emoji_end_txt, self.config['prefix']),
                                  colour=0xf20006)
            start = await self.bot.say(embed=page0)

            generate_pages_result = generate_pages()

            await self.bot.add_reaction(start, self.emoji_start)
            await self.bot.add_reaction(start, self.emoji_five_back) #Maybe if there are more commands
            await self.bot.add_reaction(start, self.emoji_oneback)
            await self.bot.add_reaction(start, self.emoji_oneahead)
            await self.bot.add_reaction(start, self.emoji_five_ahead) #Maybe if there are more commands
            await self.bot.add_reaction(start, self.emoji_end)

            await asyncio.sleep(0.6)

            page0.set_footer(text=f'Version: {self.version}\tReady...')
            await self.bot.edit_message(start, embed=page0)

            # print('Reactions added')

            # remove duplicates
            page = 0
            paginator = {}
            paginator['0'] = page0
            for key, value in generate_pages_result.items():
                paginator[key] = value[0]
                page += 1

            page_number = 1
            lenght_help = int(len(paginator.keys()) - 1)

            # print(f'QUery lenght: {lenght_help}')

            for i in range(100):
                reaction = await wait_for_reaction(start)
                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_start):
                    if page_number >= 1 and page_number <= lenght_help:
                        page_number = 0
                        # print(page_number)

                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_five_back):
                    if page_number >= 5 and page_number <= lenght_help:
                        page_number = page_number - 5
                        # print(page)

                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_oneback):
                    if page_number >= 1 and page_number <= lenght_help:
                        page_number = page_number - 1
                        # print(page)

                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_oneahead):
                    if page_number >= 0 and page_number <= lenght_help - 1:
                        page_number = page_number + 1
                        # print(page_number)

                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_five_ahead):
                    if page_number >= 0 and page_number <= lenght_help - 5:
                        page_number = page_number + 5
                        # print(page)

                if ascii(str(reaction.reaction.emoji)) == ascii(self.emoji_end):
                    if page_number <= lenght_help:
                        page_number = lenght_help
                        # print(page_number)

                embed = paginator[str(page_number)]
                embed.set_footer(text=f'Version: {self.version}\tPage: {int(page_number + 1)}/{int(len(paginator.keys()))}')
                await self.bot.edit_message(start, embed=embed)

        if command != None:
            commanden = get_command_by_name()
            print(commanden)
            if str(command).lower() in commanden:
                self.database.cur.execute("select * from botzilla.help where name = '{}';".format(str(command).lower()))
                command_object = self.database.cur.fetchone()
                self.database.cur.execute("ROLLBACK;")
                desc = str(command_object[2]).replace('<insert semicolon here>', ';')
                embed = discord.Embed(title=f'Help for: {ctx.message.author.display_name}',
                                      description=f'**\nCommand:** - **`{self.config["prefix"]}{command_object[0]}`**\n**Category:** - **`{command_object[1]}`**\n\n**Description:**\n**```\n{desc}\n```**',
                                      colour=0xf20006)
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['succes'])
            else:
                embed = discord.Embed(title=f'Help for: {ctx.message.author.display_name}',
                                      description=f'Unfortunately the command **`{self.config["prefix"]}{command}`** doesnt exist.\nAll commands can be found in **`{self.config["prefix"]}help`**',
                                      colour=0xf20006)
                last_message = await self.bot.say(embed=embed)
                await self.bot.add_reaction(last_message, self.emojiUnicode['warning'])


    async def build_rtfm_lookup_table(self):
        cache = {}

        page_types = {
            'rewrite': (
                'https://rapptz.github.io/discord.py/docs/api.html',
                'https://rapptz.github.io/discord.py/docs/ext/commands/api.html'
            ),
            'latest': (
                'https://discordpy.readthedocs.org/en/latest/api.html',
            )
        }

        for key, pages in page_types.items():
            sub = cache[key] = {}
            for page in pages:
                async with self.bot.session.get(page) as resp:
                    if resp.status != 200:
                        await self.bot.say('Cannot build rtfm lookup table, try again later.')
                        return

                    text = await resp.text(encoding='utf-8')
                    root = xml.etree.fromstring(text, xml.etree.HTMLParser())
                    nodes = root.findall(".//dt/a[@class='headerlink']")

                    for node in nodes:
                        href = node.get('href', '')
                        as_key = href.replace('#discord.', '').replace('ext.commands.', '')
                        sub[as_key] = page + href
        self._rtfm_cache = cache

    @commands.command(pass_context=True)
    async def rtfm(self, ctx, key, obj):
        """
        Discord.py documentation.
        Usefull for developers.

        Usage:
          - !!rtfm <Event | Object | Function>
        Example:
          - !!rtfm message
        """
        print(f'{datetime.date.today()} {datetime.datetime.now()} - {ctx.message.author} ran command !!rtfm <{obj}> in -- Channel: {ctx.message.channel.name} Guild: {ctx.message.server.name}')
        base_url = f'https://discordpy.readthedocs.org/en/{key}/'

        if obj is None:
            await self.bot.say(base_url)
            return

        if not hasattr(self, '_rtfm_cache'):
            await self.bot.send_typing(ctx.message.channel)

        # identifiers don't have spaces
        obj = obj.replace(' ', '_')

        if key == 'rewrite':
            pit_of_success_helpers = {
                'vc': 'VoiceClient',
                'msg': 'Message',
                'color': 'Colour',
                'perm': 'Permissions',
                'channel': 'TextChannel',
                'chan': 'TextChannel',
            }

            # point the abc.Messageable types properly:
            q = obj.lower()
            for name in dir(discord.abc.Messageable):
                if name[0] == '_':
                    continue
                if q == name:
                    obj = f'abc.Messageable.{name}'
                    break

            def replace(o):
                return pit_of_success_helpers.get(o.group(0), '')

            pattern = re.compile('|'.join(fr'\b{k}\b' for k in pit_of_success_helpers.keys()))
            obj = pattern.sub(replace, obj)

        cache = list(self._rtfm_cache[key].items())
        def transform(tup):
            return tup[0]

        matches = fuzzy.finder(obj, cache, key=lambda t: t[0], lazy=False)[:5]

        e = discord.Embed(colour=discord.Colour.blurple())
        if len(matches) == 0:
            return await self.bot.say('Could not find anything. Sorry.')

        e.description = '\n'.join(f'[{key}]({url})' for key, url in matches)
        await self.bot.say(embed=e)



def setup(bot):
    bot.add_cog(Help(bot))