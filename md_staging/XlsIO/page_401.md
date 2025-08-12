```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_401.jpeg
document_name: XlsIO
page_number: 401
page_id: XlsIO#page_401
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:08Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to protect and unprotect a chart sheet in XlsIO.
- Demonstrates using the `Protect` and `Unprotect` methods.
- Sample code in C# and VB.NET for both protection and unprotection.

## Content

### Protecting a Chart Sheet
The chart sheet can be protected using the `Protect` method, as shown below.

#### C#
```csharp
// Protect chart sheet.
chart.Protect("syncfusion");
```

#### VB.NET
```vb.net
' Protect chart sheet.
chart.Protect("syncfusion")
```

The protection can also be performed by using the enumerations in the code as shown below.

#### C#
```csharp
// Protect chart sheet.
chart.Protect("syncfusion", ExcelSheetProtection.Content);
```

#### VB.NET
```vb.net
' Protect chart sheet.
chart.Protect("syncfusion", ExcelSheetProtection.Content)
```

The chart sheet is protected. The content in the sheet cannot be edited.

### Removing protection of a Chart Sheet

You can remove the protection of a protected chart sheet by using the `Unprotect` method. Following code sample illustrates this.

#### C#
```csharp
// Unprotect chart sheet
chart.Unprotect("syncfusion");
```

#### VB.NET
```vb.net
' Unprotect chart sheet.
chart.Unprotect("syncfusion")
```

The protection of the chart sheet is removed.

## API Reference
- **Method**: `Protect(string password, ExcelSheetProtection options)`
  - **Parameters**:
    - `password`: The password to protect the chart sheet.
    - `options`: Enumerations to specify the protection options (e.g., `ExcelSheetProtection.Content`).
  - **Returns**: None.
  - **Description**: Protects the chart sheet with the given password and specified options.

- **Method**: `Unprotect(string password)`
  - **Parameters**:
    - `password`: The password used to unprotect the chart sheet.
  - **Returns**: None.
  - **Description**: Removes the protection from the chart sheet using the provided password.

## Code Examples
- Demonstrates both protecting and unprotecting a chart sheet using Syncfusion XlsIO.

<!-- tags: [XlsIO, chart sheet, protection, unprotection, ExcelSheetProtection] keywords: [protect, unprotect, chart sheet, password, enumeration] -->
```