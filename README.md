# Image Zoom Lens - Streamlit Component

An interactive Streamlit component that displays images with a movable zoom lens.

## Features

✨ **Interactive Zoom Lens**
- Move your mouse over the image to see a circular zoom lens
- The lens follows your mouse cursor in real-time

🎚️ **Configurable Controls**
- Adjust zoom level using mouse wheel (1x to 5x magnification)
- Configure lens size via slider (50-300 pixels)
- Set initial zoom level programmatically or via UI

💾 **Image Export**
- Right-click anywhere on the image to download
- Downloaded image includes the zoomed lens overlay at the click position
- Preserves original image quality

## Installation

### Install from GitHub

```bash
pip install git+https://github.com/abhijitmajumdar/image_zoom_lens.git
```

### Install from Source

```bash
git clone https://github.com/abhijitmajumdar/image_zoom_lens.git
cd image_zoom_lens
pip install -e .
```

### Development Installation

For development with additional tools (ruff, pre-commit):

```bash
git clone https://github.com/abhijitmajumdar/image_zoom_lens.git
cd image_zoom_lens
pip install -e ".[dev]"
pre-commit install
```

## Usage

### Basic Usage

```python
import streamlit as st
from image_zoom_lens import image_zoom_lens

st.title("Image Zoom Example")

image_zoom_lens(
    image_url="https://example.com/image.jpg",
    lens_size=150,
    zoom_level=2.0
)
```

### With Configuration

```python
import streamlit as st
from image_zoom_lens import image_zoom_lens

# Sidebar controls
lens_size = st.sidebar.slider("Lens Size", 50, 300, 150)
zoom_level = st.sidebar.slider("Zoom Level", 1.0, 5.0, 2.0)

# Display component
image_zoom_lens(
    image_url="https://example.com/image.jpg",
    lens_size=lens_size,
    zoom_level=zoom_level,
    key="my_zoom_lens"
)
```

### With PIL Image

```python
import streamlit as st
from PIL import Image
from image_zoom_lens import image_zoom_lens

# Load and process image with PIL
pil_image = Image.open("path/to/image.jpg")
pil_image = pil_image.resize((800, 600))  # Resize if needed

# Pass PIL image directly
image_zoom_lens(image=pil_image, lens_size=200)
```

### With Numpy Array

```python
import streamlit as st
import numpy as np
from image_zoom_lens import image_zoom_lens

# Create or process image as numpy array
np_image = np.random.randint(0, 255, (600, 800, 3), dtype=np.uint8)

# Pass numpy array directly
image_zoom_lens(image=np_image, zoom_level=3.0)
```

### With Uploaded Images

```python
import streamlit as st
from PIL import Image
from image_zoom_lens import image_zoom_lens

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Open with PIL and pass directly
    pil_image = Image.open(uploaded_file)
    image_zoom_lens(image=pil_image)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image` | str, PIL.Image, or np.ndarray | Required | Image to display: URL string, PIL Image object, or numpy array (H,W,3) or (H,W,4) |
| `lens_size` | int | 150 | Size of the zoom lens in pixels (50-500) |
| `zoom_level` | float | 2.0 | Initial zoom magnification (1.0-20.0) |
| `download_format` | str | 'jpg' | Format for downloaded images: 'jpg' or 'png' |
| `key` | str | None | Unique key for the component instance |

## Running the Demo

To see the component in action, run the demo application:

```bash
cd streamlit_plugins/image_zoom_lens/demo
streamlit run demo_app.py
```

## How It Works

### Mouse Interactions
- **Hover**: Move mouse over image to show zoom lens
- **Move**: Lens follows cursor position
- **Wheel**: Scroll to adjust zoom level dynamically
- **Right-click**: Download image with lens overlay

### UI Controls
- **Lens Size Slider**: Adjust the diameter of the zoom lens
- **Zoom Level Slider**: Set the magnification level

### Download Feature
When you right-click on the image:
1. Creates a canvas with the original image
2. Draws the zoomed portion in a circular lens at cursor position
3. Adds a border around the lens
4. Downloads the composite image as PNG

## File Structure

```
image_zoom_lens/
├── __init__.py           # Python component wrapper
├── README.md            # This file
├── demo/                # Demo application
│   ├── demo_app.py     # Demo Streamlit application
│   └── requirements.txt # Demo dependencies
└── frontend/
    └── index.html       # HTML/JavaScript implementation
```

## Use Cases

- 📊 **Data Analysis**: Examine details in charts and graphs
- 🏥 **Medical Imaging**: Inspect medical scans and X-rays
- 🗺️ **Maps**: Explore detailed map regions
- 🎨 **Design Review**: Check fine details in designs
- 🔬 **Scientific Images**: Analyze microscopy and research images
- 📸 **Photography**: Inspect image quality and details

## Browser Compatibility

Works in all modern browsers that support:
- HTML5 Canvas
- Mouse/wheel events
- CSS3

## License

MIT License - feel free to use and modify as needed.

## Contributing

Suggestions and improvements welcome! This is a custom component for Streamlit applications.
