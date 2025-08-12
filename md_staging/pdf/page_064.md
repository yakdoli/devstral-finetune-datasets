```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: pdf
page_number: 064
page_id: pdf#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:24Z
fidelity: lossless
-->

# Essential PDF

It manipulates with general document properties and stores sections. By default, an empty PDF document is created with a single page.

## PdfDocument Class

PdfDocument class is used to create a PDF document. The following are the public members of the PdfDocument class.

### Note

To save the document asynchronously for Windows Store apps, refer to the **Asynchronous Support** section.

## Methods

| Name            | Description                                                      |
|-----------------|------------------------------------------------------------------|
| AddFields       | Adds the fields connected to the page.                           |
| Append          | Appends the specified loaded document to this one.               |
| CheckFields     | Checks what fields are connected with the page.                 |
| Clone           | Creates a shallow copy of the current document.                 |
| ClonePage       | Clones pages and their resource dictionaries and adds them into the document. |
| Close           | Closes the document and releases the memory.                    |
| DisposeOnClose  | Adds an object to a collection of the objects that will be disposed during document closing. |
| GetForm         | Gets the form.                                                  |
| ImportPage      | Imports a Page.                                                 |
| ImportPageRange | Imports a page range from a loaded document.                    |
| OnDocumentSaved | Raises DocumentSaved event.                                     |
| OnPageSave      | Called when a page is saved.                                    |
| OnSaveProgress  | Raises the [E:Progress] event.                                  |
| PageLabelsSet   | Informs the document that the page labels were set.             |
| Save            | Saves the document.                                             |

## Properties
```