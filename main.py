import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def drawA(currentX):
    plt.plot([currentX, currentX], [0,5],'b')
    
def drawAAfterL(currentX):
    plt.plot([currentX+1, currentX-0.5], [0,3.5],'b')
    
def drawLStart(currentX):
    plt.plot([currentX, currentX], [0,5],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    
def drawLEnd(currentX):
    plt.plot([currentX, currentX], [0,5],'b')
    ctr =np.array( [(currentX-2 , 0), (currentX-2, -3) ,(currentX, -3),(currentX, 0),])
    x=ctr[:,0]
    y=ctr[:,1]
    
    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])

    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.plot(out[0],out[1],'b')
    
def drawBStart(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    plt.scatter(currentX-1, -0.5, s=10, color='blue')
    
def drawBEnd(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-4], [0,0],'b')
    plt.plot([currentX-4, currentX-4], [0,1],'b')
    plt.scatter(currentX-2, -0.5, s=10, color='blue')
    
def drawTStart(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    plt.scatter(currentX-0.667, 1.5, s=10, color='blue')
    plt.scatter(currentX-1.334, 1.5, s=10, color='blue')
    
def drawTEnd(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-4], [0,0],'b')
    plt.plot([currentX-4, currentX-4], [0,1],'b')
    plt.scatter(currentX-1.334, 1.5, s=10, color='blue')
    plt.scatter(currentX-2.667, 1.5, s=10, color='blue')
    
def drawThStart(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    plt.scatter(currentX-0.667, 1.5, s=10, color='blue')
    plt.scatter(currentX-1.334, 1.5, s=10, color='blue')
    plt.scatter(currentX-1, 2, s=10, color='blue')
    
def drawThEnd(currentX):
    plt.plot([currentX, currentX], [0,1],'b')
    plt.plot([currentX, currentX-4], [0,0],'b')
    plt.plot([currentX-4, currentX-4], [0,1],'b')
    plt.scatter(currentX-1.334, 1.5, s=10, color='blue')
    plt.scatter(currentX-2.667, 1.5, s=10, color='blue')
    plt.scatter(currentX-2, 2.2, s=10, color='blue')
    
def drawR(currentX):
    ctr =np.array( [(currentX, 1), (currentX, -2),(currentX - 0.5, -2),(currentX-1,-2),])
    x=ctr[:,0]
    y=ctr[:,1]

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])
    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.plot(out[0],out[1],'b')
    
def drawZ(currentX):
    ctr =np.array( [(currentX, 1), (currentX, -2),(currentX - 0.5, -2),(currentX-1,-2),])
    x=ctr[:,0]
    y=ctr[:,1]

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])
    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.scatter(currentX, 2, s=10, color='blue')
    plt.plot(out[0],out[1],'b')
    
def drawW(currentX):
    ctr =np.array( [(currentX,0),(currentX-1,0),(currentX-1,2.5),(currentX, 0.5), (currentX, -2),(currentX-1, -2),])
    x=ctr[:,0]
    y=ctr[:,1]

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])
    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.plot(out[0],out[1],'b')
    
def drawD(currentX):
    ctr =np.array( [(currentX-1,1.2),(currentX, 0.5), (currentX,0.3),(currentX, 0),])
    x=ctr[:,0]
    y=ctr[:,1]

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])
    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.plot(out[0],out[1],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    
def drawDh(currentX):
    ctr =np.array( [(currentX-1,1.2),(currentX, 0.5), (currentX,0.3),(currentX, 0),])
    x=ctr[:,0]
    y=ctr[:,1]

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])
    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
    out = interpolate.splev(u3,tck)
    plt.plot(out[0],out[1],'b')
    plt.plot([currentX, currentX-2], [0,0],'b')
    plt.scatter(currentX-1.2, 2, s=10, color='blue')

w = 'زوار'

currentX = 0
for i,c in enumerate(w):
    if(c == 'ا'):
        if(w[i-1] == 'ل'):
            drawAAfterL(currentX) 
        else:
            drawA(currentX)
        currentX -= 1
        continue
    
    if(c == 'ب'):
        if(i==len(w)-1):
            drawBEnd(currentX)
            currentX -= 2
        
        elif(i<len(w)-1):
            drawBStart(currentX)
            currentX -= 2
        continue
        
    if(c == 'ت'):               
        if(i==len(w)-1):
            drawTEnd(currentX)
            currentX -= 2
        
        elif(i<len(w)-1):
            drawTStart(currentX)
            currentX -= 2
        continue
    
    if(c == 'ث'):             
        if(i==len(w)-1):
            drawThEnd(currentX)
            currentX -= 2
        
        elif(i<len(w)-1):
            drawThStart(currentX)
            currentX -= 2
        continue
    
    if(c == 'ل'):
        if(i==len(w)-1):
            drawLEnd(currentX)
            currentX -= 2
        
        elif(i<len(w)-1):
            drawLStart(currentX)
            currentX -= 2
        continue
        
    if(c == 'ذ'):
        drawDh(currentX)
        currentX -= 3
        continue
    
    if(c == 'د'):
        drawD(currentX)
        currentX -= 3
        continue
        
    if(c == 'ر'):
        drawR(currentX)
        currentX -= 1
        continue
        
    if(c == 'ز'):
        drawZ(currentX)
        currentX -= 1
        continue
    
    if(c == 'و'):
        drawW(currentX)
        currentX -= 2
        continue
        
    print(c, 'is not handled')
    print('Only the following letters are handled: و ز ر د ذ ب ت ث ا ل')
    break
        
# plt.axis([-40,1,-3,20])
plt.axis([-40,5,-6,20])
plt.show()