pip install markovify

import markovify

# Take input text from user
text = input("Enter training text:\n")

# Build Markov model
text_model = markovify.Text(text)

# Generate text
for i in range(3):
    print(text_model.make_sentence(tries=100))
