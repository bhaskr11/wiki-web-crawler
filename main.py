import wikipedia, sys
import utils as util


start = input("Enter your wikipedia article/page title: ")
start = wikipedia.page(start)

end = input("Enter your wikipedia article/page title: ")
end = wikipedia.page(end)

graph = {}
graph[start.title] = {
    'title': start.title,
    'parent': None
}

que = []

que = [graph[start.title]]

print("Start Page = " + start.title)
print("End Page = " + end.title)

while True:
    print("loading....")
    while len(que) > 0:
        current_que = que[0]
        que = que[1:]
        try:
            page = wikipedia.page(current_que['title'])
            for link in page.links:
                if link not in graph:
                    graph[link] = {
                        'title': link,
                        'parent': current_que
                    }
                    if link == end.title:
                        print("FOUND A PATH")
                        util.path_finder(graph[link])
                        sys.exit()
                    que.append(graph[link])
        #handle error when one title could mean different website title
        except wikipedia.exceptions.DisambiguationError as e:
            graph[e.title] = {
                'title': e.title,
                'parent': current_que
            }
            for option in e.options:
                if option not in graph:
                    graph[option] = {
                        'title': option,
                        'parent': graph[e.title]
                    }
                    if option == end.title:
                        print("FOUND A PATH")
                        util.path_finder(graph[option])
                        sys.exit()
                    que.append(graph[option])
        #Handle page error exception
        except wikipedia.exceptions.PageError as e:
            print('loading....finding a path, please wait')

