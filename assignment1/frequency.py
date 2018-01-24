import sys
import json

def main():
	tweet_file = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	normalization_factor = 0
	for line in tweet_file:
		line_dict = json.loads(line)
		tweet = ''
		if 'text' in line_dict:
			tweet = line_dict['text']
		encoded_tweet = tweet.encode('utf-8')
		for word in encoded_tweet.split():
			if word in scores:
				scores[word] += 1
				normalization_factor += 1
			else:
				scores[word] = 1
				normalization_factor += 1
	tweet_file.close()
	for key in scores:
		frequency = scores[key] / float(normalization_factor)
		print key, frequency


if __name__ == '__main__':
    main()
