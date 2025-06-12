import streamlit as st
import urllib.parse
import math
from datetime import datetime

def clean_nan(val):
    if val is None:
        return ''
    if isinstance(val, float) and math.isnan(val):
        return ''
    if str(val).lower() == 'nan':
        return ''
    return val

st.set_page_config(
    page_title="OEM Ticket Details",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(90deg, #fff 0%, #ffe5e5 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(178,34,34,0.08);
        border-left: 8px solid #b22222;
    }
    
    /* Ticket card styling */
    .ticket-card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 4px 24px rgba(178,34,34,0.08);
        padding: 2.5rem 2rem;
        margin-bottom: 2rem;
        border-left: 8px solid #b22222;
    }
    
    .ticket-section {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 12px;
    }
    
    .ticket-label {
        color: #b22222;
        font-weight: 600;
        font-size: 1.1em;
        margin-bottom: 0.5em;
    }
    
    .ticket-value {
        color: #2c3e50;
        font-size: 1.1em;
        margin-bottom: 1.5em;
        padding: 0.5rem;
        background: #fff;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    .ticket-header {
        color: #b22222;
        font-size: 1.8em;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .ticket-subheader {
        color: #495057;
        font-size: 1.2em;
        margin-bottom: 2rem;
    }
    
    /* Status badge styling */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9em;
        text-transform: uppercase;
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        color: #92400e;
    }
    
    /* Back button styling */
    .back-button {
        display: inline-block;
        background: #b22222;
        color: #fff;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-size: 1em;
        font-weight: 600;
        text-decoration: none;
        margin-top: 2rem;
        transition: all 0.3s ease;
    }
    
    .back-button:hover {
        background: #8b0000;
        color: #fff;
        text-decoration: none;
        transform: translateY(-2px);
    }
    
    /* Logo styling */
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Info box styling */
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 8px;
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
st.image("https://s3ktech.ai/wp-content/uploads/2025/03/S3Ktech-Logo.png", width=200)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<h1 class="ticket-header">OEM Ticket Details</h1>', unsafe_allow_html=True)
st.markdown('<p class="ticket-subheader">View and manage your service ticket information</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Parse query params
query_params = st.query_params

def get_param(key):
    return clean_nan(query_params.get(key, ""))

# Main ticket information
st.markdown('<div class="ticket-card">', unsafe_allow_html=True)

# Ticket ID and Status
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(f'<div class="ticket-label">Ticket ID</div><div class="ticket-value">{get_param("ticket_id")}</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="ticket-label">Status</div><div class="status-badge">Open</div>', unsafe_allow_html=True)

# Customer Information Section
st.markdown('<div class="ticket-section">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #b22222; margin-bottom: 1rem;">Customer Information</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="ticket-label">Company Name</div><div class="ticket-value">{get_param("company")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">Contact Person</div><div class="ticket-value">{get_param("contact")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">Phone Number</div><div class="ticket-value">{get_param("phone")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">Mobile Number</div><div class="ticket-value">{get_param("mobile")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">Email</div><div class="ticket-value">{get_param("email")}</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="ticket-label">Address</div><div class="ticket-value">{get_param("address")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">City</div><div class="ticket-value">{get_param("city")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">State</div><div class="ticket-value">{get_param("state")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ticket-label">Pincode</div><div class="ticket-value">{get_param("pincode")}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Product Information Section
st.markdown('<div class="ticket-section">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #b22222; margin-bottom: 1rem;">Product Information</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="ticket-label">Product</div><div class="ticket-value">{get_param("product")}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="ticket-label">Serial Number</div><div class="ticket-value">{get_param("serial_no")}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Issue Details Section
st.markdown('<div class="ticket-section">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #b22222; margin-bottom: 1rem;">Issue Details</h3>', unsafe_allow_html=True)

st.markdown(f'<div class="ticket-label">Case Nature</div><div class="ticket-value">{get_param("case_nature")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ticket-label">Problem Description</div><div class="ticket-value">{get_param("problem")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ticket-label">Additional Comments</div><div class="ticket-value">{get_param("comments")}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Service Information Section
st.markdown('<div class="ticket-section">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #b22222; margin-bottom: 1rem;">Service Information</h3>', unsafe_allow_html=True)
st.markdown(f'<div class="ticket-label">Scheduled Service Date</div><div class="ticket-value">{get_param("service_date")}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Demo notice
st.markdown("""
    <div class="info-box">
        <strong>Note:</strong> This is a demo OEM ticket page. In production, this would POST to the real OEM endpoint.
    </div>
""", unsafe_allow_html=True)

# Back button with proper URL
st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <a href="http://localhost:8501" target="_self" class="back-button">⬅️ Back to Ticket App</a>
    </div>
""", unsafe_allow_html=True)
