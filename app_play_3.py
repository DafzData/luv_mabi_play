import streamlit as st
import base64

st.markdown("<h1 style='text-align: center;'>❤️</h1>", unsafe_allow_html=True)

try:
    with open("yung_kai__blue.mp3", "rb") as f:
        audio_bytes = f.read()

    b64 = base64.b64encode(audio_bytes).decode()  # Encode to base64

    st.components.v1.html(f"""
    <audio id="audioPlayer" src="data:audio/mpeg;base64,{b64}" loop preload="auto"></audio>
    <script>
        var audio = document.getElementById('audioPlayer');
        audio.autoplay = true;  // Autoplay attempt
        audio.addEventListener('error', function(error) {{
            console.error('Audio playback error:', error);
        }});
    </script>
    """, height=1)

except FileNotFoundError:
    st.error("MP3 file not found. Make sure 'yung_kai__blue.mp3' is in the same directory.")
except Exception as e:
    st.error(f"An error occurred: {e}")