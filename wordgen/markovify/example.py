import markovify

with open("cb_text.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    print(text_model.make_short_sentence(100))