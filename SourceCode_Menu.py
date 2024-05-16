import pygame, random,time,sys

pygame.init()
pygame.mixer.init()

gameMenu = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rắn săn mồi")

file = open('HightScore.txt', 'r')
hsrFile = file.read()
file.close()

sound_thua = pygame.mixer.Sound("Lose.mp3")
sound_thang = pygame.mixer.Sound("Win.mp3")
sound_anThucan = pygame.mixer.Sound("AnThucAn.mp3")
sound_click = pygame.mixer.Sound("ClickPiu.mp3")
sound_dangChoi = pygame.mixer.Sound("DangChoi.mp3")
channel_dangChoi = pygame.mixer.Channel(0)

pygame.mixer.music.load("NhacCho.mp3")
# Thiết lập sự kiện kết thúc của âm thanh
music_end_event = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(music_end_event)

m = 20 # kích thước
ImgBackGround1 = pygame.transform.scale(pygame.image.load('Background1.png'),(800,600))
ImgBackGround2 = pygame.transform.scale(pygame.image.load('Background2.png'),(760,500))
Imgfood = pygame.transform.scale(pygame.image.load('apple.png'),(m,m))



# màu sắc 
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
green4 = pygame.Color(0,139,0)
green3	 = pygame.Color(0,205,0)
DarkGreen = pygame.Color(0,100,0)

While_playGame = True
playGame = True

flag_food1 = True
flag_food2 = True

flag_pause = 0
playerGame = 1

score1 = 0
hscore = int(hsrFile)
direction1 = 'RIGHT'
changeto1 = direction1

score2 = 0

direction2 = 'LEFT'
changeto2 = direction2

player1 = False
player2 = False
click_voice =0
 

# màu sắc 
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
DarkSlateGray =  pygame.Color(47,79,79)
LightSlateGray = pygame.Color(119, 136, 153)
Green1 =  pygame.Color	(0, 255, 0)
MediumSeaGreen = pygame.Color(60 ,179 ,113)
Azure3 = pygame.Color(193, 205, 205)

# Set the font sizes
font_TTF_small = pygame.font.Font('SuperMario256.ttf', 20)
font_TTF_medium = pygame.font.Font('SuperMario256.ttf', 40)
font_TTF_large = pygame.font.Font('SuperMario256.ttf', 50)
font_TTF_small_type2 = pygame.font.Font('SuperMario256.ttf', 30)


button_back = pygame.Rect(319,362,120,65)
ImgButton_Back = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(120,65))

text_back = font_TTF_medium.render("Back", True, Azure3 )
text_playContinue = font_TTF_small.render("Press the 'p' key to continue", True, Azure3 )
text_playAgain = font_TTF_small.render("Press 'space' key to play again", True, Azure3 )


flag_music = False
def game_over(str, player = 1):
    global playerGame
    global flag_music
    text_player = font_TTF_medium.render(str, True, DarkSlateGray)
    
    gameMenu.blit(text_playAgain, (200,330))
    
    gameMenu.blit(ImgButton_Back, button_back)
    gameMenu.blit(text_back, (330,380))
    

    if str == 'PAUSE':
        gameMenu.blit(text_playContinue, (210,290))
        gameMenu.blit(text_player,(305,120))
        
        flag_music = False
    elif str == 'Drawn':
        if playerGame == 1:
            sound_dangChoi.stop()
            if flag_music_main == True:
                sound_thua.play()
                flag_music = True  
        
        elif playerGame == 2:
            sound_dangChoi.stop()
            if flag_music_main == True:
                sound_thang.play()
                flag_music = True
        gameMenu.blit(text_player,(305,120))
    else:
        if playerGame == 1:
           
            sound_dangChoi.stop()
            if flag_music_main == True:
                sound_thua.play()
                flag_music = True  
        
        elif playerGame == 2:
            sound_dangChoi.stop()
            if flag_music_main == True:
                sound_thang.play()
                flag_music = True
        gameMenu.blit(text_player,(250,120))
    
    show_score(0,player)
       

def show_score(choice = 1, player = 1):
    text_Score = font_TTF_small.render("Score player : {0}".format(score1), True, Azure3)
    text_HightScore = font_TTF_small.render("High score player : {0}".format(hscore), True, Azure3)

    text_Score1 = font_TTF_small.render("Score player 1 : {0}".format(score1), True, Azure3)
    text_Score2 = font_TTF_small.render("Score player 2 : {0}".format(score2), True, Azure3)
    
    if choice ==1: # Đang chơi
        if player == 1:
            gameMenu.blit(text_Score,(290,545))
        elif player == 2:
            gameMenu.blit(text_Score1,(40,545))
            gameMenu.blit(text_Score2,(530,545))
    elif choice ==0:
        if player == 1:
            gameMenu.blit (text_Score, (290,190))
            gameMenu.blit (text_HightScore, (260,230))
        if player == 2:
            gameMenu.blit (text_Score1, (70,190))
            gameMenu.blit (text_Score2, (500,190))
            gameMenu.blit (text_HightScore, (260,230))
            


playGame_main = True
# khai báo các biến 
Screen_1 = True # bật màn hình 1
Screen_2 = False # tắt màn hình 2

Active_Screen1 = True # bật sự kiện cho màn hình 1
Active_Screen2 = False # tắt sự kiện màn hình 2

str_player = "" # số người chơi
flag_gamePlayer = 0

inputGame = False
button_screen1_dai = 227
button_screen1_rong = 65
# ImgButton_screen1 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(227,65))





# tạo chữ màn hình 1
text_ranSanMoi = font_TTF_large.render("Ran san moi", True,DarkSlateGray )


button_1Player = pygame.Rect(285,202,227,65)
text_1Player = font_TTF_medium.render("1 Player", True, Azure3)

button_2Player = pygame.Rect(285,292,227,65)
text_2Player = font_TTF_medium.render("2 Player", True, Azure3)

button_exit = pygame.Rect(285,382,227,65)
text_exit = font_TTF_medium.render("Exit", True, Azure3)

button_openVoice = pygame.Rect(20,530,80,80)


button_screen1_dai1 = 227
button_screen1_rong1 = 65
button_screen1_dai2 = 227
button_screen1_rong2 = 65
button_screen1_dai3 = 227
button_screen1_rong3 = 65
voice_dai = 50
voice_rong = 50

