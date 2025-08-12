```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_293.jpeg
document_name: edit
page_number: 293
page_id: edit#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:12:07Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.editControl.MoveToLineStart();
this.editControl.InsertText(this.editControl.CurrentLine, (this.editControl.CurrentColumn), " ");
this.editControl.InsertText(this.editControl.CurrentLine, this.editControl.CurrentColumn, "<" + this.inputString + ">");
this.editControl.InsertText(this.editControl.CurrentLine, (this.editControl.CurrentColumn), " ");
this.editControl.AppendText("</" + this.inputString + ">");
}
}
```

### [VB.NET]
```vb
Private Sub menuItem_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles menuItem2.Click
    Me.inputDialog.ShowDialog()
    If Me.accepted = True Then
        If Me.inputString.Equals("") Then
            MessageBox.Show("The node name cannot be empty")
        Else
            Me.editControl1.MoveToLineStart()
            Me.editControl1.InsertText(Me.editControl1.CurrentLine, (Me.editControl1.CurrentColumn), " ")
            Me.editControl1.InsertText(Me.editControl1.CurrentLine, Me.editControl1.CurrentColumn, "<" + Me.inputString + ">")
            Me.editControl1.InsertText(Me.editControl1.CurrentLine, (Me.editControl1.CurrentColumn), " ")
            Me.editControl1.AppendText("</" + Me.inputString + ">")
        End If
    End If
End Sub
```

## 5.14 How To Perform VS.NET-like Underlining For Offending Code In the Edit Control

Edit Control supports VS.NET-like wavy underlining of text. The wavy underlines can also have custom color and double lines. The following code snippet illustrates how you can implement this feature in Edit Control.

### [C#]
```csharp
// Starting offset converted to virtual point
```

---
<!-- tags: [product, feature, windows forms, edit control, underlining, vs.net] keywords: [essential edit, windows forms, vs.net-like underlining, custom color, double lines, implementation, edit control] -->
```