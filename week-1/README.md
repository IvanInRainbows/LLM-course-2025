# Introduction to Generative AI and Large Language Models (LLM)

Week 1 is the most theory-heavy week of the course. You can find the lecture slides here: [Week 1 Slides](https://github.com/Helsinki-NLP/LLM-course-2024/blob/main/week-1/LLM-Course%20Lecture%201.pdf).

## Lab Assignment

Research on Tokenizers and write a section to your final report reflecting on the following questions:

* What are tokenizers?

A token in this context is a relevant unit that appears in a text or in the speech, not necessarily delimited by spaces or punctuation. Tokens can be characters, stems, words, semantic units (like multi word tokens), sentences or even a full paragraph. The task of a tokenizer is to split a character string (text or other sequence of elements such as an image) into these tokens (the specific token may depend of the task, but generally for text it relates roughly to words). 

* Why are they important for language modeling and LLMs?

The same that we, humans, delimit the different elements of language (characters, sounds, morphemes, words, clauses, sentences, paragraphs...) LLMs do the same so they can efficiently process that data. The process of tokenization helps LLMs to generalize and find patterns across language. Probably, the biggest use of tokens and tokenization is to split text into units of semantic information that will be later represented through word embeddings.

* What different tokenization algorithms are there and which ones are the most popular ones and why?

The simplest tokenization algorithm is simply to split the text by whitespaces, called Naive tokenization. Byte Pair Encoding (BPE) is the most widely used tokenization algorithm and it is based on merging the most frequent pair of tokens and adding the merge to the list of tokens. Then repeat this process until the desired number of tokens is reached. WordPiece is similar to BPE in the way that both merge tokens into new vocabulary tokens but WordPiece merges based on score formula instead of sheer frequency. Regular Expressions can also be used to tokenize based on the rules determined by the regex.

**Some references:**
* Neural Machine Translation of Rare Words with Subword Units: 
[https://arxiv.org/abs/1508.07909](https://arxiv.org/abs/1508.07909)
* SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing: 
[https://arxiv.org/abs/1808.06226](https://arxiv.org/abs/1808.06226)
