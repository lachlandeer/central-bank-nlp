# Central Bank Text Corpus

A text corpus of central bank communications. I hope it is useful. Please submit an issue if it is not. 

The New Zealand Central Bank corpus is in folders by year. The United States Central Bank Corpus is a list and not in folder by year. The reason for doing so is because I do not know the best way to structure a corpus.

I have added word vectors using fastText. [text vectors](https://storage.googleapis.com/cbtext/fomc.vec) + [bin](https://storage.googleapis.com/cbtext/fomc.bin)

"As you learn more apply this knowledge to the whole corpus and be prepared to make changes, including leaving out data you have gathered, if this improves the final corpus. Keep a detailed record of the data you collect." David Evans, University of Nottingham

### Natural Language Processing

The notebook Sentiment Analysis R is where I am learning how to do text mining in R with my central bank text data. 

#### Challenges

Scraping to download communications would be best to get the data. Right now I am copying the communications and putting them in text files. I need to explore more how I can use scraping to get quicker access to text data.

I am struggling to load all of the fomc text data so I can use more documents than one. Right now, I am cutting and pasting a text document and then doing analysis on it.


### Similar Work

- [ FOMC Communication Policy and the Accuracy of Fed Funds Futures ](https://www.newyorkfed.org/research/staff_reports/sr491.html)
- [Fedspeak: Who Moves U.S. Asset Prices?](http://www.ijcb.org/journal/ijcb16q4a6.htm)

### Resources

- [Text Mining with R by Julia Silge and David Robinson](https://www.tidytextmining.com/tidytext.html)
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
- [A Primer on Neural Network Models for Natural Language Processing]
(http://u.cs.biu.ac.il/~yogo/nnlp.pdf)

- [ A Roadmap towards Machine Intelligence](https://arxiv.org/abs/1511.08130)
- [ Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051)
- [ Simple and Effective Multi-Paragraph Reading Comprehension](https://arxiv.org/abs/1710.10723)
- [ SQuAD: 100,000+ Questions for Machine Comprehension of Text](https://arxiv.org/abs/1606.05250)
- [ Teaching Machines to Read and Comprehend](https://arxiv.org/abs/1506.03340)
- [ Bidirectional Attention Flow for Machine Comprehension](https://arxiv.org/abs/1611.01603)

- [Search Engines Information Retrieval in Practice](https://ciir.cs.umass.edu/irbook/)
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html)
- [INFORMATION RETRIEVAL](http://www.dcs.gla.ac.uk/Keith/Preface.html)
- [Foundations of Statistical Natural Language Processing](https://nlp.stanford.edu/fsnlp/)
