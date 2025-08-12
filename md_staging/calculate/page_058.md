```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: calculate
page_number: 058
page_id: calculate#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:18Z
fidelity: lossless
-->

# Essential Calculate

```csharp
SetValueRowCol(Value, row + 1, col + 1)
End Set
End Property
```

## Overview
- This section explains how the "Generate Data" button handler creates a random double array and populates it with random double values.
- It discusses the creation of an `ArrayCalcData` class to wrap the double array and the creation of a `CalcEngine` object using this `ArrayCalcData` object as the datasource.
- The `ShowObject` method is used to display the values from the `ArrayCalcData` object in a multiline text box.
- The `UseDependencies` property in the engine allows automatic recalculations when dependent values change.
- The `RecalculateRange` method helps the `CalcEngine` traverse all data and set up necessary dependencies.

## Content

### Implementation Details

11. Your **Generate Data** button handler will create a random double array and populate it with random double values. It also creates an instance of an `ArrayCalcData` class to wrap the double array that it creates. It then creates a `CalcEngine` object that uses this `ArrayCalcData` object as its datasource. The **ShowObject** method will just display the values from your `ArrayCalcData` object in the multiline text box that you added to the form.

The engine's **UseDependencies** property will tell the `CalcEngine` that you want it to track dependencies so the value will automatically recalculate when dependent values change. The engine's **RecalculateRange** call allows the `CalcEngine` to traverse all the data and set up the necessary dependencies to do the calculations.

### Code Example

Here is the code:

```csharp
[C#]

using Syncfusion.Calculate;

//..

private Random r = new Random();
private ArrayCalcData data;
int nRows;
int nCols;

/// <summary>
/// Populates the double array.
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
private void button1_Click(object sender, System.EventArgs e)
{
    // Creates some sample data.
    this.nRows = r.Next(10) + 2;
    this.nCols = r.Next(3) + 1;
    double[,] a = new double[nRows, nCols];
    for (int row = 0; row < nRows; ++row)
        for (int col = 0; col < nCols; ++col)
            a[row, col] = ((double)r.Next(100)) / 10;

    // Creates an ArrayCalcData object and passes it in this array.
    this.data = new ArrayCalcData(a);
}
```

<!-- tags: [syncfusion, winforms, generate data, arraycalcdata, calcengine, usedependencies, recalculaterange, random array, button click event, multiline text box] -->
```