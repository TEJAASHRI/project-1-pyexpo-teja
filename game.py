import streamlit as st
import random

# Part 1: Portfolio
def portfolio():
    st.markdown("""
    <style>
    .header {
        font-size: 50px;
        color: #4CAF50;
        text-align: center;
    }
    .subheader {
        font-size: 30px;
        color: #f44336;
        text-align: center;
    }
    .section {
        padding: 10px;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">My Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Welcome to my portfolio! Here you\'ll find information about my projects, skills, and interests.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("Hi! I'm Tejaashri.K, a first year Artificial intelligence and Data Science Engineering student, with a passion for exploring and researching the technology behind the developing AI World.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Projects")
    st.write("- **Project 1**: Scientific Calculator.")
    st.write("- **Project 2**: Guessing game using Streamlit.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Skills and Abilities")
    st.write("Here are some of my skills and abilities:")
    st.write("- I can converse in english fluently.")
    st.write("- I can research new ideas through prompting by using the advanced developing AI tools.")
    st.write("- I can grasp the concepts of new technologies by practically working on hands on projects.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.header("Interests")
    st.write("I would like to build my career as an Prompt AI Engineer.")
    st.write("Further more I am deeply fascinated towards the Domain of Data Science and its related studies and analysis too.")
    st.markdown('</div>', unsafe_allow_html=True)

# Part 2: Guessing Game
def guessing_game():
    st.title("Guessing Game")
    mode = st.selectbox("Choose Game Mode", ["User Guessing", "Machine Guessing"])
    if mode == "User Guessing":
        user_guessing_game()
    else:
        machine_guessing_game()

def user_guessing_game():
    st.header("User Guessing Game")
    st.write("Try to guess the number I'm thinking of between 1 and 100!")
    number = random.randint(1, 100)
    if "user_guess" not in st.session_state:
        st.session_state.user_guess = None
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == number:
            st.success(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        elif guess < number:
            st.warning("Try a higher number.")
        else:
            st.warning("Try a lower number.")
    if st.button("Play Again"):
        st.session_state.user_guess = None
        st.session_state.attempts = 0
        st.experimental_rerun()

def machine_guessing_game():
    st.header("Machine Guessing Game")
    st.write("Think of a number between 1 and 100 and the machine will try to guess it!")
    if "lower_bound" not in st.session_state:
        st.session_state.lower_bound = 1
    if "upper_bound" not in st.session_state:
        st.session_state.upper_bound = 100
    if "machine_guess" not in st.session_state:
        st.session_state.machine_guess = None
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if st.button("Make a Guess"):
        st.session_state.attempts += 1
        mid = (st.session_state.lower_bound + st.session_state.upper_bound) // 2
        st.session_state.machine_guess = mid
        st.write(f"Is your number {mid}?")
        feedback = st.radio("Select Feedback", ["Correct", "Higher", "Lower"])
        if feedback == "Correct":
            st.success(f"The machine guessed your number in {st.session_state.attempts} attempts!")
        elif feedback == "Higher":
            st.session_state.lower_bound = mid + 1
        else:
            st.session_state.upper_bound = mid - 1
    if st.button("Play Again"):
        st.session_state.lower_bound = 1
        st.session_state.upper_bound = 100
        st.session_state.machine_guess = None
        st.session_state.attempts = 0
        st.experimental_rerun()

# Main Application
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Portfolio", "Guessing Game"])
    if selection == "Portfolio":
        portfolio()
    else:
        guessing_game()

if __name__ == "__main__":
    main()
