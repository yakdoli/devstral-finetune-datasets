```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: grid
page_number: 165
page_id: grid#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explores the features of Grid cells, particularly the Month Calendar and Numeric Up Down CellTypes.
- Demonstrates how to set up NumericUpdownCellInfo with example code snippets.

## Content

### Month Calendar Cells

![Figure 86: Month Calendar Cells](#)

### 4.1.4.1.11 Numeric Up Down

A **NumericUpDown CellType** lets you input numeric data either by editing the displayed text or by using spinner buttons to increase or decrease the displayed value. As your value hits a limit, you can either have it stick at that limit or wrap to the opposite limiting value. To hold information such as the upper and lower limits, Essential Grid uses a **GridNumericUpDownCellInfo** object whose constructor accepts the parameters used in the control. This is illustrated in the following code.

#### Example Code

##### C#

```csharp
// Set up a NumericUpDown Control and set up upper and lower limits.
public GridNumericUpDownCellInfo(int min, int max, int start, int step, bool wrap)
```

##### VB.NET

```vb
' Set up a NumericUpDown Control and set up upper and lower limits.
Public Sub New(min As Integer, max As Integer, start As Integer, step1 As Integer, wrap As Boolean)
```

![Figure 87: Numeric Up Down Cells](#)

## API Reference

### GridNumericUpDownCellInfo

- **Parameters**:
  - `min`: Integer representing the minimum value.
  - `max`: Integer representing the maximum value.
  - `start`: Integer representing the starting value.
  - `step`: Integer representing the step size.
  - `wrap`: Boolean indicating whether to wrap numeric values when a limit is reached.

### Methods and Properties

- **Properties**:
  - `Minimum`: Gets or sets the minimum value of the Numeric Up Down cell.
  - `Maximum`: Gets or sets the maximum value of the Numeric Up Down cell.
  - `Value`: Gets or sets the current value of the Numeric Up Down cell.
  - `Increment`: Gets or sets the step size when the spinner buttons are used.
  - `Wrap`: Gets or sets whether the value wraps around when the limit is reached.

## Code Examples

### C#

```csharp
GridNumericUpDownCellInfo cellInfo = new GridNumericUpDownCellInfo(0, 100, 50, 1, false);
gridModel[0, 0].CellInfo = cellInfo;
```

### VB.NET

```vb
Dim cellInfo As New GridNumericUpDownCellInfo(0, 100, 50, 1, False)
gridModel(0, 0).CellInfo = cellInfo
```

## RAG Annotations
<!-- tags: [GridNumericUpDownCellInfo, CellType, MonthCalendarCell, NumericUpDown, SpinnerButtons, UpperLowerLimits, Wrap, SyncfusionWinforms, ControlSetup] keywords: [Grid, NumericUpDown, MonthCalendar, CellType, UpperLimit, LowerLimit, Wrap, Spinner, Control, Setup, C#, VB.NET] -->
```