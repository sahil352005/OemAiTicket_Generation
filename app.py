import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import io
import json
from ui import (
    load_css, render_header, render_upload_section,
    render_scanner_selection, render_customer_input,
    render_admin_dashboard, render_customer_portal
)

# Set page config
st.set_page_config(
    page_title="Scanner Ticket Workflow",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

def restore_state():
    """Restore state from session state"""
    if 'master_sheet_data' in st.session_state:
        try:
            st.session_state.master_sheet = pd.DataFrame(json.loads(st.session_state.master_sheet_data))
        except:
            st.session_state.master_sheet = pd.DataFrame(columns=[
                "Company Name", "Contact Person Name", "Phone Number", "Mobile Number",
                "Email", "Address", "City", "State", "Pincode", "Select Product",
                "Serial No", "Select Case Nature", "Enter Comments / Problem",
                "ticket", "status"
            ])
    else:
        st.session_state.master_sheet = pd.DataFrame(columns=[
            "Company Name", "Contact Person Name", "Phone Number", "Mobile Number",
            "Email", "Address", "City", "State", "Pincode", "Select Product",
            "Serial No", "Select Case Nature", "Enter Comments / Problem",
            "ticket", "status"
        ])

    if 'scanners_data' in st.session_state:
        try:
            st.session_state.scanners = json.loads(st.session_state.scanners_data)
        except:
            st.session_state.scanners = []
    else:
        st.session_state.scanners = []

    if 'current_customer_serial' not in st.session_state:
        st.session_state.current_customer_serial = ""

# Initialize or restore state
restore_state()

# Function to save state
def save_state():
    """Save current state to session state"""
    if not st.session_state.master_sheet.empty:
        st.session_state.master_sheet_data = st.session_state.master_sheet.to_json()
    if st.session_state.scanners:
        st.session_state.scanners_data = json.dumps(st.session_state.scanners)

# Render header
render_header()

# Main workflow
tab1, tab2, tab3 = st.tabs(["Home", "Customer Portal", "Admin Dashboard"])

with tab1:
    # File upload
    uploaded_file = render_upload_section()
    
    if uploaded_file is not None:
        try:
            # Read the file content
            content = uploaded_file.read()
            
            # Check if file is empty
            if len(content) == 0:
                st.error("The uploaded file is empty. Please upload a valid CSV file.")
                st.stop()
            
            # Try different encodings
            encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
            df = None
            
            for encoding in encodings:
                try:
                    # Reset file pointer
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, encoding=encoding)
                    
                    # Check if DataFrame is empty
                    if df.empty:
                        st.error("The CSV file contains no data. Please ensure it has content.")
                        st.stop()
                    
                    # Check if DataFrame has columns
                    if len(df.columns) == 0:
                        st.error("The CSV file has no columns. Please ensure it's properly formatted.")
                        st.stop()
                    
                    break
                except UnicodeDecodeError:
                    continue
                except pd.errors.EmptyDataError:
                    st.error("The CSV file is empty or has no data. Please upload a valid CSV file.")
                    st.stop()
                except Exception as e:
                    st.error(f"Error reading CSV file: {str(e)}")
                    st.stop()
            
            if df is None:
                st.error("Could not read the CSV file. Please ensure it's a valid CSV file.")
                st.stop()
            
            # Convert column names to match the expected format
            df.columns = [col.strip() for col in df.columns]
            
            # Validate required columns
            required_columns = [
                "Company Name", "Contact Person Name", "Phone Number", "Mobile Number",
                "Email", "Address", "City", "State", "Pincode", "Select Product",
                "Serial No", "Select Case Nature", "Enter Comments / Problem"
            ]
            
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                st.error(f"Missing required columns: {', '.join(missing_columns)}")
                st.error("Please ensure your CSV file has all the required columns.")
                st.stop()
            
            # Clean the data
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].astype(str).str.strip()
            
            st.session_state.scanners = df.to_dict('records')
            save_state()  # Save state after updating scanners
            st.success("CSV data loaded successfully!")
            
            # Scanner selection
            selected_scanner = render_scanner_selection(st.session_state.scanners)
            
            if selected_scanner:
                st.session_state.current_customer_serial = selected_scanner['Serial No']
                
                # Customer input
                case_nature, problem, comments = render_customer_input(selected_scanner)
                
                # Directly submit ticket to OEM after customer input
                if st.button("Submit Ticket to OEM"):
                    ticket_id = f"TICKET-{random.randint(10000, 99999)}"
                    service_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                    
                    # Update master sheet
                    mask = st.session_state.master_sheet['Serial No'] == selected_scanner['Serial No']
                    if mask.any():
                        st.session_state.master_sheet.loc[mask, ['ticket', 'status']] = [
                            ticket_id, "Open"
                        ]
                    else:
                        new_row = pd.DataFrame([{
                            **selected_scanner,
                            "ticket": ticket_id,
                            "status": "Open"
                        }])
                        st.session_state.master_sheet = pd.concat([st.session_state.master_sheet, new_row], ignore_index=True)
                    
                    save_state()  # Save state after updating master sheet
                    
                    st.markdown(f"""
                    <div style='background: linear-gradient(90deg, #f8fafc 0%, #ffe5e5 100%); border-left: 6px solid #b22222; padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem;'>
                        <h3 style='color: #b22222;'>✅ Ticket submitted to OEM successfully!</h3>
                        <p style='color: #333; font-size: 1.1em;'>
                        <b>Ticket:</b> {ticket_id} for <b>{selected_scanner['Select Product']}</b><br>
                        <b>Service scheduled:</b> {service_date}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                    # --- Go to OEM Ticket Page button ---
                    import urllib.parse
                    params = {
                        'ticket_id': ticket_id,
                        'company': selected_scanner['Company Name'],
                        'contact': selected_scanner['Contact Person Name'],
                        'phone': selected_scanner['Phone Number'],
                        'mobile': selected_scanner['Mobile Number'],
                        'email': selected_scanner['Email'],
                        'address': selected_scanner['Address'],
                        'city': selected_scanner['City'],
                        'state': selected_scanner['State'],
                        'pincode': selected_scanner['Pincode'],
                        'product': selected_scanner['Select Product'],
                        'serial_no': selected_scanner['Serial No'],
                        'case_nature': case_nature,
                        'problem': problem,
                        'comments': comments,
                        'service_date': service_date
                    }
                    base_url = 'http://localhost:8502'  # Default Streamlit port for second app
                    query = urllib.parse.urlencode(params)
                    oem_url = f"{base_url}/?{query}"
                    st.markdown("<hr>", unsafe_allow_html=True)
                    st.markdown(f'<a href="{oem_url}" target="_blank"><button style="background: linear-gradient(90deg, #b22222 0%, #ff7f7f 100%); color: white; border: none; border-radius: 8px; padding: 0.75rem 2rem; font-size: 1.1em; font-weight: bold; margin-top: 1rem; cursor: pointer;">Go to OEM Ticket Page</button></a>', unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"Error processing CSV file: {str(e)}")
            st.error("Please ensure your CSV file has the correct format and encoding.")

with tab2:
    customer_tickets = st.session_state.master_sheet[
        st.session_state.master_sheet['Serial No'] == st.session_state.current_customer_serial
    ]
    render_customer_portal(customer_tickets)

with tab3:
    ticket_to_close = render_admin_dashboard(st.session_state.master_sheet)
    
    if ticket_to_close and st.button("Close Selected Ticket"):
        mask = st.session_state.master_sheet['ticket'] == ticket_to_close
        st.session_state.master_sheet.loc[mask, 'status'] = "Closed"
        save_state()  # Save state after closing ticket
        st.success(f"Ticket {ticket_to_close} has been closed successfully!")
        st.rerun() 