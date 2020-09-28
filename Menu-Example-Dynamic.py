fakeQueryResults = [["alpha","one","level1-3"],
                    ["bravo","two","level2-3"],
                    ["bravo","two","level3-3"],
                    ["alpha","three","level1-3"],
                    ["charlie", "four", "level4-3"],
                    ["alpha", "one", "NewLev3"]]

def create_item(name):
    temp_item = {"randomStuff": 1, "text": name, "items": []}
    return temp_item

def find_match(menu_item, text_name):
    menu_length = len(menu_item)
    for x in range(menu_length):
        if menu_item[x]["text"] == text_name:
            return x
    return -1

# menu[index]["items"][indexL2]["items"]  -> current_menu
def append_if(current_menu, append_index, append_index2):
    if find_match(current_menu, fakeQueryResults[append_index][append_index2]) == -1:
        current_menu.append(create_item(fakeQueryResults[append_index][append_index2]))
        print("Added from query line: " + str(append_index) + " " + fakeQueryResults[append_index][append_index2])

menu = []
for x in range(len(fakeQueryResults)):
    append_if(menu, x, 0)

for x in range(len(fakeQueryResults)):
    index = find_match(menu, fakeQueryResults[x][0])
    append_if(menu[index]["items"], x, 1)

for x in range(len(fakeQueryResults)):
    index = find_match(menu, fakeQueryResults[x][0])
    indexL2 = find_match(menu[index]["items"], fakeQueryResults[x][1] )
    append_if(menu[index]["items"][indexL2]["items"], x, 2)

print(menu)
