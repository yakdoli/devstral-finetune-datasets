```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_423.jpeg
document_name: XlsIO
page_number: 423
page_id: XlsIO#page_423
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:15Z
fidelity: lossless
-->

# Essential XlsIO

## 5 Frequently Asked Questions

This section contains questions that are frequently asked pertaining to Essential XlsIO and answers for the corresponding questions. This section is divided into two bases on the level of the user:

- Common-This section contains most common questions and answers for beginners of XlsIO.
- Advanced-This section contains various questions and answers at the Advanced level.

### 5.1 Common

This section contains most common questions and answers for beginners of XlsIO.

#### 5.1.1 How to change the grid line color of the Excel sheet?

You can change the grid line color of the Excel worksheet by using the ExcelKnownColors property. The following code example illustrates this.

```csharp
[C#]
sheet.GridLineColor = ExcelKnownColors.Blue;
```

```vbnet
[VB.NET]
sheet.GridLineColor = ExcelKnownColors.Blue
```

#### 5.1.2 How to copy and paste the values of the cells that contain only formulas?

You can copy and paste the values of the cells that contain only formulas by setting ExcelCopyRangeOptions of the CopyTo method to None. The following code example illustrates this.

```csharp
[C#]
```

<!-- tags: [XlsIO, Syncfusion, Excel, Winforms, Essential XlsIO, FAQ, Common, Advanced, Grid line color, ExcelKnownColors, Copy and paste, formulas, version 11.4.0.26] keywords: [XlsIO, Excel, grid line color, formulas, cell values, copy and paste, ExcelKnownColors, C#, VB.NET, Syncfusion Winforms] -->
```