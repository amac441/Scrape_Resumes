
import nltk
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
from nltk.corpus import stopwords


class NaiveSummarizer:
       
        def summarize(self, input, num_sentences):

                punt_list=['.',',','!','?']
                summ_sentences = []

                sentences = sent_tokenize(input)
                lowercase_sentences =[sentence.lower() 
                        for sentence in sentences]
                #print lowercase_sentences
                
                s=list(input)
                ts=''.join([ o for o in s if not o in  punt_list ]).split()
                lowercase_words=[word.lower() for word in ts]
                words = [word for word in lowercase_words if word not in stopwords.words()]
                word_frequencies = FreqDist(words)
                
                most_frequent_words = [pair[0] for pair in 
                        word_frequencies.items()[:100]]

                # add sentences with the most frequent words
                for word in most_frequent_words:
                        for i in range(0, len(lowercase_sentences)):
                                if len(summ_sentences) < num_sentences:
                                        if (lowercase_sentences[i] not in summ_sentences and word in lowercase_sentences[i]):
                                                summ_sentences.append(sentences[i])
                                                break
                                        
                        
                # reorder the selected sentences
                summ_sentences.sort( lambda s1, s2: input.find(s1) - input.find(s2) )
                return " ".join(summ_sentences)


if __name__ == "__main__":

        naivesum = NaiveSummarizer()
        text='''
hello
        '''
        text2 = '''
        Early life and career

Main article: Early life and career of Thomas Jefferson
The third of ten children, Thomas Jefferson was born on April 13, 1743 (April 2, 1743 OS) at the family home in Shadwell, Goochland County, Virginia, now part of Albemarle County.[2] His father was Peter Jefferson, a planter and surveyor.[3] He was of possible Welsh descent, although this remains unclear.[4] His mother was Jane Randolph, daughter of Isham Randolph, a ship's captain and sometime planter. Peter and Jane married in 1739.[5] Thomas Jefferson showed little interest in learning about his ancestry; he only knew of the existence of his paternal grandfather.[4]
Before the widower William Randolph, an old friend of Peter Jefferson, died in 1745, he appointed Peter as guardian to manage his Tuckahoe Plantation and care for his four children. That year the Jeffersons relocated to Tuckahoe, where they lived for the next seven years before returning to Shadwell in 1752. Peter Jefferson died in 1757 and the Jefferson estate was divided between Peter's two sons; Thomas and Randolph.[6] Thomas inherited approximately 5,000 acres (2,000 ha; 7.8 sq mi) of land, including Monticello and between 20 and 40 slaves. He took control of the property after he came of age at 21. The precise amount of land and number of slaves that Jefferson inherited is estimated. The first known record Jefferson made in regards to slave ownership, was in 1774, when he owned 41.[7]

Education

Further information: Thomas Jefferson and education
Jefferson began his childhood education under the direction of tutors at Tuckahoe along with the Randolph children.[8] In 1752, Jefferson began attending a local school run by a Scottish Presbyterian minister. At the age of nine, Jefferson began studying Latin, Greek, and French; he learned to ride horses, and began to appreciate the study of nature. He studied under Reverend James Maury from 1758 to 1760 near Gordonsville, Virginia. While boarding with Maury's family, he studied history, science and the classics.[9]
At age 16, Jefferson entered the College of William & Mary in Williamsburg, and first met the law professor George Wythe, who became his influential mentor. He studied mathematics, metaphysics, and philosophy under Professor William Small, who introduced the enthusiastic Jefferson to the writings of the British Empiricists, including John Locke, Francis Bacon, and Isaac Newton.[10] He also improved his French, Greek, and violin. A diligent student, Jefferson displayed an avid curiosity in all fields[11] and graduated in 1762, completing his studies in only two years. Jefferson read law while working as a law clerk for Wythe. During this time, he also read a wide variety of English classics and political works. Jefferson was admitted to the Virginia bar in 1767.[12]
Throughout his life, Jefferson depended on books for his education. He collected and accumulated thousands of books for his library at Monticello. When Jefferson's father Peter died Thomas inherited, among other things, his large library.[13] A significant portion of Jefferson's library was also bequeathed to him in the will of George Wythe, who had an extensive collection. After the British burned the Library of Congress in 1814 Jefferson offered to sell his collection of more than six thousand books to the Library of Congress for $23,950. After realizing he was no longer in possession of such a grand collection he wrote in a letter to John Adams, "I cannot live without books". He intended to pay off some of his large debt, but immediately started buying more books.[14] In February 2011 the New York Times reported that a part of Jefferson's retirement library, containing 74 volumes with 28 book titles, was discovered at Washington University in St. Louis.[15] In honor of Jefferson's contribution, the library's website for federal legislative information was named THOMAS.[15][16]

Marriage and family
After practicing as a circuit lawyer for several years, Jefferson married the 23-year-old widow Martha Wayles Skelton on January 1, 1772. Martha Jefferson was attractive, gracious and popular with her friends; she was a frequent hostess for Jefferson and managed the large household. They had a happy marriage. She read widely, did fine needle work and was an amateur musician. Jefferson played the violin and Martha was an accomplished piano player. It is said that she was attracted to Thomas largely because of their mutual love of music.[17] [18] During the ten years of their marriage, Martha bore six children: Martha, called Patsy, (1772?1836); Jane (1774?1775); an unnamed son (1777); Mary Wayles, called Polly, (1778?1804); Lucy Elizabeth (1780?1781); and Lucy Elizabeth (1782?1785). Only Martha and Mary survived to adulthood.[19] After her father John Wayles died in 1773, Martha and her husband Jefferson inherited his 135 slaves, 11,000 acres (4,500 ha; 17 sq mi) and the debts of his estate. These took Jefferson and other co-executors of the estate years to pay off, which contributed to his financial problems. Later in life, Martha Jefferson suffered from diabetes and ill health, and frequent childbirth further weakened her. A few months after the birth of her last child, Martha died on September 6, 1782, at the age of 33. Jefferson was at his wife's bedside and was distraught after her death. In the following three weeks, Jefferson shut himself in his room, where he paced back and forth until he was nearly exhausted. Later he would often take long rides on secluded roads to mourn for his wife.[19][20] As he had promised his wife, Jefferson never remarried.
Monticello

Further information: Monticello and Jeffersonian architecture
Jefferson's Home Monticello

Monticello west lawn in October 2010
In 1768, Jefferson began construction of his primary residence, Monticello, (Italian for "Little Mountain") on a hilltop overlooking a 5,000 acre plantation.[note 2] Construction was done mostly by local masons and carpenters, assisted by Jefferson's slaves. Jefferson moved into the South Pavilion (an outbuilding) in 1770, where his new wife, Martha, joined him in 1772. Turning Monticello into a neoclassical masterpiece after the Palladian style would be his continuing project.[22]
In 18th century colonial Virginia there were no architecture schools, so Jefferson learned the trade on his own from various books and by studying some of the various classical architectural designs of the day. His "bible" was Andrea Palladio's The Four Books of Architecture, which taught him the basic principles of classical design.[23][24] While Minister to France during 1784?1789, Jefferson had opportunity to see some of the classical buildings with which he had become acquainted from his reading, as well as to discover the "modern" trends in French architecture then fashionable in Paris. In 1794, following his service as Secretary of State (1790?93), he began rebuilding Monticello based on the ideas he had acquired in Europe. The remodeling continued throughout most of his presidency (1801?09). The most notable change was the addition of the octagonal dome.[25][26]
Lawyer and House of Burgesses
Jefferson was a lawyer in colonial Virginia from 1768 to 1773 with his friend and mentor, George Wythe.[27] Jefferson's client list featured members of Virginia's elite families, including members of his mother's family, the Randolphs.[27] Beside practicing law, Jefferson represented Albemarle County in the Virginia House of Burgesses beginning on May 11, 1769 and ending June 20, 1775.[28] Following the passage of the Intolerable Acts by the British Parliament in 1774, Jefferson wrote a set of resolutions against the acts. These were later expanded into A Summary View of the Rights of British America, in which he expressed his belief that people had the right to govern themselves.[29]

'''
        print(naivesum.summarize(text2,4))
        #print(naivesum.summarize(text,2))

