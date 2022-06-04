#Reading-Text-Files and Counting-Words

#def read_file_content(filename):
    # [assignment] Add your code here 
    
with open("read.txt", 'r') as file:
    var = file.read()
    print(var)
    file.close()

#def count_words():
    #text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = open("story.txt", "r")

    d = dict()

    for line in text:

        line = line.strip()

        line = line.lower()

        words = line.split(" ")

        for word in words:
            if word in d:

                d[word] = d[word] + 1
            else:

                d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])




 





