```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_399.jpeg
document_name: XlsIO
page_number: 399
page_id: XlsIO#page_399
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:43Z
fidelity: lossless
-->

## Unprotecting Workbook

### C#

```csharp
// Unprotect workbook.
// Opening an Existing (Protected) Workbook.
IWorkbook workbook = application.Workbooks.Open(@"ProtectedWorkbook.xls");

// Unprotecting (unlocking) Workbook by using the Password.
workbook.Unprotect("syncfusion");
```

### VB.NET

```vbnet
' Unprotect workbook.
' Opening an Existing (Protected) Workbook.
Dim workbook As IWorkbook = application.Workbooks.Open("ProtectedWorkbook.xls")

' Unprotecting (unlocking) Workbook by using the Password.
workbook.Unprotect("syncfusion")
```

## 4.6.2.2 Worksheet Protection

### Overview

- Prevent unauthorized users from making changes to specific elements in an Excel workbook when sharing and collaborating on files.

### Key Features

- Excel allows protection of worksheets and provides options to specify which elements users can modify when a worksheet is protected.
- Access protection options through the **Tools** menu by selecting the **Protection** option.

### Worksheet Protection with XlsIO

- **XlsIO** supports both protecting and unprotecting elements in worksheets using the `Protect` method of the **Worksheet** class.
- Use the `ExcelSheetProtection` enumerator to specify the elements that need protection.

### Code Example: Protecting a Worksheet

The following code demonstrates how to protect a worksheet with a password, restricting formatting columns in the worksheet.

```csharp
// Protecting the Worksheet by using a Password.
sheet.Protect("syncfusion", ExcelSheetProtection.FormattingColumns);
```

## Explanation

- **Protect Method**: The `Protect` method is used to secure a worksheet, ensuring that specified elements cannot be altered without the correct password.
- **ExcelSheetProtection Enumerator**: This enumerator specifies the types of protection, such as preventing users from formatting columns.
- **Password**: A password is required to both protect and unprotect the worksheet, enhancing file security.

## Conclusion

Using XlsIO, developers can effectively protect specific elements in Excel workbooks, ensuring controlled collaboration and data integrity.

## API Reference

### ExcelSheetProtection Enumerator

- **FormattingColumns**: Restricts users from formatting columns in the worksheet.

### Methods

- **Protect(string password, ExcelSheetProtection options)**:  
  **Parameters**:  
  - `password`: The password required to protect the worksheet.  
  - `options`: The specific elements to protect, defined using the `ExcelSheetProtection` enumerator.  
  **Description**: Secures the worksheet based on the specified password and options.

## Code Examples

### C#

```csharp
sheet.Protect("syncfusion", ExcelSheetProtection.FormattingColumns);
```

## Page-level Navigation/TOC

- Unprotecting Workbook
- Worksheet Protection
  - Overview
  - Key Features
  - Worksheet Protection with XlsIO
  - Code Example: Protecting a Worksheet
  - Explanation
  - Conclusion
  - API Reference
  - Code Examples

## Cross References

- **Relevant Topics**:
  - Data Protection in Excel
  - Collaborative Excel Usage
  - Excel Sheet Security Features

## RAG Annotations

```html
<!-- tags: [XlsIO, workbook protection, worksheet protection, ExcelSheetProtection, password protection, Syncfusion Winforms, Excel] keywords: [unprotect, protect, password, Excel, collaboration, data integrity, security] -->
```
```