## Very simple summarizer - https://github.com/thavelick/summarize/blob/master/summarize.py
## And a navie bayes summarizer - https://github.com/amsqr/NaiveSumm/blob/master/naivesumm.py
## This one might be the best b/c it gives explanation - https://gist.github.com/shlomibabluki/5473521
           # http://thetokenizer.com/tag/python/

#print('Hello World')

#import urllib
#import re
#from bs4 import BeautifulSoup

## WikiHow
## http://www.wikihow.com/Special:GoogSearch?cx=008953293426798287586%3Amr-gwotjmbs&cof=FORID%3A10&ie=UTF-8&q=build+a+hot+air+balloon&siteurl=www.wikihow.com%2FMain-Page
## http://www.wikihow.com/Special:GoogSearch?cx=008953293426798287586%3Amr-gwotjmbs&cof=FORID%3A10&ie=UTF-8&q=fly&siteurl=www.wikihow.com%2FMain-Page&siteurl=www.wikihow.com%252FMain-Page

## Google
## https://www.google.com/#q=how+to+build+a+hot+air+balloon
## https://www.google.com/#q=how+to+fly

## About.com
## http://search.about.com/?q=how+to+build+a+hot+air+balloon

## Need to create a custom search engine, and be bashful about the scraping
#    # https://www.google.com/cse/
#    # try xgoogle - https://github.com/pkrumins/xgoogle

