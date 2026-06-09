# PDF Metadata Editor

A web-based PDF metadata editor built with Python, Gradio, and PyPDF.

This application allows users to:

* Upload PDF files.
* View existing PDF metadata.
* Edit metadata fields.
* Add new metadata entries.
* Remove or replace author and creator information.
* Generate and download an updated PDF with modified metadata.

---

## Features

### Metadata Viewing

* Read metadata directly from uploaded PDF files.
* Display metadata in an editable text area.

### Metadata Editing

* Modify existing metadata fields.
* Add custom metadata fields.
* Update document information without changing PDF content.

### Privacy Enhancement

* Remove identifying information such as:

  * Author
  * Creator
  * Producer
  * Company
  * Last Modified By

### Download Updated PDF

* Generate a new PDF containing the updated metadata.
* Download the processed file directly from the web interface.

---

## Technology Stack

* Python 3.x
* Gradio
* PyPDF

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd pdf-metadata-editor
```

### Install Dependencies

```bash
pip install gradio pypdf
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

The Gradio interface will start automatically and provide:

* Local URL
* Public share URL (if enabled)

---

## Usage

### Step 1: Upload PDF

Upload any PDF document using the file selector.

### Step 2: Load Metadata

Click:

```text
Load Metadata from PDF
```

The current metadata will appear in the editor.

Example:

```text
/Title: Sample Document
/Author: John Doe
/Creator: Microsoft Word
/Producer: PDF Producer
```

### Step 3: Edit Metadata

Modify existing values or add new entries.

Example:

```text
/Title: Research Report
/Subject: Machine Learning
/Keywords: AI, Research, Data Science
```

### Step 4: Generate Updated PDF

Click:

```text
Update & Download PDF
```

A new PDF will be generated with the updated metadata.

---

## Metadata Format

Each metadata entry should follow:

```text
/Key: Value
```

Example:

```text
/Title: Project Report
/Author: Jane Doe
/Subject: Final Year Project
/Keywords: Python, AI
```

---

## Supported Metadata Fields

Common PDF metadata keys include:

```text
/Title
/Author
/Subject
/Keywords
/Creator
/Producer
/CreationDate
/ModDate
```

Custom metadata fields may also be added.

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Example Workflow

1. Upload PDF.
2. Load existing metadata.
3. Edit metadata values.
4. Generate updated PDF.
5. Download modified file.

---

## Requirements

Create a requirements file:

```text
gradio
pypdf
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Notes

* The application modifies PDF metadata only.
* Document content remains unchanged.
* Existing metadata is preserved unless overwritten.
* Invalid metadata formats may be ignored by some PDF readers.
* Some PDF viewers cache metadata; reopening the file may be necessary to view changes.

---

## License

This project is provided for educational and research purposes.

Use responsibly and ensure compliance with applicable laws and regulations when modifying document metadata.