def manHinh1 ():
    global button_screen1_rong1
    global button_screen1_dai1
    global button_screen1_dai2 
    global button_screen1_rong2 
    global button_screen1_dai3 
    global button_screen1_rong3 
    global voice_dai 
    global voice_rong 
    global click_voice

    gameMenu.blit(text_ranSanMoi, (210,90))
    
    text_HightScore_screen1 = font_TTF_small_type2.render("High score : {0}".format(hscore), True, DarkSlateGray)
    gameMenu.blit(text_HightScore_screen1, (275,160))
    
    ImgButton_screen1_1 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen1_dai1,button_screen1_rong1)) 
    gameMenu.blit(ImgButton_screen1_1, button_1Player)
    gameMenu.blit(text_1Player, (300,220))

    ImgButton_screen1_2 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen1_dai2,button_screen1_rong2))     
    gameMenu.blit(ImgButton_screen1_2, button_2Player)
    gameMenu.blit(text_2Player, (300,310))

    ImgButton_screen1_3 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen1_dai3,button_screen1_rong3))     
    gameMenu.blit(ImgButton_screen1_3, button_exit)
    gameMenu.blit(text_exit, (350,400))
    if click_voice%2 != 0:
         Img_voice =  pygame.transform.scale(pygame.image.load('close_voice.png'),(voice_dai,voice_rong))
    elif click_voice%2 == 0:
        Img_voice =  pygame.transform.scale(pygame.image.load('open_voice.png'),(voice_dai,voice_rong))
    gameMenu.blit(Img_voice, (button_openVoice))
    





text_chonCheDo = font_TTF_large.render("Chon che do", True,DarkSlateGray )

button_tuDo = pygame.Rect(280,167,240,65) 
text_tuDo = font_TTF_medium.render("Tu do", True, Azure3)


button_thoiGian = pygame.Rect(280,247,240,65)
text_thoiGian = font_TTF_medium.render("Thoi gian", True, Azure3)


button_ngaiVat = pygame.Rect(280,327,240,65)
text_ngaiVat = font_TTF_medium.render("Ngai vat", True, Azure3)


button_tongHop  = pygame.Rect(280,407,240,65)
text_tongHop = font_TTF_medium.render("Tong hop", True, Azure3)


button_troLai  = pygame.Rect(280,487,240,65)
text_troLai = font_TTF_medium.render("Tro lai", True, Azure3)

Img_Lui1 = pygame.transform.scale(pygame.image.load('Lui.png'),(40,40)) 
Img_Tien1 = pygame.transform.scale(pygame.image.load('Tien.png'),(40,40)) 
Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 

button_lui1  = pygame.Rect(20,320,40,40)
button_tien1  = pygame.Rect(190,320,40,40)

Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 
button_lui2  = pygame.Rect(565,320,40,40)
button_tien2  = pygame.Rect(730,320,40,40)

button_screen2_dai1 = 240
button_screen2_rong1 = 65
button_screen2_dai2 = 240
button_screen2_rong2 = 65
button_screen2_dai3 = 240
button_screen2_rong3 = 65
button_screen2_dai4 = 240
button_screen2_rong4 = 65
button_screen2_dai5 = 240
button_screen2_rong5 = 65

click_ImgSkin1 = 1
click_ImgSkin2 = 1

def manHinh2 (str):
    global button_screen2_dai1 
    global button_screen2_rong1 
    global button_screen2_dai2 
    global button_screen2_rong2 
    global button_screen2_dai3 
    global button_screen2_rong3 
    global button_screen2_dai4 
    global button_screen2_rong4 
    global button_screen2_dai5 
    global button_screen2_rong5 
    global flag_gamePlayer

    
    gameMenu.blit(text_chonCheDo, (220,65))
    text_player = font_TTF_small_type2.render(str,True,DarkSlateGray )
    gameMenu.blit(text_player, (320,125))

    if flag_gamePlayer == 1:
        text_skin = font_TTF_small_type2.render("Skin",True,DarkSlateGray )
        gameMenu.blit(text_skin, (90,180))
        gameMenu.blit(Img_Lui1, button_lui1) # vị trí của chữ
        gameMenu.blit(Img_Tien1, button_tien1) # vị trí của chữ
        gameMenu.blit(Img_skin1, (85,265)) # vị trí của chữ
    elif flag_gamePlayer == 2:
        text_player1 = font_TTF_small_type2.render("Player 1",True,DarkSlateGray )
        gameMenu.blit(text_player1, (55,180))
        
        gameMenu.blit(Img_Lui1, button_lui1) # vị trí của chữ
        gameMenu.blit(Img_Tien1, button_tien1) # vị trí của chữ
        gameMenu.blit(Img_skin1, (85,265)) # vị trí của chữ

        text_player2 = font_TTF_small_type2.render("Player 2",True,DarkSlateGray )
        
        gameMenu.blit(text_player2, (595,180))
        gameMenu.blit(Img_Lui1, button_lui2) # vị trí của chữ
        gameMenu.blit(Img_Tien1, button_tien2) # vị trí của chữ
        gameMenu.blit(Img_skin2, (625,265)) # vị trí của chữ
    

    ImgButton_screen2_1 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen2_dai1,button_screen2_rong1))
    gameMenu.blit(ImgButton_screen2_1, button_tuDo) # vị trí của chữ
    gameMenu.blit(text_tuDo, (330,185)) # vị trí của chữ
        
    ImgButton_screen2_2 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen2_dai2,button_screen2_rong2))
    gameMenu.blit(ImgButton_screen2_2, button_thoiGian) # vị trí của chữ
    gameMenu.blit(text_thoiGian, (290,265))

    ImgButton_screen2_3 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen2_dai3,button_screen2_rong3))
    gameMenu.blit(ImgButton_screen2_3, button_ngaiVat) 
    gameMenu.blit(text_ngaiVat, (297,345)) 

    ImgButton_screen2_4 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen2_dai4,button_screen2_rong4))
    gameMenu.blit(ImgButton_screen2_4, button_tongHop) 
    gameMenu.blit(text_tongHop, (295,425)) 

    ImgButton_screen2_5 = pygame.transform.scale(pygame.image.load('Button_screen1.png'),(button_screen2_dai5,button_screen2_rong5))
    gameMenu.blit(ImgButton_screen2_5, button_troLai) 
    gameMenu.blit(text_troLai, (310,505)) 

    
    if click_voice%2 != 0:
         Img_voice =  pygame.transform.scale(pygame.image.load('close_voice.png'),(voice_dai,voice_rong))
    elif click_voice%2 == 0:
        Img_voice =  pygame.transform.scale(pygame.image.load('open_voice.png'),(voice_dai,voice_rong))
    gameMenu.blit(Img_voice, (button_openVoice))

