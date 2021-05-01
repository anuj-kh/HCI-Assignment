file = open("test_snapdealUser2.py","r")
content = file.readlines()
content = [x.strip() for x in content]
nclicks = 0
ndclicks = 0
nscroll = 0
for i in range(len(content)):
    if (content[i].find('click()') != -1):
        nclicks += 1
    if (content[i].find('double_click') != -1):
        ndclicks += 1
    if (content[i].find('window.scrollTo') != -1):
        nscroll += 1

print("Number of Clicks: ", nclicks)
print("Number of Double Clicks: ", ndclicks)
print("Number of times user scrolled: ", nscroll)