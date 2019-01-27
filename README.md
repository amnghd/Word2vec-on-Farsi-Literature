# Word2vec model for Farsi literature

This document is dedicated to providing a word2vec model developed for Farsi poems of 48 poets. The complete list of poets and their documents are available [here](https://github.com/amnghd/Persian_poems_corpus).

## Brief introduction to Farsi poems:

Traditional Farsi poems are a set of sentence rows knowen as ``beyts``. Each beyt is split into two ``mesra``s that could be thought of as clauses that complete each other and convey a single concept.
Most of the existing Farsi literature are composed in this framework of mesras and beyts. Here is an example of a Farsi poem by [Rumi](https://en.wikipedia.org/wiki/Rumi):

**(beyt1 - mesra1)**

Out beyond ideas of wrongdoing and right-doing,

**(beyt1 - mesra2)**

there is a field.  I'll meet you there.

**(beyt2 - mesra1)**

When the soul lies down in that grass,

**(beyt2 - mesra2)**

the world is too full to talk about.

**(beyt3 - mesra1)**

Ideas, language, even the phrase each other

**(beyt3 - mesra2)**

doesn't make any sense.


## About this corpus:

The corpus that we developed the word2vec model on consists of 1,216,286 mesras of Farsi poems that can be thought of as 608,143 sentences. 
Moreover, this document consists of 8,102,119 words from which 148,588 are unique.

## Word2vec model:

The developed word2vec model is accessible [here](https://github.com/amnghd/Word2vec-on-Farsi-Literature/tree/master/word2vec%20model).

## Demonstration:

Here are some examples of the results of this model:

#### Example 1:
``گوش به چشم شبیه شنیده است:
دیده``

Which means:

``Ear to eye is similar to heard to:
Saw``

#### Example 2:
مرد به زن شبیه آدم است:
حوا

Which means:

``Man to woman is similar to Adam to:
Eve``




## Limitations:

Please note that the model capability is limited due to its data input size which is only 8 million words.
Moreover, due to different format and vocabulary between Farsi poems and nowadays Farsi conversation, please be carful in generalizing the model.