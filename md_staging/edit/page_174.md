```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: edit
page_number: 174
page_id: edit#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:56Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
    e.Cancel = False
Else
    e.Cancel = True
End If
End If
End Sub
```

### Handling Context Prompt Events

#### Clearing the Context Prompt Lexem Name on Close

##### C#

```csharp
// Clear the Context Prompt lexem name on close.
private void editControl1_ContextPromptClose(object sender, Syncfusion.Windows.Forms.Edit.ContextPromptCloseEventArgs e)
{
    this.contextPromptLexem = "";
}
```

##### VB.NET

```vb
' Clear the Context Prompt lexem name on close.
Private Sub editControl1_ContextPromptClose(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.ContextPromptCloseEventArgs)
    Me.contextPromptLexem = ""
End Sub
```

#### Displaying the Selected Context Prompt Item's Index

##### C#

```csharp
// Display the selected Context Prompt item's index.
private void editControl1_ContextPromptSelectionChanged(Syncfusion.Windows.Forms.Edit.Forms.Popup.ContextPrompt sender, Syncfusion.Windows.Forms.Edit.ContextPromptSelectionChangedEventArgs e)
{
    Console.WriteLine("SelectedIndex : " + e.SelectedIndex.ToString());
    Console.WriteLine("ContextPromptSelectionChanged");
}
```

##### VB.NET

```vb
' Display the selected Context Prompt item's index.
Private Sub editControl1_ContextPromptSelectionChanged(ByVal sender As Syncfusion.Windows.Forms.Edit.Forms.Popup.ContextPrompt, ByVal e As Syncfusion.Windows.Forms.Edit.ContextPromptSelectionChangedEventArgs)
    Console.WriteLine("SelectedIndex : " + e.SelectedIndex.ToString())
    Console.WriteLine("ContextPromptSelectionChanged")
End Sub
```

```html
<!-- tags: [windows forms, edit, context prompt, event handling, selection changed, lexem, clear, close] keywords: [windows forms, edit control, context prompt, event handling, selection changed, lexem, close, VB.NET, C#] -->
```