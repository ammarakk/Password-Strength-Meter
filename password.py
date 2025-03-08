import streamlit as st
import pandas as pd

# Custom styling for a professional, modern UI
SPACE_THEME = """
<style>
    body {
        background-image: url('https://wallpapercave.com/wp/wp5028290.jpg');
        background-size: cover;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 20px;
    }
    .strength-bar {
        width: 100%;
        height: 15px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .very-weak { background-color: #ff4b4b; }
    .weak { background-color: #ff884b; }
    .moderate { background-color: #ffc107; }
    .strong { background-color: #4caf50; }
    .very-strong { background-color: #2196f3; }
    .guide-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        margin-top: 10px;
    }
    .white-text {
        color: white;
        font-size: 16px;
        font-weight: bold;
    }
</style>
"""

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\" for char in password)

    strength_score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6:
        return "Very Weak", 1, "very-weak"
    elif strength_score == 1:
        return "Weak", 2, "weak"
    elif strength_score == 2:
        return "Moderate", 3, "moderate"
    elif strength_score == 3:
        return "Strong", 4, "strong"
    else:
        return "Very Strong", 5, "very-strong"

# Streamlit UI
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    st.markdown(SPACE_THEME, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>🚀 Password Strength Meter</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: lightgray;'>Ensure your password is strong and secure</h4>", unsafe_allow_html=True)

    # White-colored label for password input
    st.markdown("<p class='white-text'>🔐 Enter your password:</p>", unsafe_allow_html=True)
    password = st.text_input("", type="password", label_visibility="collapsed")

    # Guide displayed below the password input box
    st.markdown("""
    <div class='guide-box'>
        <b>🔹 Password Strength Guide:</b>
        <ul>
            <li>Use at least 8 characters</li>
            <li>Include uppercase and lowercase letters</li>
            <li>Add numbers and special characters</li>
            <li>Avoid common words and personal information</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    if password:
        strength, score, css_class = check_password_strength(password)

        # Display strength level with progress bar
        st.markdown(f"<div class='strength-bar {css_class}' style='width: {score * 20}%;'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: white;'>{strength}</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
