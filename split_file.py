import os

# Open the input file
with open('example.txt', 'r') as input_file:
    # Read the entire content of the file
    text = input_file.read()

# Split the text into words
words = text.split()

# Create a directory to store the output files
if not os.path.exists('output'):
    os.makedirs('output')

# Loop through the words and save 1000 words in each file
for i in range(0, len(words), 1000):
    # Create the filename for this chunk
    filename = 'output/chunk_{0}.txt'.format(i // 1000 + 1)
    # Get the next 1000 words
    chunk = words[i:i+1000]
    # Join the words into a string with spaces between them
    chunk_text = ' '.join(chunk)
    # Write the chunk to a file
    with open(filename, 'w') as output_file:
        output_file.write(chunk_text)

