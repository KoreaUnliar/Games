import pygame, time, math, pickle, os, sys

pygame.init()
WIDTH, HEIGHT= 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.image.load("data/image/icon.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Travel - Game start key is Space.")

score = 0
playerid = 0
playerimg = pygame.image.load("data/image/players/player"+str(playerid)+".png")
playerx = 0
travel_ver = "1.0.1"
win_sound = pygame.mixer.Sound("data/sound/victory.wav")
play = 0
play_time = 0

IVORY = (238,230,196)
WHITE = (255,255,255)
BLACK = (0,0,0)

#이미지 로드
trophy = pygame.image.load("data/image/trophy.png")
trophy10 = pygame.image.load("data/image/trophy10.png")
trophy50 = pygame.image.load("data/image/trophy50.png")
trophy100 = pygame.image.load("data/image/trophy100.png")



data_list = []

run = True
print("\n\n------------------------\nTravel Version: ", travel_ver)
print("Key Tutoiral:")
print("ESC: Delete Data\nSpaceBar: Move\nLeft arrow and Right arrow: Skin")



def player(x):
    screen.blit(playerimg,(x, 405))

def draw_image(img,x,y):
    screen.blit(img,(x,y))

def text(textwrite,x,y,size, color=WHITE):
    font = pygame.font.Font("data/font/game.ttf",size)
    write = font.render(textwrite, True, color)
    screen.blit(write,(x,y))

def win():
    text("Victory!",250,150,100)
    win_sound.play(-1)

def save():
    #os.system("cls")
    try:
        os.makedirs("data/data")
        print("\n맵 데이터를 저장했습니다!")
        print(data_list)
        pickle.dump(data_list,open("data/data/data.unliar","wb"))
    except:
        pickle.dump(data_list,open("data/data/data.unliar","wb"))
        print("\n맵 데이터를 저장했습니다!")
        print(data_list)
  
    #데이터 로드

try:
    data_load = pickle.load(open("data/data/data.unliar","rb"))
    playerx = data_load[0]
    playerid = data_load[1]
    play_time = data_load[2]
    play = data_load[3]
    score = data_load[4]
    #player img load
    playerimg = pygame.image.load("data/image/players/player"+str(playerid)+".png")
except EOFError:
    data_list.append(playerx)
    data_list.append(playerid)
    data_list.append(play_time)
    data_list.append(play)
    data_list.append(score)
    save()
    print("데이터를 리셋했습니다!")
except FileNotFoundError:
    data_list.append(playerx)
    data_list.append(playerid)
    data_list.append(play_time)
    data_list.append(play)
    data_list.append(score)
    save() 
    print("데이터를 생성했습니다.")

start = time.time()
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            data_list.append(playerx)
            data_list.append(playerid)
            data_list.append(play_time)
            data_list.append(play)
            data_list.append(score)
            save()
            run = False

        if event.type == pygame.KEYDOWN:
            pygame.display.set_caption("Travel")
            win_sound.stop()
            if event.key == pygame.K_ESCAPE:
                #데이터 리스트에 함수 추가
                try:
                    os.remove("data/data/data.unliar")
                    print("데이터를 지웠습니다.")
                    print("3초뒤에 게임이 종료됩니다.")
                    time.sleep(3)
                    run = False
                    sys.exit()
                except FileNotFoundError: print("데이터가 없습니다.")
                
            if event.key == pygame.K_RIGHT:
                
                if playerid == 8:
                    playerid = 0
                else:
                    playerid += 1
                    playerimg = pygame.image.load("data/image/players/player"+str(playerid)+".png")
                    
                player(playerx)
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                if playerid == 0:
                    playerid = 8
                else:
                    playerid -= 1
                    playerimg = pygame.image.load("data/image/players/player"+str(playerid)+".png")
                player(playerx)
                pygame.display.update()
                
            elif event.key == pygame.K_SPACE:
                if score >= 805:
                    play += 1
                    win()
                    play_time = time.time()-start
                    text("Play Time: "+str(math.floor(play_time))+"s", 250, 100, 70)
                    pygame.display.update()
                    score = 0
                    playerx = 0
                    print(play)
                else:
                    playerx += 0.1#0.1
                    score += 0.1
                    print_score = str(score)
                    if play >= 1:
                        draw_image(trophy,0,0)
                    if play >= 10:
                        draw_image(trophy10,69, 0)
                    if play >= 50:
                        draw_image(trophy50,138, 0)
                    if play >= 100:
                        draw_image(trophy100,207,0)
                        text("100...", 0,75, 30,color=BLACK)
                    text("게임 클리어: "+str(play), 0,125,30)
                    pygame.display.update()

    screen.fill(IVORY)
    text(str(score),800,20,30)
    player(playerx)
    #pygame.display.update()
