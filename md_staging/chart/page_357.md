```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: chart
page_number: 357
page_id: chart#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Specific Data Point Setting

ToolTipFormat can be applied for individual points by using Series.Styles[0].ToolTipFormat property settings.

### Code Examples

#### C#
```csharp
for (int i = 0; i < series1.Points.Count; i++)
{
    series1.SeriesStyles[i].ToolTipFormat = "{0}";
}
```

#### VB
```vb
Dim i As Integer = 0
Do While i < series1.Points.Count
    series1.SeriesStyles(i).ToolTipFormat = "{0}"
    i += 1
Loop
```

### Illustration

![Figure 226: ToolTip Format set for Data Point in a Series](https://via.placeholder.com/600x300?text=Illustrates+TooltipFormat)

**Figure 226: ToolTip Format set for Data Point in a Series**

## See Also

### References

```
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [product, module, control, api, version?] keywords: [ToolTipFormat, Series, Styles, individual points, Windows Forms, Syncfusion Winforms] -->
```