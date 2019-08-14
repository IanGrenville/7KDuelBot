import praw
import re
import Duel
import time
reddit = praw.Reddit('duelbot', user_agent='Python:com.7k.duelbot:v0.1.0 (by /u/as334)')
subreddit = reddit.subreddit('SevenKingdoms')
for comment in subreddit.stream.comments(skip_existing=True):
	replied = False
	comment.refresh()
	for second_level_comment in comment.replies.list():  #Don't proccess comments we've already replied to
		if(second_level_comment.author and second_level_comment.author.name.lower() == "7kduelbot"):
			print("Already replied, duel skipped")
			replied = True		
	if(re.search("/u/7kduelbot",comment.body.lower()) and not replied): #Make sure we're tagged in order to run. Non caps-sensitive.
		#Terrifying regex that matches two lines of the form <Name> <Bonus> <Yield>
		duelinfo = re.match("(\w+ \w+) ([\+\-]?\d+) (\d+)\n+(\w+ \w+) ([\+\-]?\d+) (\d+)",comment.body)
		if(duelinfo):
			duel = Duel.Duel()
			if(re.search("Dramatic Mode",comment.body)):
				lastcomment = comment
				for round in duel.run(duelinfo).split("____"):
					try:
						lastcomment = lastcomment.reply(round)
					except: #Shouldn't happen too much, but in case we get rate limited.
						print("Rate limited. Sleeping for 6 minutes.")
						time.sleep(360)
						lastcomment = lastcomment.reply(round)
					time.sleep(120)
			else:
				comment.reply(duel.run(duelinfo))#Post all at once
		else:
			print("Improperly formatted duel info")
		time.sleep(180) #We sleep for 3 minutes after each duel so we don't get screwed by rate limits. Delete this when karma is high enough.