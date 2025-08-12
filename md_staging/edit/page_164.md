```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_164.jpeg
document_name: edit
page_number: 164
page_id: edit#page_164
product: Syncfusion Winforms 
version: 11.4.0.26
timestamp: 2025-08-09T05:03:24Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb.net
Me.editControl1.ContextChoiceSize = New System.Drawing.Size(100, 50)
```

## Context Choice Operations

The Edit Control provides the following set of events for performing Context Choice operations.

| Edit Control Event             | Description                                                                                                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContextChoiceBeforeOpen       | This event occurs when the Context Choice window is about to open.                                                                                                     |

### [C#]

```csharp
private void editControl1_ContextChoiceBeforeOpen(object sender, System.ComponentModel.CancelEventArgs e)
{
    // Display Context Choice popup if the lexem used to invoke Context Choice is "this" or "me" only
    int ind = GetContextChoiceCharIndex(lexemLine);
    ILexem lex = lexemLine.LineLexems[ind - 1] as ILexem;
    if ((lex.Text == "this") || (lex.Text == "me"))
        e.Cancel = false;
    else
        // Cancels the display of the Context Choice list.
        e.Cancel = true;
}
```

### [VB.NET]

```vb.net
Private Sub editControl1_ContextChoiceBeforeOpen(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles EditControl1.ContextChoiceBeforeOpen
    ' Display Context Choice popup if the lexem used to invoke the Context Choice is "this" or "me" only
    Dim ind As Integer = GetContextChoiceCharIndex(lexemLine)
    Dim lex As ILexem = lexemLine.LineLexems(ind - 1)
    If lex.Text = "this" OrElse lex.Text = "me" Then
        e.Cancel = False
    Else
        ' Cancel the display of the Context Choice list.
        e.Cancel = True
    End If
End Sub
```

## Page-level Navigation/TOC (if applicable)
- **Getting Started**
- **Properties**
- **Methods**
- **Events**

## Cross References
- **See also:** Context Menu, Text Display, Editing Operations

<!-- tags: [Syncfusion Winforms, edit control, context choice, events] keywords: [context choice operations, edit control, lexical elements, text editing, display popup, cancel event, event handling] --> 
```