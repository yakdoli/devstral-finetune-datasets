```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_940.jpeg
document_name: grid
page_number: 940
page_id: grid#page_940
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
ldCell.Interior = new BrushInfo(Color.Orange);
```

### Visual Basic .NET

```vb.net
' Customize the Appearance.
Me.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue
Me.gridGroupingControl1.TableOptions.GridLineBorder = New GridBorder(BorderStyle.Solid, Color.FromArgb(208, 215, 229), BorderWeight.Thin)
Me.gridGroupingControl1.TopLevelGroupOptions.ShowCaption = False
Me.gridGroupingControl1.Appearance.AnyCell.Font.FontName = "Verdana"
Me.gridGroupingControl1.Appearance.AnyCell.TextColor = Color.MidnightBlue
Me.gridGroupingControl1.TableDescriptor.Appearance.AlternateRecordCell.Interior = New BrushInfo(Color.Orange)
```

## Serialization

3. Create a button name 'Serialize', clicking which will start the serialization process. Add the below code into the ButtonClick event handler. This will save the grid schema into an Xml file.

### C#

```csharp
// Serialization
private void Serialize_Click(object sender, EventArgs e)
{
    FileDialog dlg = new SaveFileDialog();
    dlg.AddExtension = true;
    dlg.Filter = "xml files (*.xml)|*.xml|All files (*.*)|*.*";
    if (dlg.ShowDialog() == DialogResult.OK)
    {
        XmlTextWriter xw = new XmlTextWriter(dlg.FileName, System.Text.Encoding.UTF8);
        xw.Formatting = System.Xml.Formatting.Indented;
        this.gridGroupingControl1.WriteXmlSchema(xw);
        xw.Close();
    }
}
```

### Visual Basic .NET

```vb.net
' Serialization
Private Sub Serialize_Click(ByVal sender As Object, ByVal e As EventArgs) Handles btnSaveXmlSchema.Click
    Dim dlg As FileDialog = New SaveFileDialog()
    dlg.AddExtension = True
```

## References

<!-- tags: [Syncfusion, WinForms, Grid, Serialization, XML] keywords: [Serialization, ButtonClick, Xml Schema, Export, C#, VB.NET] -->
```