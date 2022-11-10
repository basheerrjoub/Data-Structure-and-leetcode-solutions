from collections import deque

graph = {}
graph["A"] = ["B", "C", "A"]
graph["B"] = ["D", "E"]
graph["C"] = ["F"]
graph["D"] = ["G"]
graph["G"] = ["H", "I", "J", "K"]

q = deque()
q += graph["A"]
searched = []
while q:
    letter = q.popleft()
    if letter not in searched:
        if letter == "K":
            print ("Found")
            quit()
        
        else:
            if graph.get(letter):
                q += graph[letter]

print ("Not Found!")