```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_942.jpeg
document_name: grid
page_number: 942
page_id: grid#page_942
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:43Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Reset Grid

```csharp
// Reset Grid.
private void reset_Click(object sender, System.EventArgs e)
{
    System.IO.MemoryStream stream2 = new
    System.IO.MemoryStream(stream.ToArray());
    this.gridGroupingControl1.ApplyXmlSchema(new 
    XmlTextReader(stream2));
}
```

```vbnet
' Reset Grid.
Private Sub reset_Click(ByVal sender As Object, ByVal e As
System.EventArgs) Handles reset.Click
    Dim stream2 As System.IO.MemoryStream = New
    System.IO.MemoryStream(stream.ToArray())
    Me.gridGroupingControl1.ApplyXmlSchema(New 
    XmlTextReader(stream2))
End Sub
```

### Instructions

1. **Serialization and Reset Process**:
   - While running the sample, click the **Serialize** button and save the grid schema into an Xml file.
   - Then click the **Reset** button to switch the grid to its default state. This action removes all the appearance settings done in the first step.
   - You can also make changes in the `TableDescriptor` of the grid manually, such as rearranging columns through drag and drop. After reloading the grid schema, you will notice that the entire grid schema has been serialized.
   - Reloading will transform the grouping grid back to the state before serialization.

## API Reference

- **gridGroupingControl1.ApplyXmlSchema**
  - **Parameters**:
    - `XmlTextReader` object derived from a MemoryStream.
  - **Description**: Applies the specified XML schema to the grid control, resetting its configuration to the serialized state.

## Code Examples

### C# Example

```csharp
// Example usage of ApplyXmlSchema
using System.IO;

// Serialize and reset sequence
// Serialize the grid schema
// ...
// Reset the grid using the serialized schema
System.IO.MemoryStream stream2 = new System.IO.MemoryStream(stream.ToArray());
gridGroupingControl1.ApplyXmlSchema(new XmlTextReader(stream2));
```

### VB.NET Example

```vbnet
' Example usage of ApplyXmlSchema
Imports System.IO

' Serialize and reset sequence
' Serialize the grid schema
' ...
' Reset the grid using the serialized schema
Dim stream2 As System.IO.MemoryStream = New System.IO.MemoryStream(stream.ToArray())
gridGroupingControl1.ApplyXmlSchema(New XmlTextReader(stream2))
```

## Notes

- Ensure proper handling of memory streams and resource management to avoid leaks.
- The exact behavior may vary based on the grid's configuration and the complexity of the schema.

<!-- tags: [grid, windows forms, serialization, reset, schema, memory stream, xml, gridgroupingcontrol, essentials] keywords: [Essential Grid, Windows Forms, gridGroupingControl, ApplyXmlSchema, Memory Stream, serialization, reset, XML, schema] -->
```