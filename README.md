# Text-Analysis-Project
 
Please read the [instructions](instructions.md).
**1. Project Overview** (~1 paragraph)

The data source I pulled comes from Project Gutenberg (http://www.gutenberg.org/) which provides two txt. file I imported using url.lib request. I choose book i. Jane Eyre and book ii. Little Women. Although written by different authors from different countries, these two books share a commonality in that they were authored by female writers from the same era. Furthermore, both books emphasize the power of women and their personal growth during a time when women's greatest achievements were often limited to marriage and motherhood.The primary aim of this project is to examine the similarities and differences between two female writers who have written on a similar topic. To achieve this objective, I have summarized the total word count, identified the top 10 words, and analyzed the overlapping and non-overlapping words to compare the similarities and differences between the two pieces. Additionally, I have employed Natural Language Processing and Text Similarity tests to gain a more profound understanding. My hope is that the results will reveal some similarities between the two works, while not being excessively high since they were written by different authors. Furthermore, I anticipate a positive sentiment to be reflected in the findings.



**2. Implementation** (~1-2 paragraphs + screenshots)

Use screenshots to describe how you used ChatGPT to help you or learn new things.

To begin, I utilized url.lib to import the two necessary txt. files into Python (importing). Next, I processed the files to extract the relevant information for our analysis (process_file). Processing the file included excluding the header and ending information that was not part of the book content. Furthermore, I removed stop words that would not be beneficial to our analysis.

Moving on, I first ran a total word count to ensure that the books were of a similar length. Then, I analyzed the top 10 words to compare if there were any similarities in wording between the two books. Additionally, I ran a program to compare the differences between the two books. Furthermore, I conducted a program to determine the frequency of the words 'marry', 'marriage', 'marrying', and 'married' to determine their importance in the book.
After gaining a general understanding of the books, I conducted Natural Language Processing and used sentiment analysis to determine the writing style of the two authors. The writing style was assessed using three elements: negative, positive, and neutral. In order to compare the true text similarity, I conducted a text similarity test since the previous results obtained from overlapping words had interesting findings. Initially, I had planned to run text clustering (part I have to make a chioce), but the text similarity results indicated that it would not generate any useful results. Chatgpt haven't help much while I'm planning my implementation, though it did confused me two days for using text_clustering with the sentiment analysis. It first explained the concept in a really techinical way which I don't quite get it, and then started to give me examples using text clustering to do 
sentimental analysis. 
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\chatgpt_implementation.png)



**3. Results** (~2-3 paragraphs + figures/examples)

Present what you accomplished in your project:
There are several things I discovered pretty interesting. First, the two books have similar word counts though written by different writers from different country. The total words in Jane Eyre are 191598 and the total words in Little Women are 194801. The total word counts makes them great options for analyzing writing styles. 

When examining the results of the similarity test, I conducted a two-part analysis focused on wording and ratio. I discovered that two books shared five common words: "will," "one," "said," "like," and "little." While these words don't carry any significant meaning on their own, "will" and "like" denote powerful individual emotions and determination. Additionally, the frequency of words related to marriage was also comparable, with 53 occurrences in "Little Women" and 46 in "Jane Eyre." This observation is intriguing as it suggests that both books touch upon the topic of marriage with similar frequency, providing readers with valuable insights for personal growth and marriage.The fuzz ratio is 0% between two books. Although this result was surprising to me, it makes total sense since one writer is British and another is American. The difference in two British-English and American-English can be causing this 0 in similarity. The books are heavily scenario based, so difference in daily expression can be causing this result
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\total.png)
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\overlapping.png)
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\marriageword.png)
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\chatgpt_implementation.png)

Regarding the sentimental analysis, I executed a sentiment ratio test on each book and received comparable results, which aligned with my expectations. Given that both books center around women's personal growth, I didn't anticipate any significant difference in the sentiment test. However, I did observe a slight variation between "Jane Eyre" and "Little Women." "Jane Eyre" exhibited a marginally higher ratio of negative words and a lower ratio of positive words, indicating a slightly more negative sentiment in comparison to "Little Women." This observation corresponds with my own personal reading experience of both books.
![alt text](C:\Users\xliu7\Documents\GitHub\Text-Analysis-Project\images\sentimentanalysis.png)

**4. Reflection** (~1-2 paragraphs)

Overall the project went well. It is in accordance with my expectation that there are some similarity in sentiment, wording but not so similar since the books are written by two difference writers. I think I can improve on studying history background and analyze the content with history background instead of simply analyzing between two books. More, I may use some data visualization tool for this project. I was too focused on text clustering that did not provide me enough time to explore other possible chances of utilizinf machine learning data visualization tool. I think my project was appropriately scoped and I had a good testing plan. 

Undertaking this project was challenging as it involved the installation of numerous tools and APIs. However, the project taught me valuable lessons such as tool installation, application of classroom learning to practical situations, and project planning in Python. While the process resembled a physics experiment, consisting of hypothesis testing and concluding, this marked my initial venture utilizing such a process for a Python project. I wish I know more code to help me with implementing analysis

Tame Chapgpt Diary (人类尝试驯服早期AI实记)
Overall Reflection about Taming Chatgpt: Only if you are smart(knowledgeable), chatgpt is smart. If you do not know what you are asking for/ have no idea what the topic is about, ChatGpt can grow to be really annoying cuz it keeps giving you answer which you do not want, and explain it with reason makes you think it's right ^-^ then you end up spending two days doing something irrelevant and destroys a nicely planned Friday





