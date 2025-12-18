import streamlit as st
from image_zoom_lens import image_zoom_lens

st.set_page_config(page_title="Image Zoom Lens Demo", layout="wide")

st.title("🔍 Image Zoom Lens Component")
st.markdown("""
This interactive component allows you to zoom into images with a movable lens.

**Features:**
- 🖱️ **Move mouse** over the image to see the zoom lens
- 🎚️ **Mouse wheel** to dynamically adjust zoom level
- 📏 **Sliders** to configure lens size and zoom level
- 💾 **Right-click** on the image to download it with the zoomed lens overlay
""")

st.divider()

# Sidebar configuration
st.sidebar.header("Configuration")
lens_size = st.sidebar.slider(
    "Lens Size (pixels)",
    min_value=50,
    max_value=500,
    value=150,
    step=10,
    help="Size of the circular zoom lens"
)

zoom_level = st.sidebar.slider(
    "Initial Zoom Level",
    min_value=1.0,
    max_value=20.0,
    value=2.0,
    step=0.1,
    help="Magnification level of the zoom lens"
)

download_format = st.sidebar.radio(
    "Download Format",
    options=["jpg", "png"],
    index=0,
    help="Format for right-click downloaded images. JPG: smaller files, PNG: lossless quality"
)

lens_shape = st.sidebar.radio(
    "Lens Shape",
    options=["circle", "square"],
    index=0,
    help="Shape of the zoom lens"
)

st.sidebar.divider()
st.sidebar.markdown("### Image Source")

# Image selection
image_option = st.sidebar.radio(
    "Select image source:",
    ["Sample Image (URL)", "Upload Your Own", "Custom URL", "Generate Test Pattern"]
)

image_url = None

if image_option == "Sample Image (URL)":
    # Use a sample image from the web
    image_url = st.sidebar.selectbox(
        "Choose a sample image:",
        [
            "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/681px-Placeholder_view_vector.svg.png",
            "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
            "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800",
        ],
        format_func=lambda x: x.split('/')[-1][:40] + "..."
    )
    
elif image_option == "Upload Your Own":
    uploaded_file = st.sidebar.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg", "gif", "bmp"]
    )
    if uploaded_file is not None:
        import base64
        # Convert uploaded file to base64 data URL
        bytes_data = uploaded_file.read()
        base64_data = base64.b64encode(bytes_data).decode()
        mime_type = uploaded_file.type
        image_url = f"data:{mime_type};base64,{base64_data}"
    else:
        st.info("👆 Please upload an image to get started")
        
elif image_option == "Custom URL":
    image_url = st.sidebar.text_input(
        "Enter image URL:",
        placeholder="https://example.com/image.jpg"
    )
    if not image_url:
        st.info("👆 Please enter an image URL to get started")
        
elif image_option == "Generate Test Pattern":
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    
    st.sidebar.info("Generating a test pattern using PIL/numpy")
    
    # Create a colorful test pattern
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw colorful gradient circles
    for i in range(20):
        x = (i * 40 + 50) % width
        y = (i * 30 + 50) % height
        radius = 30 + i * 5
        color = (
            (i * 30) % 255,
            (i * 50 + 100) % 255,
            (255 - i * 20) % 255
        )
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                     fill=color, outline='black', width=2)
    
    # Draw grid lines
    for i in range(0, width, 50):
        draw.line([(i, 0), (i, height)], fill='lightgray', width=1)
    for i in range(0, height, 50):
        draw.line([(0, i), (width, i)], fill='lightgray', width=1)
    
    # Add text
    try:
        font = ImageFont.truetype("Arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    draw.text((width//2 - 150, height//2), "Test Pattern", fill='black', font=font)
    
    # Use PIL image directly (not converted to URL yet)
    image_url = img

# Display the component
st.divider()
st.subheader("Interactive Zoom Lens")

if image_url:
    st.markdown("""
    **Instructions:**
    - Hover your mouse over the image to activate the zoom lens
    - Scroll with your mouse wheel while hovering to adjust zoom level
    - Use the sliders below the image to adjust lens size and zoom level
    - Right-click anywhere on the image to download a snapshot with the zoom lens overlay
    """)
    
    image_zoom_lens(
        image=image_url,  # Can be URL string, PIL Image, or numpy array
        lens_size=lens_size,
        zoom_level=zoom_level,
        download_format=download_format,
        lens_shape=lens_shape,
        key="zoom_lens_component"
    )
else:
    st.warning("⚠️ Please select or provide an image to display")

st.divider()

# Additional information
with st.expander("ℹ️ About this Component"):
    st.markdown("""
    ### Image Zoom Lens Component
    
    This is a custom Streamlit component that provides an interactive way to zoom into images.
    
    **Technical Details:**
    - Built with HTML5 Canvas and JavaScript
    - Uses circular clipping for the zoom lens effect
    - Mouse wheel events for dynamic zoom control
    - Canvas API for rendering the downloadable image
    
    **Use Cases:**
    - Medical image analysis
    - Photo inspection and quality control
    - Map exploration
    - Art and design review
    - Scientific image analysis
    
    **Component Files:**
    - `__init__.py` - Python wrapper for Streamlit
    - `frontend/index.html` - HTML/JavaScript implementation
    - `demo_app.py` - This demo application
    """)

st.divider()
st.caption("Made with ❤️ using Streamlit Custom Components")
