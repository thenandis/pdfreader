#!/usr/bin/env python
# coding: utf-8

# In[13]:


import PyPDF2
import pyttsx3
  
# path of the PDF file
path = open('09_Kane et al. Digital Leadership SMR 2019.pdf', 'rb')
# path = open('03_Westerman SMR 2018 No Digital Strategy.pdf', 'rb')
   
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)
totalPages = pdfReader.numPages
  

print(totalPages)

for x in range(totalPages):
    # the page with which you want to start
    # this will read the page of nth page.
    pageNum = x
    from_page = pdfReader.getPage(pageNum)

    # extracting the text from the PDF
    text = from_page.extractText()
    
    #print('!!!!!!!!!!!!!!!!!!!!!!!!! ^^^^^^^^^^^^^^^^^^ ###################### @@@@@@@@@@@@@@@@@@')
    print(text)
    print(pageNum)

    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

