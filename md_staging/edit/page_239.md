```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: edit
page_number: 239
page_id: edit#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:17Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb.net
Private Sub editControl1_CanUndoRedoChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("CanUndoRedoChanged event is raised ")
End Sub
```

## 4.14.2 Closing Event

This event is discussed in the **Saving and Cancelling Changes** topic.

### 4.14.3 Code Snippet Events

This section discusses the below given code snippet events.

#### 4.14.3.1 CodeSnippetActivating Event

This event occurs when the code snippet is to be activated.

The event handler receives an argument of type **CancelableCodeSnippetsEventArgs**. The following `CancelableCodeSnippetsEventArgs` members provide information specific to this event.

| Member       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Cancel**   | Indicates whether action has to be cancelled.                             |
| **CodeSnippet** | Code snippet that is currently activated.                            |

```csharp
private void editControl_CodeSnippetActivating(object sender, Syncfusion.Windows.Forms.Edit.CancelableCodeSnippetsEventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine("CodeSnippetActivating event is raised ");
}
```

```html
<!-- tags: [syncfusion winforms, essential edit, canundoredochanged event, closing event, codesnippetactivating event, cancelablecodesnippetseventargs, windows forms] 
keywords: [event handling, code snippet, canundo redo, eventargs, activiation, cancel action] -->
```
```