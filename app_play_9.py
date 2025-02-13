import streamlit as st

def play_youtube_audio_interval(youtube_url, start_time_seconds, end_time_seconds):
    """Plays YouTube audio at a specific interval repeatedly (internal, robust)."""

    def get_youtube_id(url):  # Helper function to extract video ID
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
            var intervalId; // Store the interval ID

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
                // Start the interval loop
                intervalId = setInterval(function() {{
                    player.seekTo(startTime);
                    player.playVideo();
                }}, (endTime - startTime) * 1000); // Interval in milliseconds
            }}

            // Clear the interval when the component is unmounted (important!)
            window.addEventListener('beforeunload', function () {{
                clearInterval(intervalId);
            }});

        </script>
        """, height=1)
    else:
        st.error("Invalid YouTube URL")


# Set URL and interval here (internal values)
youtube_url = "https://www.youtube.com/watch?v=IpFX2vq8HKw&ab_channel=yungkai"  # Replace with your URL
start_time_seconds = 48  # 0:48 in seconds
end_time_seconds = 77.4  # 1:17 in seconds

play_youtube_audio_interval(youtube_url, start_time_seconds, end_time_seconds)

st.markdown("<h1 style='text-align: center; font-size: 5em;'>❤️</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Abra o cartão, Mabi.</h2>", unsafe_allow_html=True)