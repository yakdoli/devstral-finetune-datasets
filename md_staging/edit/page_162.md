```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: edit
page_number: 162
page_id: edit#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:06Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

---

## Content

```vb
Me.editControl1.ContextChoiceController.Images("Image0")
controller.Items.Add("FindText", "FindText",
Me.editControl1.ContextChoiceController.Images("Image1")
controller.Items.Add("GetTextAsHTML", "GetTextAsHTML",
Me.editControl1.ContextChoiceController.Images("Image2")
controller.Items.Add("LoadFile", "LoadFile",
Me.editControl1.ContextChoiceController.Images("Image3")
controller.Items.Add("ToString", "ToString",
Me.editControl1.ContextChoiceController.Images("Image4")
controller.Items.Add("Event", "Event",
Me.editControl1.ContextChoiceController.Images("Image5")
End Sub
```

### Adding Custom Images to List Items

Custom images can also be added to the Context Choice list items by indexing them into the **Images** collection of the `IContextChoiceController` object associated with the Edit Control. The `Images` collection of the `IContextChoiceController` can be populated by using the code given below.

#### C#

```csharp
int index = 0;
foreach (Image img in this.imageList1.Images)
{
    // Populating images using an external ImageList.
    this.editControl1.ContextChoiceController.AddImage("Image" + index.ToString(), img);
    index++;
}
```

#### VB.NET

```vb
Dim index As Integer = 0
Dim img As Image
For Each img In Me.imageList1.Images
    ' Populating images using an external ImageList.
    Me.editControl1.ContextChoiceController.AddImage("Image" + index.ToString(), img)
    index += 1
Next img
```

### List Item ToolTip

ToolTip text is specified for each Context Choice list item while adding the items to the `IContextChoiceController`, as shown in the following code snippet.

---

## Footer

© 2013 Syncfusion. All rights reserved.
162 | Page
```

<!-- tags: [edit, windows forms, context choice, images, tool tips, c#, vb.net, version:11.4.0.26] keywords: [Syncfusion Winforms, IContextChoiceController, Images, Edit Control, Custom Images, ToolTip, C#, VB.NET] -->