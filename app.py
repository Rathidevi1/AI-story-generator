import streamlit as st
from PIL import Image
from cv_module import analyze_image
from story_generator import generate_story

# 🌟 Page Config
st.set_page_config(
    page_title="🖼️➡️📖 Unified Story Generator",
    page_icon="📖",
    layout="centered"
)

# 🎨 Add custom background and styling
def add_custom_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f2f2f2;
            background-image: url("https://www.transparenttextures.com/patterns/white-wall-3.png");
            background-size: cover;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #6C63FF;
            text-align: center;
        }
        .subtitle {
            font-size: 18px;
            color: #444444;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_style()

# 📝 Title and description
st.markdown("<h1 class='title'>🖼️➡️📖 Unified Story Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload multiple images and let the AI craft a unified story out of them!</p>", unsafe_allow_html=True)

# 📂 File uploader
uploaded_files = st.file_uploader("📤 Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    if st.button("✨ Generate Combined Story"):
        all_objects = []

        for idx, uploaded_file in enumerate(uploaded_files):
            image = Image.open(uploaded_file)
            st.image(image, caption=f"🖼️ Image {idx+1}", use_column_width=True)

            with st.spinner(f"🔍 Analyzing Image {idx+1}..."):
                objects = analyze_image(image)
                all_objects.extend(objects)

        if all_objects:
            unique_objects = list(set(all_objects))  # Remove duplicates
            st.success(f"✅ Detected Objects: {', '.join(unique_objects)}")

            with st.spinner("🧠 Generating combined story..."):
                story = generate_story(unique_objects)

            st.markdown("### 📖✨ Your AI-Generated Story")
            st.markdown(f"<div style='background-color: #fff; padding: 15px; border-radius: 10px; border: 1px solid #ccc;'>{story}</div>", unsafe_allow_html=True)

            # 📥 Download button
            st.download_button("📥 Download Story", story, file_name="combined_story.txt")
        else:
            st.error("⚠️ No objects detected in any image.")
