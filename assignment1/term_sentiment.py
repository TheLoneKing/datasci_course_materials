import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    sentiment = {}
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
        for word in encoded_tweet.split():
            if word not in scores:
                if score > 0:
                    if word in sentiment:
                        sentiment[word] += 1
                    else:
                        sentiment[word] = 1
                elif score < 0:
                    if word in sentiment:
                        sentiment[word] -= 1
                    else:
                        sentiment[word] = -1
                elif word not in sentiment:
                    sentiment[word] = 0
    sent_file.close()
    tweet_file.close()
    for word in sentiment:
        print word, float(sentiment[word])

if __name__ == '__main__':
    main()
