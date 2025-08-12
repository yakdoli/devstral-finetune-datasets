```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: tools
page_number: 103
page_id: tools#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:23:18Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
Dim radReturn As RadioButton = New RadioButton()
For Each ctrl As Control In Me.groupBox1.Controls
    Dim rad As RadioButton = CType(IIf(TypeOf ctrl Is RadioButton, ctrl, Nothing), RadioButton)
    If rad.Checked Then
        radReturn = rad
    End If
Next ctrl
Return (radReturn.Text)
End Function
```

### Add the following code for each CheckedChanged event of the Radio Button.

#### C#

```csharp
private void radXML_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "XML";
}

private void radBinary_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "Binary Format";
}

private void radIsoS_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "Isolated Storage";
}

private void radBinFmt_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "Binary Fmt Format";
}

private void radReg_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "Windows Registry";
}

private void radXMLFmt_CheckedChanged(object sender, System.EventArgs e)
{
    selRad = "XML Fmt Format";
}
```
```