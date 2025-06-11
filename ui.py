import streamlit as st
import pandas as pd

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
        <style>
        /* Fixed Footer */
        html body::after {
            content: '';
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50px;
            background-color: #fff;
            border-top: 1px solid #e9ecef;
            box-shadow: 0 -2px 4px rgba(0,0,0,0.04);
            z-index: 1000;
        }
        html body::before {
            content: '© 2025 S3K Technologies | All rights reserved';
            position: fixed;
            bottom: 18px;
            left: 0;
            width: 100%;
            color: #495057;
            text-align: center;
            z-index: 1001;
            font-size: 0.9em;
        }

        /* General Layout */
        body {
            color: #495057;
            background-color: #f8f9fa;
            font-family: sans-serif;
        }

        .main .block-container {
            padding-bottom: 80px;
        }

        /* Header styling */
        .stApp > header {
            background-color: #fff;
            padding: 10px 20px;
            border-bottom: 2px solid #e9ecef;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
            position: sticky;
            top: 0;
            z-index: 999;
        }

        /* Button styling */
        .stButton > button {
            border-radius: 8px;
            padding: 10px 20px;
            background-color: #b22222 !important;
            color: white !important;
            border: none;
            cursor: pointer;
            box-shadow: 0 2px 3px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #8b0000 !important;
            transform: translateY(-1px);
        }

        /* Visit Us Button */
        .visit-button {
            display: inline-block;
            padding: 8px 20px;
            background-color: #b22222;
            color: white !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
            margin-right: 10px;
        }

        .visit-button:hover {
            background-color: #8b0000;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            text-decoration: none;
        }

        /* File uploader styling */
        .stFileUploader > div > div > div {
            border-radius: 8px;
            border: 2px dashed #e9ecef;
            padding: 20px;
            background-color: #f9fafb;
        }

        /* Sidebar styling */
        .stSidebar > div:first-child {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        /* Status badges */
        .status-open {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            color: #92400e;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        .status-closed {
            background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
            color: #065f46;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        .status-n-a {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            color: #475569;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        /* Additional styles for new form fields */
        .stTextInput > div > div > input {
            border-radius: 8px;
            padding: 12px 16px;
            border: 2px solid #e9ecef;
            background-color: #fff;
            font-size: 14px;
            color: #495057;
            transition: all 0.2s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #b22222;
            box-shadow: 0 0 0 3px rgba(178,34,34,0.1);
        }

        .customer-info-card {
            background: linear-gradient(90deg, #fff 0%, #ffe5e5 100%);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 4px solid #b22222;
            box-shadow: 0 2px 12px rgba(178,34,34,0.07);
        }

        .modern-section {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(178,34,34,0.07);
            padding: 2rem 1.5rem 1.5rem 1.5rem;
            margin-bottom: 2rem;
            border-left: 6px solid #b22222;
        }

        .modern-header {
            color: #b22222;
            font-size: 1.5em;
            font-weight: 700;
            margin-bottom: 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the application header with logo and visit button"""
    with st.container():
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.image("https://s3ktech.ai/wp-content/uploads/2025/03/S3Ktech-Logo.png", width=140)
        with col2:
            st.markdown("<h1 style='display: inline-block; margin-left: 20px;'>Scanner Ticket Workflow</h1>", unsafe_allow_html=True)
        with col3:
            st.markdown("""
                <div style="display: flex; justify-content: flex-end; align-items: center; height: 100%;">
                    <a href="https://s3ktech.ai/" target="_blank" class="visit-button">Visit Us</a>
                </div>
            """, unsafe_allow_html=True)

def render_upload_section():
    st.sidebar.markdown('<div class="modern-header" style="margin-bottom:0.5em;">📤 Upload Scanner Data</div>', unsafe_allow_html=True)
    st.sidebar.markdown(
        "Upload your scanner inventory CSV file below. The file should include all required columns."
    )
    uploader = st.sidebar.file_uploader("Choose CSV file", type=['csv'])
    return uploader

def render_scanner_selection(scanners):
    """Render the scanner selection dropdown with a prompt option."""
    scanner_options = ["Select your scanner..."] + [f"{s['Serial No']} - {s['Select Product']}" for s in scanners]
    selected_option = st.selectbox("Select Your Scanner", options=scanner_options)
    
    if selected_option == "Select your scanner...":
        return None
    else:
        serial_number = selected_option.split(" - ")[0]
        selected_scanner = next((s for s in scanners if s['Serial No'] == serial_number), None)
        return selected_scanner

def render_customer_info(scanner):
    """Render customer information from the selected scanner"""
    st.markdown("""
        <div class="customer-info-card">
            <h3 style="color: #b22222; margin-bottom: 1rem;">Customer Information</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Company Name:** {scanner['Company Name']}")
        st.write(f"**Contact Person:** {scanner['Contact Person Name']}")
        st.write(f"**Phone:** {scanner['Phone Number']}")
        st.write(f"**Mobile:** {scanner['Mobile Number']}")
        st.write(f"**Email:** {scanner['Email']}")
    
    with col2:
        st.write(f"**Address:** {scanner['Address']}")
        st.write(f"**City:** {scanner['City']}")
        st.write(f"**State:** {scanner['State']}")
        st.write(f"**Pincode:** {scanner['Pincode']}")
        st.write(f"**Product:** {scanner['Select Product']}")
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_customer_input(scanner):
    """Render the customer input form"""
    st.markdown('<div class="modern-section"><div class="modern-header">Step 2: Customer Input</div>', unsafe_allow_html=True)
    render_customer_info(scanner)
    
    # Safely get case nature value
    case_nature_value = scanner.get('Select Case Nature', '')
    if not isinstance(case_nature_value, str):
        case_nature_value = ''
    case_nature_value = case_nature_value.strip()

    # Problem description: handle NaN or empty
    problem_val = scanner.get('Enter Comments / Problem', '')
    if pd.isna(problem_val) or str(problem_val).lower() == 'nan':
        problem_val = ''

    # Case nature selection
    case_nature = st.selectbox(
        "Case Nature",
        options=["Hardware Issue", "Software Issue", "Network Issue", "Other"],
        index=0 if case_nature_value == "" else 0
    )
    
    # Problem description
    problem = st.text_area(
        "Problem Description",
        value=problem_val,
        placeholder="Please describe the issue you're experiencing with your scanner..."
    )
    
    # Additional comments
    comments = st.text_area(
        "Additional Comments",
        placeholder="Any additional information that might help us resolve your issue..."
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    return case_nature, problem, comments

def render_customer_portal(customer_tickets):
    """Render the customer portal section"""
    st.header("Customer Portal")
    st.subheader("Your Support Tickets")
    
    if customer_tickets.empty:
        st.info("No tickets found.")
    else:
        st.dataframe(customer_tickets, use_container_width=True)

def render_admin_dashboard(master_sheet):
    """Render the admin dashboard section"""
    st.header("Admin Dashboard")
    st.subheader("Ticket Management")
    
    if master_sheet.empty:
        st.info("No tickets available.")
    else:
        st.dataframe(master_sheet, use_container_width=True)
        
        # Close ticket functionality
        st.subheader("Close Ticket")
        ticket_to_close = st.selectbox(
            "Select Ticket to Close",
            options=master_sheet[master_sheet['status'] == 'Open']['ticket'].tolist()
        )
        
        return ticket_to_close 