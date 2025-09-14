import discord, random, json, os, asyncio
from discord.ext import commands
from collections import defaultdict
from discord.ext.commands import Context
from discord.ext.commands import CommandOnCooldown



if os.path.exists("balances.json"):
	with open("balances.json", "r") as f:
		data = json.load(f)
		balances = defaultdict(int, {int(k): v for k, v in data.items()})
else:
	balances = defaultdict(int)
	

#with open("balances .json", "w") as f:
#	json.dump(dict(balances), f) # <---- save data.
	
#with open("balance.json", "w") as f:
#	balances = json.load(f) 
#	balances = defaultdict(int, data) # <---- load data

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents) # Here you can change the bot's prefix.'

@bot.event
async def on_ready():
	print("Your text here.")
	# It ill print any text you want in the console whenever you initiate the bot.
	
@bot.command(name="work")
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx:commands.Context):
	user = ctx.author.name
	user_id = ctx.author.id
	
	gained = random.randint(1, 700)
	
	balances[user_id] += gained
	total = balances[user_id]
	await ctx.send(f"Your text here.")
	with open("balances.json", "w") as f:
		json.dump(dict(balances), f)
	# In this line, the code will add a random number between 1 and 700 (you can change it freely) to his balances .

		role = ctx.guild.get_role() # Inside this (), you'll put the role's id, if you don't want this shit, delete this and the whole "add role" and "remove role".'
		
		# Add role.
		if balances[user_id] >= 1 and role not in member.roles:
			await member.add_roles(roleabc)
			await ctx.send(f'Your text here.')
			# This line will check if the author has the role, if not, the bot will add the role to his profile (the author needs to have an equal or higher balance than 1, you can change it freely too).
		
		# Remove role.
		if balances[user_id] <= 0 and role in member.roles:
			await member.remove_roles(roleabc)
			await ctx.send("Your text here.")
			# This line will check if the author has the role or not, if he has, the bot will remove his role (the author needs to have 0 or less to remove it, you can change it freely tho).
			
@work.error
async def work_error(ctx:commands.Context, error):
	if isinstance(error, CommandOnCooldown):
		await ctx.reply(f'Your text here.')
		# This one will prevent the author to use this command while in cooldown.
	
@bot.command()
async def bank(ctx:commands.Context):
	user_id = ctx.author.id
	
	if balances[user_id] == 0:
		await ctx.reply(f"Your text here.")
		return
		# This one will be an easter egg for whoever has 0 in his balances (you can remove if you want).
		
	if balances[user_id] >= 1:
		await ctx.reply(f"Your text here.")
		return
		# This line will show his balances (nothing to say).
		
	elif balances[user_id] <= -1:
		await ctx.reply(f"Your text here.")
		return
		# This message is an easter egg for anyone who has a negative balance (you can change the balances in the .json).
		
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bet(ctx:commands.Context, bet:str, value:int):
	user_id = ctx.author.id
	user = ctx.author.name
	if value <= 0:
		await ctx.reply(f"Your text here.")
		return
	# This line will prevent the author to bet a value thats equal or lower than 0.
		
	if balances[user_id] < value:
		await ctx.reply(f'Your text here.')
		return
	# This line will make the bot say whatever you want if balances is lower than the value he inserted.
	
	
	elif bet.lower() == "koi":
		await ctx.send(f"...")
		return
	
	elif bet.lower() == "acrskoi":
		await ctx.send("...")
		return
		
	elif bet.lower() == "k0i":
		await ctx.send("...")
		return
	
	elif bet.lower() == "k01":
		await ctx.send("...")
		
	elif bet.lower() == "4crsk01":
		await ctx.send ("...")
	
	elif bet.lower() == "4crsk0i":
		await ctx.send("...")
		
	elif bet.lower() == "4crsko1":
		await ctx.send("...")
	
	elif bet.lower() == "acrsk0i":
		await ctx.send("...")
		
	elif bet.lower() == "acrsk01":
		await ctx.send("...")
	
	elif bet.lower() == "acrsko1":
		await ctx.send("...")
		# self explain
		
	slot = random.choice(["win", "lose", "lose"])
	if slot == "win":
		slot_win = value*2
		balances[user_id] += slot_win
		await ctx.send(f"Your text here.")
		with open("balances.json", "w") as f:
			json.dump(dict(balances), f)
		# This entire line will choose between lose or win for the bet, and it'll duplicate his value and credited in his balances, the 193 line is what the bot is going to say.'
		
	else:
		balances[user_id] -= value
		await ctx.send(f"Your text here.")
		with open ("balances.json", "w") as f:
			json.dump(dict(balances), f) # This part will determinate if the author loses his bet, the 198 line will make his balances decrease by the total he used on the bet, 199 is what the bot will say to him, and 201, 202 will overwrite his new balance.

@bet.error
async def bet_error(ctx:commands.Context, error):
			if isinstance(error, CommandOnCooldown):
				await ctx.reply(f"Your text here.") # this message will show while the person is on cooldown.
			
@bot.command()
async def credits(ctx:commands.Context):
		user = ctx.author.mention
		await ctx.send(f"Bot made by AcrsKoi and (your name)")
		
@bot.command()
async def commands(ctx:commands.Context):
	await ctx.reply(f"Your text here."
	" $work"
	" $commands"
	" $bank"
	" $credit"
	" $bet"
	" $leaderboard"
	" $give"
	)	# This command will show every command that i created, if you add a new command, please, insert in this list.	

@bot.command()
async def give(ctx, member:discord.Member, value:int):
	sender_id = ctx.author.id
	receiver_id = member.id
	
	if value <= 0:
		await ctx.reply(f"Your text here.") # This one will print the text if the value the sender is giving is equal or less than 0.
		return
	if balances[sender_id] < value:
		await ctx.reply(f"Your text here.") # It'll show if the sender has no money or the value he inserted is higher than his balances.
		return
	balances[sender_id] -= value
	balances[receiver_id] += value
	await ctx.reply(f"Your text here.")
	with open("balances.json", "w") as f:
		json.dump(dict(balances), f) # This will print how much money you gave to a person (optional), and it will overwrite yours and his balances.json.
		
@bot.command()
async def leaderboard(ctx):
		if not balances:
			await ctx.reply("Your text here.") # This message will show if there's no balances to read.
			return
		
		guild = ctx.guild
		sorted_balances = sorted(balances.items(), key=lambda x: x[1], reverse=True)
		top_10 = sorted_balances[:10]
		embed = discord.Embed(title="Leaderboard", color=discord.Color.red()) # Here you can change the title and the embed color (in the left).
		for i , (user_id, money) in enumerate(sorted_balances[:10], start=1):
			member = guild.get_member(user_id)
			if member:
				name = member.display_name
			else:
				name = f"Foreigner ({user_id})" # Here you can determinate how the bot is going to name everyone who isn't in your server.
			user = await bot.fetch_user(user_id)
			embed.add_field(name=f"#{i}. {name}", value=f"{money}", inline=False)
		
		await ctx.reply(embed=embed)
		
bot.run("BOT'S TOKEN")
