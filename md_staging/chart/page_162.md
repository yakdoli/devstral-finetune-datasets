```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: chart
page_number: 162
page_id: chart#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.sparkLine1.Source = new double[] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };
// Set line type sparkline
this.sparkLine1.Type = SparkLine.SparkLineType.Line;
```

### VB.NET

```vb
' Set Sparkline points to source property
Me.sparkLine1.Source = New Double() {30, -20, 80, 20, 40, -50, -30, 70, -40, 50}

' Set line type sparkline
Me.sparkLine1.Type = SparkLine.SparkLineType.Line
```

![Line SparkLine](https://via.placeholder.com/150x100?text=Figure%2089:%20Line%20SparkLine)

## Drawing Column Sparkline in an Application

The column type of spark line represents each data point by a column. The vertical column direction represents the negative or positive value.

Refer to the following code snippets to draw the column sparkline:

### C#.NET

```csharp
// Set Sparkline points to source property
this.sparkLine1.Source = new double[] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };
// Set line type sparkline
```

## API Reference (if applicable)

### Properties
- `Source`: Specifies the data points for the sparkline.
- `Type`: Specifies the type of sparkline to render.

### Methods
- `Update()`: Updates the sparkline based on the current data source.

### Events
- `PropertyChanged`: Triggered when a property of the sparkline is changed.

## Code Examples (multi-language supported)

#### C# Example
```csharp
sparkLine1.Source = new double[] { 30, -20, 80, 20, 40, -50, -30, 70, -40, 50 };
sparkLine1.Type = SparkLine.SparkLineType.Line;
```

#### VB.NET Example
```vb
Me.sparkLine1.Source = New Double() {30, -20, 80, 20, 40, -50, -30, 70, -40, 50}
Me.sparkLine1.Type = SparkLine.SparkLineType.Line
```

### WinForms-specific conventions
- Ensure that the source array is properly defined with double data types.
- Use the `Update()` method if data needs to be refreshed.

## RAG Annotations

<!-- tags: [windowsforms, chart, sparkline, line, column, data visualization] keywords: [source property, line type, data points, negative value, positive value, column type, sparkline, drawing, column sparkline, C#, VB.NET] -->
```