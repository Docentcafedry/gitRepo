def my_func(*, name,  age):
    print(name, age)



my_func(name='Lesha', age=2)

def meeting_rooms(rooms: list[list[int]]) -> list[list[int]]:
    rooms.sort()
    for i in range(1, len(rooms)):
        if rooms[i][0] < rooms[i-1][1]:
            return False

    return True

if __name == "__main__":
    my_func(name='Lesha', age=12)