```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_292.jpeg
document_name: edit
page_number: 292
page_id: edit#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:11:38Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
ILexemLine lexemLine = this.editControl.GetLine(this.editControl.CurrentLine);
foreach (Lexem lexem in lexemLine.LineLexems)
{
    lexemArrayList.Add(lexem);
}
```

```vbnet
Dim lexemLine As ILexemLine = Me.editControl.GetLine(Me.editControl1.CurrentLine)
Dim lexem As Lexem
For Each lexem In lexemLine.LineLexems
    lexemArrayList.Add(lexem)
Next
```

## 5.13 How To Implement VS.NET-like XML Tag Insertion Feature Using Edit Control

The VS.NET-like XML tag insertion feature can be used while editing XML language tags in Essential Edit. The cursor can be placed at any position of the line, and the nodes will be inserted exactly at the beginning and end of the current line.

This feature saves time while editing your XML documents by using Essential Edit. The following code snippet illustrates this.

```csharp
private void menuItem_Click(object sender, System.EventArgs e)
{
    this.inputDialog.ShowDialog();
    if (this.accepted == true)
    {
        if (this.inputString.Equals(""))
        {
            MessageBox.Show("The node name cannot be empty");
        }
        else
        {
```

---
© 2013 Syncfusion. All rights reserved.
``` 

<!-- tags: [essential edit, windows forms, xml tag insertion, edit control, vs.net-like feature, vs.net, xml language tags, cursor placement, node insertion, vs.net-like, xml editing, essential edit for windows forms] keywords: [xml tag insertion, edit control, vs.net-like feature, cursor placement, node insertion, vs.net-like, xml editing, essential edit, windows forms, vs.net, xml language tags, xml documents, feature implementation, time-saving, code snippet, input dialog, message box, accepted, inputString, node name, empty, feature description] -->
``` 
