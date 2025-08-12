```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_527.jpeg
document_name: grid
page_number: 527
page_id: grid#page_527
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:27Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.1.4.30.2 Data Handling

### Example:

This example will step you through the following three ways of populating an Essential Grid:

- The first technique just loops through the cells and uses an indexer on the Grid control to set the values.
- The second uses the PopulateValues method that optimally places data from a data source into a grid range.
- The third technique uses an Essential Grid in a virtual manner.

You can specify the size of the grid that is to be populated while running the sample and then you can try all the three methods to compare the performance. However, the .NET Framework JIT slows the first population owing to one-time jitting of the code.

### 1. Using Indexer

This technique loops through the cells and uses an indexer on the Grid control to set the values.

#### a. Using C#

```csharp
[C#]

for (int i = 0; i < this.numArrayRows; ++i)
   for (int j = 0; j < this.numArrayCols; ++j)
        this.gridControl[i + 1, j + 1].CellValue = this.intArray[i, j];
```

#### b. Using VB.NET

```vb.net
[VB.NET]

For i As Integer = 0 To Me.numArrayRows - 1
   For j As Integer = 0 To Me.numArrayCols - 1
        Me.gridControl(i + 1, j + 1).CellValue = Me.intArray(i, j)
        Next j
Next i
```

### 2. Populating Values
```html
<!-- tags: [Essential Grid, Windows Forms, data handling, grid, populate values, indexer, virtual grid, performance comparison] keywords: [Essential Grid, Windows Forms, data handling, grid population, virtual grid, performance comparison, indexer, PopulateValues method] -->
```