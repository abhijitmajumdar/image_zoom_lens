"""
Image Zoom Lens Component for Streamlit

A custom Streamlit component that displays an image with an interactive zoom lens.
Features:
- Configurable zoom level (mouse wheel or slider)
- Configurable lens size
- Mouse tracking for lens movement
- Right-click to download image with zoomed lens overlay
"""

import streamlit.components.v1 as components
import os
from pathlib import Path
from typing import Optional
from urllib.parse import quote

# Get the directory of this file (use absolute path)
_COMPONENT_DIR = Path(__file__).resolve().parent


def image_zoom_lens(
    image_url: str,
    lens_size: int = 150,
    zoom_level: float = 2.0,
    download_format: str = 'jpg',
    key: Optional[str] = None,
) -> None:
    """
    Display an image with an interactive zoom lens.
    
    Parameters
    ----------
    image_url : str
        URL or path to the image to display. Can be a data URL, web URL, 
        or file path.
    lens_size : int, optional
        Size of the zoom lens in pixels (default: 150).
        Range: 50-300 pixels.
    zoom_level : float, optional
        Initial zoom magnification level (default: 2.0).
        Range: 1.0-5.0x.
    download_format : str, optional
        Format for downloaded images: 'jpg' or 'png' (default: 'jpg').
        JPG provides smaller file sizes, PNG preserves transparency.
    key : str, optional
        An optional string to use as the unique key for the component.
        If this is None, and the component's arguments are changed, the
        component will be re-mounted in the Streamlit app.
        
    Usage
    -----
    - Move your mouse over the image to see the zoom lens
    - Use the mouse wheel to adjust zoom level dynamically
    - Use the sliders to adjust lens size and zoom level
    - Right-click on the image to download it with the zoomed lens overlay
    
    Example
    -------
    >>> import streamlit as st
    >>> from image_zoom_lens import image_zoom_lens
    >>> 
    >>> st.title("Image Zoom Lens Demo")
    >>> image_zoom_lens(
    ...     image_url="https://example.com/image.jpg",
    ...     lens_size=200,
    ...     zoom_level=3.0
    ... )
    """
    
    # Validate parameters
    lens_size = max(50, min(300, lens_size))
    zoom_level = max(1.0, min(5.0, zoom_level))
    download_format = download_format.lower()
    if download_format not in ['jpg', 'jpeg', 'png']:
        download_format = 'jpg'
    # Normalize jpeg to jpg
    if download_format == 'jpeg':
        download_format = 'jpg'
    
    # Load the HTML file
    html_path = _COMPONENT_DIR / "frontend" / "index.html"
    with open(html_path, 'r') as f:
        html_template = f.read()
    
    # Inject parameters by replacing the script initialization
    html_content = html_template.replace(
        "let imageUrl = '';",
        f"let imageUrl = '{image_url}';"
    ).replace(
        "let currentZoomLevel = 2;",
        f"let currentZoomLevel = {zoom_level};"
    ).replace(
        "let lensSize = 150;",
        f"let lensSize = {lens_size};"
    ).replace(
        "let downloadFormat = 'jpg';",
        f"let downloadFormat = '{download_format}';"
    ).replace(
        'mainImage.src = imageUrl;',
        f'mainImage.src = "{image_url}";'
    ).replace(
        'zoomLensImage.src = imageUrl;',
        f'zoomLensImage.src = "{image_url}";'
    )
    
    # Render using components.html
    components.html(html_content, height=700, scrolling=True)
    
    return None


# Make the component available at package level
__all__ = ["image_zoom_lens"]
