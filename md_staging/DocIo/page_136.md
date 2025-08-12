```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: DocIo
page_number: 136
page_id: DocIo#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:33Z
fidelity: lossless
-->

## Field Dialog Box

### Overview
- Field dialog box allows users to choose from various field options within a document.
- Categorizes fields for easy selection and configuration.

### Content

#### Field Properties
- The "Field properties" section provides options to configure advanced settings for the selected field.
- Users can click the "Formula..." button to set advanced field options, such as calculating expressions.

#### Field List
- The fields available include a variety of options such as:
  - Formula
  - AddressBlock
  - Advance
  - Ask
  - Author
  - AutoNum
  - AutoNumLgl
  - AutoNumOut
  - AutoText
  - AutoTextList
  - BarCode
  - BidiOutline
  - Comments
  - Compare
  - CreateDate

#### Description
- The fields listed are described in terms of their function. For example, the "Formula" field calculates the result of an expression.

#### Options
- Users can preserve formatting during updates by checking the corresponding box.
- Standard dialog buttons are present: OK and Cancel for confirmation, or cancellation of the action.

#### Preservation of Formatting
- The "Preserve formatting during updates" checkbox ensures consistency in document appearance and structure while making updates.

## Fields in Word Documents

### Overview
- Fields are widely used in document preparation, especially for mail merge functionality.
- Structure of a field in a Word document includes a field start marker, separator, value, and end marker.

### Detailed Description
- **Frame Dynamics**: Each field defined in a document is encapsulated with start and end markers, specifying the type and values.
- **Contextual Information**: The field value is often placed between separators for clarity and editing convenience.

## WField Class in Word Documentation

### Overview
- The `WField` class represents a field in the Word document.
- It encapsulates the functionality and properties of various field types used in document creation.

### Types of Fields
- There are numerous types of fields available, each serving different purposes in document automation and formatting.

#### Examples of Fields
- Formula field for calculations.
- AddressBlock for assembling mailing addresses.
- AutoNum for automatic numbering based on various styles (legal, standard, etc.).
- AutoText for quickly inserting predefined text and images.
- BarCode for embedding barcodes.
- Comments for storing annotations and notes for document review.
- CreateDate for displaying the creation date of a document.

## Cross References
- Refer to section "Mail Merge" for further application of field functionalities.
- Check "Document Automation" for best practices in using fields for efficient document management.

## RAG Annotations
<!-- tags: Syncfusion, WinForms, DocIO, FieldDialogBox, WordDocument, WFieldClass, Fieldproperties, MailMerge, DocumentAutomation keywords: field, dialog, properties, formula, mailmerge, document, fielddialogbox, wfieldclass -->
```