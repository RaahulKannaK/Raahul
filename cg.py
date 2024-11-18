import streamlit as ra
import random
from PIL import Image

def guess():
    g = random.randint(1, 100)
    image = Image.open(r'C:\Users\raahu\Downloads\guess2.png')
    image1 = Image.open(r'C:\Users\raahu\Downloads\guess4.png')
    c1,c2 = ra.columns(2)
    with c1:
        ra.image(image, caption="Range of 1 to 100", width=350)
    with c2:
        ra.image(image1, caption="Computer Guessing",  width=350)
    attempts = 0
    ra.header("Guessing Game By Computer")
    ra.write("Guess a Number between the Range of 1 and 100.")


    with ra.form("guessing_form"):
        u = ra.number_input("What is the Number you give for Computer?", min_value=1, max_value=100)
        submit_button = ra.form_submit_button(label='Submit')

        if submit_button:
            
            difference = abs(g - u)
            

            if u == g:
                ra.success(f"Congratulations! You Guessed the Correct Number with {attempts} attempts.")
            elif difference <= 10 or difference < 5:
                ra.write("Computer Guess is",g)
                ra.write("That’s almost it, just a little more")
            elif u < g:
                ra.write("Computer Guess is",g)
                ra.write("It is High So, try a bit lower.")
            else:
                ra.write("Computer Guess is",g)
                ra.write("It is Low So, try a bit higher")

def title():
    ra.title("Guessing Game PLatform 🤔")
    guess()

if __name__ == "__main__":
    title()