time_start = 3.5
flag_timeStart = True
def start ():
    
    global time_start
    while True:
        pygame.time.delay(140) 
        
        time_start -=0.1
        rect_timeStart  = pygame.Rect(380,250,30,30)
        pygame.draw.rect(gameMenu, blue, rect_timeStart)
        text_timeStart = font_TTF_medium.render("{0}".format(int(time_start)), True, Azure3)
        gameMenu.blit(text_timeStart, (380,250))
        pygame.display.flip()
        if time_start == 1.0999999999999979:
            break


time_countdown = 61
flag_timeCountdown = False
def countDown ():
    global time_countdown
    if playerGame == 1:
        text_timeCountdown = font_TTF_small.render("Time : {0}".format(int(time_countdown)), True, Azure3)
        gameMenu.blit(text_timeCountdown, (600,545))
    elif playerGame == 2:
        text_timeCountdown = font_TTF_small.render("Time : {0}".format(int(time_countdown)), True, Azure3)
        gameMenu.blit(text_timeCountdown, (330,545))


dai = 420
rong = 40
flag_ngaiVat = False
ImgNgaiVat = pygame.transform.scale(pygame.image.load('ngaivat.png'),(420,40))

che_do_time = False
che_do_ngaiVat = False

list_ngaiVat = list()
ngaiVat_x = 180
ngaiVat_y = 120

for i in range(4):
    if i == 0:
       ngaiVat_x = 180
       ngaiVat_y = 120
      
    if i == 1:
        ngaiVat_x = 180
        ngaiVat_y = 360
    
    ngaiVatPos = [ngaiVat_x,ngaiVat_y]
    list_ngaiVat.append(ngaiVatPos)



flag_music_main = True
flag_block = True
flag_p = False
pressed_keys1 = []
pressed_keys2 = []
pygame.mixer.music.play()



