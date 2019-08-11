import praw
import re
import Duel

reddit = praw.Reddit('duelbot', user_agent='Python:com.7k.duelbot:v0.0.1 (by /u/as334)')
subreddit = reddit.subreddit('ByTheShadow')
for comment in subreddit.stream.comments():
	for second_level_comment in comment.replies:  #Don't proccess comments we've already replied to
		if(second_level_comment.author.name == "/u/7KDuelBot"):
			print("Already replied, duel skipped")
			continue
	if(re.search("/u/7KDuelBot",comment.body)): #Make sure we're tagged in order to run
		#Terrifying regex that matches two lines of the form <Name> <Bonus> <Yield>
		duelinfo = re.match("(\w+ \w+) ([\+\-]?\d+) (\d+)\n+(\w+ \w+) ([\+\-]?\d+) (\d+)",comment.body)
		if(duelinfo):
			duel = Duel.Duel()
			comment.reply(duel.run(duelinfo))
		else:
			print("Improperly formatted duel info")