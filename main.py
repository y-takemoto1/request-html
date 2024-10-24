from requests_html import HTMLSession
import streamlit as st
st.title('request-htmlのテスト')
session = HTMLSession()
r = session.get('https://www.staff-q.co.jp/')
r.html.render()
st.text(r)
