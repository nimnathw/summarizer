import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('test.pdf', 'rb')

# Create a PyPDF2 PdfFileReader object to read the file
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Create an empty string variable to hold the text
text = ""

# Loop through each page in the PDF file
for i in range(num_pages):
    # Get the page object for the current page
    page = pdf_reader.pages[i]
    # Extract the text from the page and add it to the text variable
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Open a new file in write mode to write the text to
txt_file = open('example.txt', 'w')

# Write the text to the file
txt_file.write(text)

# Close the file
txt_file.close()


