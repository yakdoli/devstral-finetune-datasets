```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_242.jpeg
document_name: edit
page_number: 242
page_id: edit#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:45Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
Syncfusion.Windows.Forms.Edit.CodeSnippetsTemplateTextChangingEventHandler(editControl1_CodeSnippetsTemplateTextChanging)
```

```vb
Private Sub editControl1_CodeSnippetsTemplateTextChanging(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CodeSnippetsTemplateTextChangingEventArgs)
    ' The below line will be displayed in the output window at runtime.
    Console.WriteLine("CodeSnippetsTemplateTextChanging event is raised ")
End Sub
```

## 4.14.3.4 NewSnippetMemberHighlighting Event

This event is raised when a new code snippet member is highlighted.

The event handler receives an argument of type `NewSnippetMemberHighlightingEventArgs`. The following `NewSnippetMemberHighlightingEventArgs` members provide information specific to this event.

| Member            | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Cancel            | Indicates whether action has to be cancelled.                           |
| CodeSnippets      | Code snippet that is currently activated.                               |
| NewSnippetMember  | Snippet member that has to be highlighted.                             |
| OldSnippetMember  | Previously highlighted snippet member.                                 |

### Example in C#

```csharp
private void editControl1_NewSnippetMemberHighlighting(object sender, Syncfusion.Windows.Forms.Edit.NewSnippetMemberHighlightingEventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine("NewSnippetMemberHighlighting event is raised ");
}
```

### Example in VB.NET

```vb
Private Sub editControl1_NewSnippetMemberHighlighting(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.NewSnippetMemberHighlightingEventArgs)
    ' The below line will be displayed in the output window at runtime.
    Console.WriteLine("NewSnippetMemberHighlighting event is raised ")
End Sub
```

---
<!-- tags: [syncfusion, windowsforms, code editor, events, snippet highlighting, sdk, 11.4.0.26] keywords: [essential edit, newsnippetmemberhighlighting, snippet member, code snippet, event handler, runtime output] -->
```