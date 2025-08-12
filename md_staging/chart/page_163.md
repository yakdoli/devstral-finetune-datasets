```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: chart
page_number: 163
page_id: chart#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:55Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.sparkLine1.Type = SparkLine.SparkLineType.Column;
```

```vb
' Set Sparkline points to source property
Me.sparkLine1.Source = New Double() { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 }

' Set line type sparkline
Me.sparkLine1.Type = SparkLine.SparkLineType. Column
```

![Figure 90: Column SparkLine](https://user-images.githubusercontent.com/87379766/233811063-ffeda097-5b61-4262-9617-9a739f762a08.png)

**Figure 90: Column SparkLine**

## Drawing WinLoss Sparkline in an Application

The Winloss type of spark line is similar to the column type but all columns have equal length for data points. The vertical column direction represents the negative or positive value.

Refer to the following code snippets to draw the WinLoss sparkline:

```csharp
// Set Sparkline points to source property
this.sparkLine1.Source = new double[] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };

// Set line type sparkline
this.sparkLine1.Type = SparkLine.SparkLineType.WinLoss;
```

## API Reference

### SparkLineType.Enum
- **Column**: Used for representing column-based sparklines.
- **WinLoss**: Used for representing WinLoss-based sparklines.

### Suggested Code
- **Source Property**:
  - Type: `double[]`
  - Description: Specifies the data points for the spark line.
  - Example: `new double[] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 }`
- **Type Property**:
  - Type: `SparkLineType`
  - Description: Specifies the type of spark line to be drawn.
  - Example: `SparkLine.SparkLineType.WinLoss`

## Cross References

- See also:  
  - [SparkLine Documentation](#)
  - [WinForms Controls Overview](#)

<!-- tags: [chart, sparkline, windows forms, winloss] keywords: [winloss sparkline, column sparkline, data points, vertical columns, sparkline type, column type, sparkline source] -->
```