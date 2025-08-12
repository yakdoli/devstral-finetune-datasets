```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: pdf
page_number: 239
page_id: pdf#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:17Z
fidelity: lossless
-->

## Overview
- A PDF document can contain several types of signatures, including document (or ordinary) signatures and at most one Modification Detection and Prevention (MDP) signature (also called an author or certifying signature).
- Recipient signatures (ordinary signatures) help in ensuring document integrity, preserving the byte range of the original signature if modified.
- The screenshot demonstrates an author signature prompt as displayed in a PDF document.

## Content

### PDF Document Signatures

A PDF document may contain the following standard types of signatures:

1. **Document (or Ordinary) Signatures**
   - These signatures are sometimes referred to as recipient signatures.
   - If a signed document is modified and saved by incremental update, the data corresponding to the byte range of the original signature is preserved.
   - If the signature is valid, it is possible to recreate the state of the document as it existed at the time of signing.

2. **Modification Detection and Prevention (MDP) Signature**
   - Also referred to as an author or certifying signature.
   - At most one MDP signature can be present in a PDF document.

#### Author Signature Prompt

The following screenshot shows an author signature prompt:

![Document Status Prompt](https://i.imgur.com/someimage.jpg)

*Figure 49: Author Signature Prompt*

### Details of the Author Signature Prompt

- **Document Status**:
  - The document has special status or special features.
  - The document is certified valid.
  - This document was certified with the Digital Signature of:
    - **Name**: PDF <support@syncfusion.com>
    - **Organization**: Syncfusion
    - **Issued by**: PDF

- **Signature Validation**:
  - The Digital Signature is valid, and the document has not been subsequently tampered with.
  - Click 'Signature Properties' to view more information about the signature and its validity.
  - Reliance upon this Certified document requires acceptance of the terms described when clicking 'Legal Notice'.

- **Accessing Signature Information**:
  - To access signature information later, open the Signatures Tab on the left, select the Certifying Signature, and choose 'Properties' from the Options menu.

- **Options**:
  - **Do not show this dialog next time this document is opened.**
  - The Document Status icons are always located at the bottom-left corner of the document window. Click a Document Status icon to view this dialog again.

- **Buttons**:
  - **Legal Notice...**
  - **Signature Properties...**
  - **Close**

#### Author Signature

The following screenshot shows an author signature.

---

## Page-level Navigation/TOC (if applicable)

- None specified in this page.

## Cross References

- None specified in this page.

## RAG Annotations

<!-- tags: [PDF, Digital Signatures, Syncfusion, Author Signature, MDP, Document Status] keywords: [author signature, document signature, digital signature, modification detection and prevention, secure PDF, Syncfusion, certifying signature] -->
```