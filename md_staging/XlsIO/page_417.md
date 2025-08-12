```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_417.jpeg
document_name: XlsIO
page_number: 417
page_id: XlsIO#page_417
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:06Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- [C#] and [VB.NET] code snippets for encrypting and decrypting Excel workbooks.
- Instructions for setting passwords for opening, modifying, and read-only access to Excel workbooks.
- Information about the encryption type supported by Essential XlsIO and its limitations regarding weak and strong encryption.

## Content

### Encryption and Decryption Code Examples

#### [C#]

```csharp
// Encryption:
// Encrypt the workbook with password.
workbook.PasswordToOpen = "syncfusion";

// Set the password to modify the workbook.
workbook.SetWriteProtectionPassword("modify");

// Set the workbook as read-only.
workbook.ReadOnlyRecommended = true;

// Decryption:
// Opening the encrypted workbook.
IWorkbook workbook = application.Workbooks.Open("FileName.xls",
ExcelParseOptions.Default, true, "syncfusion");
```

#### [VB.NET]

```vbnet
' Encryption:
' Encrypt the workbook with password.
workbook.PasswordToOpen = "syncfusion"

' Set the password to modify the workbook.
workbook.SetWriteProtectionPassword("modify")

' Set the workbook as read-only.
workbook.ReadOnlyRecommended= true

' Decryption:
' Opening the encrypted workbook.
Dim workbook As Syncfusion.XlsIO.IWorkbook = 
Application.Workbooks.Open("FileName.xls", ExcelParseOptions.Default, True, "syncfusion")
```

### Note

**Note:** Essential XlsIO supports default encryption of the type "Office97-2000 compatible", and does not support weak and strong encryption types.

### Decryption

**Decryption** is the process of converting encrypted data back into its original form, so that the data can be read from the workbook. You can decrypt the workbook with the encrypted password. Note that XlsIO cannot open workbooks without knowing the password.

## API Reference

### Methods and Properties
- `PasswordToOpen`: Sets the password required to open the workbook.
- `SetWriteProtectionPassword`: Sets the password required to modify the workbook.
- `ReadOnlyRecommended`: Sets the workbook as read-only.

### Parameters
- `FileName`: The file name of the Excel workbook.
- `Password`: The password to decrypt the Excel workbook.

### Returns
- An `IWorkbook` object representing the decrypted Excel workbook.

### Exceptions
- Throws an exception if the password is incorrect.

## Code Examples

### C# Example

```csharp
using Syncfusion.XlsIO;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Initialize Excel Engine
        using (ExcelEngine excelEngine = new ExcelEngine())
        {
            IApplication application = excelEngine.Excel;
            application.DefaultVersion = ExcelVersion.Excel97to2003;

            // Create a new workbook
            IWorkbook workbook = application.Workbooks.Create(1);
            IWorksheet worksheet = workbook.Worksheets[0];

            // Encrypt the workbook
            workbook.PasswordToOpen = "syncfusion";
            workbook.SetWriteProtectionPassword("modify");
            workbook.ReadOnlyRecommended = true;

            // Save the workbook
            workbook.SaveAs("EncryptedWorkbook.xls", ExcelSaveType.Normal);

            // Close the workbook
            workbook.Close();
        }

        Console.WriteLine("Workbook encrypted and saved successfully.");
    }
}
```

### VB.NET Example

```vbnet
Imports Syncfusion.XlsIO
Imports System

Module Program
    Sub Main()
        ' Initialize Excel Engine
        Using excelEngine As New ExcelEngine()
            Dim application As IApplication = excelEngine.Excel
            application.DefaultVersion = ExcelVersion.Excel97to2003

            ' Create a new workbook
            Dim workbook As IWorkbook = application.Workbooks.Create(1)
            Dim worksheet As IWorksheet = workbook.Worksheets(0)

            ' Encrypt the workbook
            workbook.PasswordToOpen = "syncfusion"
            workbook.SetWriteProtectionPassword("modify")
            workbook.ReadOnlyRecommended = True

            ' Save the workbook
            workbook.SaveAs("EncryptedWorkbook.xls", ExcelSaveType.Normal)

            ' Close the workbook
            workbook.Close()
        End Using

        Console.WriteLine("Workbook encrypted and saved successfully.")
    End Sub
End Module
```

## Cross References
- See also: [Document Encryption and Protection](#document-encryption-and-protection) for more details on securing Excel documents.

## RAG Annotations
<!-- tags: [Essential XlsIO, Excel, Encryption, Decryption, File Handling] keywords: [workbook, password, read-only, modify, open, save, Excel document, security] -->
```