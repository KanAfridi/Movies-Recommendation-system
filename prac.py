import os

#progress_file = "progress.txt"
#start_page = 0
if os.path.exists("progress.txt"):
    with open("progress.txt", "r") as f:
        start_page = int(f.read().strip())
        #print(start_page)
else:
    print("No progress file found. Starting from page 1.")
    start_page = 1
    with open("progress.txt", "w") as f:
        start_page = f.write(str(start_page))


for i in range(start_page, 9):
    print(i)
    with open("progress.txt", "w") as f:
        f.write(str(i + 1))
        
        





   

