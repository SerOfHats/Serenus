# Tempo Mapping Algorithm
import numpy as np
from numpy import array
import matplotlib.pyplot as plot

# Get x values of the sine wave

#time = np.arange(0, 10, 0.1);

# Amplitude of the sine wave is sine of a variable like time

#amplitude = np.sin(time)

# Plot a sine wave using time and amplitude obtained for the sine wave

#plot.plot(amplitude, time)

# Give a title for the sine wave plot

#plot.title('Sine wave')

# Give x axis label for the sine wave plot

#plot.xlabel('Time')

# Give y axis label for the sine wave plot

#plot.ylabel('Amplitude = sin(time)')

#plot.grid(False, which='both')

#plot.axhline(y=0, color='k')

#plot.show()

# Display the sine wave

##plot.show()
def tempoMapping(list):
    # Generate a standard list (of 100 values) for our x-axis

    xValues = array(np.arange(0, len(list)));
    yValues = [];
    # For each value of the input we have, plot a y-val from the list of generic x-vals we have to make a standard Sine
    # Curve, then multiply this y-val by by the input list to transform the amplitude
    for val in range(0,len(list)):
        yValues.append((list[val] * np.sin(xValues[val])))

    #Make the y-val list into a numpy array
    numpyY = array(yValues)

    #Test
    print(numpyY)
    print(xValues)

    plot.plot(yValues, xValues)
    plot.show()

    return numpyY,xValues


a = [218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375, 218.6312255859375,
     124.63524627685547, 124.63524627685547, 84.00457763671875, 84.00457763671875, 84.02559661865234, 84.02559661865234,
     99.22999572753906, 99.22999572753906, 99.22999572753906, 143.71060180664062, 143.71060180664062, 143.71060180664062,
     143.4640655517578, 143.4640655517578, 143.4640655517578, 136.1667022705078, 136.1667022705078, 136.1667022705078,
     135.6464080810547, 135.6464080810547, 135.6464080810547, 99.05933380126953, 99.05933380126953, 207.430419921875,
     207.430419921875, 207.430419921875, 207.430419921875, 207.430419921875, 153.20779418945312, 153.20779418945312,
     153.20779418945312, 153.20779418945312, 152.39468383789062, 152.39468383789062, 152.39468383789062, 152.82662963867188,
     152.82662963867188, 152.82662963867188, 152.82662963867188, 129.05523681640625, 129.05523681640625, 129.05523681640625,
     140.84901428222656, 140.84901428222656, 140.84901428222656, 123.16157531738281, 123.16157531738281, 123.16157531738281,
     123.51661682128906, 123.51661682128906, 123.51661682128906, 123.36471557617188, 123.36471557617188, 123.36471557617188,
     125.81694030761719, 125.81694030761719, 125.81694030761719, 122.69566345214844, 122.69566345214844, 122.69566345214844,
     122.69566345214844, 124.37157440185547, 124.37157440185547, 124.37157440185547, 165.61009216308594, 165.61009216308594,
     165.61009216308594, 165.61009216308594, 166.16798400878906, 166.16798400878906, 166.16798400878906, 166.16798400878906,
     167.66539001464844, 167.66539001464844, 167.66539001464844, 167.66539001464844, 169.45013427734375, 169.45013427734375,
     169.45013427734375, 169.45013427734375, 171.06520080566406, 171.06520080566406, 171.06520080566406, 171.06520080566406,
     168.87319946289062, 168.87319946289062, 168.87319946289062, 171.30950927734375, 171.30950927734375, 171.30950927734375,
     171.30950927734375, 171.30950927734375, 167.40208435058594, 167.40208435058594, 167.40208435058594, 173.67913818359375,
     173.67913818359375, 173.67913818359375, 173.67913818359375, 174.0574951171875,174.0574951171875, 174.0574951171875,
     174.0574951171875, 172.56285095214844, 172.56285095214844, 172.56285095214844, 172.56285095214844, 171.64547729492188,
     171.64547729492188, 171.64547729492188, 171.64547729492188, 171.49069213867188, 171.49069213867188, 171.49069213867188,
     171.49069213867188, 166.62686157226562, 166.62686157226562, 166.62686157226562, 166.62686157226562, 166.62686157226562,
     165.283447265625, 165.283447265625, 165.283447265625, 165.283447265625, 168.43714904785156, 168.43714904785156,
     168.43714904785156, 168.43714904785156, 169.86395263671875, 169.86395263671875, 169.86395263671875, 169.86395263671875,
     168.99830627441406, 168.99830627441406, 168.99830627441406, 168.99830627441406, 169.09254455566406, 169.09254455566406,
     169.09254455566406, 169.09254455566406, 165.67347717285156, 165.67347717285156, 165.67347717285156, 165.67347717285156,
     167.0813446044922, 167.0813446044922, 167.0813446044922, 167.0813446044922, 167.90858459472656, 167.90858459472656,
     167.90858459472656, 167.90858459472656, 167.62318420410156, 167.62318420410156, 167.62318420410156, 167.62318420410156,
     168.48629760742188, 168.48629760742188, 168.48629760742188, 168.48629760742188, 94.85501861572266, 94.85501861572266,
     96.76336669921875, 96.76336669921875, 97.23727416992188, 97.23727416992188, 97.23727416992188, 97.22908020019531,
     97.22908020019531, 97.3634033203125, 97.3634033203125, 97.3634033203125, 97.33203887939453, 97.33203887939453,
     96.41535949707031, 96.41535949707031, 96.41535949707031, 96.54424285888672, 96.54424285888672, 96.58293914794922,
     96.58293914794922, 96.58293914794922, 144.9617156982422, 144.9617156982422, 144.9617156982422, 147.62582397460938,
     147.62582397460938, 147.62582397460938, 147.290771484375, 147.290771484375, 147.290771484375, 147.290771484375,
     147.0087890625, 147.0087890625, 147.0087890625, 147.0087890625, 147.37588500976562, 147.37588500976562,
     147.37588500976562, 147.01918029785156, 147.01918029785156, 147.01918029785156, 147.01918029785156,
     146.81582641601562, 146.81582641601562, 146.81582641601562, 145.2208251953125, 145.2208251953125, 145.2208251953125,
     145.2208251953125, 147.05096435546875, 147.05096435546875, 147.05096435546875, 147.05096435546875, 147.84063720703125,
     147.84063720703125, 147.84063720703125, 148.2267608642578, 148.2267608642578, 148.2267608642578, 148.2267608642578,
     147.85159301757812, 147.85159301757812, 147.85159301757812, 147.85159301757812, 147.7698211669922, 147.7698211669922,
     147.7698211669922, 147.4141082763672, 147.4141082763672, 147.4141082763672, 147.4141082763672, 145.63356018066406,
     145.63356018066406, 145.63356018066406, 146.14230346679688, 146.14230346679688, 146.14230346679688, 146.14230346679688,
     144.18504333496094, 144.18504333496094, 144.18504333496094, 144.18504333496094, 140.97206115722656, 140.97206115722656,
     140.97206115722656, 141.35560607910156, 141.35560607910156, 141.35560607910156,
     141.35560607910156, 141.44192504882812, 141.44192504882812, 141.44192504882812, 146.92784118652344, 146.92784118652344,
     146.92784118652344, 146.92784118652344]

tempoMapping(a);