## Need to compile list of sites
#       #about.com
#       #wikihow
#       #indeed.com

#url = "http://www.wikihow.com/Make-a-Mini-Flyable-Hot-Air-Balloon-with-Candles"

#htmlfile = urllib.urlopen(url)
#htmltext = htmlfile.read()

## regex = '<span id="yfs_184_aapl">(.+?)</span>'
## regex = '>"\s*([^"]*)\s*"'
#regex = '"([A-Za-z0-9_\./\\-]*)"'

## i'm afraid it will be like a bottle rocket
## they went from talking about their terrible ex wifes to talking about sex
## maybe i should just set the bar low  - what time do you have to go pickup kids 
## i dont want to keep you from your kids  - im in the basement - just got a wall and a door up
## i'm in the basement and it's not completed - house stays fairly clean, but yah

#pattern = re.compile(regex)

#text = re.findall(pattern,htmltext)
#    #findall takes two arguments.  1. compiled regex expression 2. the htmltext you want to search

#print text



# -*- coding: utf8 -*-

#from __future__ import absolute_import
#from __future__ import division, print_function, unicode_literals

##from sumy.parsers.html import HtmlParser
#from sumy.nlp.tokenizers import Tokenizer
#from sumy.summarizers.lsa import LsaSummarizer
#from sumy.nlp.stemmers.english import stem_word
#from sumy.utils import get_stop_words


#if __name__ == "__main__":
#    url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
#    #parser = HtmlParser.from_url(url, Tokenizer("english"))
#    parser = "After practicing as a circuit lawyer for several years, Jefferson married the 23-year-old widow Martha Wayles Skelton on January 1, 1772. Martha Jefferson was attractive, gracious and popular with her friends; she was a frequent hostess for Jefferson and managed the large household. They had a happy marriage. She read widely, did fine needle work and was an amateur musician. Jefferson played the violin and Martha was an accomplished piano player. It is said that she was attracted to Thomas largely because of their mutual love of music.[17] [18] During the ten years of their marriage, Martha bore six children: Martha, called Patsy, (1772?1836); Jane (1774?1775); an unnamed son (1777); Mary Wayles, called Polly, (1778?1804); Lucy Elizabeth (1780?1781); and Lucy Elizabeth (1782?1785). Only Martha and Mary survived to adulthood.[19] After her father John Wayles died in 1773, Martha and her husband Jefferson inherited his 135 slaves, 11,000 acres (4,500 ha; 17 sq mi) and the debts of his estate. These took Jefferson and other co-executors of the estate years to pay off, which contributed to his financial problems. Later in life, Martha Jefferson suffered from diabetes and ill health, and frequent childbirth further weakened her. A few months after the birth of her last child, Martha died on September 6, 1782, at the age of 33. Jefferson was at his wife's bedside and was distraught after her death. In the following three weeks, Jefferson shut himself in his room, where he paced back and forth until he was nearly exhausted. Later he would often take long rides on secluded roads to mourn for his wife.[19][20] As he had promised his wife, Jefferson never remarried."

