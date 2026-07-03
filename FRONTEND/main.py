import streamlit as st

st.title(
    "MY APP, MY RULE"
)
st.markdown(
    """
<style>
.stApp{
  background-color:#605f9c;
}
<style>
""",unsafe_allow_html=True

)
st.write("This App is used for small kids")
if st.button("Click Me"):
 st.switch_page("pages/Apage.py")
