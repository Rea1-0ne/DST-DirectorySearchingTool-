import os
import subprocess
checkimg = subprocess.check_output("ls", shell=True, text=True)
if 'image.txt' in checkimg:
    with open("image.txt", 'r') as image:
        img = image.read()
        print(img)
print("welcome to DST (DirectorySearchingTool) ")
print("built by rea1-0ne")
print("domain and path:")
target = input()
print("wordlist:")
wordlist_path = input()

with open(wordlist_path, 'r') as wrdlist:
    content = wrdlist.read()

flwrdlst = content.split()
l = len(flwrdlst)
i = 0
print("counted words:" , l)
while i < l:
    word = target.replace("DST", flwrdlst[i])
    try:
        rspns = subprocess.check_output(
            f"curl -s -w '%{{http_code}}' -o /dev/null {word}",
            shell=True,
            text=True
        )
        print("[", rspns, "]", "(", flwrdlst[i], ")", "WordNm:","{", i, "}")
    except subprocess.CalledProcessError as e:
        print(f"Request failed for {word}: {e}")
    i += 1
