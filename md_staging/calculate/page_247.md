```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_247.jpeg
document_name: calculate
page_number: 247
page_id: calculate#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Understand how to read XLS files into Essential Calculate using Essential XlsIO.
- Learn methods to suspend calculations while updating values in ICalcData objects.

## Content

### 5.2.2 How To Read an XLS File Into Essential Calculate?
To get Essential Calculate to work with an XLS file requires Essential XlsIO. Essential ExcelRW is a library that exposes Excel-Like Automation APIs without any dependence upon Excel. It has the ability to Read / Write XLS files.

For details, see [Working with an Excel SpreadSheet](Working with an Excel SpreadSheet).

### 5.2.3 How To Suspend Calculations While a Series Of Values Are Updated?
You can use the property `CalcEngine.CalculationSuspended` to control the calculations that will be performed as values change in your ICalcData object.

#### Example in C#
```csharp
// Creates some data object that implements ICalcData.
this.data = new ArrayCalcData(a);

// Creates a CalcEngine object using this ICalcData object.
CalcEngine engine = new CalcEngine(this.data);
//...
// Turn off calculations.
engine.CalculationSuspended = true;

// Makes multiple updates to this.data somehow...
// Turn on calculations.
engine.CalculationSuspended = false;
```

#### Example in VB
```vb
' Creates some data object that implements ICalcData.
Me.data = New ArrayCalcData(a)

' Creates a CalcEngine object using this ICalcData object.
Dim engine As New CalcEngine(Me.data)

'...
' Turn off calculations.
```

## API Reference
### Methods
- `CalcEngine.CalculationSuspended`: A property to suspend or resume calculations.

### Parameters
- `ICalcData`: The data object that implements the ICalcData interface.

## Code Examples

#### C#
```csharp
this.data = new ArrayCalcData(a);
CalcEngine engine = new CalcEngine(this.data);
engine.CalculationSuspended = true;
// Multiple updates to this.data
engine.CalculationSuspended = false;
```

#### VB
```vb
Me.data = New ArrayCalcData(a)
Dim engine As New CalcEngine(Me.data)
engine.CalculationSuspended = True
' Multiple updates to Me.data
engine.CalculationSuspended = False
```

## See also
- [Working with an Excel SpreadSheet](Working with an Excel SpreadSheet)
- `CalcEngine`
- `ICalcData`

<!-- tags: [Syncfusion Winforms, Essential Calculate, XlsIO, ICalcData, CalcEngine, ExcelRW] keywords: [read XLS file, suspend calculations, Excel automation, Excel-like APIs, XlsIO library, Essential Calculate, ExcelSpreadSheet, CalculationSuspended] -->
```