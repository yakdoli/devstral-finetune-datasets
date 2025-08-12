```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: XlsIO
page_number: 190
page_id: XlsIO#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:54Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This section explains how to hide and unhide rows and columns in XlsIO using the `ShowRow` and `ShowColumn` methods.
- Demonstrates example code snippets for hiding and unhiding specific rows and columns in both C# and VB.NET.

## Content

### Hiding and Unhiding Rows in XlsIO

XlsIO provides support for hiding/unhiding rows and columns. This can be done by using `ShowRow` and `ShowColumn` methods.

#### C#

```csharp
// Hiding the First Column and Second Row.
sheet.ShowColumn( 1, false );
sheet.ShowRow( 2, false );

// Hiding the Fifth Column and Fifth Row.
sheet.ShowColumn( 5, false );
sheet.ShowRow( 5, false );

// Unhiding the Fifth Column and Second Row.
sheet.ShowColumn( 5, true );
sheet.ShowRow( 2, true );
```

#### VB.NET

```vbnet
' Hiding the First Column and Second Row.
sheet.ShowColumn(1, False)
sheet.ShowRow(2, False)

' Hiding the Fifth Column and Fifth Row.
sheet.ShowColumn(5, False)
sheet.ShowRow(5, False)

' Unhiding the Fifth Column and Second Row.
```

<!-- tags: [XlsIO, hiding rows, unhiding rows, VB.NET, C#] keywords: [hide rows, unhide rows, ShowColumn, ShowRow, Excel, XlsIO] -->
```