"""
Crawling 할 주소를 저장하는 queue를 생성하여 주고
해당 queue에서 주소를 획득하여 데이터를 crawling한 후 crawling 된 데이터를 crawled.txt
파일에 저장함
"""
import os

# Each website you want to crawl is a separate project(folder / dirctory)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)
    else:
        print(directory + " already exists")

# Create queue and crawled files(if not created)
def create_data_files(project_name, base_url):
    queue = project_name+"_queue.txt"
    crawled = project_name+"_crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

# Create a new file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

"""
기본 URL에서 crawling하기 위해서 수집한 링크를 파일에 저장함
멀티 쓰레딩 혹은 멀티 프로세싱을 통해서 링크를 찾는 과정과 수집된 링크를 통해서 data를 crawling 하는 과정을 분리하려고 함
중복 링크로 인한 중복 crawling을 막기 위한 로직을 추가할 것임(set을 이용하여 중복링크를 제거하는 작업이 추가됨)
"""

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, "w"):
        # for doing nothing
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, "rt") as file:
        for line in file:
            results.add(line.replace("\n", ""))
    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)