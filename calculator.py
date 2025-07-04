import streamlit as st


def main():
    st.set_page_config(page_title="Python Streamlit Calculator", page_icon="🧮")
    st.title("🧮 Calculator using Streamlit")
    st.write("Made by Your Name")

    # User input numbers
    num1 = st.number_input("Enter first number", format="%.4f")
    num2 = st.number_input("Enter second number", format="%.4f")

    # Select operation
    operation = st.selectbox(
        "Select operation",
        ("Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Power")
    )

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")

        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")

        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"Result: {num1} × {num2} = {result}")

        elif operation == "Division":
            if num2 == 0:
                st.error("Error! Division by zero.")
            else:
                result = num1 / num2
                st.success(f"Result: {num1} ÷ {num2} = {result}")

        elif operation == "Modulus":
            if num2 == 0:
                st.error("Error! Division by zero in modulus.")
            else:
                result = num1 % num2
                st.success(f"Result: {num1} % {num2} = {result}")

        elif operation == "Power":
            result = num1 ** num2
            st.success(f"Result: {num1} ^ {num2} = {result}")

if __name__ == "__main__":
    main()