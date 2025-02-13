import streamlit as st
import base64

# Larger heart and text
st.markdown("<h1 style='text-align: center; font-size: 5em;'>❤️</h1>", unsafe_allow_html=True)  # Increased font size
st.markdown("<h2 style='text-align: center;'>Abra o cartão, Mabi.</h2>", unsafe_allow_html=True) # Added text

try:
    with open("yungkaibluecut.mp3", "rb") as f:
        audio_bytes = f.read()

    b64 = base64.b64encode(audio_bytes).decode()

    st.components.v1.html(f"""
    <audio id="audioPlayer" src="data:audio/mpeg;base64,{b64}" loop preload="auto"></audio>
    <script>
        var audio = document.getElementById('audioPlayer');
        audio.autoplay = true;
        audio.addEventListener('error', function(error) {{
            console.error('Audio playback error:', error);
        }});
    </script>
    """, height=1)

except FileNotFoundError:
    st.error("MP3 file not found. Make sure 'yungkaibluecut.mp3' is in the same directory.")
except Exception as e:
    st.error(f"An error occurred: {e}")