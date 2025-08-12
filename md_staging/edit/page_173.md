```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: edit
page_number: 173
page_id: edit#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:26Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
else
{
    // Display Context Choice popup if the lexem used to invoke them is "this" or "me" only.
    if ((lex.Text == "Chat") || (lex.Text == "Database") || (lex.Text == "NewFile") || (lex.Text == "Find") || (lex.Text == "Home") || (lex.Text == "PieChart") || (lex.Text == "Tools"))
    {
        this.contextPromptLexem = lex.Text;
        e.Cancel = false;
    }
    else
        e.Cancel = true;
}
```

### [VB.NET]

```vb
' Store the lexem name invoking the Context Prompt popup.
Dim contextPromptLexem As String = ""

Private Sub editControl_ContextPromptBeforeOpen(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles editControl.HttpContextPromptBeforeOpen
    Dim lex As ILexem
    Dim lexemLine As ILexemLine = Me.editControl1.GetLine(Me.editControl1.CurrentLine)

    ' Gets the index of the current word in that line.
    Dim ind As Integer = GetContextPromptCharIndex(lexemLine)

    If ind <= 0 Then
        e.Cancel = True
        Return
    End If
    lex = lexemLine.LineLexems(ind - 1)

    ' If the count is less than '2', do not show the Context Prompt popup.
    If lexemLine.LineLexems.Count < 2 Then
        e.Cancel = True
    Else
        ' Display Context Choice popup if the lexem used to invoke them is "this" or "me" only.
        If lex.Text = "Chat" OrElse lex.Text = "Database" OrElse lex.Text = "NewFile" OrElse lex.Text = "Find" OrElse lex.Text = "Home" OrElse lex.Text = "PieChart" OrElse lex.Text = "Tools" Then
            Me.contextPromptLexem = lex.Text
        End If
    End If
End Sub
```

<!-- tags: [edit, windowsforms, contextprompt, essentialedit, lexemfilter] keywords: [contextpromptbeforeopen, lexem, lexemline, ilexem, il exemline, editcontrol, winforms, syncfusion] -->
```