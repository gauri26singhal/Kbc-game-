import pygame
import os 
import time

def play_sound(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()



def play_segment(start_time, end_time):
    pygame.mixer.music.play(start=start_time)
    time.sleep(end_time - start_time)
    pygame.mixer.music.stop()


if __name__ == "__main__":
    mp3_file_path = os.path.join(os.path.dirname(__file__), "KBC.mp3")
    play_sound(mp3_file_path)

    
    start_time = 1 # Start playing in seconds
    end_time = 7.5   # End playing in seconds
    print(f"Playing from {start_time} to {end_time} seconds...")
    play_segment(start_time, end_time)

print("helo sir !! welcome to koun banega crore pati ")
print("do you want to play the game ")
y= input("type yes or no ")

if y =="yes" :
    print('lets start ')
    print("so !! here is your first question ")
    print("who is the first prime minister of India ?")
    print("your option are :")
    option =["nehru" ,  " narendra modi ", "mother teresa" ," priyanka gandi "]

    start_time = 7.6 # Start playing 
    end_time = 12   # End playing 
    print(f"Playing from {start_time} to {end_time} seconds...")      #use of f string 
    play_segment(start_time, end_time)

    start_time = 55 # Start playing 
    end_time = 60 # End playing 
    print(option)
    #print(f"Playing from {start_time} to {end_time} seconds...")
    play_segment(start_time, end_time) 
    option1 = input("enter your option ")  
        
    if option1==option[0]:
        print("you have won 10k ")
        print('so here is you next question')
        print("what is 2+2 =?")
        print("your option are :")
        option2=[4,5,6,7]

        start_time = 7.6 # Start playing 
        end_time = 12   # End playing 
        print(f"Playing from {start_time} to {end_time} seconds...")
        play_segment(start_time, end_time)

        start_time = 55 # Start playing 
        end_time = 60 # End playing 
        print(option2)
        #print(f"Playing from {start_time} to {end_time} seconds...")
        play_segment(start_time, end_time) 
        option3 = int(input("enter your option "))

        if option3==option2[0]:

            print ("you have won 20k")
            print("so here is ur next question")
            print("what is the short form form of world helath organization")
            print("your option are ")
            option=["WHO","WOH","XDS","SDWS"]

            start_time = 7.6 # Start playing 
            end_time = 12   # End playing
            print(f"Playing from {start_time} to {end_time} seconds...")
            play_segment(start_time, end_time)
            
            start_time = 55 # Start playing 
            end_time = 60 # End playing 
            print(option)
            #print(f"Playing from {start_time} to {end_time} seconds...")
            play_segment(start_time, end_time) 
            option1 = (input("enter your option "))

            if option1==option[0]:
                print("you have won 30k")
                print("so here is ur next question")
                print("what is differnet in these names")
                option=["apple","mango","tomato","gauva"]

                start_time = 7.6 # Start playing 
                end_time = 12   # End playing
                print(f"Playing from {start_time} to {end_time} seconds...")
                play_segment(start_time, end_time)

                start_time = 55 # Start playing
                end_time = 60 # End playing 
                print(option)
                #print(f"Playing from {start_time} to {end_time} seconds...")
                play_segment(start_time, end_time) 
                option1 = (input("enter your option "))

                if option1==option[2]: 
                   print("you have won 40k")
                   print("so here is ur last question")
                   print("in which year india was independent ? ")
                   option=[1932,1987,1973,1947]

                   start_time = 7.6 # Start playing 
                   end_time = 12   # End playing 
                   print(f"Playing from {start_time} to {end_time} seconds...")
                   play_segment(start_time, end_time)


                   start_time = 55 # Start playing 
                   end_time = 60 # End playing 
                   print(option)
                   #print(f"Playing from {start_time} to {end_time} seconds...")
                   play_segment(start_time, end_time) 
                   option1 = int(input("enter your option "))
                   if option1==option[3]: 
                       print("you have won 50k")
                       print("thnk you for playing !!")
                       print("hope you enjoyed the game ")
          
                else:
                    print ("wrong answer ")   
                    print("sorry you lose ")
                    start_time = 64 # Start playing 
                    end_time = 67 # End playing 
                    print(f"Playing from {start_time} to {end_time} seconds...")
                    play_segment(start_time, end_time)
                    print("thank you !! for playing ")



            else  :
                print ("wrong answewr")
                start_time = 64 # Start playing 
                end_time = 67 # End playing 
                print(f"Playing from {start_time} to {end_time} seconds...")
                play_segment(start_time, end_time)

            

        else:
            print("wrong answer")    

            start_time = 64 # Start playing 
            end_time = 67 # End playing 
            print(f"Playing from {start_time} to {end_time} seconds...")
            play_segment(start_time, end_time)

            
    else :
        print("wrong answer ")    

        start_time = 64 # Start playing 
        end_time = 70 # End playing 
        print(f"Playing from {start_time} to {end_time} seconds...")
        play_segment(start_time, end_time)
 
        

else :
    print("okh thank u !!")    