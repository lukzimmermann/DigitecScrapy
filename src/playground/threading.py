import threading, time, random

NUMBER_OF_THREADS = 4

articles = list(range(1,45))
print(articles)

def split_batch(number_of_threads: int, article_list: list[int]):
    articles_small_list = []
    rest = len(article_list)%number_of_threads
    length = len(article_list)//number_of_threads
    print(length)
    for i in range(number_of_threads):
        articles_small_list.append(article_list[length*i:(i+1)*length])

    index = 0
    rest_list = article_list[number_of_threads*length:number_of_threads*length+rest]

    for r in rest_list:
        articles_small_list[index].append(r)
        index += 1
        if index > len(articles_small_list)-1:
            index = 0

    return articles_small_list

def scanner(bath: list[int], id: int, sleep: int):
    for item in bath:
        print(f'ID: {id} - {item}')
        time.sleep(sleep)
    
    print(f'ID {id} is finished')
    

splitted_batch_list = split_batch(NUMBER_OF_THREADS, articles)

threads = []
for i in range(NUMBER_OF_THREADS):
    thread = threading.Thread(target=scanner, args=(splitted_batch_list[i], i, random.uniform(1, 3)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("FINISHED")