while playGame_main:
    
    gameMenu.blit(ImgBackGround1,(0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("HightScore.txt", "w") as f:
                f.write(str(hscore))
                f.close()
            pygame.quit()
            sys.exit(False)
        elif event.type == music_end_event  and flag_music_main == True and flag_music == True:
            pygame.mixer.music.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if Active_Screen1 == True:
                
                if button_1Player.collidepoint(mouse_pos):
                    sound_click.play()
                    
                    # Tắt màn hình và sự kiện của screen 1
                    Screen_1 = False
                    Active_Screen1 = False
                    
                    # Bật màn hình và sự kiện của screen 2
                    Screen_2 = True
                    Active_Screen2 = True
                    
                    str_player = '1 Player' # str 1 người chơi
                    flag_gamePlayer = 1 # flag 1 người chơi
                    
                if button_2Player.collidepoint(mouse_pos):
                    
                    sound_click.play()
                    # Tắt màn hình và sự kiện của screen 1
                    Screen_1 = False
                    Active_Screen1 = False
                    
                    # Bật màn hình và sự kiện của screen 2
                    Screen_2 = True
                    Active_Screen2 = True
                    
                    str_player = '2 Player'  # str 2 người chơi
                    flag_gamePlayer = 2 # flag 2 người chơi
                    
                
                if button_openVoice.collidepoint(mouse_pos):
                    click_voice +=1
                    if click_voice%2 != 0:
                        Img_voice =  pygame.transform.scale(pygame.image.load('close_voice.png'),(50,50))
                        pygame.mixer.music.stop()
                        flag_music_main = False
                    else:
                        Img_voice =  pygame.transform.scale(pygame.image.load('open_voice.png'),(50,50))
                        pygame.mixer.music.play()
                        flag_music_main = True
                
                elif button_exit.collidepoint(mouse_pos):
                    with open("HightScore.txt", "w") as f:
                        f.write(str(hscore))
                        f.close()
                    sound_click.play()
                    pygame.quit()
                    sys.exit()
                 
            elif Active_Screen2 == True:
                if click_ImgSkin1 ==1:
                        Imghead1 = pygame.transform.scale(pygame.image.load('Skin1_HeadMain.png'),(m,m))
                        Imgbody1 = pygame.transform.scale(pygame.image.load('Skin1_BodyMain.png'),(m,m))
                if click_ImgSkin1 ==2 : 
                    Imghead1 = pygame.transform.scale(pygame.image.load('Skin2_HeadMain.png'),(m,m))
                    Imgbody1 = pygame.transform.scale(pygame.image.load('Skin2_BodyMain.png'),(m,m))
                if click_ImgSkin1 ==3:
                        Imghead1 = pygame.transform.scale(pygame.image.load('Skin3_HeadMain.png'),(m,m))
                        Imgbody1 = pygame.transform.scale(pygame.image.load('Skin3_BodyMain.png'),(m,m))
                if click_ImgSkin1 ==4 or click_ImgSkin1 == 0: 
                    Imghead1 = pygame.transform.scale(pygame.image.load('Skin4_HeadMain.png'),(m,m))
                    Imgbody1 = pygame.transform.scale(pygame.image.load('Skin4_BodyMain.png'),(m,m))


                if click_ImgSkin2 == 1:
                    Imgbody2 = pygame.transform.scale(pygame.image.load('Skin1_BodyMain.png'),(m,m))
                    Imghead2 = pygame.transform.scale(pygame.image.load('Skin1_HeadMain.png'),(m,m))
                    Imghead2  = pygame.transform.rotate(Imghead2, 180)
                if click_ImgSkin2 == 2 :
                    Imgbody2 = pygame.transform.scale(pygame.image.load('Skin2_BodyMain.png'),(m,m))
                    Imghead2 = pygame.transform.scale(pygame.image.load('Skin2_HeadMain.png'),(m,m))
                    Imghead2  = pygame.transform.rotate(Imghead2, 180)
                
                if click_ImgSkin2 == 3:
                    Imgbody2 = pygame.transform.scale(pygame.image.load('Skin3_BodyMain.png'),(m,m))
                    Imghead2 = pygame.transform.scale(pygame.image.load('Skin3_HeadMain.png'),(m,m))
                    Imghead2  = pygame.transform.rotate(Imghead2, 180)
                if click_ImgSkin2 == 4 or click_ImgSkin2 == 0:
                    Imgbody2 = pygame.transform.scale(pygame.image.load('Skin4_BodyMain.png'),(m,m))
                    Imghead2 = pygame.transform.scale(pygame.image.load('Skin4_HeadMain.png'),(m,m))
                    Imghead2  = pygame.transform.rotate(Imghead2, 180)
                
                
                
                if button_tuDo.collidepoint(mouse_pos):
                    che_do_time = False
                    inputGame = True
                    playGame = True
                    While_playGame = True
                    Screen_2 = False
                    Active_Screen2 = False    
                    flag_timeStart = True
                    flag_pause =0
                    sound_click.play()
                    pygame.mixer.music.stop()

                    
                    
                    if flag_gamePlayer == 1:
                        n_food = 3
                        playerGame = 1   
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                    if flag_gamePlayer == 2:
                        n_food = 8
                        playerGame = 2
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
              
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                        direction2 = 'LEFT'
                        changeto2 = 'LEFT'
                 
                        snakepos2 = [680,440] # vị trí của con rắn khi xuất hiện lần đầu
                        snakebody2 = [[680,440],[700,440],[720,440]] # 3 khúc mỗi khúc có tọa độ như trên
                        score2=0    
                    
                    foodpos_list = list()
                    for i in range(n_food):
                        foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                        foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                        if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                        if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                        foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                        foodpos_list.append(foodpos)

                elif button_thoiGian.collidepoint(mouse_pos):
                    che_do_time = True
                    flag_timeCountdown = True
                    inputGame = True
                    playGame = True
                    While_playGame = True
                    Screen_2 = False
                    Active_Screen2 = False    
                    flag_timeStart = True
                    flag_pause =0
                    sound_click.play()
                    pygame.mixer.music.stop()
                    
                    
                    
                    
                    if flag_gamePlayer == 1:
                        playerGame = 1
                        n_food = 3   
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
                        
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                    if flag_gamePlayer == 2:
                        playerGame = 2
                        n_food = 8
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
                        
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                        direction2 = 'LEFT'
                        changeto2 = 'LEFT'
                  
                        snakepos2 = [680,440] # vị trí của con rắn khi xuất hiện lần đầu
                        snakebody2 = [[680,440],[700,440],[720,440]] # 3 khúc mỗi khúc có tọa độ như trên
                        score2=0
                    
                    foodpos_list = list()
                    for i in range(n_food):
                        foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                        foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                        if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                        if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                        foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                        foodpos_list.append(foodpos)
                
                elif button_ngaiVat.collidepoint(mouse_pos):
                    che_do_ngaiVat = True
                    flag_ngaiVat = True
                    inputGame = True
                    playGame = True
                    While_playGame = True
                    Screen_2 = False
                    Active_Screen2 = False    
                    flag_timeStart = True
                    flag_pause =0
                    sound_click.play()
                    pygame.mixer.music.stop()
                    
                    
                    
                    if flag_gamePlayer == 1:
                        playerGame = 1
                        n_food = 5   
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
                       
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                    if flag_gamePlayer == 2:
                        playerGame = 2
                        n_food = 8
                        direction1 = 'RIGHT'
                        changeto1 = 'RIGHT'
                       
                        snakepos1 = [100,60]
                        snakebody1 = [[100,60],[80,60],[60,60]]
                        score1=0
                        direction2 = 'LEFT'
                        changeto2 = 'LEFT'
                        
                        snakepos2 = [680,440] # vị trí của con rắn khi xuất hiện lần đầu
                        snakebody2 = [[680,440],[700,440],[720,440]] # 3 khúc mỗi khúc có tọa độ như trên
                        score2=0
                    
                    foodpos_list = list()
                    for i in range(n_food):
                        foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                        foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                        if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                        if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                        foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                        foodpos_list.append(foodpos)
                 
                elif button_tongHop.collidepoint(mouse_pos):
                        che_do_time = True
                        flag_timeCountdown = True
                        che_do_ngaiVat = True
                        flag_ngaiVat = True
                        inputGame = True
                        playGame = True
                        While_playGame = True
                        Screen_2 = False
                        Active_Screen2 = False    
                        flag_timeStart = True
                        flag_pause =0
                        sound_click.play()
                        pygame.mixer.music.stop()
                        
                       
                        
                        if flag_gamePlayer == 1:
                            playerGame = 1
                            n_food = 5   
                            direction1 = 'RIGHT'
                            changeto1 = 'RIGHT'
                           
                            snakepos1 = [100,60]
                            snakebody1 = [[100,60],[80,60],[60,60]]
                            score1=0
                        if flag_gamePlayer == 2:
                            playerGame = 2
                            n_food = 8
                            direction1 = 'RIGHT'
                            changeto1 = 'RIGHT'
                           
                            snakepos1 = [100,60]
                            snakebody1 = [[100,60],[80,60],[60,60]]
                            score1=0
                            direction2 = 'LEFT'
                            changeto2 = 'LEFT'
                            
                            snakepos2 = [680,440] # vị trí của con rắn khi xuất hiện lần đầu
                            snakebody2 = [[680,440],[700,440],[720,440]] # 3 khúc mỗi khúc có tọa độ như trên
                            score2=0
                    
                        foodpos_list = list()
                        for i in range(n_food):
                            foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                            foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                            if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                            if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                            foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                            foodpos_list.append(foodpos)

                if button_tien1.collidepoint(mouse_pos):
                    sound_click.play()
                    click_ImgSkin1 +=1
                    if click_ImgSkin1 == 1 or click_ImgSkin1 == 5:
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 
                        if click_ImgSkin1 == 5:
                            click_ImgSkin1 = 1
                    elif click_ImgSkin1 == 2:
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin2.png'),(80,150)) 
                    elif click_ImgSkin1 == 3:
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin3.png'),(80,150)) 
                    elif click_ImgSkin1 == 4  :
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin4.png'),(80,150)) 
                        click_ImgSkin1 = 0

                if button_lui1.collidepoint(mouse_pos):
                    sound_click.play()
                    click_ImgSkin1 -=1
                    if click_ImgSkin1 == 1 :
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 
                    elif click_ImgSkin1 == 2:
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin2.png'),(80,150)) 
                    elif click_ImgSkin1 == 3 or click_ImgSkin1 == -1:
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin3.png'),(80,150)) 
                        if click_ImgSkin1 == -1:
                            click_ImgSkin1 = 3
                    elif click_ImgSkin1 == 4 or click_ImgSkin1 == 0 :
                        Img_skin1 = pygame.transform.scale(pygame.image.load('img_skin4.png'),(80,150))     
                        click_ImgSkin1 = 4

                if button_tien2.collidepoint(mouse_pos):
                    sound_click.play()
                    click_ImgSkin2 +=1
                    if click_ImgSkin2 == 1 or click_ImgSkin2 == 5:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 
                        if click_ImgSkin2 == 5:
                            click_ImgSkin2 = 1
                    elif click_ImgSkin2 == 2:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin2.png'),(80,150)) 
                    elif click_ImgSkin2 == 3:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin3.png'),(80,150)) 
                    elif click_ImgSkin2 == 4:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin4.png'),(80,150)) 
                        click_ImgSkin2 = 0

                if button_lui2.collidepoint(mouse_pos):
                    sound_click.play()
                    click_ImgSkin2 -=1
                    if click_ImgSkin2 == 1 :
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin1.png'),(80,150)) 
                    elif click_ImgSkin2 == 2:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin2.png'),(80,150)) 
                    elif click_ImgSkin2 == 3 or click_ImgSkin2 == -1:
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin3.png'),(80,150)) 
                        if click_ImgSkin2 == -1:
                            click_ImgSkin2 = 3
                    elif click_ImgSkin2 == 4 or click_ImgSkin2 == 0 :
                        Img_skin2 = pygame.transform.scale(pygame.image.load('img_skin4.png'),(80,150))     
                        click_ImgSkin2 = 4


                if button_openVoice.collidepoint(mouse_pos):
                    sound_click.play()
                    click_voice +=1
                    if click_voice%2 != 0:
                        
                        pygame.mixer.music.stop()
                        flag_music_main = False
                    else:
                        
                        pygame.mixer.music.play()
                        flag_music_main = True


                elif button_troLai.collidepoint(mouse_pos):
                    sound_click.play()
                   # Tắt màn hình và sự kiện của screen 2
                    Scrern_2 = False
                    Active_Screen2 = False
                   
                   # Bật màn hình và sự kiện của screen 1
                    Screen_1 = True
                    Active_Screen1 = True

        if event.type == pygame.MOUSEMOTION:
            if Active_Screen1:
                if button_1Player.collidepoint(event.pos):
                    button_screen1_dai1 = 232
                    button_screen1_rong1 = 70
                else:
                    button_screen1_dai1 = 227
                    button_screen1_rong1 = 65
                
                if button_2Player.collidepoint(event.pos):
                    button_screen1_dai2 = 232
                    button_screen1_rong2 = 70
                else:
                    button_screen1_dai2 = 227
                    button_screen1_rong2 = 65
                
                if button_exit.collidepoint(event.pos):
                    button_screen1_dai3 = 232
                    button_screen1_rong3 = 70
                else:
                    button_screen1_dai3 = 227
                    button_screen1_rong3 = 65
                
                if button_openVoice.collidepoint(event.pos):
                    voice_dai = 55
                    voice_rong = 55
                else:
                    voice_dai = 50
                    voice_rong = 50
            
            elif Active_Screen2:
                if button_tuDo.collidepoint(event.pos):
                    button_screen2_dai1 = 245
                    button_screen2_rong1 = 70
                else:
                    button_screen2_dai1 = 240
                    button_screen2_rong1 = 65
                
                if button_thoiGian.collidepoint(event.pos):
                    button_screen2_dai2 = 245
                    button_screen2_rong2 = 70
                else:
                    button_screen2_dai2 = 240
                    button_screen2_rong2 = 65
                
                if button_ngaiVat.collidepoint(event.pos):
                    button_screen2_dai3 = 245
                    button_screen2_rong3 = 70
                else:
                    button_screen2_dai3 = 240
                    button_screen2_rong3 = 65
                if button_tongHop.collidepoint(event.pos):
                    button_screen2_dai4 = 245
                    button_screen2_rong4 = 70
                else:
                    button_screen2_dai4 = 240
                    button_screen2_rong4 = 65
                
                if button_troLai.collidepoint(event.pos):
                    button_screen2_dai5 = 245
                    button_screen2_rong5 = 70
                else:
                    button_screen2_dai5 = 240
                    button_screen2_rong5 = 65
                
                
                if button_openVoice.collidepoint(event.pos):
                    voice_dai = 55
                    voice_rong = 55
                else:
                    voice_dai = 50
                    voice_rong = 50


    
    if (Screen_1 == True):
        manHinh1()
    elif (Screen_2 == True):
        manHinh2(str_player)
    
    elif inputGame:
        
        while While_playGame :
            pygame.time.delay(140) 
            
            
            gameMenu.blit(ImgBackGround1,(0,0)) 
            gameMenu.blit(ImgBackGround2, (20,20)) 
            player1 = False
            player2 = False
            if not channel_dangChoi.get_busy() and flag_music == True and flag_music_main == True:
                channel_dangChoi.play(sound_dangChoi)
            if not channel_dangChoi.get_busy() and playGame == True and flag_music_main == True :
                 channel_dangChoi.play(sound_dangChoi)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                        if event.key not in pressed_keys1:
                            # Thêm phím vào danh sách nếu phím đó chưa được nhấn
                            pressed_keys1.append(event.key)
                        # Kiểm tra xem có nhiều hơn một phím đang được nhấsn không
                        if len(pressed_keys1) == 2:
                            # Nếu có, bỏ qua sự kiện
                            continue
                    
                    # Xử lý sự kiện tương ứng với phím được nhấn
                    if event.key == pygame.K_w:
                        if ( direction1 == 'RIGHT' and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, 90)
                        if (direction1 == 'LEFT' and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, -90)
                        changeto1 = 'UP'
                    
                    elif event.key == pygame.K_s:
                        if (direction1 == 'RIGHT'and flag_timeStart == False ):
                            Imghead1  = pygame.transform.rotate(Imghead1, -90)
                        if (direction1 == 'LEFT'and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, 90)
                        changeto1 = 'DOWN'
                    elif event.key == pygame.K_a:
                        if (direction1 == 'DOWN'and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, -90)
                        if (direction1 == 'UP'and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, 90)
                        changeto1 = 'LEFT'
                    elif event.key == pygame.K_d:
                        if (direction1 == 'DOWN'and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, 90)
                        if (direction1 == 'UP'and flag_timeStart == False):
                            Imghead1  = pygame.transform.rotate(Imghead1, -90)
                        changeto1 = 'RIGHT'
                    
                    
            
                    if playerGame == 2:
                        if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                            if event.key not in pressed_keys2:
                                # Thêm phím vào danh sách nếu phím đó chưa được nhấn
                                pressed_keys2.append(event.key)
                            # Kiểm tra xem có nhiều hơn một phím đang được nhấsn không
                            if len(pressed_keys2) == 2:
                                # Nếu có, bỏ qua sự kiện
                                continue
                        
                        
                        if event.key == pygame.K_RIGHT:
                            if (direction2 == 'DOWN'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, 90)
                            if (direction2 == 'UP'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, -90)
                            changeto2 = 'RIGHT' 
                        elif event.key == pygame.K_LEFT:
                            if (direction2 == 'DOWN'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, -90)
                            if (direction2 == 'UP'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, 90)
                            changeto2 = 'LEFT'
                        elif event.key == pygame.K_UP:
                            if ( direction2 == 'RIGHT' and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, 90)
                            if (direction2 == 'LEFT'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, -90)
                            changeto2 = 'UP'
                        elif event.key == pygame.K_DOWN:
                            if (direction2 == 'RIGHT'and flag_timeStart == False ):
                                Imghead2  = pygame.transform.rotate(Imghead2, -90)
                            if (direction2 == 'LEFT'and flag_timeStart == False):
                                Imghead2  = pygame.transform.rotate(Imghead2, 90)
                            changeto2 = 'DOWN'
                    
                    
                    
                    
                    if event.key == pygame.K_p :
                        flag_pause +=1
                        if flag_pause%2== 0  :
                            
                            if playerGame == 1:
                                if flag_p == False:
                                    sound_click.play()
                                    
                                    playGame = True
                                    flag_timeStart = True
                                    time_start = 3.5
                                   
                            if playerGame == 2:
                                if flag_p == False:
                                    sound_click.play()
                                    
                                    
                                    playGame = True
                                    flag_timeStart = True
                                    time_start = 3.5

                    if event.key == pygame.K_SPACE and playGame == False:
                        playGame = True
                        sound_click.play()
                        sound_thua.stop()
                        sound_thang.stop()
                        
                        if click_ImgSkin1 ==1:
                            Imghead1 = pygame.transform.scale(pygame.image.load('Skin1_HeadMain.png'),(m,m))
                           
                        if click_ImgSkin1 ==2 : 
                            Imghead1 = pygame.transform.scale(pygame.image.load('Skin2_HeadMain.png'),(m,m))
                        
                        if click_ImgSkin1 ==3:
                            Imghead1 = pygame.transform.scale(pygame.image.load('Skin3_HeadMain.png'),(m,m))
                           
                        if click_ImgSkin1 ==4 or click_ImgSkin1 == 0 : 
                            Imghead1 = pygame.transform.scale(pygame.image.load('Skin4_HeadMain.png'),(m,m))    


                        if click_ImgSkin2 == 1:
                            
                            Imghead2 = pygame.transform.scale(pygame.image.load('Skin1_HeadMain.png'),(m,m))
                            Imghead2  = pygame.transform.rotate(Imghead2, 180)
                        if click_ImgSkin2 == 2 :
                            
                            Imghead2 = pygame.transform.scale(pygame.image.load('Skin2_HeadMain.png'),(m,m))
                            Imghead2  = pygame.transform.rotate(Imghead2, 180)
                        
                        if click_ImgSkin2 == 3:
                            
                            Imghead2 = pygame.transform.scale(pygame.image.load('Skin3_HeadMain.png'),(m,m))
                            Imghead2  = pygame.transform.rotate(Imghead2, 180)
                        if click_ImgSkin2 == 4 or click_ImgSkin2 == 0:
                            
                            Imghead2 = pygame.transform.scale(pygame.image.load('Skin4_HeadMain.png'),(m,m))
                            Imghead2  = pygame.transform.rotate(Imghead2, 180)



                        if playerGame == 1: 
                            n_food = 3
                            direction1 = 'RIGHT'
                            changeto1 = 'RIGHT'
                            snakepos1 = [100,60]
                            snakebody1 = [[100,60],[80,60],[60,60]]
                            
                            score1=0
                        
                        
                        if playerGame ==2:
                            
                            n_food = 8
                            direction1 = 'RIGHT'
                            changeto1 = 'RIGHT'
                            snakepos1 = [100,60]
                            snakebody1 = [[100,60],[80,60],[60,60]]
                            score1=0

                            direction2 = 'LEFT'
                            changeto2 = 'LEFT'
                            
                            snakepos2 = [680,440] # vị trí của con rắn khi xuất hiện lần đầu
                            snakebody2 = [[680,440],[700,440],[720,440]] # 3 khúc mỗi khúc có tọa độ như trên
                            score2=0
                        flag_p = False
                        flag_pause =0
                        
                        flag_timeStart = True
                        time_start = 3.5
                        if che_do_time :
                            flag_timeCountdown = True
                            time_countdown = 61
                        if che_do_ngaiVat:
                            flag_ngaiVat = True
                        foodpos_list = list()
                        
                        for i in range(n_food):
                            foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                            foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                            if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                            if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                            foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                            foodpos_list.append(foodpos)

                
                   


                elif event.type == pygame.KEYUP:
                    if event.key in pressed_keys1:
                        # Xóa phím khỏi danh sách nếu phím đó đã được nhả ra
                        pressed_keys1.remove(event.key)
                    
                    if event.key in pressed_keys2:
                        # Xóa phím khỏi danh sách nếu phím đó đã được nhả ra
                        pressed_keys2.remove(event.key)
                    
                
                
                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos   
                    if playGame == False:
                        if button_back.collidepoint(mouse_pos):
                            flag_p = False
                            flag_ngaiVat = False
                            che_do_time = False
                            che_do_ngaiVat = False
                            flag_ngaiVat = False
                            Screen_2 = True
                            Active_Screen2 = True
                            While_playGame = False
                            inputGame = False
                            playGame = False
                            flag_timeStart = True
                            time_start = 3.5
                            flag_timeCountdown = False
                            time_countdown = 61
                            sound_click.play()
                            sound_dangChoi.stop()
                            sound_thang.stop()
                            sound_thua.stop()
                            if flag_music_main == True:
                                pygame.mixer.music.play()

                
                

            if playGame:
               
                # huong di
                if changeto1 == 'RIGHT' and not direction1 == 'LEFT':   # không được đi lại ngược chiều mà nó đang đi
                    direction1 = 'RIGHT'
                if changeto1 == 'LEFT' and not direction1 == 'RIGHT':
                    direction1 = 'LEFT'
                if changeto1 == 'UP' and not direction1 == 'DOWN':
                    direction1 = 'UP'
                if changeto1 == 'DOWN' and not direction1 == 'UP':
                    direction1 = 'DOWN'
                
                if playerGame == 2:
                    if changeto2 == 'RIGHT' and not direction2 == 'LEFT':   # không được đi lại ngược chiều mà nó đang đi
                        direction2 = 'RIGHT'
                    if changeto2 == 'LEFT' and not direction2 == 'RIGHT':
                        direction2 = 'LEFT'
                    if changeto2 == 'UP' and not direction2 == 'DOWN':
                        direction2 = 'UP'
                    if changeto2 == 'DOWN' and not direction2 == 'UP':
                        direction2 = 'DOWN'
                    
                # cập nhật vị trí mới
                if direction1 == 'RIGHT':
                    snakepos1[0] += m  # nếu đi qua bên phải thì đi theo trục x và sẽ cộng x
                if direction1 == 'LEFT':
                    snakepos1[0] -= m
                if direction1 == 'UP':
                    snakepos1[1] -= m # snakepos1[1] có nghĩa là đang tác động vào y, và ở đây là đi lên nên phải trừ y
                if direction1 == 'DOWN':
                    snakepos1[1] += m
                
                if playerGame == 2:
                    if direction2 == 'RIGHT':
                        snakepos2[0] += m  # nếu đi qua bên phải thì đi theo trục x và sẽ cộng x
                    if direction2 == 'LEFT':
                        snakepos2[0] -= m
                    if direction2 == 'UP':
                        snakepos2[1] -= m # snakepos1[1] có nghĩa là đang tác động vào y, và ở đây là đi lên nên phải trừ y
                    if direction2 == 'DOWN':
                        snakepos2[1] += m






#----------------------------------------------------------------------------------------------------------------
# GÁN THÂN VÀ ĐẦU CON RẮN VÀO MÀN HÌNH                
                if playerGame ==1:
                    i = 0
                    for pos in snakebody1: # đây là vòng for chạy hết cái list của body rắn
                        if i == 0:
                            gameMenu.blit(Imghead1,pygame.Rect(snakebody1[0][0],snakebody1[0][1],m,m)) # gắn cái đầu con rắn đè lên vị trí đầu tiên
                        else :
                            gameMenu.blit(Imgbody1,pygame.Rect(pos[0],pos[1],m,m)) # gán thân vào
                        i+=1
                
                if playerGame == 2:
                    i1 = 0
                    for pos in snakebody1: # đây là vòng for chạy hết cái list của body rắn
                        if i1 == 0: 
                            gameMenu.blit(Imghead1,pygame.Rect(snakebody1[0][0],snakebody1[0][1],m,m)) # gắn cái đầu con rắn đè lên vị trí đầu tiên
                        else :
                            gameMenu.blit(Imgbody1,pygame.Rect(pos[0],pos[1],m,m)) # gán thân vào
                        i1+=1

                    i2 = 0
                    for pos in snakebody2: # đây là vòng for chạy hết cái list của body rắn
                        if i2 == 0 :
                            gameMenu.blit(Imghead2,pygame.Rect(snakebody2[0][0],snakebody2[0][1],m,m)) # gắn cái đầu con rắn đè lên vị trí đầu tiên
                        else :
                            gameMenu.blit(Imgbody2,pygame.Rect(pos[0],pos[1],m,m)) # gán thân vào
                        i2+=1




#----------------------------------------------------------------------------------------------------------------j
# THÊM THỨC ĂN VÀO MÀN HÌNH
                for foodpos in foodpos_list:
                    gameMenu.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))



