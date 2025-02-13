import streamlit as st

def play_youtube_audio_interval(youtube_url, start_time_seconds, end_time_seconds):
    """Plays YouTube audio at a specific interval repeatedly (internal, robust)."""

    def get_youtube_id(url):
        from urllib.parse import urlparse, parse_qs
        parsed_url = urlparse(url)
        if parsed_url.netloc == "youtu.be":
            return parsed_url.path[1:]
        elif parsed_url.netloc in ("www.youtube.com", "m.youtube.com"):
            query_params = parse_qs(parsed_url.query)
            if "v" in query_params:
                return query_params["v"][0]
        return None

    video_id = get_youtube_id(youtube_url)

    if video_id:
        st.components.v1.html(f"""
        <div id="player"></div>
        <script>
            var tag = document.createElement('script');
            tag.src = "https://www.youtube.com/iframe_api";
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

            var player;
            var startTime = {start_time_seconds};
            var endTime = {end_time_seconds};
            var intervalId;

            function onYouTubeIframeAPIReady() {{
                player = new YT.Player('player', {{
                    height: '1',
                    width: '1',
                    videoId: '{video_id}',
                    playerVars: {{
                        'autoplay': 1,
                        'mute': 0,
                        'playsinline': 1,
                        'start': startTime
                    }},
                    events: {{
                        'onReady': onPlayerReady
                    }}
                }});
            }}

            function onPlayerReady(event) {{
                event.target.playVideo();
                intervalId = setInterval(function() {{
                    player.seekTo(startTime);
                    player.playVideo();
                }}, (endTime - startTime) * 1000);
            }}

            window.addEventListener('beforeunload', function () {{
                clearInterval(intervalId);
            }});

        </script>
        """, height=1)
    else:
        st.error("Invalid YouTube URL")


# Set URL and interval here (internal values)
youtube_url = "https://www.youtube.com/watch?v=IpFX2vq8HKw&ab_channel=yungkai"  # **REPLACE WITH YOUR YOUTUBE URL**
start_time_seconds = 48.0  # **REPLACE WITH YOUR START TIME (SECONDS)**
end_time_seconds = 77.4  # **REPLACE WITH YOUR END TIME (SECONDS)**

play_youtube_audio_interval(youtube_url, start_time_seconds, end_time_seconds)

st.markdown("""
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <div style="display: flex; align-items: center; justify-content: center;">
        <span style="font-size: 3em; margin-right: 0.5em;">🎵</span>
        <span style="font-size: 7em;">❤️</span>
        <span style="font-size: 3em; margin-left: 0.5em;">🎵</span> 
    </div>
    <div style="margin-left: 20px;">  <h2 style="text-align: left; font-size: 2em;">Abra o cartão, Mabi!</h2> </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
        <button onclick="window.location.reload();" style="border: none; background: none; padding: 0; cursor: pointer;">
            <span style="font-size: 2em;">▶️</span>  </button>
        <span style="text-align: center; margin-top: 0.5em;">Toque aqui se a música não iniciar</span>
    </div>
</div>
""", unsafe_allow_html=True)
