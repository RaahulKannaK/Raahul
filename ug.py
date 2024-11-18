import streamlit as ra
import random
from PIL import Image

def guess():
    g = random.randint(1, 100)
    image = Image.open(r'C:\Users\raahu\Downloads\guess2.png')
    image1 = Image.open(r'C:\Users\raahu\Downloads\guess.png')
    c1,c2 = ra.columns(2)
    with c1:
        ra.image(image, caption="Range of 1 to 100", width=350)
    with c2:
        ra.image(image1, caption="User Guessing",  width=350)

    ra.header("Guessing Game by Computer")
    ra.write("The Computer Guess",g)
    ra.write("Guess a Number between the Range of 1 and 100.")

    with ra.form("guessing_form"):
        u = ra.number_input("What Is your Guess? Enter Below!:", min_value=1, max_value=100)
        con = ra.form_submit_button(label='Confirm')

        if con:
            
            diff = abs(g - u)
            

            if u == g:
                ra.success("Congratulations! You got the correct Guess.")
                ra.write(diff)
            elif diff <= 10 or diff < 5:
                ra.write("That's almost it, just a little more")
                ra.write("Difference Between your Guess and Computer Guess",diff)

            elif u < g:
                ra.write("It is Lower So, try a bit higher.")
                ra.write("Difference Between your Guess and Computer Guess",diff)
            else:
                ra.write("It is Higher So, try a bit Lower")
                ra.write("Difference Between your Guess and Computer Guess",diff)

def T():
    ra.title("Guessing Game PLatform 🤔")
    guess()
if __name__ == "__main__":
    T()
