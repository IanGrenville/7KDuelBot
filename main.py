import praw
import re
import Duel

reddit = praw.Reddit('duelbot', user_agent='Python:com.7k.duelbot:v0.0.1 (by /u/as334)')
subreddit = reddit.subreddit('Triarchs')
for comment in subreddit.stream.comments():
	replied = False
	comment.refresh()
	for second_level_comment in comment.replies.list():  #Don't proccess comments we've already replied to
		if(second_level_comment.author.name.lower() == "7kduelbot"):
			print("Already replied, duel skipped")
			replied = True		
	if(re.search("/u/7kduelbot",comment.body.lower()) and not replied): #Make sure we're tagged in order to run. Non caps-sensitive.
		#Terrifying regex that matches two lines of the form <Name> <Bonus> <Yield>
		duelinfo = re.match("(\w+ \w+) ([\+\-]?\d+) (\d+)\n+(\w+ \w+) ([\+\-]?\d+) (\d+)",comment.body)
		if(duelinfo):
			duel = Duel.Duel()
			comment.reply(duel.run(duelinfo))
		else:
			print("Improperly formatted duel info")