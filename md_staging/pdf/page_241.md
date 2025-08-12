```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: pdf
page_number: 241
page_id: pdf#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:46Z
fidelity: lossless
-->

## Overview
- Displays the process of adding and validating PDF signatures in a document.
- Shows the interface for managing recipient signatures and their details.
- Illustrates the dialog for validating signature status after verification.

## Content

### Figure: Standard Signature

The following screenshot shows the interface displaying standard signatures within a document.

**Figure 51: Standard Signature**

This screenshot provides details about the options available for managing signatures in a PDF document. Key aspects include:

- **Recipient Signatures**: 
  - The following people have digital signatures.
  - Signatures are validated and displayed, including the time and reason for signing.

- **Signature Details**:
  - **Signature is valid**: Verifies that the signature held up during checks.
  - **Time**: The specific date and time of the signature.
  - **Reason**: The purpose or justification for applying the signature.
  - **Location**: The location associated with the signature.
  - **Field**: The field where the signature is applied.
  - **Document revision**: Indicates the specific revision of the document where the signature was added.

The document also displays a visual element with the Syncfusion logo and details about the validity period of the signature, emphasizing its security features.

### Signature Validation Process

The following screen shot shows the dialog that appears during verification of the signature.

**Figure 52: Signature Validation Status**

This dialog provides confirmation of the validation status:
- **Signature is VALID**: Signed by PDF `<support@syncfusion.com>`.
- **The Document has not been modified**: verifies that no changes have occurred since the application of the signature.
- **The document is signed by the current user**: assures that the signature belongs to the user performing the verification.

### Summary of Validation Status
- The validation status confirms that the document has a valid signature applied, ensuring no unauthorized modifications have occurred.
- The dialog also highlights that the current user is the signer, reinforcing trust and authenticity in the document.

## Code Examples

While the page does not provide direct code examples, the context implies that similar functionality can be implemented programmatically using Syncfusion's PDF library:

```csharp
// Example: Verifying a PDF signature programmatically
using Syncfusion.Pdf;

try
{
    using (PdfDocument pdfDocument = new PdfDocument("sample.pdf"))
    {
        PdfLoadedDocument loadedDocument = new PdfLoadedDocument(pdfDocument);
        if (loadedDocument.IsSignatureValid("path/to/certificate"))
        {
            Console.WriteLine("The signature is valid.");
        }
        else
        {
            Console.WriteLine("The signature is invalid.");
        }
    }
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
```

## RAG Annotations
<!-- tags: [pdf-signature, pdf-validation, recipient-signatures, document-security, syncfusion-winform, signature-verification] keywords: [Signatures, Valid, Syncfusion, Document, Validation, PDF] -->
```