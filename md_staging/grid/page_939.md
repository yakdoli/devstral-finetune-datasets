```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_939.jpeg
document_name: grid
page_number: 939
page_id: grid#page_939
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

With `XmlSerialization`, the grid schema information can be converted into Xml format. Grouping Grid provides two methods to support Xml Serialization.

- `WriteXmlSchema` - It writes the engine settings into an Xml stream (Serialization).
- `ApplyXmlSchema` - It loads the engine settings from an Xml stream (Deserialization).

All the grid elements can be serialized. Not only the data but also the look and feel of the grid can be serialized and deserialized. The following code example best illustrates this process.

## Example

1. Setup a grouping grid and load it with some data. Save the initial state of the grid schema so that it could be used to reset the grid.

### C#

```csharp
// Knowing the initial state.
System.IO.MemoryStream stream;
stream = new System.IO.MemoryStream();
this.gridGroupingControl.WriteXmlSchema(new XmlTextWriter(stream, null));
```

### VB.NET

```vb
' Knowing the initial state.
Private stream As System.IO.MemoryStream
stream = New System.IO.MemoryStream()
Me.gridGroupingControl1.WriteXmlSchema(New XmlTextWriter(stream, Nothing))
```

2. Apply the look and feel properties that you desire.

### C#

```csharp
// Customize the Appearance.
this.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue;
this.gridGroupingControl1.TableOptions.GridLineBorder = new GridBorder(GridBorderStyle.Solid, Color.FromArgb(208, 215, 229), GridBorderWeight.Thin);
this.gridGroupingControl1.TopLevelGroupOptions.ShowCaption = false;
this.gridGroupingControl1.Appearance.AnyCell.Font.Name = "Verdana";
this.gridGroupingControl1.Appearance.AnyCell.TextColor = Color.MidnightBlue;
this.gridGroupingControl1.TableDescriptor.Appearance.AlternateRecordFie
```

<!-- tags: [Syncfusion Winforms, Essential Grid, XmlSerialization, Grid Grouping] keywords: [XmlSerialization, engine settings, look and feel, resets, properties, appearance, data, Grouping Grid, Visual Studio] -->
```