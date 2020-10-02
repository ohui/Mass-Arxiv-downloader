import multiprocessing as mp
import time
import json
import re
from pyarxiv import query, download_entries

# Python script that can download Arxiv pdf files for you  
# https://stackoverflow.com/questions/13446445/python-multiprocessing-safely-writing-to-a-file

fn = 'papers.txt'

def worker(papers,  i):
    time.sleep(1)
    edited_title = re.sub("[^a-zA-Z0-9 \-]+", "", papers[i][0])
    #print (edited_title)
    entries = query(title=edited_title, authors = papers[i][1].split(" ")[0] )
    if len(entries) == 0:
        print ("could not download ", papers[i])
    download_entries(entries, target_folder='./pdfs',use_title_for_filename = True)

def main():
    papers = []

    with open('papers.txt') as pf:
        for l in pf:
            print (l)
            next_line = next(pf, None)
            print ("next ", next_line)
            if next_line is not None:
                papers.append( ((l.strip()),next_line.strip()))

    print (papers)

    manager = mp.Manager()
    print ("mp.cpu_count() is ", mp.cpu_count())
    pool = mp.Pool(mp.cpu_count() + 2)

    #fire off workers
    jobs = []

    for i in range(len(papers)): # number of universities in the file
        job = pool.apply_async(worker, (papers, i))


        jobs.append(job)

    # collect results from the workers through the pool result queue
    for job in jobs:
        job.get()


    pool.close()
    pool.join()

if __name__ == "__main__":
   main()
