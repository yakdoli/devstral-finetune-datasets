```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: calculate
page_number: 061
page_id: calculate#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:24Z
fidelity: lossless
-->

## Displaying Data with SumColumns and SumRows

### Overview
- Demonstrates how to display a double array with sums for columns and rows.
- Shows how to update the displayed data dynamically.
- Allows setting a specific value in the data array to observe the effects on sums.

### Implementation

```vb
Dim j As Integer

For j = 0 To Me.nCols
    Me.TextBox1.Text += Me.data(i, j).ToString() + ControlChars.Tab
Next
Me.TextBox1.Text += ControlChars.Cr + ControlChars.Lf
```

### Display Example

Here is a typical display you might see if you run the application at this point. Recall that the data is random, so you may see fewer or more rows and columns. The column on the right is the sum of the columns that precede it in the same row. The row at the bottom is the sum of the columns above it. You can click the **Generate Data** button several times to see different data.

![Figure 27: Sample Display Showing Double Array, SumColumn and SumRow](https://i.imgur.com/ramdomimage.jpg)

### Set Button Functionality

The Set button allows you to set a particular value in the displayed data so you can see the effect of changing this value on the calculations in the last row and last column. Recall that your data store is mimicking an array of doubles, so it indexes from zero even though the `ICalcData` interface expects one-based indexing. The implementation code takes this into account.

## API Reference

### Properties
- `data`: The array of double values displayed.
- `nCols`: The number of columns in the data array.

### Methods
- `SetData(row As Integer, col As Integer, value As Double)`: Updates the data array with the specified value at the given row and column indices.

## Code Examples

```vb
' Example usage of SetData
Me.SetData(0, 0, 123)
```

## Cross References

- See also: `ICalcData` interface for data manipulation.

<!-- tags: [syncfusion, windowsforms, icalcdata, data array, sum columns, sum rows] keywords: [random data, display, set button, data manipulation] -->
```