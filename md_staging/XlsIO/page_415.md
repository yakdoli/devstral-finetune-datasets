```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_415.jpeg
document_name: XlsIO
page_number: 415
page_id: XlsIO#page_415
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:41Z
fidelity: lossless
--> 

# Essential XlsIO

## Document Security Settings

### Overview
- This section explains how to manage document security using passwords to control access and modifications.
- Figure 154 depicts the Options Dialog Box - Security, illustrating the settings for file encryption and sharing.

### Content

#### Options Dialog Box - Security
- The Options Dialog Box - Security provides settings for securing a workbook:
  - **File encryption settings**:
    - **Password to open**: Encrypts the document to protect data from unauthorized access.
  - **File sharing settings**:
    - **Password to modify**: Allows specific users to edit and save changes to the document.
  - **Privacy options**: Includes an option to remove personal information from the file on save.
  - **Macro security**: Adjusts the security level for files containing macro viruses and specifies names of trusted macro developers.

- **User Interaction**:
  - The user is required to enter two separate passwords:
    - **Password To Open**: Encrypted to protect data from unauthorized access.
    - **Password To Modify**: Not encrypted; provides specific users permission to edit workbook data and save changes.

#### Entering Passwords

##### Password To Open
- **Purpose**: Encrypts the document to protect data.
- **Entry Process**: Users must enter a password in the dialog box shown in Figure 155 and click "OK" to proceed.
- **Figure 155**: Entering Password to Open

##### Password To Modify
- **Purpose**: Allows specific users to edit and save changes to the document.
- **Characteristics**: Not encrypted; used to grant edit permissions.
- **Usage**: Specific users are given this password to allow them to make modifications.

### Summary
- The security features in XlsIO allow users to protect and control access to their documents effectively.
- Passwords play a key role in securing documents by encrypting them for protection or granting specific permissions for editing.

## Code Examples

### Example: Setting Document Passwords
This example demonstrates how to set both open and modify passwords for an Excel document using XlsIO.

```csharp
using(SpreadsheetLoadOptions options = new SpreadsheetLoadOptions())
{
    using(SpreadsheetDocument doc = new SpreadsheetDocument())
    {
        // Load the document
        doc.Load("document.xlsx", options);

        // Set open password
        doc.WorkbookProtection.PasswordToOpen = "your_password";

        // Set modify password
        doc.WorkbookProtection.PasswordToModify = "your_password";

        // Save the document
        doc.Save("protected_document.xlsx");
    }
}
```

## Cross References

- **See also**: Additional information on document security and encryption in the XlsIO documentation.

<!-- tags: [Syncfusion, Winforms, XlsIO, document security, password protection] keywords: [password, open, modify, encryption, unauthorized access, workbook protection, Excel] -->
```