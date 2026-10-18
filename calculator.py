import streamlit as st

st.title("Interactive Calculator App")

# Get numbers and operation from the user via the webpage
num_1 = st.number_input("Enter the first number:", value=0.0)
num_2 = st.number_input("Enter the second number:", value=0.0)

# A dropdown is a great web alternative to typing the operation manually!
operation = st.selectbox("Enter the operation:", ("+", "-", "*", "/"))

# Add a button so the math only happens when the user clicks it
if st.button("Calculate"):
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        # We can use our new '!=' operator here to prevent dividing by zero!
        if num_2 != 0:
            result = num_1 / num_2
        else:
            result = "Error: Cannot divide by zero!"
    else:
        result = "Invalid operation"
        
    # Display the result on the screen for your users to see
    st.success(f"The result is: {result}")