#------------------------------------------------------------------------------------------------               
# THÊM NGẠI VẬT VÀ XỬ LÝ VA CHẠM
                if flag_ngaiVat:
                    for ngaiVatPos in list_ngaiVat:
                        gameMenu.blit(ImgNgaiVat,pygame.Rect(ngaiVatPos[0],ngaiVatPos[1],m,m))
                    if playerGame == 1:    
                        if snakepos1[0] > 170 and snakepos1[0] < 600  and snakepos1[1] >110 and snakepos1[1] <160:
                                playGame = False
                                game_over("Game over !",1)
                                flag_p = True 
                        if snakepos1[0] > 170 and snakepos1[0] < 600  and snakepos1[1] >350 and snakepos1[1] <390:
                                playGame = False
                                game_over("Game over !",1)
                                flag_p = True   
                        
                    if playerGame == 2:
                        if snakepos1[0] > 170 and snakepos1[0] < 600  and snakepos1[1] >110 and snakepos1[1] <160:
                                playGame = False
                                player2 = True
                        if snakepos1[0] > 170 and snakepos1[0] < 600  and snakepos1[1] >350 and snakepos1[1] <390:
                                playGame = False
                                player2 = True
                        
                        if snakepos2[0] > 170 and snakepos2[0] < 600  and snakepos2[1] >110 and snakepos2[1] <160:
                                playGame = False
                                player1 = True
                        if snakepos2[0] > 170 and snakepos2[0] < 600  and snakepos2[1] >350 and snakepos2[1] <390:
                                playGame = False
                                player1 = True                               
