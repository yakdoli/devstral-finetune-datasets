```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: edit
page_number: 161
page_id: edit#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
this.editControl1.AutoCompleteSingleLexem = true;
```

```vb
Me.editControl1.AutoCompleteSingleLexem = True
```

## Populating the Context Choice List Items

The Context Choice list is populated by handling the `ContextChoiceOpen` event of the Edit Control, and adding items to the `Items` collection associated with the `IContextChoiceController` object.

| Edit Control Event       | Description                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| ContextChoiceOpen        | This event occurs when the Context Choice window has been opened.                             |

### [C#]

```csharp
private void
editControl1_ContextChoiceOpen(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController controller)
{
    // Add items to the Items collection associated with the IContextChoiceController object.
    controller.Items.Add("Method", "Method",
        this.editControl1.ContextChoiceController.Images["Image0"]);
    controller.Items.Add("FindText", "FindText",
        this.editControl1.ContextChoiceController.Images["Image1"]);
    controller.Items.Add("GetTextAsHTML", "GetTextAsHTML",
        this.editControl1.ContextChoiceController.Images["Image2"]);
    controller.Items.Add("LoadFile", "LoadFile",
        this.editControl1.ContextChoiceController.Images["Image3"]);
    controller.Items.Add("ToString", "ToString",
        this.editControl1.ContextChoiceController.Images["Image4"]);
    controller.Items.Add("Event", "Event",
        this.editControl1.ContextChoiceController.Images["Image5"]);
}
```

### [VB.NET]

```vb
Private Sub editControl1_ContextChoiceOpen(ByVal controller As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController) Handles EditControl1.ContextChoiceOpen
    ' Add items to the Items collection associated with the IContextChoiceController object.
    controller.Items.Add("Method", "Method",
```

``` 
© 2013 Syncfusion. All rights reserved. 161 | Page 
```

<!-- tags: [Syncfusion Winforms, edit control, ContextChoiceController, Items collection, essential edit] keywords: [edit controller, context choice open, image controller, items, IContextChoiceController, method, findtext, gettextashtml, loadfile, tostring, event] -->
``` 
