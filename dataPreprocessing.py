def clean_text(text):
    words = text.split()
    # To remove punctuations
    table = str.maketrans('','', string.punctuation)
    words = [w.translate(table) for w in words]
    # Remove anything that is not alphabetic
    words = [word for word in words if word.isalpha()]
    return words
    
def generate_sequences(words):
	length = 10 + 1
	sentences = []
	for i in range(length, len(words)):
		seq = words[i-length:i]
		line = ' '.join(seq)
		sentences.append(line)


def process_data(path):
	raw_data = open(path, 'r', encoding='utf-8').read()
	lower_text = raw_data.lower()
	words = clean_text(lower_text)


