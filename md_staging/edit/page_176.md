```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_176.jpeg
document_name: edit
page_number: 176
page_id: edit#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:05Z
fidelity: lossless
-->

### Displaying Bold Text in Context Prompt

#### [VB.NET]

```vb
' To display some text in bold within the prompt.
Private Sub editControl1_ContextPromptOpen(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs) Handles editControl1.ContextPromptOpen
    Console.WriteLine("ContextPromptOpen")

    ' Bolded Items should be added in this handler.
    Dim item As ContextPromptItem

    item = e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedImageIndex)", "Specify the text of the item, its tooltip text, image index and selected image index")

    ' Specify the text to be displayed in bold in the Context Prompt.
    item.BoldedItems.Add(18, 11, "Text to be added")
    item.BoldedItems.Add(31, 18, "Text of the tooltip")
    item.BoldedItems.Add(51, 14, "Zero-based index of the image or -1 if no image should be used.")
    item.BoldedItems.Add(67, 14, "Zero-based index of the image for selection or -1 if no image should be used.")

    item = e.AddPrompt("Control.Items.Add(string text, string tooltipText, int imageIndex)", "Specify the text of the item, its tooltip text, and image index")
    item.BoldedItems.Add(18, 11, "Text to be added")
    item.BoldedItems.Add(31, 18, "Text of the tooltip")
    item.BoldedItems.Add(51, 14, "Zero-based index of the image or -1 if no image should be used.")

    item = e.AddPrompt("Control.Items.Add(string text, string tooltipText)", "Specify the text of the item and its tooltip text ")
```

#### Selecting Bolded Items in the ContextPromptUpdate Event Handler

Select the items that should be bolded in the `ContextPromptUpdate` event handler. The following code snippet illustrates this.

#### [C#]

```csharp
private void editControl1_ContextPromptUpdate(object sender, Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs e)
{
    // Select the items that should be bolded.
    if (e.List.SelectedItem != null)
    {
```

---

<!-- tags: [syncfusion, winforms, edit control, context prompt, bold text, event handling] keywords: [vb.net, c#, visual basic, event handler, selecteditem, boldeditems] -->
```