#--------------------------------------------------------------------------------------------------------------
# ĐẾM THỜI GIAN ĐỂ BẮT ĐẦU
                if flag_timeStart:
                    pygame.mixer.music.stop()
                    sound_dangChoi.stop()
                    pygame.event.set_blocked(None)
                    start()
                    if flag_music_main == True:
                        channel_dangChoi.play(sound_dangChoi)
                    pygame.event.get()
                    pygame.event.set_allowed(None)
                    flag_timeStart = False
                
                    

#--------------------------------------------------------------------------------------------------------   
# NẾU SỐ LẦN NHẤN P LÀ LẺ THÌ CHO DỪNG MÀN HÌNH
                if flag_pause%2!= 0  :
                        playGame = False
                        if playerGame == 1:
                            sound_click.play()
                            sound_dangChoi.stop()
                            if flag_music_main == True:
                                pygame.mixer.music.play()
                            
                            game_over ("PAUSE",1)
                        elif playerGame == 2:
                            sound_click.play()
                            sound_dangChoi.stop()
                            if flag_music_main == True:
                                pygame.mixer.music.play()
                            
                            game_over ("PAUSE",2)    
                        flag_space = 1

#------------------------------------------------------------------------------------------------------

# XỬ LÝ ĐẾM NGƯỢC
                if flag_timeCountdown :
                    time_countdown -= 0.14
                    
                    countDown()           
                    if time_countdown == 0.3799999999997917:
                        if playerGame == 1:
                            game_over ("End game",1)
                            flag_p = True 
                        
                        if playerGame == 2:
                            if score1 > score2:
                                player1 = True
                            if score1 < score2:
                                player2 = True
                            if score1 == score2:
                                player1 = True
                                player2 = True
                        flag_timeCountdown = False
                        playGame = False
                        

