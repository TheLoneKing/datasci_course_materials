import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        line_dict = json.loads(line)
        tweet = ''
        if 'text' in line_dict:
            tweet = line_dict['text']
        score = 0
        encoded_tweet = tweet.encode('utf-8')
        for word in encoded_tweet.split():
            if word in scores:
                score += scores[word]
        print str(score)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()