#    summarizer = LsaSummarizer(stem_word)
#    summarizer.stop_words = get_stop_words("english")

#    for sentence in summarizer(parser, 20):
#        print(sentence)


## coding=UTF-8
#from __future__ import division
#import re
 
## This is a naive text summarization algorithm
## Created by Shlomi Babluki
## April, 2013
 
 
#class SummaryTool(object):
 
#    # Naive method for splitting a text into sentences
#    def split_content_to_sentences(self, content):
#        content = content.replace("\n", ". ")
#        return content.split(". ")
 
#    # Naive method for splitting a text into paragraphs
#    def split_content_to_paragraphs(self, content):
#        return content.split("\n\n")
 
#    # Caculate the intersection between 2 sentences
#    def sentences_intersection(self, sent1, sent2):
 
#        # split the sentence into words/tokens
#        s1 = set(sent1.split(" "))
#        s2 = set(sent2.split(" "))
 
#        # If there is not intersection, just return 0
#        if (len(s1) + len(s2)) == 0:
#            return 0
 
#        # We normalize the result by the average number of words
#        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)
 
#    # Format a sentence - remove all non-alphbetic chars from the sentence
#    # We'll use the formatted sentence as a key in our sentences dictionary
#    def format_sentence(self, sentence):
#        sentence = re.sub(r'\W+', '', sentence)
#        return sentence
 
#    # Convert the content into a dictionary <K, V>
#    # k = The formatted sentence
#    # V = The rank of the sentence
#    def get_senteces_ranks(self, content):
 
#        # Split the content into sentences
#        sentences = self.split_content_to_sentences(content)
 
#        # Calculate the intersection of every two sentences
#        n = len(sentences)
#        values = [[0 for x in xrange(n)] for x in xrange(n)]
#        for i in range(0, n):
#            for j in range(0, n):
#                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])
 
#        # Build the sentences dictionary
#        # The score of a sentences is the sum of all its intersection
#        sentences_dic = {}
#        for i in range(0, n):
#            score = 0
#            for j in range(0, n):
#                if i == j:
#                    continue
#                score += values[i][j]
#            sentences_dic[self.format_sentence(sentences[i])] = score
#        return sentences_dic
 
#    # Return the best sentence in a paragraph
#    def get_best_sentence(self, paragraph, sentences_dic):
 
#        # Split the paragraph into sentences
#        sentences = self.split_content_to_sentences(paragraph)
 
#        # Ignore short paragraphs
#        if len(sentences) < 2:
#            return ""
 
#        # Get the best sentence according to the sentences dictionary
#        best_sentence = ""
#        max_value = 0
#        for s in sentences:
#            strip_s = self.format_sentence(s)
#            if strip_s:
#                if sentences_dic[strip_s] > max_value:
#                    max_value = sentences_dic[strip_s]
#                    best_sentence = s
 
#        return best_sentence
 
#    # Build the summary
#    def get_summary(self, title, content, sentences_dic):
 
#        # Split the content into paragraphs
#        paragraphs = self.split_content_to_paragraphs(content)
 
#        # Add the title
#        summary = []
#        summary.append(title.strip())
#        summary.append("")
 
#        # Add the best sentence from each paragraph
#        for p in paragraphs:
#            sentence = self.get_best_sentence(p, sentences_dic).strip()
#            if sentence:
#                summary.append(sentence)
 
#        return ("\n").join(summary)
 
 
## Main method, just run "python summary_tool.py"
#def main():
 
#    # Demo
#    # Content from: "http://en.wikipedia.org/wiki/Thomas_Jefferson"
 
#    title = """
#    Thomas Jefferson
#    """
 
