A simple discord casino bot with some simple features:
- Automatic bets
- Automatic roles
- Leaderboard

prerequisites:
- Python 3.13+
- Discord.py

Setup TIME!

1 - Copy:
```bash
git clone https://github.com/AcrsKoi/casino-bot.git
```
2 - Enter the folder:
```cd casino-bot```

3 - Make a virtual ambient (recommended)
```python -m venv venv```

4 - Activate the virtual ambient:

WINDOWS:
```venv\Scripts\activate```

LINUX/MACOS:
```source venv/bin/activate```

5 - Install the requirements:
```pip install -r requirements.txt```

Done! Now you can configurate the bot, check this list:
- Change the "BOT'S TOKEN" to your bot's token in the main.py.
- Change every "Your text here." with the messages that the bot will send (i explained most in the code).
- If you want or not an automatic system with the bot adding roles, make sure to edit that part too, or else the code will break.
- Make sure that there's a balances.json with an empty {} .

Execute the bot using the command:
```python main.py```

Now, time for the commands.

Work: Makes the author "work" and add a random number between 1 and 700 (you can change it in the code) and add it into balances.json with his discord id.


Bet: It let the author to bet a value and an item ($bet int(value) str(item)).


Give: If the author is good enough, he can give part of his money to a person ($give int(value) ping)).


Leaderboard: Shows a top 10 leaderboard with anyone who's in the balances.json, if the person isn't in the server, the bot will recognize him as "foreigner", you can change that too.


Credits: Self explain


Bank: Let the author to see how many money he have.


Commands: Send a list with all the commands (EDITABLE, IF YOU CREATE A NEW COMMAND, MAKE SURE TO ADD IT IN THIS LIST).

credits: AcrsKoi
