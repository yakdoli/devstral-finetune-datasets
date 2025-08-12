```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_246.jpeg
document_name: calculate
page_number: 246
page_id: calculate#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- This page demonstrates how to force calculations to be processed after `Engine.CalculatingSuspended` has been set to `true`.
- Covers both C# and VB.NET implementations.

## Content

To illustrate the process of calculating calculations after setting `Engine.CalculatingSuspended` to `true`, the following code samples in C# and VB.NET are provided:

### C#

```csharp
// Creates some data object that implements ICalcData.
this.data = new ArrayCalcData(a);

// Creates a CalcEngine object using this ICalcData object.
CalcEngine engine = new CalcEngine(this.data);

// Turn off calculations.
engine.CalculatingSuspended = true;

// Makes multiple updates to this.data.
// Turn on calculations.
engine.CalculatingSuspended = false;

// Calls RecalculateRange so any formulas in the data can be computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data);
```

### VB.NET

```vb
' Creates some data object that implements ICalcData.
Me.data = New ArrayCalcData(a)

' Creates a CalcEngine object using this ICalcData object.
Dim engine As New CalcEngine(Me.data)

' Turn off calculations.
engine.CalculatingSuspended = True

' Makes multiple updates to this.data.
' Turn on calculations.
engine.CalculatingSuspended = False

' Calls RecalculateRange so any formulas in the data can be computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), Data)
```

## Cross References

- See also: [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation) for more details on the `CalcEngine` and `ICalcData` interfaces.

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, CalcEngine, ICalcData, calculations, suspended, recalculateRange, C#, VB.NET] keywords: [calculations, suspended, recalculateRange, CalcEngine, ICalcData, Engine, Async, Data, Range] -->
```