#    content = """
#    Lior Degani, the Co-Founder and head of Marketing of Swayy, pinged me last week when I was in California to tell me about his startup and give me beta access. I heard his pitch and was skeptical. I was also tired, cranky and missing my kids ? so my frame of mind wasn?t the most positive.
 
#    I went into Swayy to check it out, and when it asked for access to my Twitter and permission to tweet from my account, all I could think was, ?If this thing spams my Twitter account I am going to bitch-slap him all over the Internet.? Fortunately that thought stayed in my head, and not out of my mouth.
 
#    One week later, I?m totally addicted to Swayy and glad I said nothing about the spam (it doesn?t send out spam tweets but I liked the line too much to not use it for this article). I pinged Lior on Facebook with a request for a beta access code for TNW readers. I also asked how soon can I write about it. It?s that good. Seriously. I use every content curation service online. It really is That Good.
 
#    What is Swayy? It?s like Percolate and LinkedIn recommended articles, mixed with trending keywords for the topics you find interesting, combined with an analytics dashboard that shows the trends of what you do and how people react to it. I like it for the simplicity and accuracy of the content curation. Everything I?m actually interested in reading is in one place ? I don?t have to skip from another major tech blog over to Harvard Business Review then hop over to another major tech or business blog. It?s all in there. And it has saved me So Much Time
 
 
 
#    After I decided that I trusted the service, I added my Facebook and LinkedIn accounts. The content just got That Much Better. I can share from the service itself, but I generally prefer reading the actual post first ? so I end up sharing it from the main link, using Swayy more as a service for discovery.
 
#    I?m also finding myself checking out trending keywords more often (more often than never, which is how often I do it on Twitter.com).
 
 
 
#    The analytics side isn?t as interesting for me right now, but that could be due to the fact that I?ve barely been online since I came back from the US last weekend. The graphs also haven?t given me any particularly special insights as I can?t see which post got the actual feedback on the graph side (however there are numbers on the Timeline side.) This is a Beta though, and new features are being added and improved daily. I?m sure this is on the list. As they say, if you aren?t launching with something you?re embarrassed by, you?ve waited too long to launch.
 
#    It was the suggested content that impressed me the most. The articles really are spot on ? which is why I pinged Lior again to ask a few questions:
 
#    How do you choose the articles listed on the site? Is there an algorithm involved? And is there any IP?
 
#    Yes, we?re in the process of filing a patent for it. But basically the system works with a Natural Language Processing Engine. Actually, there are several parts for the content matching, but besides analyzing what topics the articles are talking about, we have machine learning algorithms that match you to the relevant suggested stuff. For example, if you shared an article about Zuck that got a good reaction from your followers, we might offer you another one about Kevin Systrom (just a simple example).
 
#    Who came up with the idea for Swayy, and why? And what?s your business model?
 
#    Our business model is a subscription model for extra social accounts (extra Facebook / Twitter, etc) and team collaboration.
 
#    The idea was born from our day-to-day need to be active on social media, look for the best content to share with our followers, grow them, and measure what content works best.
 
#    Who is on the team?
 
#    Ohad Frankfurt is the CEO, Shlomi Babluki is the CTO and Oz Katz does Product and Engineering, and I [Lior Degani] do Marketing. The four of us are the founders. Oz and I were in 8200 [an elite Israeli army unit] together. Emily Engelson does Community Management and Graphic Design.
 
#    If you use Percolate or read LinkedIn?s recommended posts I think you?ll love Swayy.
 
#    Want to try Swayy out without having to wait? Go to this secret URL and enter the promotion code thenextweb . The first 300 people to use the code will get access.
 
#    Image credit: Thinkstock
 
#    """
 
#    # Create a SummaryTool object
#    st = SummaryTool()
 
#    # Build the sentences dictionary
#    sentences_dic = st.get_senteces_ranks(content)
 
#    # Build the summary with the sentences dictionary
#    summary = st.get_summary(title, content, sentences_dic)
 
#    # Print the ratio between the summary length and the original length
#    print ""
#    print "Original Length %s" % (len(title) + len(content))
#    print "Summary Length %s" % len(summary)
#    print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))

#    # Print the summary
#    print summary
 
 
#if __name__ == '__main__':
#    main()