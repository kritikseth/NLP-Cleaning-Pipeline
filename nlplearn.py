def learn(toggle):  
    text = ''
    
    if 'html' in toggle:
        text += 'HTML Cleaning- \n'
        text += 'Removes any URLs and HTML tags that may be present in the text (due to inconsistencies during Web Crawling). It preserves the data between the tags. \n'
        text += 'Sample Text- \n'
        text += '<p>Sample Text between the tags </p> Google URL- https://www.google.com \n\n'

    if 'mention' in toggle:
        text += 'Mention Handling- \n'
        text += 'Removes any @mentions present in the text, usually performed on comments/tweets. It removes \‘@\‘ as well as the mention. \n'
        text += 'Sample Text- \n'
        text += 'Kritik Seth @kritikseth is a Data Scientist \n\n'

    if 'contraction' in toggle:
        text += 'Contraction Mapping- \n'
        text += 'Contractions are shortened versions of words or syllables, eg- you’re: you are, cause: because, ain’t: are not, they’re: they are, it’s: it is, etc. \n'
        text += 'Sample Text- \n'
        text += 'you’re cause ain’t they’re it’s \n\n'

    if 'spelling' in toggle:
        text += 'Spelling Correction- \n'
        text += 'It is a very crucial step. If one is analysing large amounts of data, inconsistencies in the spelling will cause most models to fail. \n'
        text += 'Sample Text- \n'
        text += 'can you tell me abot yur plands this weeekend \n\n'

    if 'emoji' in toggle:
        text += 'Emoji Handling- \n'
        text += 'Algorithms cannot figure out meaning of emojis, hence it is necessary that we either remove them or replace. In this application we would be replacing them. \n'
        text += 'Sample Text- \n'
        text += '☺️😌😳😂😖 \n\n'

    if 'punctuation' in toggle:
        text += 'Punctuation Handling- \n'
        text += 'Punctuations do not play any role in model building, hence we should remove all the unnecessary data. \n'
        text += 'Sample Text- \n'
        text += 'Hi, how are you? I am great! \n\n'

    if 'tokenisation' in toggle:
        text += 'Tokenisation- \n'
        text += 'Is a very important step, here we are tokenising using whitespaces, but tokenisation may not always be about words. We can also perform sentence tokenisation. \n'
        text += 'Sample Text- \n'
        text += 'Hi, how are you? I am great! \n\n'

    if 'stopword' in toggle:
        text += 'Stopwords Handling- \n'
        text += 'A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that an algorithm has been programmed to ignore.  \n'
        text += 'Sample Text- \n'
        text += 'Hi, how are you? I am great! \n\n'

    if 'stemming' in toggle:
        text += 'Stemming- \n'
        text += 'Stemming is the process of producing morphological variants of a root/base word, eg- troubling: troubl, eating: eat, asked: ask, changed: chang \n'
        text += 'Sample Text- \n'
        text += 'troubling eating changed \n\n'

    if 'lemmatization' in toggle:
        text += 'Lemmatisation- \n'
        text += 'Lemmatisation is the process of grouping together the different inflected forms of a word so they can be analysed as a single item. Lemmatization is similar to stemming but it brings context to the words., eg- troubling: trouble, eating: eat, asked: ask, changed: change \n'
        text += 'Sample Text- \n'
        text += 'troubling eating changed  \n\n'
        
    return text