#-------------------------------------------------------------------------------------------------------------   
# XỬ LÝ 2 CON RẮN ĐỤNG NHAU TRONG CHẾ ĐỘ CHƠI 2 NGƯỜI         
                if playerGame == 2: 
                        for t1 in snakebody1[0:]:
                            for b1 in snakebody2[0:]:
                                if snakepos2[0] == t1[0] and snakepos2[1] == t1[1] or b1[0] == t1[0] and b1[1] == t1[1]:
                                    # game_over('Player 1 WIN',2)
                                    player1 = True
                                    playGame = False
                                    
                        for t2 in snakebody2[0:]:
                            for b2 in snakebody1[0:]:
                                if snakepos1[0] == t2[0] and snakepos1[1] == t2[1] or b2[0] == t2[0] and b2[1] == t2[1]:
                                    # game_over('Player 2 WIN',2)
                                    player2 = True
                                    playGame = False
                                    
#--------------------------------------------------------------------------------------------------------------- 
# XỬ LÝ TỰ ĂN CHÍNH MÌNH TRONG CHẾ ĐỘ CHƠI MỘT NGƯỜI
                if playerGame ==1 :
                    for b in snakebody1[1:]:
                        if snakepos1[0] == b[0] and snakepos1[1] == b[1]:
                            game_over("Game over !",1)
                            flag_p = True 
                            playGame = False
