import os

inf = '/home/vishwa/Downloads/Easy stories_easy_learning_using_self-developed_stories_to_enhance_children_s_listening_and_speaking_skills.pdf'
print inf
info = os.stat(inf)
print info
print info.st_size

if(info.st_size > 10240):
    print "File is to large. Please Select the file size less that 10kb"

elif(info.st_size > 10240):
    print "File uploaded sucessfully"