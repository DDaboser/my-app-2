import streamlit as st

st.title("Grade Calculator")

# Create a text box for the user to enter their grade
grade_input = st.text_input("Enter your grade:")

# Check if the user has typed something before running the logic
if grade_input:
    try:
        # Convert the input string into a number
        grade = int(grade_input)

        # Your original conditional logic
        if grade > 90:
            st.success("You got an A PLUS!")
        elif grade > 80:
            st.info("You got a B.")
        elif grade > 70:
            st.warning("You got a C.")
        elif grade > 60:
            st.warning("You got a D.")
        else:
            st.error("You got an F.")
            
    except ValueError:
        st.error("Please enter a valid number.")
