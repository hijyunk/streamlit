import streamlit as st
from PIL import Image

# ---------- 사이드 바 화면 구성 ----------
st.sidebar.title('Side Bar')
st.sidebar.header('텍스트 입력 사용 예')
user_id = st.sidebar.text_input('아이디(ID) 입력', value='streamlit', max_chars=15)
user_pw = st.sidebar.text_input('비밀번호(PW) 입력', value='abcd', type='password')

st.sidebar.header('셀렉트 박스 사용 예')
selectbox_options = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectbox_options, index=3)
st.sidebar.write('**당신의 선택** : ', your_option)


# ---------- 메인(Main) 바 화면 구성 ----------

image_files = ['https://github.com/hijyunk/streamlit/blob/main/sidebar/data/Vermeer.png?raw=true', 
               'https://github.com/hijyunk/streamlit/blob/main/sidebar/data/Gogh.png?raw=true', 
               'https://github.com/hijyunk/streamlit/blob/main/sidebar/data/Munch.png?raw=true', 
               'https://github.com/hijyunk/streamlit/blob/main/sidebar/data/ShinYoonbok.png?raw=true']

selectbox_options_index = selectbox_options.index(your_option)
image_file = image_files[selectbox_options_index]
st.image(image_file, caption=your_option)