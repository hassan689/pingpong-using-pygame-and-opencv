import pygame
import sys
import cv2
import mediapipe as mp
import time 
# Initialize Pygame
pygame.init()
cap =cv2.VideoCapture(0)
background_image = pygame.image.load('C:\\Users\\HP\Desktop\\opencv\\background.png')
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0 
cTime = 0  
# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Sample")

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 255, 255)
WHITE = (255, 255, 255)

# Set up the initial position and speed of the square
square_size = 10
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2




velocityx = 12
velocityy = 12  
# Line properties
start_pos = (100, 100)
end_pos = (700, 500)
line_color = WHITE
line_width = 5

speed = 35
x_axsis= 50
y_axsis= 50

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     y_axsis-=speed
    #     if y_axsis <= 0 :
    #         y_axsis = 0
    # if keys[pygame.K_RIGHT] :
    #     y_axsis+=speed 
    #     if y_axsis + 120 > screen_height:
    #         y_axsis = screen_height - 120 
        
    pygame.display.flip()
    # Key presses handling
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     square_x -= speed
    # if keys[pygame.K_RIGHT]:
    #     square_x += speed
    # if keys[pygame.K_UP]:
    #     square_y -= speed
    # if keys[pygame.K_DOWN]:
    #     square_y += speed
    # Fill the screen with black color
    
    
    
    
    
    
    square_x+=velocityx
    square_y+=velocityy
    
        
    
    if square_x + square_size >= x_axsis and square_x <= x_axsis + 20 and square_y + square_size >= y_axsis and square_y <= y_axsis + 120:
        if square_x + square_size >= x_axsis and square_x <= x_axsis + 20:
            velocityx = -velocityx
        if square_y + square_size >= y_axsis and square_y <= y_axsis + 120:
            velocityy = -velocityy








    if  square_x >= screen_width - square_size :
        velocityx =-velocityx
    if square_y <= 0 or square_y >= screen_height - square_size:
        velocityy =-velocityy 
    
    
    
    
    
    
  #  screen.fill(BLACK)
    screen.blit(background_image, (0, 0))

    # Draw the line
    pygame.draw.line(screen, line_color, (0, 0), (screen_width, 0), line_width)          # Top border
    pygame.draw.line(screen, line_color, (0, screen_height), (screen_width, screen_height), line_width)  # Bottom border
    pygame.draw.line(screen, line_color, (0, 0), (0, screen_height), line_width)         # Left border
    pygame.draw.line(screen, line_color, (screen_width, 0), (screen_width, screen_height), line_width)  # Right border
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    pygame.draw.rect(screen, WHITE, pygame.Rect(x_axsis, y_axsis, 20, 120))
    pygame.time.Clock().tick(60)
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks : 
         for handLms in results.multi_hand_landmarks : 
             for id , lm in enumerate(handLms.landmark):
                 h , w , c = img.shape
                 cx , cy = int(lm.x * w ) , int(lm.y * h)
                 print(id , cx ,cy)
                 fingerup =results[0]
             mpDraw.draw_landmarks(img , handLms , mpHands.HAND_CONNECTIONS)
             if handLms.landmark[8].y < handLms.landmark[6].y:
                y_axsis-=speed
                if y_axsis <= 0 :
                        y_axsis = 0
             if handLms.landmark[12].y < handLms.landmark[10].y :
                 y_axsis+=speed 
                 if y_axsis + 120 > screen_height:
                   y_axsis = screen_height - 120 
                 
                 
                 
    cTime = time.time()
    fps= 1/(cTime-pTime)
    pTime= cTime
    #print(fps)
    cv2.putText(img , str(int(fps)) ,(10 , 70) , cv2.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 255 ) , 3)
    cv2.imshow("image" , img)
    cv2.waitKey(1)
# Quit Pygame
pygame.quit()
cap.release()
cv2.destroyAllWindows()
sys.exit()
