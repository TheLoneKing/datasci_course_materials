import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    tag_ocurrences = {} # initialize an empty dictionary
    hashtags = {}
    for line in tweet_file:
        line_dict = json.loads(line)
        if ('entities' in line_dict and 'hashtags' in line_dict['entities']):
            hashtags = line_dict['entities']['hashtags']
        for hashtag in hashtags:
            tag = hashtag['text'].encode('utf-8')
            if tag in tag_ocurrences:
                tag_ocurrences[tag] += 1
            else:
                tag_ocurrences[tag] = 1
    tweet_file.close()
    for i in xrange(10):
        top_Tag = max(tag_ocurrences, key=tag_ocurrences.get)
        print top_Tag, tag_ocurrences[top_Tag]
        del tag_ocurrences[top_Tag]

if __name__ == '__main__':
    main()
