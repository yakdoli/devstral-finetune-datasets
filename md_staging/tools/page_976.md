```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_976.jpeg
document_name: tools
page_number: 976
page_id: tools#page_976
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:54Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Databinding Using CheckBoxAdv

#### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // Using CheckBoxAdv's IntValue property for Databinding.
    this.oleDbDataAdapter1.Fill(this.dataSet1.Table1);
    this.checkBoxAdv1.DataBindings.Add("IntValue", this.dataSet1.Table1, "BitField");
}
```

#### VB.NET

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    ' Using CheckBoxAdv's IntValue property for Databinding.
    Me.oleDbDataAdapter1.Fill(Me.dataSet1.Table1)
    Me.checkBoxAdv1.DataBindings.Add("IntValue", Me.dataSet1.Table1, "BitField")
End Sub
```

A sample which demonstrates how bit values are used to set the state of the CheckBoxAdv is available in the below sample installation path.

### Sample Installation Path

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

#### How to databind a CheckBoxAdv to an SQL database if the corresponding datatable field is boolean

---

The CheckBoxAdv's `BoolValue` property can be used to databind `bool` values as illustrated below.

#### C#

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    this.oleDbDataAdapter1.Fill(this.dataSet1.Table1);
    // Using CheckBoxAdv's BoolValue property for Databinding.
    this.checkBoxAdv1.DataBindings.Add("BoolValue", this.dataSet1.Table1, "CheckValue");
}
```

---

## API Reference

### CheckBoxAdv Properties
- **IntValue**: Used for databinding with bit fields.
- **BoolValue**: Used for databinding with boolean fields.

---

## Code Examples

### Databinding a CheckBoxAdv to an SQL Database

Detailed examples are provided in the sample installation path.

---

### Related Information

For more information on databinding CheckBoxAdv to SQL databases, refer to the sample installation path provided.

---

<!-- tags: [syncfusion, winforms, checkboxadv, databinding, boolean, bitfield, sql, essentialstudio, version 11.4.0.26, checkboxes, windows forms] -->
```