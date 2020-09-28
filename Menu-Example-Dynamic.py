queryResults = [["alpha", "one", "level1-3", "alphalev4", "alphalev5"],
                    ["bravo", "two", "level2-3", "bravolev4", "bravolev5"],
                    ["bravo", "two", "level3-3", "anotherlev4", "anotherlev5"],
                    ["alpha", "three", "level1-3", "anotherlev4", "anotherlev5"],
                    ["charlie", "four", "level4-3", "charlielev4", "charlielev5"],
                    ["alpha", "one", "NewLev3", "AlLev4", "AlLev5"]]

# queryResults = system.db.runQuery("SELECT TEST_DJ_IGN.lk_region.region_name, TEST_DJ_IGN.lk_basin.basin_name, TEST_DJ_IGN.lk_area.area_name, TEST_DJ_IGN.facility.facility_name, TEST_DJ_IGN.pipeline.pipeline_name, TEST_DJ_IGN.lk_region.region_id, TEST_DJ_IGN.lk_basin.basin_id, TEST_DJ_IGN.lk_area.area_id,  TEST_DJ_IGN.facility.facility_id, TEST_DJ_IGN.pipeline.pipeline_id, TEST_DJ_IGN.pipeline.pipeline_description FROM TEST_DJ_IGN.facility JOIN TEST_DJ_IGN.pipeline ON (TEST_DJ_IGN.facility.facility_id = TEST_DJ_IGN.pipeline.facility_id) JOIN TEST_DJ_IGN.lk_area ON (TEST_DJ_IGN.facility.area_id = TEST_DJ_IGN.lk_area.area_id) JOIN TEST_DJ_IGN.lk_basin ON (TEST_DJ_IGN.facility.basin_id = TEST_DJ_IGN.lk_basin.basin_id) JOIN TEST_DJ_IGN.lk_region ON (TEST_DJ_IGN.facility.region_id = TEST_DJ_IGN.lk_region.region_id) ORDER BY TEST_DJ_IGN.lk_region.region_name, TEST_DJ_IGN.lk_basin.basin_name, TEST_DJ_IGN.lk_area.area_name, TEST_DJ_IGN.facility.facility_name, TEST_DJ_IGN.pipeline.pipeline_name")



def create_item(name, nav):
    # temp_item = {"randomStuff": 1, "text": name, "items": []}
    temp_item = {"items": [], "label": {"icon": {"path": ""}, "text": name}, "navIcon": {"color": "#6C6C6C", "path": "material/chevron_right"}, "showHeader": True, "target": nav}
    return temp_item


def find_match(menu_item, text_name):
    menu_length = len(menu_item)
    for x in range(menu_length):
        if menu_item[x]["label"]["text"] == text_name:
            return x
    return -1


# menu[index]["items"][indexL2]["items"]  -> current_menu
def append_if(current_menu, append_index, append_index2, nav):
    if find_match(current_menu, queryResults[append_index][append_index2]) == -1:
        current_menu.append(create_item(queryResults[append_index][append_index2], nav))
        # print("Added from query line: " + str(append_index) + " " + queryResults[append_index][append_index2])


menu = []
for x in range(len(queryResults)):
    append_if(menu, x, 0, "/")

for x in range(len(queryResults)):
    index = find_match(menu, queryResults[x][0])
    append_if(menu[index]["items"], x, 1, "/")

for x in range(len(queryResults)):
    index = find_match(menu, queryResults[x][0])
    indexL2 = find_match(menu[index]["items"], queryResults[x][1] )
    append_if(menu[index]["items"][indexL2]["items"], x, 2, "/")

for x in range(len(queryResults)):
    index = find_match(menu, queryResults[x][0])
    indexL2 = find_match(menu[index]["items"], queryResults[x][1])
    indexL3 = find_match(menu[index]["items"][indexL2]["items"], queryResults[x][2])
    append_if(menu[index]["items"][indexL2]["items"][indexL3]["items"], x, 3, "/")

for x in range(len(queryResults)):
    index = find_match(menu, queryResults[x][0])
    indexL2 = find_match(menu[index]["items"], queryResults[x][1])
    indexL3 = find_match(menu[index]["items"][indexL2]["items"], queryResults[x][2])
    indexL4 = find_match(menu[index]["items"][indexL2]["items"][indexL3]["items"], queryResults[x][3])
    append_if(menu[index]["items"][indexL2]["items"][indexL3]["items"][indexL4]["items"], x, 4, "/basicdataentrytest/" + str(queryResults[x][8]) + "/" + str(queryResults[x][9]) + "/" + str(queryResults[x][3]) + "/" + str(queryResults[x][4]))

# self.getSibling("MenuTree").props.items = menu
# self.getChild("root").getChild("MenuTree").props.items = menu

print(menu)
