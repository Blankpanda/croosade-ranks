import os
import sys
import time
import urllib.request
import math

from bs4 import BeautifulSoup
from datetime import datetime
#ranking-scrape.py <name>
temp_files = []
def main():
    start_time = time.time()
    args = sys.argv

    if len(args) != 2:
        print("format: ranking-scrape.py <character name>")
        sys.exit(0)
  
    url_stub_rank =  "https://www.croosade.com/rankings?type=0&job=0&rank="
    url_stub_name_search = "https://www.croosade.com/rankings?type=0&job=0&search_type=0&search_value="

    search_class, start_rank = get_character_stats(url_stub_name_search,str(args[1]))

    if(search_class == None or start_rank == None):
        print("failed to grab character!")
        sys.exit(0)

    start_rank = int(start_rank.text)
    seach_class = str(search_class)

    ranking_data = []
    iteration_count = get_iter_estimate(start_rank)
    rank_iter = start_rank
    while rank_iter  >= 1:
        iter_start_time = time.time()
        rank_count = 0
        raw_html = read_tmp_file(get_page_html(url_stub_rank,rank_iter))
        if(raw_html != ""):
            table = get_table(raw_html)
            rows = get_rows(table)
        
            val_list = [(row.find_all("td")) for row in rows]
            for i in reversed(range(0,len(val_list))):
                if (val_list[i] != []): # prevent exception if empty, not chaining if's
                    if(val_list[i][1].text == search_class):
                        for e in val_list[i][0].findAll('b'): e.extract() # remove guild
                        for e in val_list[i][2].findAll('small'): e.extract() # remove exp
                        for e in val_list[i][2].findAll('i'): e.extract() # remove ranking change
                        # stack push
                        ranking_data.insert(0,{"name":val_list[i][0].text,\
                                               "job":val_list[i][1].text,
                                               "level":val_list[i][2].text.split(" ")[0],
                                               "ranking":[row.find_all("th") for row in rows][i][0].text
                                           })

        iter_end_time = time.time()
        iter_estimate_seconds = (iter_end_time-iter_start_time)*get_iter_estimate(start_rank)
        
        if(iter_estimate_seconds/60.0 >= 1.0) and (rank_iter == start_rank): # do it once
            print("Estimated completion time in minutes: " + str((iter_estimate_seconds / 60) - ((iter_estimate_seconds / 60) % -1)))
        elif (rank_iter == start_rank):
            print("Estimated completion time in seconds:" + str(iter_estimate_seconds - (iter_estimate_seconds % -1)))
        rank_iter -= 5

    end_time = time.time()
    time_spent = end_time - start_time
    time_str = str()

    if((time_spent/60.0) >= 1.0):
        time_str = "time taken in minutes: " + str(time_spent / 60.0)
    else:
        time_str = "time taken in seconds: " + str(time_spent)
    
    display_ranks(ranking_data,time_str)
    delete_temp_files()

    # find the name of the character by searching the rankings and return their rank
def get_iter_estimate(rank):
    estim_iters = rank / 5 # 5 = the number of rankings displayed per pge
    return (estim_iters - (estim_iters % -1))
    
    
def get_character_stats(url_stub, character_name):   
    raw_html = read_tmp_file(get_page_html(url_stub,character_name))

    if "No character found." in raw_html:
        print("Character not found. exiting.")
        sys.exit(0)

    table = get_table(raw_html)
    rows = get_rows(table)
    
    val_list = [(row.find_all("td")) for row in rows]   

    for i in reversed(range(0,len(val_list))):
        if (val_list[i] != []): # prevent exception if empty, not chaining if's
            for e in val_list[i][0].findAll('b'): e.extract() # remove guild
            
            if(val_list[i][0].text == character_name):
                return val_list[i][1].text,[row.find_all("th") for row in rows][i][0]

    return None, None # P = NP if this happens

def display_ranks(ranks,time_str):
    print("todays date: " + str(datetime.now()))
    print("total execution time: " + time_str)
    print("for job: " + ranks[0]["job"])

    for rank in ranks:
        rank['level'] = rank["level"].replace('-','')
        print("class rank=" + str(ranks.index(rank)+1)+ ":" +"\ttotal rank=" + str(rank["ranking"]) +"\tname=" + str(rank["name"]) + "\tlevel=" + str(rank["level"]))
    
def get_table(html):
    bs4 = BeautifulSoup(html,'html.parser')
    table = bs4.find(lambda tag: tag.name == 'table' and tag.has_attr('class'))
    return table

def get_rows(table):
    return table.findAll(lambda tag: tag.name=='tr')

def get_page_html(url_stub,st):
    local_filename, headers = urllib.request.urlretrieve(url_stub + str(st))
    temp_files.append(local_filename)
    return local_filename

def read_tmp_file(file_name):
    contents = str()
    try:
        f = open(file_name,'r')
        #print("Reading " + file_name)
        contents = f.read()
        f.close()
    except IOError:
        print("could not read file " + file_name)
        return ""
        
    return contents

def delete_temp_files():
    for temp_file in temp_files:
        os.remove(temp_file)

if __name__ == '__main__':
    main()
