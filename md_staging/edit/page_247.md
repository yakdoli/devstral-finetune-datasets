```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_247.jpeg
document_name: edit
page_number: 247
page_id: edit#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:39Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### References

| Property Name       | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| SelectedItem        | Gets / sets currently selected item.                                      |
| UseAutocomplete     | Specifies whether autocomplete technique should be used with current <br> context choice. |

### Code Examples (C#)

```csharp
// Create a new instance of the context choice item collection.
private ContextChoiceItemCollection c = new ContextChoiceItemCollection();

// Handle the ContextChoiceUpdate event.
this.editControl1.ContextChoiceUpdate += new
Syncfusion.Windows.Forms.Edit.ContextChoiceEventHandler(editControl1_ContextChoiceUpdate);

// IContextChoiceController.LexemBeforeDropper property returns the lexem <br>
// before the dropper which displays the context choice. It is possible to <br>
// control the lexem being searched in the context choice list using the <br>
// ContextChoiceUpdate event.
private void editControl1_ContextChoiceUpdate(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController controller)
{
    Console.WriteLine("LexemBeforeDropper: " + controller.LexemBeforeDropper.Text);
    controller.Items.Clear();
    foreach (IContextChoiceItem item in c)
    {
        if (item.Text.Equals(controller.LexemBeforeDropper.Text))
        {
            controller.Items.Add(item.Text);
        }
    }
}
```

### Code Examples (VB.NET)

```vb
' Create a new instance of the context choice item collection.
Private c As ContextChoiceItemCollection = New ContextChoiceItemCollection()

' Handle the ContextChoiceUpdate event.
Me.editControl1.ContextChoiceUpdate += New
Syncfusion.Windows.Forms.Edit.ContextChoiceEventHandler(editControl1_ContextChoiceUpdate)

' IContextChoiceController.LexemBeforeDropper property returns the lexem
```

<!-- tags: [syncfusion, winforms, contextchoice, autocomplete, lexem, eventhandler] keywords: [editControl1, ContextChoiceItemCollection, ContextChoiceUpdate, IContextChoiceController, LexemBeforeDropper, Text, Item, List] -->
```