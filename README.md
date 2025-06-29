# Scanner Ticket Workflow App

This is a Streamlit-based web application for managing scanner support tickets. It allows users to upload scanner inventory, generate and track support tickets, and provides both customer and admin dashboards. There is also a demo OEM ticket page for viewing ticket details.

## Features

- **CSV Upload:** Upload scanner inventory data in CSV format.
- **Ticket Generation:** Generate support tickets for scanners with issues.
- **Customer Portal:** Customers can view their ticket status and details.
- **Admin Dashboard:** Admins can view and close tickets.
- **OEM Ticket Page:** Demo page to view ticket details as sent to OEM.

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd aiticketgenerate
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Start the main app:**
   ```sh
   streamlit run app.py
   ```

2. **Start the OEM ticket page (in a new terminal):**
   ```sh
   streamlit run oem_ticket_page.py --server.port 8502
   ```

3. **Open your browser:**
   - Main app: [http://localhost:8501](http://localhost:8501)
   - OEM ticket page: [http://localhost:8502](http://localhost:8502)

## CSV Format

Your CSV file should include the following columns:

- Company Name
- Contact Person Name
- Phone Number
- Mobile Number
- Email
- Address
- City
- State
- Pincode
- Select Product
- Serial No
- Select Case Nature
- Enter Comments / Problem

## Project Structure

```
.
├── app.py                # Main Streamlit app
├── oem_ticket_page.py    # Demo OEM ticket details page
├── ui.py                 # UI helper functions and styles
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

##
