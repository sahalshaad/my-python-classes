
# from docx import Document
# f = Document("a.docx")

# print(f)


# f.close()

# with open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/Module/python.docx", "r", encoding="latin1") as f:  # or "windows-1252"
#     readd = f.read()
#     print(readd)

# from docx import Document

# # Provide the correct path to your .docx file
# file_path = "/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/Module/python.docx"

# try:
#     # Load the document
#     doc = Document(file_path)

#     # Read and print the content
#     for paragraph in doc.paragraphs:
#         print(paragraph.text)
# except FileNotFoundError:
#     print(f"File not found: {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")

# fi = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/27-nov-alighnment-padding./Module/a.txt", "r")
# print(fi.read())
# fi.close()
fi = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/27-nov-alighnment-padding./Module/a.txt", "a")
fi.write("my append text")
fi.close()
fi = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/27-nov-alighnment-padding./Module/a.txt","r")
print(fi.read())

# fil = open("pythontext.txt","x")
fil = open("pythontext.txt","w")
fil.write("hi")
fil = open("pythontext.txt")
print(fil.read())
fil.close()
