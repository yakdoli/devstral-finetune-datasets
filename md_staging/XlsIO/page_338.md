```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_338.jpeg
document_name: XlsIO
page_number: 338
page_id: XlsIO#page_338
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:28Z
fidelity: lossless
-->

## Essential XlsIO

```csharp
workbook.CalculationOptions.IsIterationEnabled = true;
workbook.CalculationOptions.MaximumIteration = 99;
workbook.CalculationOptions.MaximumChange = 40;
```

```vb
[VB.NET]

Dim workbook as IWorkbook
workbook = application.Workbooks.Create()
workbook.CalculationOptions.IsIterationEnabled = true;
workbook.CalculationOptions.MaximumIteration = 99;
Workbook.CalculationOptions.MaximumChange = 40;
```

### 4.4.2.2 Calculation Engine

Essential XlsIO has a calculation engine of its own and can compute the values of the formula entered during runtime. Essential Calculate is now [from v9.1.x.x] integrated with Essential XlsIO, and thus makes it possible to get the values of the formula entered by using XlsIO during runtime, without any additional references or packages. Currently, there are over 180+ functions that are supported by this Calculate engine, which cover all common usage scenarios.

#### Sample Link

To understand this process, consider the sample project:

{Drive:\\}\\Program Files\\EssentialStudio\\*.**.* \\Windows\\XlsIO.Windows\\Samples\\2.0\\Data Management\\Compute All Formulas.

### 4.4.2.2.1 Adding Calculation Engine to an Application

#### Enable Formula Calculations:

Essential XlsIO includes support for enabling the calculations of Essential Calculate supported formulas that are added at runtime to the worksheet. The computed value will be set to the "CalculatedValue" property associated to the "IRange" object. The following code sample illustrates how to enable the sheet formula calculations.

```csharp
[C#]
IWorksheet sheet = workbook.Worksheets[0];

//Formula calculation is enabled for the sheet.
sheet.EnableSheetCalculations();
string computedValue = sheet.Range["C1"].CalculatedValue;
```

#### Disable Formula Calculations:

---
```