from gtts import gTTS
from io import BytesIO

st.title("🔊 Pronunciation Practice")

word = st.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp.getvalue(), format="audio/mp3")
