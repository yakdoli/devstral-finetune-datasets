```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: edit
page_number: 248
page_id: edit#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:29Z
fidelity: lossless
-->

## ContextChoiceUpdate Event

It is possible to control the lexem being searched in the context choice list using the `ContextChoiceUpdate` event.

```csharp
Private Sub editControl1_ContextChoiceUpdate(ByVal controller As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController)
    Console.WriteLine("LexemBeforeDropper:" + controller.LexemBeforeDropper.Text)
    controller.Items.Clear()
    Dim item As IContextChoiceItem
    For Each item In c
        If item.Text.Equals(controller.LexemBeforeDropper.Text) Then
            controller.Items.Add(item.Text)
        End If
    Next
End Sub
```

## 4.14.6.6 ContextChoiceOpen Event

This event is discussed in the **Context Choice** topic.

## 4.14.6.7 ContextChoiceRightClick Event

This event is raised when the context choice item is right-clicked.

The event handler receives an argument of type `ContextChoiceItemEventArgs`. The following `CancellableCodeSnippetsEventArgs` member provides information specific to this event.

| Member | Description         |
|--------|----------------------|
| Item   | Underlying ContextChoiceItem. |

### Code Example

```csharp
private void editControl1_ContextChoiceRightClick(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController sender, Syncfusion.Windows.Forms.Edit.ContextChoiceItemEventArgs e)
{
    e.Item.ForeColor = System.Drawing.Color.Maroon;
    e.Item.BackColor = System.Drawing.Color.MistyRose;
    MessageBox.Show(" ContextChoiceRightClick event is raised ");
}
```

## API Reference

- **Class**: `IContextChoiceController`
- **Method**: `editControl1_ContextChoiceUpdate`
- **Event**: `ContextChoiceRightClick`
- **EventArgs**: `ContextChoiceItemEventArgs`

## Code Examples 

### C#

```csharp
private void editControl1_ContextChoiceRightClick(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController sender, Syncfusion.Windows.Forms.Edit.ContextChoiceItemEventArgs e)
{
    e.Item.ForeColor = System.Drawing.Color.Maroon;
    e.Item.BackColor = System.Drawing.Color.MistyRose;
    MessageBox.Show(" ContextChoiceRightClick event is raised ");
}
```

<!-- tags: [product, syncfusion, winforms, event, contextchoice, contextchoiceupdate, contextchoiceopenevent, contextchoicerightclick, userguide, controlchoice] keywords: [context choice, event handler, Syncfusion Windows Forms, lexem, right-click, context choice item, ContextChoiceItemEventArgs, edit control, item] -->
```