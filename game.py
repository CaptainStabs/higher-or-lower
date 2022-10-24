import json
import random
from scripts import sine
import pyaudio # NOt used here but pyinstaller was ignoring it as a req


volume = 1  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 2.0  # in seconds, may be float

# Note names and their frequencies
notes = json.load(open("./scripts/notes.json", "r"))
note_names = list(notes)

note_dif = ["H", "L"]


lives = 3
level = 1
diff_tracker = 50 # Difficulty number
while lives > 0:
    # diff = random.uniform((diff_tracker/level*0.01)/100, (diff_tracker/level*0.92)/100)
    diff = random.uniform((diff_tracker/level*0.5)/100*25, (diff_tracker/level*0.92)/100*50) # Difficulty
    # if level < 3:
    #     diff = diff * 100

    for i in range(5):
        h_or_l = random.choice(note_dif)              # Choose whether to make the note higher or lower
        chosen_note_name = random.choice(note_names)  # Choose the note
        chosen_note_freq = notes[chosen_note_name]    # Get the frequency of the chosen note
        
        if h_or_l == "H": # Get the new note frequency from sum/difference 
            freq = float("{:6f}".format(chosen_note_freq + diff))
        
        else:
            freq = float("{:6f}".format(chosen_note_freq - diff))

        # Play the notes
        sine(volume, fs, duration, chosen_note_freq)
        sine(volume, fs, duration, freq)
        

        user_choice = input("\nH or L?: ").upper().strip()

        if user_choice == h_or_l:
            print(f"Correct, the note was {chosen_note_name}")
        else:
            print(f"Incorrect. The note was {h_or_l}")
            lives -= 1
            print(f"You have {lives} lives left")
        if not lives:
            break
    if not lives:
        break
    level += 1
    print(f"\nLevel {level}:")
print(f"\nYou made it to level {level}!")

            