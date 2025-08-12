```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: pdf
page_number: 194
page_id: pdf#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:44Z
fidelity: lossless
-->

# Essential PDF

## Document Security

### Overview
- Security settings for a PDF document are managed through various security methods and permissions.

### Content

#### Security Method: Password Security
The given screenshot illustrates the security settings for a PDF document with **Password Security** as the selected security method:

---

**Figure 31: Encryption Level**

| **Security Method:** | Password Security |
|----------------------|-------------------|
| Document Open Password: | Yes              |
| Permissions Password:   | Yes              |
| Printing:               | None             |
| Changing the Document: | Not Allowed      |
| Commenting:             | Not Allowed      |
| Form Field Fill-in or Signing: | Not Allowed |
| Document Assembly:      | Not Allowed      |
| Content Copying:        | Not Allowed      |
| Content Accessibility Enabled: | Not Allowed |
| Page Extraction:        | Not Allowed      |
| **Encryption Level:** | 256-bit AES     |

---

This window shows detailed permissions and restrictions applied to the document, such as prohibiting printing, editing, commenting, filling in form fields, assembling documents, copying content, and enabling content accessibility. Encryption is set to a high level with **256-bit AES**.

### PdfSecurity

PdfSecurity is a class that enables the management of security properties for a PDF document.

#### Owner Password

- **Owner Password:**  
  The owner password provides full access to the document when entered correctly. This includes the ability to change passwords and modify permissions. If the owner password is different from the user password, it grants unrestricted access to all document properties.

#### User Password

- **User Password:**  
  The user password allows access to the document according to the specified permissions. Operations such as printing, editing, commenting, and signing are controlled through these permissions. If the user password matches the owner password or the document does not have a user password, additional operations can be performed as permitted in the document's permissions settings.

#### Permissions

This section outlines how permissions control the various functionalities within the document, ensuring that users can only perform actions explicitly allowed by the permissions settings.

## API Reference

### Class: PdfSecurity

#### Methods
- **SetPermissions()**
  - Assigns or modifies the security permissions for the PDF document.
  - Parameters:
    - **permissions**: The set of permissions to be applied to the document.

#### Properties
- **DocumentOpenPassword**
  - Retrieves or sets the password required to open the document.
- **PermissionsPassword**
  - Retrieves or sets the password required for accessing specific permissions.

## Code Examples

### Setting Security for a PDF Document

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Security;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Set the security properties
PdfSecurity pdfSecurity = new PdfSecurity();
pdfSecurity.DocumentOpenPassword = "ownerpassword";
pdfSecurity.PermissionsPassword = "userpassword";
pdfSecurity.EnablePrinting = false;
pdfSecurity.EnableAnnotations = false;

// Save the document
document.Security = pdfSecurity;
document.Save("SecureDocument.pdf");

// Close the document
document.Close();
```

## RAG Annotations

<!-- tags: [pdf, security, password, document, permissions, encryption] keywords: [password security, 256-bit AES, document open password, permissions password, owner password, user password, encryption level, security method, form field fill, signing, content copying, accessibility, commenting] -->
```