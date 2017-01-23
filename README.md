Shane Byers

CMPSC 442 (Artificial Intelligence Course) Project 5: Write a program that can create an n-gram model of 

10/13/2016

TO RUN: 

    python -i n_gram_models.py
    Create an n-gram model
        model_variable = create_ngram_model(n,path_to_text_document) - Where n is the size of the context used for each randomly generated word sequence.
        model_variable.random_text(length) - Where length is the number of words that are to be randomly generated.

EXAMPLE:

    python -i n_gram_models.py
    m = create_ngram_model(3,"frankenstein.txt")
    m.random_text(15)

This program uses a Markov Chain method to create ngram models that can allow the user to randomly generate strings of words of differing contextual understandings from a source text document.

The contextual understanding value that the user provides determines how many words are examined before each word in the document to allow the algorithm to have a better (or worse) understanding of what words precede any given word in the document. From this understanding, the program will then randomly choose a series of words at a length that is provided as input by the user given the context from each word in the initial text document.

KNOWN ISSUES:

No major issues at this time.

Maybe clean up a few bugs when the user enters in an (nonsensical) invalid input.
