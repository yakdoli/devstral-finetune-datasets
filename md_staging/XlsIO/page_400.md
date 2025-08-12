```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_400.jpeg
document_name: XlsIO
page_number: 400
page_id: XlsIO#page_400
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:07Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Overview of worksheet protection and unprotection using passwords.
- Description of how to protect and unprotect chart sheets using specific methods in XlsIO.

---

## Content

### Protecting and Unprotecting Worksheets

You can also unprotect the worksheet by using the `Unprotect` method of XlsIO. It allows the user to remove the restriction added to worksheet elements.

#### Code Example: Removing Worksheet Protection

**C#**
```csharp
// Unprotecting (unlocking) the Worksheet using the Password.
sheet.Unprotect("syncfusion");
```

**VB.NET**
```vb.net
' Unprotecting (unlocking) the Worksheet using the Password.
sheet.Unprotect("syncfusion")
```

### Chart Sheet Protection

Essential XlsIO now provides support to protect or unprotect a chart sheet.

#### a) Protecting a Chart Sheet

XlsIO provides options to protect chart sheets by using the `Protect` method. This method allows you to protect selected elements in a worksheet, so that they cannot be modified.

By using the `ExcelSheetProtection` enumeration, you can set the elements that need protection.

##### Code Example: Protecting a Chart Sheet (with password)

The password chosen in the code sample below is "syncfusion".

**C#**
```csharp
// Example for protecting a chart sheet using ExcelSheetProtection enumeration.
// The code will choose default enumerations "Contents" and "Objects".
sheet.Protect("syncfusion");
```

### Notes on Chart Sheet Protection
- This default call will protect the chart for **Contents** and **Objects**.
- You can also choose protection by using the overload.
- The code mentioned below will choose default enumerations "Contents" and "Objects". The password chosen in the code sample below is "syncfusion".

---

## Page-level Navigation/TOC (if applicable)
- [Worksheet Protection and Unprotection](#protecting-and-unprotecting-worksheets)
- [Chart Sheet Protection](#chart-sheet-protection)
  - [a) Protecting a Chart Sheet](#a-protecting-a-chart-sheet)

## Cross References
See also:
- Related documentation on worksheet and chart sheet modifications.
- Additional features and methods in XlsIO for worksheet security.

<!-- tags: [worksheet protection, chart sheet protection, XlsIO, VB.NET, C#, Syncfusion, Winforms] keywords: [password, protect, unprotect, chart sheet, worksheet protection, ExcelSheetProtection] -->
```