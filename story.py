# adventure_app.py
import streamlit as st

st.title("🌩️ Choose Your Own Adventure")

st.write("The day started off great—clear skies and a warm breeze. A perfect day for a walk.")
st.write("As you were on your walk, the wind started to pick up and the skies turned grey...")

# First choice
choice1 = st.radio("The weather's starting to make you nervous. What do you do?", 
                   ("Choose an option", "Continue walking", "Wait out the storm"))

if choice1 == "Wait out the storm":
    choice2 = st.radio("You run over to a nearby shack. Do you:", 
                       ("Choose an option", "Go into the shack", "Wait under the tree"))

    if choice2 == "Wait under the tree":
        st.success("🌳 Good idea! You waited out the storm and can now return home safe. The end!")
    elif choice2 == "Go into the shack":
        st.error("🧙‍♀️ Bad choice! You were trapped by an evil witch. You never made it back home. The end!")

elif choice1 == "Continue walking":
    st.error("⚡ Bad choice! You got struck by lightning and never made it back home. The end!")

# Optional footer
st.markdown("---")
st.caption("Created by Arianna Hicks - 10/11/24")