#-----------------------------------------------------------------------------------------------------------
# XỬ LÝ ĐI XUYÊN MAP 1 NGƯỜI CHƠI                
                if playerGame == 1 and flag_ngaiVat == False or playerGame == 1 and flag_timeCountdown == True:
                    if snakepos1[0] >=780:
                            snakepos1 = [20,snakepos1[1]]
                    if snakepos1[0] <19:
                            snakepos1 = [760,snakepos1[1]]
                    if snakepos1[1] >=519:
                            snakepos1 = [snakepos1[0],20]
                    if snakepos1[1] <20:
                            snakepos1 = [snakepos1[0],500]                 
#----------------------------------------------------------------------------------------------------------
# AUTO CHÈN CÁI ĐẦU VÀO ĐẦU DANH SÁCH BODY
                if playerGame == 1:
                    snakebody1.insert(0,list(snakepos1)) # mặc định là chèn vào đầu danh sách
                if playerGame == 2 :
                    snakebody1.insert(0,list(snakepos1)) # mặc định là chèn vào đầu danh sách
                    snakebody2.insert(0,list(snakepos2)) # mặc định là chèn vào đầu danh sách
#--------------------------------------------------------------------------------------------------              
# KIỂM TRA XEM ĂN ĐƯỢC MỒI CHƯA  
                for foodpos in foodpos_list:
                    if playerGame == 1 :
                        if snakepos1[0] == foodpos[0] and snakepos1[1] == foodpos[1]  :
                            sound_anThucan.play()
                            foodpos_list.remove(foodpos) # xóa mồi cũ
                            score1 += 1
                            if score1 > hscore:
                                hscore = score1
                            flag_food1 = False
                            foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                            foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                            if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                            if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                            foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                            foodpos_list.append(foodpos)

                    if playerGame == 2:
                        
                        if snakepos1[0] == foodpos[0] and snakepos1[1] == foodpos[1]  :
                            sound_anThucan.play()
                            foodpos_list.remove(foodpos) # xóa mồi cũ
                            score1 += 1
                            if score1 > hscore:
                                hscore = score1
                            flag_food1 = False
                            foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                            foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                            if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                            if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                            foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                            foodpos_list.append(foodpos)
                        
                        if snakepos2[0] == foodpos[0] and snakepos2[1] == foodpos[1] :
                            sound_anThucan.play()
                            foodpos_list.remove(foodpos) # xóa mồi cũ
                            score2 += 1
                            if score2 > hscore:
                                hscore = score2
                            flag_food2 = False
                            foodx = random.randrange(1,76) # sinh ngẫu nhiên tọa độ x của thức ăn
                            foody = random.randrange(1,50) # sinh ngẫu nhiên tọa độ y của thức ăn
                            if foodx %2 !=0: foodx +=1 # nếu foodx là số lẽ thì tăng thêm 1 để thành số chẵn
                            if foody %2 !=0: foody +=1 # nếu foody là số lẽ thì tăng thêm 1 để thành số chẵn
                            foodpos = [foodx*10, foody*10] # đây sẽ là tọa độ của thức ăn
                            foodpos_list.append(foodpos)
#----------------------------------------------------------------------------------------------------------------
# AUTO XÓA CUỐI DANH SÁCH NẾU KHÔNG ĂN ĐƯỢC MỒI    
                if playerGame == 1:
                    if flag_food1 == True: # không ăn được mồi nên xóa  
                        snakebody1.pop() # vì không ăn được nên cứ xóa đi
                if playerGame == 2:
                    if flag_food1 == True: # không ăn được mồi nên xóa  
                        snakebody1.pop() # vì không ăn được nên cứ xóa đi
                    if flag_food2 == True: # không ăn được mồi nên xóa  
                        snakebody2.pop()
                
                flag_food1 = True       
                flag_food2 = True       
#----------------------------------------------------------------------------------------------------------------
# XỬ LÝ VA CHẠM KHUNG CỦA CHẾ ĐỘ 1 NGƯỜI            
                if playerGame == 1 and flag_ngaiVat and flag_timeCountdown == False:
                    if snakepos1[0] > 779 or snakepos1[0] <1:
                            
                            playGame = False
                            game_over("Game over !",1)
                            
                    elif snakepos1[1] > 519 or snakepos1[1] <1:
                            
                            playGame = False
                            game_over("Game over !",1)
#--------------------------------------------------------------------------------------------------------        
# XỬ LÝ VA CHẠM KHUNG CỦA CHẾ ĐỘ 2 NGƯỜI             
                
                if playerGame == 2:
                    if snakepos1[0] > 779 or snakepos1[0] <1:
                        
                        playGame = False
                        player2 = True
                        
                    elif snakepos1[1] > 519 or snakepos1[1] <1:
                        
                        playGame = False
                        player2 = True
                        
                    if snakepos2[0] > 779 or snakepos2[0] <1:
                        
                        playGame = False
                        player1 = True
                        
                    elif snakepos2[1] > 519 or snakepos2[1] <1:
                        
                        playGame = False
                        player1 = True
                        
#-------------------------------------------------------------------------------------------------------------
# XỬ LÝ THẮNG THUA CHO CHẾ ĐỘ CHƠI 2 NGƯỜI
                if playerGame == 2:
                    if player1 == True and player2 == True:
                        if score1 > score2 :
                            game_over("Player 1 Win",2)
                            flag_p = True
                        elif score1 < score2:
                            game_over("player 2 Win",2)
                            flag_p = True
                        elif score1 == score2 :
                            game_over("Drawn",2) 
                            flag_p = True
                    elif player1 == True:
                        game_over("Player 1 Win",2)
                        flag_p = True
                    elif player2 == True :
                        game_over("Player 2 Win",2)
                        flag_p = True
#---------------------------------------------------------------------------------------------------------   
                show_score(1,playerGame)
                pygame.draw.rect(gameMenu,green4,(20,20,760,500),3)
                pygame.display.flip() # cập nhật màn hình
            
    pygame.display.flip() 
    
    
    




