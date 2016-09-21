# TiltMusic by Alex "Chozabu" P-B. September 2016.
#
# Tilt Y to change Pitch
# press A or B to change note length, and turn sound on or off
#
# A quick demo can be found at https://youtu.be/vvECQTDiWxQ
#
# This program has been placed into the public domain.

from microbit import *
import music

#A selection of sharp notes
notes = [233.08, 277.18, 311.13, 369.99, 415.30,
466.16, 554.37, 622.25, 739.99, 830.61, 932.33,
1108.73, 1244.51, 1479.98, 1661.22, 1864.66,
2217.46, 2489.02, 2959.96, 3322.44, 3729.31,
4434.92, 4978.03, 5919.91, 6644.88, 7458.62]

#note lengths
note_durations = [
 0, 50, 100, 200, 400, 800
]
durationlen = len(note_durations)
notelen = len(notes)

duration_index = 2

duration = 100

play_music = True

while True:
    #get accelerometer readings
    xreading = abs(accelerometer.get_x())
    yreading = abs(accelerometer.get_y())
    
    #use a to toggle music
    if button_a.was_pressed():
        duration_index +=1
    if button_b.was_pressed() == 1:
        duration_index -=1
    duration_index = duration_index%durationlen
    duration = note_durations[duration_index]
    if not duration:
        continue
    
    #get a note based on tilt
    note = xreading*.01
    pitch = notes[int(note)%notelen]
    
    #if b is pressed, alter the length based on tilt
    
    #play our sound!
    music.pitch(int(pitch), duration)
        
