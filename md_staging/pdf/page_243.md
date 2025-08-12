```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: pdf
page_number: 243
page_id: pdf#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:34Z
fidelity: lossless
-->

## Digital Signature and Timestamping in Essential PDF

### Overview
- The document describes how to add a timestamp to digital signatures in Essential PDF.
- Explains the benefits of including timestamps, such as easier verification and reducing the chances of an invalid signature.
- Specifies that only self-created and third-party `.pfx` certificates are supported for digital signatures.

### Content

#### Digital Signature Properties

- **Location Information**: 
  ```csharp
  signature.LocationInfo = "Honolulu, Hawaii"
  ```
- **Reason for Signing**: 
  ```csharp
  signature.Reason = "I am author of this document."
  ```

#### Note: Currently only self-created and third-party `.pfx` certificates are supported.

##### Timestamp in Digital Signature

- **Overview**: Essential PDF supports the addition of a timestamp to digital signatures.
- **Timestamp Functionality**: 
  - The date and time of document signing can be included as part of the signature.
  - Timestamps are easier to verify when associated with a trusted certificate from a timestamp authority.
  - Including a timestamp helps establish the exact moment of signing, reducing the risk of an invalid signature.
  - The timestamp can be obtained from a third-party timestamp authority or the certificate authority that issued the digital ID.

- **Timestamp Display**:
  - Timestamps are visible in the signature field and the Signature Properties dialog box.
  - If a timestamp is included, the certificate information appears in the `Date/Time` tab of the Signature Properties dialog box.
  - If no timestamp is added, the signature field displays the local time of the computer at the moment of signing.

- **Example**: 
  - The following figure shows the timestamp properties of the digital signature.

### API Reference

- Namespace: `Essential PDF`
- Class: `Signature`
  - Properties:
    - `LocationInfo`: Specifies the location information for the digital signature.
    - `Reason`: Specifies the reason for the digital signature.

### Code Examples (C#)

```csharp
// Example of setting location and reason in a digital signature
Signature signature = new Signature();
signature.LocationInfo = "Honolulu, Hawaii";
signature.Reason = "I am author of this document.";
```

### Summary

Digits signatures with timestamps in Essential PDF provide a secure and verifiable way to authenticate documents. The integration supports self-created and third-party `.pfx` certificates, ensuring robust validation and tamper detection.

<!-- tags: [Essential PDF, digital signature, timestamp, self-created certificates, third-party certificates] keywords: [digital signature, timestamp, author, location, reason, verification, trusted certificate, authority] -->
```