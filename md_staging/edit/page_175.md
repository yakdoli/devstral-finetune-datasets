```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: edit
page_number: 175
page_id: edit#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:28Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Advanced Customization

If you wish to do some advanced customization in the Context Prompt feature, like highlighting the current parameter to be input in bold, you can use the `ContextPromptOpen` and `ContextPromptUpdate` events.

For example, add the bolded items in the `ContextPromptOpen` event handler. The indices for the exact position of the text that needs to be bolded has to be manually calculated and specified along with some text information associated with that particular argument. The following code snippet illustrates this.

```csharp
// To display some text in bold within the prompt.
private void editTextCtlController_ContextPromptOpen(object sender, Syncfusion.Windows.Forms.Edit.ContextPromptUpdateEventArgs e)
{
    Console.WriteLine("ContextPromptOpen");

    // Bolded Items should be added in this handler.
    ContextPromptItem item = null;
    item = e.AddPrompt( "Control.Items.Add(string text, string tooltipText, int imageIndex, int selectedIndex)", "Specify the text of the item, its tooltip text, image index and selected image index" );

    // Specify the text to be displayed in bold in the Context Prompt.
    item.BoldedItems.Add( 18, 11, "Text to be added" );
    item.BoldedItems.Add( 31, 18, "Text of the tooltip" );
    item.BoldedItems.Add( 51, 14, "Zero-based index of the image or -1 if no image should be used." );
    item.BoldedItems.Add( 67, 14, "Zero-based index of the image for selection or -1 if no image should be used." );

    item = e.AddPrompt( "Control.Items.Add(string text, string tooltipText, int imageIndex)", "Specify the text of the item, its tooltip text, and image index" );
    item.BoldedItems.Add( 18, 11, "Text to be added" );
    item.BoldedItems.Add( 31, 18, "Text of the tooltip" );
    item.BoldedItems.Add( 51, 14, "Zero-based index of the image or -1 if no image should be used." );

    item = e.AddPrompt( "Control.Items.Add(string text, string tooltipText)", "Specify the text of the item, and its tooltip text" );
    item.BoldedItems.Add( 18, 11, "Text to be added" );
    item.BoldedItems.Add( 31, 18, "Text of the tooltip" );
}
```

<!-- tags: [essential edit, advanced customization, context prompt] keywords: [ContextPromptOpen, ContextPromptUpdate, bolded items, Syncfusion.Windows.Forms.Edit] -->
```