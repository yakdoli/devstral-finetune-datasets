```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_430.jpeg
document_name: XlsIO
page_number: 430
page_id: XlsIO#page_430
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:20Z
fidelity: lossless
-->

# `Essential XlsIO`

## Overview

- Demonstrates how to print Title Rows and Title Columns using XlsIO in a spreadsheet.
- Explains how to unfreeze rows and columns in XlsIO using the `RemovePanes` method.

## Content

### Printing Title Rows

The following code illustrates printing Title Rows.

```csharp
[C#]
// Print Rows 1 to 3.
sheet.PageSetup.PrintTitleRows = "$A$1:$IV$3";
```

```vb.net
[VB.NET]
' Print Rows 1 to 3.
sheet.PageSetup.PrintTitleRows = "$A$1:$IV$3"
```

### Printing Title Columns

The following code illustrates printing Title Columns.

```csharp
[C#]
// Print Columns 1 to 3.
sheet.PageSetup.PrintTitleColumns = "$A$1:$C$65536";
```

```vb.net
[VB.NET]
' Print Columns 1 to 3.
sheet.PageSetup.PrintTitleColumns = "$A$1:$C$65536"
```

For information on Print settings, refer to section **4.3.3.1 Print Settings**.

### 5.1.13 How to unfreeze the rows and columns in XlsIO?

You can unfreeze rows and columns in XlsIO by using the `RemovePanes` method. The following code example illustrates this.

```csharp
[C#]
sheet.Range[8, 1].FreezePanes();
```

<!-- tags: [XlsIO, Print Settings, PrintTitleRows, PrintTitleColumns, RemovePanes, Unfreeze Rows, Unfreeze Columns] keywords: [Essential XlsIO, Print Settings,冻, unfreeze rows, unfreeze columns, RemovePanes method, PrintTitleRows, PrintTitleColumns, sheet.PageSetup, Excel, C#, VB.NET] -->
```