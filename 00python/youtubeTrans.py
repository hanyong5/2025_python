
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

st.title("Youtube 자막 요약")

video_id = st.text_input("Youtube 영상 ID를 입력하세요")

def extract_transcript(url):
    import re
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None


if st.button("요약하기"):
    video_id = extract_transcript(video_id)
    st.write(video_id)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko', 'en'])
            st.success("대본 추출 완료")
            full_text = "\n".join([t['text'] for t in transcript])
            st.text_area("대본", value=full_text, height=400)
        except Exception as e:
            st.error(f"대본을 추출할 수 없습니다: {e}")
    else:
        st.error("URL에서 영상 ID를 찾을 수 없습니다.")







