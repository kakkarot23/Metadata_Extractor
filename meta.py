
import gradio as gr
from pypdf import PdfReader, PdfWriter
from datetime import datetime
import tempfile
import os

def parse_metadata_string(metadata_text):
    parsed_meta = {}
    if not metadata_text:
        return parsed_meta
    for line in metadata_text.split('\n'):
        line = line.strip()
        if ': ' in line:
            key, value = line.split(': ', 1)
            key = key.strip()
            if not key.startswith('/'):
                key = '/' + key
            parsed_meta[key] = value.strip()
    return parsed_meta

def update_pdf_metadata(pdf_file, metadata_text):
    try:
        if pdf_file is None:
            return None

        reader = PdfReader(pdf_file.name)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        existing_metadata = reader.metadata or {}
        new_metadata_dict = parse_metadata_string(metadata_text)

        # Combine existing and new metadata, with new_metadata_dict overriding existing keys
        final_metadata_to_apply = {**existing_metadata, **new_metadata_dict}

        writer.add_metadata(final_metadata_to_apply)

        output_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        with open(output_file.name, "wb") as f:
            writer.write(f)

        return output_file.name

    except Exception as e:
        print(f"Error in update_pdf_metadata: {e}")
        return None

def get_metadata_from_file(pdf_file_obj):
    if pdf_file_obj is None or not os.path.exists(pdf_file_obj.name):
        return "No PDF file available to read metadata or file does not exist."
    try:
        reader = PdfReader(pdf_file_obj.name)
        metadata = reader.metadata
        if metadata:
            # Format for display and potential re-parsing
            return "\n".join([f"{key}: {value}" for key, value in metadata.items()])
        else:
            return "No metadata found in the PDF."
    except Exception as e:
        return f"Error reading metadata: {e}"

with gr.Blocks(title="PDF Metadata Editor") as demo:
    gr.Markdown("# PDF Metadata Editor")

    with gr.Row():
        pdf_input = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )
        output_pdf = gr.File(
            label="Download Updated PDF"
        )

    gr.Markdown("## Edit PDF Metadata")
    editable_metadata_input = gr.Textbox(
        label="Edit Metadata (Key: Value per line, e.g., /Title: My Document)",
        lines=10,
        interactive=True,
        placeholder="e.g., /Title: My Document\n/Author: John Doe\n/CreationDate: D:20230101120000Z00'00'"
    )

    with gr.Row():
        load_metadata_btn = gr.Button("Load Metadata from PDF")
        update_metadata_btn = gr.Button("Update & Download PDF")

    load_metadata_btn.click(
        fn=get_metadata_from_file,
        inputs=[pdf_input],
        outputs=editable_metadata_input
    )

    update_metadata_btn.click(
        fn=update_pdf_metadata,
        inputs=[pdf_input, editable_metadata_input],
        outputs=output_pdf
    )

demo.launch(share=True)
