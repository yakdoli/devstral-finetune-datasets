```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: calculate
page_number: 050
page_id: calculate#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:33Z
fidelity: lossless
-->


## Essential Calculate

If you notice, you are actually populating these added arrays with formula strings such as "=Sum(A5:D5)". While using Essential Calculate with an ICalcData interface, Essential Calculate uses Excel-like notation to refer to the cells in a rectangular collection. A1 is the first cell in the first row, B1 is second cell in the first row, and so on. So, "=Sum(A5:D5)" sums columns 1 through 4 in row 5. The method **RangeInfo.GetAlphaLabel** used in the code, converts a numerical value like 1, 2, or 3, into the proper column letter A, B, or C.

## Content

### Wrapping the Double Array with Calculated Sums

The following code demonstrates how to wrap a double array with an extra row and column that holds calculated sums.

#### C#

```csharp
/// <summary>
/// Wraps the double array with an extra row and column that holds calculated sums.
/// </summary>
/// <param name="dValues"></param>
public ArrayCalcData(double[,] dValues)
{
    this.dValues = dValues;
    rowCount = dValues.GetLength(0);
    colCount = dValues.GetLength(1);
    rowSums = new object[rowCount + 1];
    colSums = new object[colCount + 1];

    // Initializes the formulas for the row sums.
    // eg. "=Sum(A5:D5)"   to sum row 5
    for (int row = 0; row <= rowCount; ++row)
    {
        rowSums[row] = string.Format("=Sum(A{1}:{0}{1})", 
                                      RangeInfo.GetAlphaLabel(colCount), row + 1);
    }

    // Initializes the formulas for the column sums.
    // eg. "=Sum(B1:B5)"   to sum column 2
    for (int col = 0; col <= colCount; ++col)
    {
        colSums[col] = string.Format("=Sum({0}1:{0}{1})", 
                                      RangeInfo.GetAlphaLabel(col + 1), rowCount);
    }
}
```

#### VB

```vb
' <summary>
' Wraps the double array with an extra row and column that holds calculated sums.
' </summary>
' <param name="dValues"></param>
Public Sub New(ByVal dValues(,) As Double)
    Me.dValues = dValues
    rowCount = dValues.GetLength(0)
    colCount = dValues.GetLength(1)
    rowSums = New Object(rowCount + 1) {}
```

### Explanation

- **dValues**: The double array containing the input data.
- **rowCount**: The number of rows in the input array.
- **colCount**: The number of columns in the input array.
- **rowSums** and **colSums**: Arrays to hold the formulas for row and column sums, respectively.

The `RangeInfo.GetAlphaLabel` method is used to convert column indices (numerical values) into corresponding Excel-style column labels (e.g., A, B, C, etc.). This ensures that the formulas generated are compatible with Excel-like notation used in Essential Calculate.

## RAG Annotations
<!-- tags: [Essential Calculate, Excel-like notation, ICalcData interface, RangeInfo.GetAlphaLabel, formula strings, array calculations] keywords: [Excel-like notation, row sums, column sums, formula strings, rectangular collection, array manipulation] -->
```