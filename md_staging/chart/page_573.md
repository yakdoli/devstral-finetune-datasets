```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_573.jpeg
document_name: chart
page_number: 573
page_id: chart#page_573
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
toPostScript.Save("EditableTextChart.eps");
}
```

```vb
[VB]
Dim toPostScript As New ToPostScript()
toPostScript.EditableText = True

Using g As Graphics =
toPostScript.GetRealGraphics(Me.chartControl1.Size)
    Me.chartControl1.Draw(g, Me.chartControl1.Size)
    g.Dispose();
    toPostScript.Save("EditableTextChart.eps")
End Using
```

## Content

### Text Editing in Adobe Illustrator

The figure below shows the chart EPS image text editing in Adobe Illustrator.

## Page-level Navigation/TOC (if applicable)

- [unclear] chart text editing

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ToPostScript
  - **Method**: `Save(String fileName)`
    - **Parameters**: 
      - `fileName` (String): Specifies the file name and path where the chart should be saved.
    - **Returns**: None
    - **Exceptions**:
      - InvalidOperationException: If the chart is not valid or cannot be saved.

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart;
// ...
ToPostScript toPostScript = new ToPostScript();
toPostScript.EditableText = true;

using (Graphics g = toPostScript.GetRealGraphics(this.chartControl1.Size))
{
    this.chartControl1.Draw(g, this.chartControl1.Size);
    g.Dispose();
    toPostScript.Save("EditableTextChart.eps");
}
```

### VB Example

```vb
Imports Syncfusion.Windows.Forms.Chart
' ...
Dim toPostScript As New ToPostScript()
toPostScript.EditableText = True

Using g As Graphics = toPostScript.GetRealGraphics(Me.chartControl1.Size)
    Me.chartControl1.Draw(g, Me.chartControl1.Size)
    g.Dispose()
    toPostScript.Save("EditableTextChart.eps")
End Using
```

## Cross References

- For more information on saving charts in different formats, refer to the [Syncfusion Windows Forms Chart documentation](https://www.syncfusion.com/documentation/windows-forms-chart/).

## RAG Annotations

<!-- tags: [Syncfusion, Windows Forms, Chart, EPS, Text Editing, Adobe Illustrator] keywords: [chart, EPS, text editing, Adobe Illustrator, ToPostScript, Save, editable text] -->
```