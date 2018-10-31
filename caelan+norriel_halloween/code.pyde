x = 0
y = 0
sound = 0
duration = 0 
add_library("sound")

def draw():
    global x
    global y
    global duration
    global sound
    
 
    y += 1.5
    
    if y >= 685:
        y = 9999
        y+= 0
    
    background(0,0,0)
    x += 1.5
    fill(255,255,255)
    noStroke()
    ellipse(y,height/1.53,75,75)
    rect(y-27,height/1.45,100,50)
    rect(y-27,height/1.345,60,90)
    fill(255,0,0)
    ellipse(y+20,height/1.53,15,15)

    if x >= 685:
        x = 680
        x += 1
        image(img,x-300,height/6)
    
    sound += 1.5
    if sound >= 675:
        sf.play()
   
    duration += 1.5
    
    if duration >= 1150:
        exit()

def setup():
    ellipse
    fullScreen()
    global img
    img = loadImage("jumpscare-sound-effect.jpg")
    global sf
    size(200,200)
    sf = SoundFile(this, "Scary Jumpscare Sound Effect.wav")

    
        
