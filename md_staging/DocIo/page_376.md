```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_376.jpeg
document_name: DocIo
page_number: 376
page_id: DocIo#page_376
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:51Z
fidelity: lossless
-->

## Overview
- You can protect word documents with or without a password to prevent modifications.
- Specify different types of protection for word documents using the `WdProtectionType` property in MS Office Interop.
- Allows customization of document accessibility, such as comments, form fields, or read-only access.

## Content

### 5.12.10 Document Protection
You can protect word documents with or without a password to prevent anyone from accidentally or deliberately modifying the word documents. You can specify the protection type for preserving the word documents.

#### Using MS Office Interop
The `WdProtectionType` property is used to specify the type of protection that can be set to the word document. This property uses the following values:

- **wdAllowOnlyComments** - Allow only comments to be added to the document.
- **wdAllowOnlyFormFields** - Allow content to be added to the document only through form fields.
- **wdAllowOnlyReading** - Allow read-only access to the document.
- **wdAllowOnlyRevisions** - Allow only revisions to be made to the existing content.
- **wdNoProtection** - Do not apply protection to the document.

## RAG Annotations
<!-- tags: [DocIo, MS Office Interop, document protection, Word documents, password protection, wdProtectionType, Syncfusion Winforms, version 11.4.0.26] keywords: [document protection, Word document, MS Office Interop, password protection, wdProtectionType, wdAllowOnlyComments, wdAllowOnlyFormFields, wdAllowOnlyReading, wdAllowOnlyRevisions, wdNoProtection] -->
```