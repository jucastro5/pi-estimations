import numpy as np
import matplotlib.pyplot as plt

def classical(iterations, noprint=False):
    if noprint==False: print("plotting {} points!".format(iterations))
    # circle radius
    radius = 1
    # accuracy of selecting random points
    accuracy = .0001
    count = 0
    t2x = []
    t2y = []
    position = 0
    #plotting config
    table = plt.figure(figsize=(20,20))
    t1 = table.add_subplot(2,2,1)
    t2 = table.add_subplot(2,1,2)
    plt.subplots_adjust(wspace=.2, hspace=.2)
    #visual circle
    circle = plt.Circle((0, 0), radius, color= 'green', alpha=.2)
    t1.add_artist(circle)
    t1.set_xlim([0,1])
    t1.set_ylim([0,1])
    t2.set_ylim([np.pi-1, np.pi+1])
    t2.set_xlim([0, iterations])
    t1.set_title\
    ('Points (Red = Outside, Blue = Inside, Green = Circle w/ radius {})'\
    .format(radius))
    t2.set_title('\u03C0 Estimate Over Iterations (\u03C0 = Red Line)')
    #pi reference line
    t2.axhline(y=np.pi, color='r', linestyle='-')
    #creating points
    for i in range(iterations):
        x = np.random.choice(np.arange(0, 1, accuracy))
        y = np.random.choice(np.arange(0, 1, accuracy))
        #distance formula. is distance from 0,0 greater than radius (1)?
        #(outside circle)
        #outside = red
        if np.sqrt(x**2 + y**2) >= 1:
            t1.scatter(x, y, color = 'red', s=10)
            t2x.append(i)
            #avoid /0
            if i != 0:
                t2y.append(count/i*4)
            else:
                t2y.append(0)
        #inside = blue
        else:
            t1.scatter(x, y, color = 'blue', s=10)
            count +=1
            t2x.append(i)
            #avoid /0
            if i != 0:
                t2y.append(count/i*4)
            else:
                t2y.append(0)
    t2.plot(t2x, t2y)
    plt.savefig('n={}_classical.png'.format(iterations))
    #printing info
    if iterations > 0 and noprint == False:
        print('_______________________________________________\n')
        print('Total Points: {}'.format(iterations))
        print('Points inside: {}'.format(count))
        print('\u03C0 approximation (total points/points inside)*4:\n{}'\
        .format(count/iterations*4))
        print('Graph saved in local directory')
        print('_______________________________________________')

x = int(input('num iterations? '))
classical(x)
