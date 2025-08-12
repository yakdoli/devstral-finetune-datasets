```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: calculate
page_number: 059
page_id: calculate#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:58Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Creates a `CalcEngine` object using `this.ArrayCalcData`.
- Enables dependency tracking for immediate value updates.
- Recalculates the specified range to compute formulas.
- Displays the `ArrayCalcData` values in a text box.

## Content

### Using ArrayCalcData in WinForms

The following code demonstrates how to use the `ArrayCalcData` class to create a `CalcEngine`, enable dependency tracking, and display the calculated values in a `TextBox`.

#### C# Example

```csharp
// Creates a CalcEngine object using this ArrayCalcData object.
CalcEngine engine = new CalcEngine(this.data);

// Turns on dependency tracking so that values set with the Set button take effect immediately.
engine.UseDependencies = true;

// Calls RecalculateRange so any formulas in the data can be initially computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data);

ShowObject();
}

/// <summary>
/// Displays the ArrayCalcData values in a text box.
/// </summary>
private void ShowObject()
{
    this.textBox1.Text = "";
    for (int i = 0; i <= this.nRows; ++i)
    {
        for (int j = 0; j <= this.nCols; ++j)
        {
            this.textBox1.Text += this.data[i, j].ToString() + "\t";
        }
        this.textBox1.Text += "\r\n";
    }
}
```

#### VB Example

```vb
Imports Syncfusion.Calculate

'...

Private r As New Random
Private data As ArrayCalcData
Dim nRows As Integer
Dim nCols As Integer

' <summary>
' Populates the double array.
```

## Code Examples

The provided C# and VB examples show how to create and use a `CalcEngine` with `ArrayCalcData`. The `CalcEngine` is initialized with the `ArrayCalcData` object, and dependency tracking is enabled to ensure immediate updates. The `RecalculateRange` method is called to compute any formulas in the data. Finally, the calculated values are displayed in a `TextBox`.

<!-- tags: [syncfusion, winforms, arraycalldata, calcengine, dependencytracking] keywords: [arraycalcdata, calcengine, recalculation, dependency tracking, textbox] -->
```