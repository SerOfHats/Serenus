import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import get_data as aub
import pyaudio, wave
import atexit
import random
# Fixing random state for reproducibility
np.random.seed(19680801)

# Variable to control the pitch up and down
yPitch = aub.get_pitch("/storage/Media/Music/80s.wav")
yPitchIndex = 1

print(yPitch)

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Create rain data
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4)])

# Initialize the raindrops in random positions and with
# random growth rates.
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors='none',
                  facecolors=rain_drops['color'])


def update(frame_number):
    b = [218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375, 124.63524627685547, 124.63524627685547, 84.00457763671875, 84.00457763671875, 84.02559661865234, 84.02559661865234, 99.22999572753906, 99.22999572753906, 99.22999572753906, 143.71060180664062, 143.71060180664062, 143.71060180664062, 143.4640655517578, 143.4640655517578, 143.4640655517578, 136.1667022705078, 136.1667022705078, 136.1667022705078, 135.6464080810547, 135.6464080810547, 135.6464080810547, 99.05933380126953, 99.05933380126953, 207.430419921875, 207.430419921875, 207.430419921875, 207.430419921875, 207.430419921875, 153.20779418945312, 153.20779418945312, 153.20779418945312, 153.20779418945312, 152.39468383789062, 152.39468383789062, 152.39468383789062, 152.82662963867188, 152.82662963867188, 152.82662963867188, 152.82662963867188, 129.05523681640625, 129.05523681640625, 129.05523681640625, 140.84901428222656, 140.84901428222656, 140.84901428222656, 123.16157531738281, 123.16157531738281, 123.16157531738281, 123.51661682128906, 123.51661682128906, 123.51661682128906, 123.36471557617188, 123.36471557617188, 123.36471557617188, 125.81694030761719, 125.81694030761719, 125.81694030761719, 122.69566345214844, 122.69566345214844, 122.69566345214844, 122.69566345214844, 124.37157440185547, 124.37157440185547, 124.37157440185547, 165.61009216308594, 165.61009216308594, 165.61009216308594, 165.61009216308594, 166.16798400878906, 166.16798400878906, 166.16798400878906, 166.16798400878906, 167.66539001464844, 167.66539001464844, 167.66539001464844, 167.66539001464844, 169.45013427734375, 169.45013427734375, 169.45013427734375, 169.45013427734375, 171.06520080566406, 171.06520080566406, 171.06520080566406, 171.06520080566406, 168.87319946289062, 168.87319946289062, 168.87319946289062, 171.30950927734375, 171.30950927734375, 171.30950927734375, 171.30950927734375, 171.30950927734375, 167.40208435058594, 167.40208435058594, 167.40208435058594, 173.67913818359375, 173.67913818359375, 173.67913818359375, 173.67913818359375, 174.0574951171875,174.0574951171875, 174.0574951171875, 174.0574951171875, 172.56285095214844, 172.56285095214844, 172.56285095214844, 172.56285095214844, 171.64547729492188, 171.64547729492188, 171.64547729492188, 171.64547729492188, 171.49069213867188, 171.49069213867188, 171.49069213867188, 171.49069213867188, 166.62686157226562, 166.62686157226562, 166.62686157226562, 166.62686157226562, 166.62686157226562, 165.283447265625, 165.283447265625, 165.283447265625, 165.283447265625, 168.43714904785156, 168.43714904785156, 168.43714904785156, 168.43714904785156, 169.86395263671875, 169.86395263671875, 169.86395263671875, 169.86395263671875, 168.99830627441406, 168.99830627441406, 168.99830627441406, 168.99830627441406, 169.09254455566406, 169.09254455566406, 169.09254455566406, 169.09254455566406, 165.67347717285156, 165.67347717285156, 165.67347717285156, 165.67347717285156, 167.0813446044922, 167.0813446044922, 167.0813446044922, 167.0813446044922, 167.90858459472656, 167.90858459472656, 167.90858459472656, 167.90858459472656, 167.62318420410156, 167.62318420410156, 167.62318420410156, 167.62318420410156, 168.48629760742188, 168.48629760742188, 168.48629760742188, 168.48629760742188, 94.85501861572266, 94.85501861572266, 96.76336669921875, 96.76336669921875, 97.23727416992188, 97.23727416992188, 97.23727416992188, 97.22908020019531, 97.22908020019531, 97.3634033203125, 97.3634033203125, 97.3634033203125, 97.33203887939453, 97.33203887939453, 96.41535949707031, 96.41535949707031, 96.41535949707031, 96.54424285888672, 96.54424285888672, 96.58293914794922, 96.58293914794922, 96.58293914794922, 144.9617156982422, 144.9617156982422, 144.9617156982422, 147.62582397460938, 147.62582397460938, 147.62582397460938, 147.290771484375, 147.290771484375, 147.290771484375, 147.290771484375, 147.0087890625, 147.0087890625, 147.0087890625, 147.0087890625, 147.37588500976562, 147.37588500976562, 147.37588500976562, 147.01918029785156, 147.01918029785156, 147.01918029785156, 147.01918029785156, 146.81582641601562, 146.81582641601562, 146.81582641601562, 145.2208251953125, 145.2208251953125, 145.2208251953125, 145.2208251953125, 147.05096435546875, 147.05096435546875, 147.05096435546875, 147.05096435546875, 147.84063720703125, 147.84063720703125, 147.84063720703125, 148.2267608642578, 148.2267608642578, 148.2267608642578, 148.2267608642578, 147.85159301757812, 147.85159301757812, 147.85159301757812, 147.85159301757812, 147.7698211669922, 147.7698211669922, 147.7698211669922, 147.4141082763672, 147.4141082763672, 147.4141082763672, 147.4141082763672, 145.63356018066406, 145.63356018066406, 145.63356018066406, 146.14230346679688, 146.14230346679688, 146.14230346679688, 146.14230346679688, 144.18504333496094, 144.18504333496094, 144.18504333496094, 144.18504333496094, 140.97206115722656, 140.97206115722656, 140.97206115722656, 141.35560607910156, 141.35560607910156, 141.35560607910156, 141.35560607910156, 141.44192504882812, 141.44192504882812, 141.44192504882812, 146.92784118652344, 146.92784118652344, 146.92784118652344, 146.92784118652344]

    interval = 10
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    global yPitchIndex
    if (yPitchIndex >= len(yPitch)-1):
        yPitchIndex = 1
    else:
        yPitchIndex += 1
    a= np.array(yPitch)
    def scale(list,ele):
        
            return((list[ele-1] - min(list))/ (max(list) - min(list)))

    r = scale(b, yPitchIndex) 
    g = scale(b, yPitchIndex)
    b = scale(b, yPitchIndex)#yPitch[int(yPitchIndex)]/50.0
    #g = yPitch[int(yPitchIndex)]/100.0
    #b = yPitch[int(yPitchIndex)]/100.0
    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    print(r,g, b)
    rain_drops['position'][current_index, 0] = np.random.uniform(0, 1, 1)
    rain_drops['position'][current_index, 1] = np.random.uniform(0.4+yPitch[yPitchIndex-1]-yPitch[yPitchIndex], 0.6+yPitch[yPitchIndex-1]-yPitch[yPitchIndex], 1)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (r, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_facecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])

def get_p(p):
    return p

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, update, interval=get_p(yPitch[1]))
plt.show()