#a program to show how sorting works visually
import pygame
pygame.init()

#variables
running = True
list1 = [5, 2, 3, 1, 4, 14, 0.3, 2, 4, 2, 4]
#x = 200
y = 10
space_counter = 20
color_counter = 0
canvas_x = len(list1)*20 + 40
canvas_y = max(list1)*10 + 20
reverse = False

# drawlist function
def drawlist(listname, space_counter, color_counter):
    """This function draws the list from the listname given, color and space counter"""
    for i in listname:
        if color_counter > 255:
            color_counter = 0
        if space_counter == (len(listname) * 20) + 100:
            space_counter = 100
            color_counter = 0
        pygame.draw.rect(gameDisplay, (color_counter, 100, 100), [space_counter, y, 20, i*10])
        pygame.display.flip()
        space_counter = space_counter + 20
        color_counter = color_counter + 30

    pygame.time.wait(100)
    gameDisplay.fill((0, 0, 1))

def bubble_sort(list1):
    for i in range(0, len(list1)-1):
        for x in list1:
            next_index = list1.index(x) + 1
            if next_index == len(list1):
                break
                'print(next_index)'
            next_one = list1[next_index]
            if reverse == True:
                if x < next_one:
                    list1[next_index] = x
                    list1[list1.index(x)] = next_one
                    print(list1)
                    drawlist(list1, space_counter, color_counter)
            else:
                if x > next_one:
                    list1[next_index] = x
                    list1[list1.index(x)] = next_one
                    print(list1)
                    drawlist(list1, space_counter, color_counter)
            newlist = []
            num = 0
    for i in list1:
        if list1.count(i) > 1 and i in newlist:
            list1.pop(num)
            list1.insert(list1.index(i)+1, i)
        newlist.append(i)
        num += 1

#set up

gameDisplay = pygame.display.set_mode((canvas_x, canvas_y))
gameDisplay.fill((0, 0, 1))

drawlist(list1, space_counter, color_counter)

while running == True:
    for i in range(0, len(list1)-1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        bubble_sort(list1)

        drawlist(list1, space_counter, color_counter)

    pygame.time.wait(200)
    running = False
