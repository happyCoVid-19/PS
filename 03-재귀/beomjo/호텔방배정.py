import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def find_room(room_dict, room):
    if room_dict[room] == 0:
        room_dict[room] = room + 1
        return room
    elif room_dict[room] != 0:
        room_dict[room] = find_room(room_dict, room_dict[room])
        return room_dict[room]
    
def solution(k, room_number):
    room_dict = defaultdict(int)
    answer = []
    for room in room_number:
        answer.append(find_room(room_dict, room))
    return answer   