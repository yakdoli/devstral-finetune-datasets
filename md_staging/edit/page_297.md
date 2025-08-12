```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_297.jpeg
document_name: edit
page_number: 297
page_id: edit#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:12:20Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
editControl1.RegisterBackColorFormat(background, foreground, style, bUseHashFille);
return format;
}

//code for setting line back color for the entire line
private void button1_Click(object sender, System.EventArgs e)
{
    IDynamicFormat[] temp = 
    editControl.GetLineBackColorFormats(editControl1.CurrentLine);
    IBackgroundFormat format = RegisterFormat();
    editControl1.SetLineBackColor(editControl1.CurrentLine, true, format);
}
```

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    //comboBox1.Items.Clear();
    comboBox1.Items.Add("Solid");
    foreach (string name in Enum.GetNames(typeof(HatchStyle)))
    comboBox1.Items.Add(name);
    comboBox1.SelectedText = "Percent05";
    comboBox1.SelectedIndex = 0;
    editControl1.Text += "\n";
    editControl1.CurrentLine = 1;
}
```

```csharp
//code to set the back color for a selected text
private void button2_Click(object sender, System.EventArgs e)
{
    IBackgroundFormat format = RegisterFormat();
    editControl1.SetSelectionBackColor(format);
}
```

## [VB.NET]

```vbnet
Private Function RegisterFormat() As IBackgroundFormat
    Dim background As Color = Color.Empty
    Dim foreground As Color = Color.Empty
    If radioButton1.Checked Then
        background = radioButton1.BackColor
    ElseIf radioButton2.Checked Then
        background = radioButton2.BackColor
    ElseIf radioButton3.Checked Then
        background = radioButton3.BackColor
    End If
    If radioButton6.Checked Then
```

<!-- tags: [Syncfusion, Windows Forms, Edit Control, Line Back Color, Selection Back Color, Version: 11.4.0.26] keywords: [editControl1, button1_Click, Form1_Load, button2_Click, RegisterFormat, IDynamicFormat, IBackgroundFormat, Enum, HatchStyle, comboBox1, editControl, sélection,背景颜色, 线背景颜色] -->
```