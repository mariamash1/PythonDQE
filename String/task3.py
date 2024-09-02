import re
text = 'homEwork: tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces.I got 87.'
# make text lowercase for siplicity
text = text.lower()
# find places where we have lowercase letter after dot and space/or without space using regex
matches = re.finditer(r'\.\s*([a-z])', text)

# iterate through matches in reversed order to maintain the correct index position
for match in reversed(list(matches)):
    # give indecies of the first and last element of first group found by regex
    start, end = match.start(1), match.end(1)
    # capitalize the matched letter found by regex and replace in the string
    text = text[:start] + text[start:end].upper() + text[end:]

# capitalize the first letter of the text if it's lowercase
text = text[0].upper() + text[1:]

print(text)


# fix misspelling of 'iz' to 'is'
corr_text = text.replace(" iz ", " is ")
print(corr_text)

# create an additional sentence from the last words of each existing sentence
# split sentences using regex as we have no space after dot in one case
sent = re.split(r'\.\s*', text)
# find the last word in each sentence
last_word = [sent.split()[-1] for sent in sent if sent]
# create new sentence
new_sentence = ' '.join(last_word) + '.'

final_text = corr_text + ' ' + new_sentence
print(final_text)

# calculate the number of whitespace characters
whitespace_count = sum(c.isspace() for c in final_text)

print(final_text)
print("Number of whitespace characters:", whitespace_count)
