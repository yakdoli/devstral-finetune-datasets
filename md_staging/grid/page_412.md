```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_412.jpeg
document_name: grid
page_number: 412
page_id: grid#page_412
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:30Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Serializing Grid Data Using XML

Below are the examples demonstrating how to serialize grid data using XML techniques in both C# and VB.NET.

#### 1. Using C#

```csharp
Stream s = null;
s = File.Create(dlg.FileName);
XmlTextWriter xw = new XmlTextWriter(s, System.Text.Encoding.Default);
XmlSerializer xs = new
System.Xml.Serialization.XmlSerializer(this.gridControl.Model.Data.GetType());
xs.Serialize(xw, this.gridControl.Model.Data);
s.Close();
```

#### 2. Using VB.NET

```vbnet
Dim s As Stream = Nothing
s = File.Create(dlg.FileName)
Dim xw As XmlWriter = New XmlTextWriter(s,
System.Text.Encoding.Default)
Dim xs As XmlSerializer = New
System.Xml.Serialization.XmlSerializer(Me.gridControl.Model.Data.GetType())
xs.Serialize(xw, Me.gridControl.Model.Data)
s.Close()
```

#### Deserializing Grid Schema Information Using XML

The following code example illustrates the deserialization of grid schema information by using XML technique.

##### 1. Using C#

```csharp
Stream s = null;
s = File.OpenRead(dlg.FileName);
XmlReader xw = new XmlTextReader(s);
XmlSerializer xs = new
System.Xml.Serialization.XmlSerializer(this.gridControl.Model.Data.GetType());
s.Close();
this.gridControl.Model.Data = (GridData)xs.Deserialize(xw);
this.gridControl.Refresh();
```

##### 2. Using VB.NET

(Note: The VB.NET code example for deserialization is not fully provided. Please ensure it is included when reconstructing the documentation.)

### Conclusion

This section provides code examples for both serializing and deserializing grid data using XML in C# and VB.NET. These examples can be used as starting points for integrating XML-based serialization and deserialization into applications utilizing Essential Grid for Windows Forms.

#### Page-Level Navigation/TOC
- **Serializing Grid Data Using XML**
  - Using C#
  - Using VB.NET
- **Deserializing Grid Schema Information Using XML**
  - Using C#
  - Using VB.NET

<!-- tags: [syncfusion, winforms, grid, xml, serialization, deserialization, csharp, vb.net, version: 11.4.0.26] keywords: [essential grid, windows forms, xml, serialize, deserialize, csharp, vb.net, file operations, grid data, schema, data handling] -->
```