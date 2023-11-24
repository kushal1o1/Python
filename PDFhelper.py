from pypdf import PdfReader,PdfWriter

print("Welcome to Pdf tools")
x=True
while x:
    print("ENter what to do with PDF.\n")
    print("1. Gather info about Pdf.  ")
    print("2. Read Content of  Pdf.   ")
    print("3. Find no of pages in Pdf  ")
    print("4. Encript the Pdf.    ")
    print("5. Merge Pdf's.    ")
    print("6. Exit.  ")
    choice = int(input())
    if choice == 2 :
        Pdfname = input('Enter the Pdf name with extension  ')
        reader = PdfReader(Pdfname)
        meta = reader.metadata
        
        y=int(input("Enter 1 for specific page number \nEnter 2 for Reading  all pdf  "))
        if y==1:
            pgnum=int(input("Enter page number :   "))
            if  not pgnum<=len(reader.pages):
               print(f"Invalid Page Number! pdf only have {len(reader.pages)} pages  ")
               continue
            else:
               page=reader.pages[pgnum]
               text=page.extract_text("page")
               l.append(text)
            
            
        elif y==2:
            l=[""]
            for page in reader.pages:
              text=page.extract_text("page")
              l.append(text)
        ans=' '.join(l)
        print(ans)
        print("PDF OPENED SUCESSFULLY.\n")
    elif choice==1:
        Pdfname = input('Enter the Pdf name with extension  ')
        reader = PdfReader(Pdfname)
        meta = reader.metadata
        print("\nMetadata Information:\n")
        print(f" Meta Author : {meta.author}")
        print(f" Meta Creator: {meta.creator}")
        print(f" Meta Producer: {meta.producer}")
        print(f" Meta Subject: {meta.subject}")
        print(f" Meta Title: {meta.title}" )
    elif choice==3:
        Pdfname = input('Enter the Pdf name with extension  ')
        reader = PdfReader(Pdfname)
        meta = reader.metadata
        print(f"The number of pages in {Pdfname} is :{len(reader.pages)}")
    elif choice==4:
        Pdfname = input('Enter the Pdf name with extension  ')
        reader = PdfReader(Pdfname)
        password = input("Enter a Password. Be sure u have to enter the password everytime u opened the Pdf File  ")
        writer = PdfWriter()
        for page in reader.pages:
          writer.add_page(page)
        writer.encrypt(password, algorithm="AES-256")
        with open(f"{Pdfname}_encrypted.pdf", "wb") as f:
          writer.write(f)
          print(f"Sucessfully Created . PLEASE CHECK THE NEW PDF FILE IN FOLDER NAMED AS {Pdfname}_encrypted.pdf\n")
    elif choice==5:
        merger = PdfWriter()
        noofpdfs=int(input("How many Pdfs u wanna merge  "))
        for i in range(noofpdfs):
            pdf=input(f"Enter name of pdf no {i+1} that you wanna merge with extensions ")
            merger.append(pdf)

        merger.write("merged-pdf.pdf")
        merger.close()
        print("Merged Sucessfully.PLEASE CHECK MERGED PDF NAMED AS merged-pdf.pdf ")
    else:
     print("Thank You for using Pdf tools ")
     x=False



# these are  just test trials IGNORE THIS
# print(len(reader.pages))

# # All of the following could be None!
# print(meta.author)
# print(meta.creator)
# print(meta.producer)
# print(meta.subject)
# print(meta.title)

# # # exact text for page no
# page=reader.pages[2]
# # print(page.extract_text("page"))
# writer = PdfWriter()

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Add a password to the new PDF
# writer.encrypt("1o1", algorithm="AES-256")

# # Save the new PDF to a file
# with open("encrypted-pdf.pdf", "wb") as f:
#     writer.write(f)



# if reader.is_encrypted:
#     reader.decrypt("1o1")

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Save the new PDF to a file
# with open("decrypted-pdf.pdf", "wb") as f:
#     writer.write(f)



# merger = PdfWriter()

# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()