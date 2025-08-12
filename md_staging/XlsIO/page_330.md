```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_330.jpeg
document_name: XlsIO
page_number: 330
page_id: XlsIO#page_330
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:59Z
fidelity: lossless
-->

## Essential XlsIO

```csharp
sheet.Range["A137"].Text = "TYPE({150,2,3,4,5,20})";
sheet.Range["B137"].Formula = "TYPE({150,2,3,4,5,20})";

sheet.Range["A138"].Text = "UPPER(B7)";
sheet.Range["B138"].Formula = "UPPER(B7)";

sheet.Range["A139"].Text = "VAR(A3:A8)";
sheet.Range["B139"].Formula = "VAR(A3:A8)";

sheet.Range["A140"].Text = "VARA(A3:A8)";
sheet.Range["B140"].Formula = "VARA(A3:A8)";

sheet.Range["A141"].Text = "VARPA(A3:A8)";
sheet.Range["B141"].Formula = "VARPA(A3:A8)";

sheet.Range["A142"].Text = "VDB(A3,A4,A5,0,1)";
sheet.Range["B142"].Formula = "VDB(A3,A4,A5,0,1)";

sheet.Range["A143"].Text = "ZTEST(A3:A8,4)";
sheet.Range["B143"].Formula = "ZTEST(A3:A8,4)";

sheet.Range["A144"].Text = "ZTEST({150,100,200,300,500,0.3},4)";
sheet.Range["B144"].Formula = "ZTEST({150,100,200,300,500,0.3},4)";
```

**Figure 118: Formula Settings**

Note that formula separators vary for each culture/regional settings, and there will be exceptions in such cases. This can be overcome by setting the separators by using the `SetSeparators` method of `IWorkbook`. Following code example illustrates how to change the formula separators through XlsIO.

### Setting Formula Separators

#### [C#]

```csharp
Workbook.SetSeparators(";", ", ");
```

- **Sheet1 and Sheet2** are the default names of the worksheets.

#### [VB.NET]

---

<!-- tags: [product, syncfusion-sdk, essentialxlsio, formula settings, xslio, api, workbook, separators, language: en, 11.4.0.26] keywords: [formula separators, SetSeparators, IWorkbook, culture settings, exceptions, XlsIO,Syncfusion Winforms] -->
```