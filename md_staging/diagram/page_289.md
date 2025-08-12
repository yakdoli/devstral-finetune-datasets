```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: diagram
page_number: 289
page_id: diagram#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:31Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
End Sub
Protected Overrides Sub GetObjectData(ByVal info As SerializationInfo, ByVal context As StreamingContext)
    MyBase.GetObjectData(info, context)

    ' Additional member variables are serialized here.
    info.AddValue("strDescription", Me.NodeInformation)
End Sub
End Class
```

## How To Set the Custom Position For a Label

We can adjust the label position by setting the **Position** property as 'Custom'. Then, we have to set the Offset values for the X and Y coordinates to specify the label position.

### C#

```csharp
// Setting custom position for a label
outerRect.Labels.Add(new Syncfusion.Windows.Forms.Diagram.Label());
outerRect.Labels[0].Text = "Rectangle";
outerRect.Labels[0].Position = Position.Custom;
outerRect.Labels[0].OffsetX = 50;
outerRect.Labels[0].OffsetY = 65;
```

### VB.NET

```vb
' Setting custom position for a label
outerRect.Labels.Add(New Syncfusion.Windows.Forms.Diagram.Label())
outerRect.Labels(0).Text = "Rectangle"
outerRect.Labels(0).Position = Position.Custom
outerRect.Labels(0).OffsetX = 50
outerRect.Labels(0).OffsetY = 65
```

## How To Protect Links From User Selection / Manipulation
<!-- tags: [diagram, windows forms, label position, custom offsets, link protection, user selection, manipulation, syncfusion winforms, 11.4.0.26] keywords: [label, custom position, offset, position custom, protect links, user selection, manipulation] -->
```