import re
import sys
from time import sleep
import math
import nltk
from nltk.corpus import stopwords
 
## Here we are using same file(resume raw text)  but number of times because of fileclose problem.That's not issue.


text_file1 = open('/home/seenu/Desktop/someplain.txt','w')    ##This is just for head file operation
text_file1.close()

resume = open('/home/seenu/Desktop/task/Output.txt','r')     ##This is the resume we need to parse
#resume_text= resume.read().lower()                                 ## we are reading all the text in lowercase only for our convience

headings_list = open('/home/seenu/Desktop/someplain.txt','a')        ## this is for saving the heads as which are having 3 words in head line

edu_words = set(stopwords.words("education"))                 
resume_text = resume.readlines()                               
resume_words = []
#j=0
first_headings = []
for i in resume_text:
        resume_words = i.split()
        if len(resume_words) <= 5 and i != '\n' and i !=' ' and resume_words != '\n':
                if i not in edu_words:
                      first_headings.append(i)
                      final  = i.replace(('•'),(''))
                      final1 = final.replace((''),(''))
                      ff  = final1.replace((''),(''))           ###    We are eliminating some symbols
                      ff1 = ff.replace((''),(''))
                      headings_list.write(ff1.lower())
                      #headings_list.write('\n')
                      #sleep(2)

headings_list.close()


edu_words = set(stopwords.words("education"))                  ## these are some stop_words  
stp_words = set(stopwords.words("english"))                   ## these are general stopwords in english

with open('/home/seenu/Desktop/total.txt','r') as all_headings:
        all_headings_list =[]
        for heads in all_headings:
                heads = heads.lower().strip()                                    ## this is the total heading dataset
                all_headings_list.append(heads)

filterd_resume_text = open('/home/seenu/Desktop/someplain.txt','r')
unfilterd_headings=filterd_resume_text.readlines()

#hh = []
head_list1 = []
head_list2 = []
#print(all_headings_list)
for word in unfilterd_headings:
       # print(word)
        j = word.replace('\n','')
        #k= word.replace('\t','')              ## eliminating nextlines and tabs in head text file
        head_list1.append(j)
for word in head_list1:
        jj = word.replace('\t','')
        head_list2.append(jj)
#print(head_list2)


edfile = open('/home/seenu/Desktop/edfile.txt','w')
tech_file = open('/home/seenu/Desktop/tech.txt','w')       ## in this files we will store the information
exp_file = open('/home/seenu/Desktop/exper.txt','w')


head_list3=[]
for words in head_list2:
        if words not in edu_words and  stp_words and words!='':      ## here we are filtering the words
                head_list3.append(words.strip())
                
print(head_list3)
sleep(2)
#print(head.split())
finalheading1 = []
for i in range(0,len(head_list3)):
        for j in range(0,len(all_headings_list)):
                r = nltk.edit_distance(head_list3[i], all_headings_list[j])      ## here we are comparing the train set headings and actual resume
                if r < 2:
                        #print(head_list3[i],all_headings_list[j],r)
                        finalheading1.append(head_list3[i])
                        #sleep(1)

print(head_list3)


# this function will take the key_words list and show from main function and saves extracted data into respective file
def Computing_information(head,show):               
        
        for i in range(0,len(finalheading1)):              ## loop runs untill the end of the final head list
                for j in range(0,len(head)):              ## lopp runs untill the end of the corresponding key words list 
                        r = nltk.edit_distance(finalheading1[i], head[j])  ## compare the similarty between headings in resume and each keyword 
                        if r <2:                       ## condition for similarity between words as threshold value 


                                try:                   ## try mehtod for error handling

		                        #print(finalhead[i],head[j],r)
		                        #sleep(2)
                                        pattern = finalheading1[i]       ## takes the corresponding heading from finalheading as pattern
                                        pat = finalheading1[i+1]               ## takes next final heading element as second heading
                                        print(pattern,pat)           ## prints in between which heading we are going extract the data
                                
                                        #show=1
                                
                                        if show == 1:          ## condition for which details we have to extract and save it into that file
                                                print(show)
                                                #sleep(1)
                                                out = skills(pattern,pat)  ##calls the'skills' with our two headings as arguments & assigns
                                                out1= ''.join(out)           ## then makes each list elements join  
                                                edfile.write(str(out1))      ## writes into corresponding file

                                        if show == 2:
                                                tec = skills(pattern,pat) 
                                                tec1= ''.join(tec)
                                                tech_file.write(str(tec1))
                                        if show == 3:
                                                
                                                ex = skills(pattern,pat)
                                                ex1= ''.join(ex)
                                                exp_file.write(str(ex1))
                                except IndexError:                              ## except the if any error present 
                                        print(error)

## Function will takes the two headings in which we have to extract data 
def skills(pattern,pat):
        RESUME = open('/home/seenu/Desktop/task/Output.txt','r')    ##opens the input resume text file in read format from given path
        copy = False                                                
        count = 0
        data = []                     ## list for to store the information between two headings
        for line in RESUME:                 ## checks the entire resume file till the end for headings  

                if count == 0:       ## condition for count to '0' for first heading in resume file
                        if str(line.strip().lower()) == pattern:     ## satisfies the condition if first heading macthed in file 
                                data.append(line)                     ##  ## adds first heading to data list
                                copy = True                       ## makes the copy to True for to get the text from that heading
                                #print("1")
                                count +=1                        ## to unsatisfy current if class and satisfy elif class

                elif count != 0:                                 ## starts searching for next heading
                        if str(line.strip().lower()) == pat:        ## condition for next heading 
                                copy = False                     ## makes the copy to false after the ending heading reached...
                        elif copy:                               ## if copy is true then  moves into next statement..
                                data.append(line)                    ##  adds first heading to data list untill second(pat) heading come 
                                #print(line)                         ## prints line
        RESUME.close()
        #print(data)
        #sleep(2)                               ## closes the input resume text file
        return data                               ## returns the list file to above function where it was called


## takes input from the user 
show = int(input("Enter \n Education_skills: 1\n Technical skills: 2\n Experince       : 3 \n Exit            : 0\n"))
#print(show)

## loop asks input untill "0" entered
while show !=0:


        if show == 1:                                ## condition for Enducaion skills extraction 
                ### opens the file education key words database file.
                with open('/home/seenu/Desktop/education.txt','r') as education:
                        Education = []                                               ## list for to store the database
                        for HEAD in education:
                                HEAD = HEAD.lower().strip()                         ## extract each key word from file and elimates the space  
                                Education.append(HEAD)                            ## adds to education list 
                #print(Education,show)                                                ## prints the list with all data base 
                print(Computing_information(Education,show))                    ## calls the function and prints the returned value

                
        if show == 2:
                 ## opens the file Technical skills key words database file.
                with open('/home/seenu/Desktop/technical.txt','r') as technical:    
                        Technical_skills = []
                        for HEAD1 in technical:
                                HEAD1 = HEAD1.lower().strip()
                                Technical_skills.append(HEAD1)
                #print(Technical_skills)
                print(Computing_information(Technical_skills,show))
                #tech_file.close()
        if show ==3:
                with open('/home/seenu/Desktop/experience.txt','r') as experience:   ## opens the file Experience database file.
                        Experience = []
                        for HEAD2 in experience:
                                HEAD2 = HEAD2.lower().strip()
                                Experience.append(HEAD2)
                #print(Experience)
                print(Computing_information(Experience,show))
                #exp_file.close()
        show = int(input("Enter \n Education_skills: 1\n Technical skills: 2\n Experince       : 3 \n Exit            : 0\n"))
edfile.close() 
tech_file.close()
  
exp_file.close()           
