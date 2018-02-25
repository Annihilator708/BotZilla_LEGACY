from discord.ext import commands
import datetime
import json
import random
import discord
import asyncio
import ast
try:
    from plugin.database import Database
except Exception as e:
    pass


class Games:
    def __init__(self, bot):
        self.bot = bot
        self.tmp_config = json.loads(str(open('./options/config.js').read()))
        self.config = self.tmp_config['config']
        self.emojiUnicode = self.tmp_config['unicode']
        self.exchange = self.tmp_config['exchange']
        self.botzillaChannels = self.tmp_config['channels']
        self.owner_list = self.config['owner-id']
        self.battleship_emoji = json.loads(str(open('./options/battleship.js').read()))
        self.battleship_emoji_text = self.battleship_emoji['text']
        self.battleship_emoji_ascii = self.battleship_emoji['ascii']
        try:
            self.database = Database(self.bot)
            self.database_file_found = True
        except Exception as e:
            print('games: Database files not found - {}'.format(e.args))
            pass


    @commands.command(pass_context=True, name='8ball')
    async def ball8(self, ctx , *, question: str = None):
        """
        8ball! Ask BotZilla Any question.
        """
        print(f'{datetime.date.today()} {datetime.datetime.now()} - {ctx.message.author} ran command !!8ball <{question}> in -- Channel: {ctx.message.channel.name} Guild: {ctx.message.server.name}')
        question = question.lower()
        ball = random.randint(1, 20)

        # uncomment the following line to let the user now what number is picked by 8ball
        # ball_anaunce = await self.safe_send_message(channel, "8Ball chose number %s" % (ball))

        if question is None:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: You did not fully address your question!',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, self.emojiUnicode['Warning'])
            return

        if ball == 1:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: It is certain',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f605') # Done
            return

        if ball == 2:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: It is decidedly so',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f913') # Done
            return

        if ball == 3:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Without a doubt',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f611') # Done
            return

        if ball == 4:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Yes, definitely!',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f98b') # Done
            return

        if ball == 5:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: You may rely on it',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f60c') # Done
            return

        if ball == 6:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: As I see it, yes',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f48d') # Done
            return

        if ball == 7:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Most likely',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f609') # Done
            return

        if ball == 8:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Outlook good',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f44c') # done
            return

        if ball == 9:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Yes',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f525') # Done
            return

        if ball == 10:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Signs point to yes',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f607') # Done
            return

        if ball == 11:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Reply hazy try again',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f47b') # Done
            return

        if ball == 12:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Ask again later',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f550') # Done
            return

        if ball == 13:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Better not tell you now',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\u2620') # Done
            return

        if ball == 14:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Cannot predict now',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f914') # Done
            return

        if ball == 15:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Concentrate and ask again',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f616') # Done
            return

        if ball == 16:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Don\'t count on it',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f625') # Done
            return

        if ball == 17:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: My reply is no',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f4a9') # Done
            return

        if ball == 18:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: My sources say no',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f614') # Done
            return

        if ball == 19:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Outlook not so good',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f60f') # Done
            return

        if ball == 20:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description=':8ball: Very doubtful',
                                  colour=0xf20006)
            last_message = await self.bot.say(embed=embed)
            await self.bot.add_reaction(last_message, '\U0001f61f') # Done
            return


    @commands.command(pass_context=True, name='highlow')
    async def HighLow(self, ctx):
        """
        Higher or Lower? Gamble your way out! 0 ~ 1.000
        Is the next number higher or lower then your current number?
        Vote with the whole server!
        """
        print(f'{datetime.date.today()} {datetime.datetime.now()} - {ctx.message.author} ran command !!highlow in -- Channel: {ctx.message.channel.name} Guild: {ctx.message.server.name}')
        while True:
            number = random.randrange(0,1000)
            embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                  description='Higher or Lower than: **`{}`**\n**`10`** Seconds to vote..'.format(number),
                                  colour=0xf20006)
            a = await self.bot.say(embed=embed)
            await self.bot.add_reaction(a, '\U0001f53c')
            await self.bot.add_reaction(a, '\U0001f53d')
            await asyncio.sleep(10)
            new_number = random.randrange(0,1000)

            message = await self.bot.get_message(ctx.message.channel, a.id)
            more = message.reactions[0]
            less = message.reactions[1]
            total_more = more.count - 1
            total_less = less.count - 1
            total_votes = total_more + total_less
            vote_list = [total_more, total_less]
            winner = max(vote_list)
            await self.bot.delete_message(a)

            if total_votes == 0:
                embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                      description='GameOver! Nobody voted...\nUse **`{}highlow`** to start a new game'.format(self.config['prefix']),
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, '\U0001f480')
                break

            elif total_less == total_more:
                embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                      description='Vote Draw!\nContinue? **`10`** Seconds remaining'.format(new_number),
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])
                await self.bot.add_reaction(a, '\U0001f3f3')
                await asyncio.sleep(10)
                message = await self.bot.get_message(ctx.message.channel, a.id)
                emoji_continue = message.reactions[0]
                total_continue = emoji_continue.count - 1
                await self.bot.delete_message(a)
                if total_continue == 0:
                    embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                          description='Gameover! Nobody to play with...\nStart a new game with **`{}highlow`**'.format(self.config['prefix']),
                                          colour=0xf20006)
                    a = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(a, '\U0001f60f')
                    break


            elif winner == total_more and new_number >= number:
                embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                      description='Victorious! You hit number **`{}`**\nYour previous number was **`{}`**\n\nTotals\n-------\n:arrow_up_small: : **`{}`**    :arrow_down_small: : **`{}`**\nTotal Votes: **`{}`**\n\nNext round in **`10`** Seconds'.format(new_number, number, total_more, total_less, total_votes),
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])
                await asyncio.sleep(10)
                await self.bot.delete_message(a)

            elif winner == total_less and new_number <= number:
                embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                      description='Victorious! You hit number **`{}`**\nYour previous number was **`{}`**\n\nTotals\n-------\n:arrow_up_small:  : **`{}`**    :arrow_down_small: : **`{}`**\nTotal Votes: **`{}`**\n\nNext round in **`10`** Seconds'.format(new_number, number, total_more, total_less, total_votes),
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])
                await asyncio.sleep(10)
                await self.bot.delete_message(a)

            else:
                embed = discord.Embed(title='HighLow started by {}:'.format(ctx.message.author.name),
                                      description='GameOver! You hit number **`{}`**\nYour previous number was **`{}`**\n\nTotals\n-------\n:arrow_up_small:  : **`{}`**    :arrow_down_small: : **`{}`**\nTotal Votes: **`{}`**\n\nUse **`{}highlow`** for a new game!'.format(new_number, number, total_more, total_less, total_votes, self.config['prefix']),
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, '\U0001f480')
                break


    @commands.command(pass_context=True, aliases=["b"])
    async def battleship(self, ctx, row=None, *, column=None):
        """
        Play Battleship the game!!
        Progress will be saved.
        alias = !!b

        Shows playground
            -  !!battleship
        Shoot
            -  !!battleship <row> <column>
        Example
            -  !!battleship 4 2
        """
        print(f'{datetime.date.today()} {datetime.datetime.now()} - {ctx.message.author} ran command !!battleship <column> <row> in -- Channel: {ctx.message.channel.name} Guild: {ctx.message.server.name}')

        exploded_boats = ['https://cdn.discordapp.com/attachments/407238426417430539/417154082776809472/-48348a4958b806f1.jpg',
                          'https://cdn.discordapp.com/attachments/407238426417430539/417154097452548111/boatfire-prmjpg-promo-image.jpg',
                          'https://cdn.discordapp.com/attachments/407238426417430539/417154106549862400/C6aG4CDXEAAtfOI.jpg',
                          'https://cdn.discordapp.com/attachments/407238426417430539/417154116385767425/ce87dba2-f920-11e7-8693-80d4e18fb3a2_1280x720_195814.jpg',
                          'https://cdn.discordapp.com/attachments/407238426417430539/417154124472123392/Freightergoesboom.jpg',
                          'https://cdn.discordapp.com/attachments/407238426417430539/417154131690782732/images.jpg',
                          'https://media.discordapp.net/attachments/407238426417430539/417154276062789632/maxresdefault.jpg'
                          ]

        unexploded_boats = ['https://cdn.discordapp.com/attachments/407238426417430539/417158056921530369/Thumb.png',
                            'https://cdn.discordapp.com/attachments/407238426417430539/417157975652827151/csm_bavaria-mb-overview-sline_7b1037714c.png',
                            'https://cdn.discordapp.com/attachments/407238426417430539/417157946926170116/4306597_20130315092133359_1_XLARGE.png',
                            'https://media.discordapp.net/attachments/407238426417430539/417157916789833728/6544403_20171201080526644_1_LARGE.png',
                            'https://cdn.discordapp.com/attachments/407238426417430539/417158374707429397/0186-LG.png']

        try:
            self.database.cur.execute(f"select * from botzilla.battleship where ID = {ctx.message.author.id};")
            game = self.database.cur.fetchone()
            self.database.cur.execute("ROLLBACK;")
            self.database.cur.execute(f"select last_message from botzilla.battleship where ID = {ctx.message.author.id};")
            last_message_id = self.database.cur.fetchone()
            self.database.cur.execute("ROLLBACK;")

            if last_message_id:
                try:
                    message_2_remove = await self.bot.get_message(ctx.message.channel, last_message_id[0])
                    await self.bot.delete_message(message_2_remove)
                except Exception as e:
                    embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                          description='Perhaps this warning has something to do with permissions\nMake sure BotZilla do have the right permissions.\n**Error:**\n```py\n{}\n```'.format(e.args),
                                          colour=0xf20006)
                    a = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(a, self.emojiUnicode['warning'])

            # If no game for user, Make game for user
            if game is None:
                board = []
                for x in range(0, 10):
                    board.append(['O'] * 10)
                score = 0
                ship_row = random.randint(0, len(board) - 1)
                ship_col = random.randint(0, len(board[0]) - 1)
                board_db_insert = str(board).replace("'", "<A>").replace(",", "<C>") # make seperater for db, A for ' C for ,

                print(f"INSERT INTO botzilla.battleship (ID, gamehash, board, score) VALUES ({ctx.message.author.id}, {random.getrandbits(128)}, '{board_db_insert}', {score}, {ship_row}, {ship_col});")
                self.database.cur.execute(f"INSERT INTO botzilla.battleship (ID, gamehash, board, score, ship_row, ship_col) VALUES ({ctx.message.author.id}, {random.getrandbits(128)}, '{board_db_insert}', {score}, {ship_row}, {ship_col});")
                self.database.conn.commit()
                self.database.cur.execute("ROLLBACK;")

            # Get user game
            self.database.cur.execute(f"select * from botzilla.battleship where ID = {ctx.message.author.id};")
            game = self.database.cur.fetchone()
            self.database.cur.execute("ROLLBACK;")

            # define fetch variables
            id = int(game[0])
            gamehash = int(game[1])
            gamehash_lenght = len(str(gamehash)) // 2
            gamehash_str = str(gamehash)
            gamehash_1 = gamehash_str[:gamehash_lenght]
            gamehash_2 = gamehash_str[gamehash_lenght:]
            board = ast.literal_eval(str(game[2]).replace("<A>", "'").replace('<C>', ','))
            score = int(game[3])
            ship_row = int(game[4])
            ship_col = int(game[5])
            if ctx.message.author.id in self.owner_list:
                print(f'ANSWER : {int(ship_row) + 1} : {int(ship_col) + 1}')

            # if no column or row show game board and info about game... TO DO
            if column is None or row is None:
                header = f"{random.choice(self.battleship_emoji_text['boats'])} {self.battleship_emoji_text['one']} {self.battleship_emoji_text['two']} {self.battleship_emoji_text['three']} {self.battleship_emoji_text['four']} {self.battleship_emoji_text['five']} {self.battleship_emoji_text['six']} {self.battleship_emoji_text['seven']} {self.battleship_emoji_text['eight']} {self.battleship_emoji_text['nine']} {self.battleship_emoji_text['ten']} "
                row_1 = str(" ".join(board[0])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_2 = str(" ".join(board[1])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_3 = str(" ".join(board[2])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_4 = str(" ".join(board[3])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_5 = str(" ".join(board[4])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_6 = str(" ".join(board[5])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_7 = str(" ".join(board[6])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_8 = str(" ".join(board[7])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_9 = str(" ".join(board[8])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_10 = str(" ".join(board[9])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description=f"Score: **`{score}`**\n\n"
                                                  f"{header}\n{self.battleship_emoji_text['one']} {row_1}\n{self.battleship_emoji_text['two']} {row_2}\n{self.battleship_emoji_text['three']} {row_3}\n{self.battleship_emoji_text['four']} {row_4}\n{self.battleship_emoji_text['five']} {row_5}\n{self.battleship_emoji_text['six']} {row_6}\n{self.battleship_emoji_text['seven']} {row_7}\n{self.battleship_emoji_text['eight']} {row_8}\n{self.battleship_emoji_text['nine']} {row_9}\n{self.battleship_emoji_text['ten']} {row_10}"
                                                  f"\n\nGameHash:\n**{gamehash_1}\n{gamehash_2}**\nIf you are stuck\nuse **`{self.config['prefix']}help battleship`**",
                                      colour=0xf20006)
                embed.set_footer(text='PuffDip#5369 ©')
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])
                self.database.cur.execute(f"UPDATE botzilla.battleship SET last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                self.database.conn.commit()
                self.database.cur.execute("ROLLBACK;")
                return

            # make sure user input is a number when exist
            try:
                user_row = int(row) - 1
                user_col = int(column) - 1
            except Exception as e:
                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description='Please make sure the column and row you provided are numbers',
                                      colour=0xf20006)
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['error'])
                self.database.cur.execute(f"UPDATE botzilla.battleship SET last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                self.database.conn.commit()
                self.database.cur.execute("ROLLBACK;")
                return

            # debug print
            # print(f'ID : {id}\nGameHash : {gamehash}\nBoard : {board}\nScore : {score}\nSHIP\nship row: {ship_row}\nship_col: {ship_col}\n###\nUser row: {int(user_row) + 1}\nUser col: {int(user_col) + 1}')

            #if user wins
            if user_row == ship_row and user_col == ship_col:
                board[user_row][user_col] = "2"
                header = f"{random.choice(self.battleship_emoji_text['boats'])} {self.battleship_emoji_text['one']} {self.battleship_emoji_text['two']} {self.battleship_emoji_text['three']} {self.battleship_emoji_text['four']} {self.battleship_emoji_text['five']} {self.battleship_emoji_text['six']} {self.battleship_emoji_text['seven']} {self.battleship_emoji_text['eight']} {self.battleship_emoji_text['nine']} {self.battleship_emoji_text['ten']} "
                row_1 = str(" ".join(board[0])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_2 = str(" ".join(board[1])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_3 = str(" ".join(board[2])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_4 = str(" ".join(board[3])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_5 = str(" ".join(board[4])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_6 = str(" ".join(board[5])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_7 = str(" ".join(board[6])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_8 = str(" ".join(board[7])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_9 = str(" ".join(board[8])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                row_10 = str(" ".join(board[9])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])

                embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                      description=f"**`DIRECT HIT`**\nScore: **`{score}`**\n\n"
                                                  f"{header}\n{self.battleship_emoji_text['one']} {row_1}\n{self.battleship_emoji_text['two']} {row_2}\n{self.battleship_emoji_text['three']} {row_3}\n{self.battleship_emoji_text['four']} {row_4}\n{self.battleship_emoji_text['five']} {row_5}\n{self.battleship_emoji_text['six']} {row_6}\n{self.battleship_emoji_text['seven']} {row_7}\n{self.battleship_emoji_text['eight']} {row_8}\n{self.battleship_emoji_text['nine']} {row_9}\n{self.battleship_emoji_text['ten']} {row_10}"
                                                  f"\n\nGameHash:\n**{gamehash_1}\n{gamehash_2}**\nIf you are stuck\nuse **`{self.config['prefix']}help battleship`**",
                                      colour=0xf20006)
                embed.set_footer(text='PuffDip#5369 ©')
                embed.set_thumbnail(url=random.choice(exploded_boats))
                a = await self.bot.say(embed=embed)
                await self.bot.add_reaction(a, self.emojiUnicode['succes'])

                self.database.cur.execute(f"UPDATE botzilla.battleship SET last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                self.database.conn.commit()
                self.database.cur.execute("ROLLBACK;")

                board = []
                for x in range(0, 10):
                    board.append(['O'] * 10)
                ship_row = random.randint(0, len(board) - 1)
                ship_col = random.randint(0, len(board[0]) - 1)
                board_db_insert = str(board).replace("'", "<A>").replace(",", "<C>")  # make seperater for db, A for ' C for ,
                score += 1
                self.database.cur.execute(f"UPDATE botzilla.battleship SET board = '{board_db_insert}', score = {score}, ship_row = {ship_row},ship_col = {ship_col} where ID = {id} and gamehash = '{gamehash}';")
                self.database.conn.commit()
                self.database.cur.execute("ROLLBACK;")


            else:
                if user_row not in range(10) or user_col not in range(10):
                    header = f"{random.choice(self.battleship_emoji_text['boats'])} {self.battleship_emoji_text['one']} {self.battleship_emoji_text['two']} {self.battleship_emoji_text['three']} {self.battleship_emoji_text['four']} {self.battleship_emoji_text['five']} {self.battleship_emoji_text['six']} {self.battleship_emoji_text['seven']} {self.battleship_emoji_text['eight']} {self.battleship_emoji_text['nine']} {self.battleship_emoji_text['ten']} "
                    row_1 = str(" ".join(board[0])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_2 = str(" ".join(board[1])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_3 = str(" ".join(board[2])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_4 = str(" ".join(board[3])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_5 = str(" ".join(board[4])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_6 = str(" ".join(board[5])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_7 = str(" ".join(board[6])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_8 = str(" ".join(board[7])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_9 = str(" ".join(board[8])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_10 = str(" ".join(board[9])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                          description=f"**`Out of range`**\nScore: **`{score}`**\n"
                                                      f"{header}\n{self.battleship_emoji_text['one']} {row_1}\n{self.battleship_emoji_text['two']} {row_2}\n{self.battleship_emoji_text['three']} {row_3}\n{self.battleship_emoji_text['four']} {row_4}\n{self.battleship_emoji_text['five']} {row_5}\n{self.battleship_emoji_text['six']} {row_6}\n{self.battleship_emoji_text['seven']} {row_7}\n{self.battleship_emoji_text['eight']} {row_8}\n{self.battleship_emoji_text['nine']} {row_9}\n{self.battleship_emoji_text['ten']} {row_10}"
                                                      f"\n\nGameHash:\n**{gamehash_1}\n{gamehash_2}**\nIf you are stuck\nuse **`{self.config['prefix']}help battleship`**",
                                          colour=0xf20006)
                    embed.set_footer(text='PuffDip#5369 ©')
                    embed.set_thumbnail(url=random.choice(unexploded_boats))
                    a = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(a, self.emojiUnicode['warning'])

                    self.database.cur.execute(
                        f"UPDATE botzilla.battleship SET last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                    self.database.conn.commit()
                    self.database.cur.execute("ROLLBACK;")

                elif board[user_row][user_col] == '1':
                    header = f"{random.choice(self.battleship_emoji_text['boats'])} {self.battleship_emoji_text['one']} {self.battleship_emoji_text['two']} {self.battleship_emoji_text['three']} {self.battleship_emoji_text['four']} {self.battleship_emoji_text['five']} {self.battleship_emoji_text['six']} {self.battleship_emoji_text['seven']} {self.battleship_emoji_text['eight']} {self.battleship_emoji_text['nine']} {self.battleship_emoji_text['ten']} "
                    row_1 = str(" ".join(board[0])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_2 = str(" ".join(board[1])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_3 = str(" ".join(board[2])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_4 = str(" ".join(board[3])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_5 = str(" ".join(board[4])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_6 = str(" ".join(board[5])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_7 = str(" ".join(board[6])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_8 = str(" ".join(board[7])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_9 = str(" ".join(board[8])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_10 = str(" ".join(board[9])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                          description=f"**You already shot in that direction!**\nScore: **`{score}`**\n\n"
                                                      f"{header}\n{self.battleship_emoji_text['one']} {row_1}\n{self.battleship_emoji_text['two']} {row_2}\n{self.battleship_emoji_text['three']} {row_3}\n{self.battleship_emoji_text['four']} {row_4}\n{self.battleship_emoji_text['five']} {row_5}\n{self.battleship_emoji_text['six']} {row_6}\n{self.battleship_emoji_text['seven']} {row_7}\n{self.battleship_emoji_text['eight']} {row_8}\n{self.battleship_emoji_text['nine']} {row_9}\n{self.battleship_emoji_text['ten']} {row_10}"
                                                      f"\n\nGameHash:\n**{gamehash_1}\n{gamehash_2}**\nIf you are stuck\nuse **`{self.config['prefix']}help battleship`**",
                                          colour=0xf20006)
                    embed.set_footer(text='PuffDip#5369 ©')
                    embed.set_thumbnail(url=random.choice(unexploded_boats))
                    a = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(a, self.emojiUnicode['warning'])

                    self.database.cur.execute(
                        f"UPDATE botzilla.battleship SET last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                    self.database.conn.commit()
                    self.database.cur.execute("ROLLBACK;")

                else:
                    board[user_row][user_col] = "3"
                    header = f"{random.choice(self.battleship_emoji_text['boats'])} {self.battleship_emoji_text['one']} {self.battleship_emoji_text['two']} {self.battleship_emoji_text['three']} {self.battleship_emoji_text['four']} {self.battleship_emoji_text['five']} {self.battleship_emoji_text['six']} {self.battleship_emoji_text['seven']} {self.battleship_emoji_text['eight']} {self.battleship_emoji_text['nine']} {self.battleship_emoji_text['ten']} "
                    row_1 = str(" ".join(board[0])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_2 = str(" ".join(board[1])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_3 = str(" ".join(board[2])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_4 = str(" ".join(board[3])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_5 = str(" ".join(board[4])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_6 = str(" ".join(board[5])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_7 = str(" ".join(board[6])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_8 = str(" ".join(board[7])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_9 = str(" ".join(board[8])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    row_10 = str(" ".join(board[9])).replace('O', self.battleship_emoji_text['ocean']).replace('1', self.battleship_emoji_text['x']).replace('2', self.battleship_emoji_text['fire']).replace('3', self.battleship_emoji_text['bomb'])
                    embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                          description=f"**`MISS`**\nScore: **`{score}`**\n\n"
                                                      f"{header}\n{self.battleship_emoji_text['one']} {row_1}\n{self.battleship_emoji_text['two']} {row_2}\n{self.battleship_emoji_text['three']} {row_3}\n{self.battleship_emoji_text['four']} {row_4}\n{self.battleship_emoji_text['five']} {row_5}\n{self.battleship_emoji_text['six']} {row_6}\n{self.battleship_emoji_text['seven']} {row_7}\n{self.battleship_emoji_text['eight']} {row_8}\n{self.battleship_emoji_text['nine']} {row_9}\n{self.battleship_emoji_text['ten']} {row_10}"
                                                      f"\n\nGameHash:\n**{gamehash_1}\n{gamehash_2}**\nIf you are stuck\nuse **`{self.config['prefix']}help battleship`**",
                                          colour=0xf20006)
                    embed.set_footer(text='PuffDip#5369 ©')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/407238426417430539/417154157724827668/miss.jpg')
                    a = await self.bot.say(embed=embed)
                    await self.bot.add_reaction(a, self.emojiUnicode['warning'])

                    board[user_row][user_col] = "1"
                    board_db_insert = str(board).replace("'", "<A>").replace(",", "<C>")  # make seperater for db, A for ' C for ,
                    self.database.cur.execute(f"UPDATE botzilla.battleship SET board = '{board_db_insert}', last_message = '{a.id}' where ID = {id} and gamehash = '{gamehash}';")
                    self.database.conn.commit()
                    self.database.cur.execute("ROLLBACK;")

        # If anything goes wrong, Raise exeption
        except Exception as e:
            embed = discord.Embed(title='{}:'.format(ctx.message.author.name),
                                  description='Something went wrong, please notify me with **`{}report <How the error came up>`**\nError:\n**``{} : {}``**'.format(self.config['prefix'], type(e).__name__, e),
                                  colour=0xf20006)
            embed.set_footer(text='PuffDip#5369 ©')
            a = await self.bot.say(embed=embed)
            await self.bot.add_reaction(a, self.emojiUnicode['error'])


def setup(bot):
    m = Games(bot)
    bot.add_cog(m)
