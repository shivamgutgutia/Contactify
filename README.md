# Contact File Backend Service

The Contact File Backend Service offers a seamless solution for users to upload contact information in various formats (CSV, XLSX, or XLS). Upon submission, the backend processes this data, extracting details such as names, phone numbers, emails, and genders. It compiles this information into a unified contact file (VCF file) compatible with Android and iOS devices, simplifying contact management.

## Features

### File Upload Prompt
- Enables users to upload contact files in various formats (CSV, XLSX, XLS) effortlessly.

### Automatic Header Extraction
- Identifies and extracts headers from uploaded files to assist in contact data organization.

### Header Mapping Interface
- Provides a user-friendly interface for mapping extracted headers to predefined contact fields like first name, middle name, last name, gender, phone number, and email for accurate data categorization.

### Custom Data Handling Options
- **Row Filtering**: Allows skipping rows without a phone number or with insufficient phone number digits.
- **Data Validation**: Offers options to set criteria for data inclusion, ensuring accuracy and completeness.

### Contact File Generation Options
- **Unified VCF File**: Generates a single VCF file containing all organized contact information.
- **Individual Contact Files**: Provides flexibility to receive contacts as separate files bundled together in a convenient zip format.

## Installation Guide

Follow these steps to set up and run the Contact File Backend Service locally:

1. **Clone the Repository**
   - Clone the repository.
     ```bash
     git clone https://github.com/shivamgutgutia/contactsGeneratorBackend.git
     ```
   - Navigate to the cloned directory and run
     ```bash
     cd contactsGeneratorBackend
     ```

2. **Install Dependencies**
   - Install all required dependencies for running the server on local machine
     ```bash
     pip3 install -r requirements.txt
     ```

3. **Configuration**
   - Create a `.env` file in the root directory.
   - Define environment variables such as:
     - `PORT=5000`

4. **Start the Server**
   - Start the backend service
     ```bash
     python3 app.py
     ```
   - The service will be running on `http://localhost:5000` by default.

## API Documentation

https://documenter.getpostman.com/view/30463796/2s9Ye8euN8