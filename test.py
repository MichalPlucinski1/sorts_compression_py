def vSFillTab(l, low_num_tabs):
    for i in range(1,low_num_tabs,2):
        l.append(i)
        l.insert(0, i+1)

def addToTab(l, step):
     step = int(step/2)
     for i in range(step):
        first_num = l[0]
        l.append(first_num+1)
        l.insert(0, first_num + 2)

r = []

low_num_tabs = 1000 #starting num of elements in tab
high_num_tabs = 2000 #num of elements in last tab
step = 100 #good to be even

r = []

vSFillTab(r, low_num_tabs)
print(len(r))

for k in range(low_num_tabs, high_num_tabs, step):
    addToTab(r, step)
    print(len(r))