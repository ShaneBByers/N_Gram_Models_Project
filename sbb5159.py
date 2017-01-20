def tokenize(text):
    str = text.strip()
    curr = str.split()
    punc_array = []
    for punctuation in string.punctuation:
        punc_array.append(punctuation)

    for (i,word) in enumerate(curr):
        for (j,letter) in enumerate(word):
            if letter in punc_array and len(word) > 1:
                if j == 0:
                    curr[i] = letter
                    curr.insert(i+1,word[1:])
                    break
                elif j == len(word)-1:
                    curr[i] = word[:-1]
                    curr.insert(i+1,letter)
                    break
                else:
                    curr[i] = word[:j]
                    curr.insert(i+1,letter)
                    curr.insert(i+2,word[j+1:])
                    break

    return curr

    pass

def ngrams(n, tokens):
    return_list = []

    tokens_copy = []

    new_n = n-1

    for token in tokens:
        tokens_copy.append(token)

    for i in range(new_n):
        tokens_copy.insert(0, "<START>")

    tokens.append("<END>")

    tokens_copy.append("<END>")

    for (i, token) in enumerate(tokens):
        context = tuple(tokens_copy[i:i+new_n])
        return_list.append((context,token))

    return return_list


    pass

class NgramModel(object):

    def __init__(self, n):
        self.order = n
        self.ngrams_dict_counts = {}
        self.context_dict = {}
        self.token_dict = {}
        pass

    def update(self, sentence):
        tokens = tokenize(sentence)
        grams_list = ngrams(self.order, tokens)

        for gram in grams_list:
            if gram in self.ngrams_dict_counts:
                self.ngrams_dict_counts[gram] += 1
            else:
                self.ngrams_dict_counts[gram] = 1.0
            if gram[0] in self.context_dict:
                self.context_dict[gram[0]] += 1
            else:
                self.context_dict[gram[0]] = 1.0
            if gram[0] in self.token_dict:
                if gram[1] not in self.token_dict[gram[0]]:
                    self.token_dict[gram[0]].append(gram[1])
                    self.token_dict[gram[0]].sort()
            else:
                self.token_dict[gram[0]] = [gram[1]]
        pass

    def prob(self, context, token):
        gram = (context, token)

        if gram in self.ngrams_dict_counts and context in self.context_dict:
            return self.ngrams_dict_counts[gram]/self.context_dict[context]
        else:
            return 0.0
        pass

    def random_token(self, context):

        tokens = self.token_dict[context]
        probs = []
        r = random.random()
        for token in tokens:
            probs.append(self.prob(context, token))

        cumm_probs = []

        for (i, prob) in enumerate(probs):
            if i == 0:
                cumm_probs.append(prob)
            else:
                cumm_probs.append(cumm_probs[i-1] + prob)

        for (i, prob) in enumerate(cumm_probs):
            if prob > r:
                return tokens[i]
        pass

    def random_text(self, token_count):
        tokens = []

        context = []

        starting_context = []

        for i in range(self.order-1):
            context.append("<START>")
            starting_context.append("<START>")

        context_tuple = tuple(context)
        starting_context_tuple = tuple(starting_context)

        for i in range(token_count):
            new_token = self.random_token(context_tuple)
            if not self.order == 1:
                if new_token == "<END>":
                    context_tuple = starting_context_tuple
                else:
                    context = list(context_tuple)
                    context.pop(0)
                    context.append(new_token)
                    context_tuple = tuple(context)
            tokens.append(new_token)

        sep = " "

        return sep.join(tokens)

        pass

def create_ngram_model(n, path):
    in_file = open(path)

    lines = in_file.readlines()

    model = NgramModel(n)

    for line in lines:
        model.update(line[:-1])

    return model
    pass
