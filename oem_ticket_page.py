import streamlit as st
import urllib.parse
import math

def clean_nan(val):
    if val is None:
        return ''
    if isinstance(val, float) and math.isnan(val):
        return ''
    if str(val).lower() == 'nan':
        return ''
    return val

st.set_page_config(page_title="OEM Ticket Page", page_icon="📝", layout="centered")

st.markdown("""
    <style>
    .oem-card {
        background: linear-gradient(90deg, #fff 0%, #ffe5e5 100%);
        border-radius: 16px;
        box-shadow: 0 4px 24px rgba(178,34,34,0.08);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
        border-left: 8px solid #b22222;
    }
    .oem-label {
        color: #b22222;
        font-weight: 600;
        font-size: 1.1em;
        margin-bottom: 0.2em;
    }
    .oem-value {
        color: #222;
        font-size: 1.1em;
        margin-bottom: 1em;
    }
    .oem-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 180px;
        margin-bottom: 1.5rem;
    }
    .oem-back {
        display: inline-block;
        background: #b22222;
        color: #fff;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 1em;
        font-weight: 600;
        text-decoration: none;
        margin-bottom: 1.5rem;
        margin-top: 1rem;
    }
    .oem-back:hover {
        background: #8b0000;
        color: #fff;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://s3ktech.ai/wp-content/uploads/2025/03/S3Ktech-Logo.png", width=180, output_format="PNG")
st.title("OEM Ticket Details (Demo)")

# Parse query params
query_params = st.experimental_get_query_params()

def get_param(key):
    return clean_nan(query_params.get(key, [""])[0])

with st.container():
    st.markdown("<div class='oem-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Ticket ID:</div><div class='oem-value'>{get_param('ticket_id')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Company Name:</div><div class='oem-value'>{get_param('company')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Contact Person:</div><div class='oem-value'>{get_param('contact')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Phone Number:</div><div class='oem-value'>{get_param('phone')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Mobile Number:</div><div class='oem-value'>{get_param('mobile')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Email:</div><div class='oem-value'>{get_param('email')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Address:</div><div class='oem-value'>{get_param('address')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>City:</div><div class='oem-value'>{get_param('city')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>State:</div><div class='oem-value'>{get_param('state')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Pincode:</div><div class='oem-value'>{get_param('pincode')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Product:</div><div class='oem-value'>{get_param('product')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Serial No:</div><div class='oem-value'>{get_param('serial_no')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Case Nature:</div><div class='oem-value'>{get_param('case_nature')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Problem Description:</div><div class='oem-value'>{get_param('problem')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Additional Comments:</div><div class='oem-value'>{get_param('comments')}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='oem-label'>Service Date:</div><div class='oem-value'>{get_param('service_date')}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.info("This is a demo OEM ticket page. In production, this would POST to the real OEM endpoint.")

st.markdown('<a href="http://localhost:8501" class="oem-back">⬅️ Back to Ticket App</a>', unsafe_allow_html=True)
