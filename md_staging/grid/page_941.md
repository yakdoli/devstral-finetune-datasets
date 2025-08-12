```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_941.jpeg
document_name: grid
page_number: 941
page_id: grid#page_941
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

dlg.Filter = "xml files (*.xml)|*.xml|All files (*.*)|*.*"  
If dlg.ShowDialog() = DialogResult.OK Then  
    Dim xw As XmlTextWriter = New XmlTextWriter(dlg.FileName,  
    System.Text.Encoding.UTF8)  
    xw.Formatting = System.Xml.Formatting.Indented  
    Me.gridGroupingControl1.WriteXmlSchema(xw)  
    xw.Close()  
End If  
End Sub  

## Content

4. Create another button named 'Deserialize' to deserialize the grid. The following code will help you to load the grid schema back from an Xml file.

### C#

```csharp
// Deserialization  
private void btnLoadXmlSchema_Click(object sender, System.EventArgs e)  
{  
    OpenFileDialog dlg = new OpenFileDialog();  
    dlg.Filter = "xml files (*.xml)|*.xml|All files (*.*)|*.*";  
    if (dlg.ShowDialog() == DialogResult.OK)  
    {  
        XmlReader xr = new XmlTextReader(dlg.FileName);  
        this.gridGroupingControl1.ApplyXmlSchema(xr);  
        xr.Close();  
    }  
}
```

### VB.NET

```vb
' Deserialization  
Private Sub btnLoadXmlSchema_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles btnLoadXmlSchema.Click  
    Dim dlg As OpenFileDialog = New OpenFileDialog()  
    dlg.Filter = "xml files (*.xml)|*.xml|All files (*.*)|*.*"  
    If dlg.ShowDialog() = DialogResult.OK Then  
        Dim xr As XmlReader = New XmlTextReader(dlg.FileName)  
        gridGroupingControl1.ApplyXmlSchema(xr);  
        xr.Close()  
    End If  
End Sub
```

5. Create a third button named 'Reset' which will reset the look and feel of the grid.

### C#

```csharp
// Existing code will be inserted here.
```

## API Reference (if applicable)

### Code Examples (multi-language supported)

* Add ALL code exactly. Use fenced blocks with language.
* Keep full signatures, imports/usings, comments, and region markers.

### Cross References

* See also: links to related documentation or examples.

<!-- tags: [Synfusion Winforms, Grid, Serialization, Deserialization, Reset, XML Schema] keywords: [Serialization, Deserialization, Resetting Grid, XML Files, Grid Schema] -->
```