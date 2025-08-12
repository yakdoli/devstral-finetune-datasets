```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: pdf
page_number: 196
page_id: pdf#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:50Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Describes the concept of digital signatures, their authentication of sender identity, and their role in ensuring message/document integrity.
- Highlights the transportability, uniqueness, and time-stamping capabilities of digital signatures.
- Explains the use of digital signatures in user authentication and document state storage.

## Content

### Digital Signatures
A digital signature is an electronic signature used to authenticate the identity of the sender of a message or the signer of a document, and to ensure that the original content of the message or document has been sent unchanged. Digital signatures are easily transportable, cannot be imitated by someone else, and can be automatically time-stamped. This feature ensures that once the original signed message is received, the sender cannot easily repudiate it later. A digital signature is used to authenticate the identity of a user and the document's contents. It stores information about the signer and the state of the document at the moment of signing.

### PdfSignature

**PdfSignature** is a base class that provides the functionality to create either visible or invisible signatures on a page. To create an invisible signature, just set the signature size to zero. Later, the visibility of the signature is verified by using the **Visible** property. **PdfSignature** contains information about the signer, signing location, signing reason, and so on. The following table lists the public properties of this class.

#### Public Properties of PdfSignature

| Name | Description |
| --- | --- |
| Appearance | Gets the signature appearance. |
| Bounds | Gets or sets the bounds of the signature. |
| Certificate | Gets the signing certificate. |
| Certificated | Gets or sets a value indicating whether the document is certificated or not. Note: Works only with Adobe Reader 7.0.8 or higher. |
| ContactInfo | Gets or sets information provided by the signer to enable a recipient to contact the signer to verify the signature; for example, a phone number. |
| DocumentPermissions | Gets or sets the permission for certificated documents. |
| Field | Gets the PDF signature field. |
| Location | Gets or sets the signature location on the page. |
| LocationInfo | Gets or sets the physical location of the signing. |
| Reason | Gets or sets the reason of signing. |
| Visible | Gets a value indicating whether the signature is visible or not. |

## RAG Annotations
<!-- tags: [digital signature, authentication, document integrity, transportability, uniqueness, time-stamping, user authentication, document state, PdfSignature, visible signature, invisible signature, certificate, signature appearance, contact information, document permissions, location, location info, reason] keywords: [syncfusion, winforms, essential pdf, version, 11.4.0.26, pdf document, pdf signature] -->
```