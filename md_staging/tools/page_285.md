```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_285.jpeg
document_name: tools
page_number: 285
page_id: tools#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

- change it to the mode of autocompletion to AutoSuggest. The different modes of autocompletion are detailed in AutoComplete Modes topic.

### Setting AutoCompleteMode to "AutoSuggest"

When configuring the AutoCompleteMode, you can select from different modes to enhance user experience in a Windows Forms TextBox control. The "AutoSuggest" mode is highlighted as a useful setting. Below is an illustration of how to set it:

#### Figure 118: Setting AutoCompleteMode = "AutoSuggest"

![](https://docs.syncfusion.com/windowsforms/images/AutoCompleteModes.png)

In the figure above, the **AutoCompleteMode** is set to **"AutoSuggest"** in the Properties window for a TextBox control. This setting enables the TextBox to suggest completions as the user types, without automatically appending any text.

### Step-by-Step Instructions

1. Set the **AutoComplete.AutoAddItem** property to **true**. This step ensures that the entered text is saved after you hit Enter.
   
2. Run the application.
   
3. Type any text in the textbox and hit **Enter** to save the entry.
   
4. Select the text, delete it, and then retype the first letter of the text you saved.
   
5. You should see autocompletion of the letter as you retype, as shown in the example provided below.

#### Example: Demonstrating Autocompletion

When the **AutoAddItem** property is set to **true**, the entered text is saved and appears in the autocompletion dropdown list after the user interacts with the textbox. Below is a demonstration of this behavior:

![](https://docs.syncfusion.com/windowsforms/images/AutoCompleteExample.png)

### Note
The text entered can be saved only when the **AutoAddItem** property is set to **True**.

## API Reference

### Properties

- **AutoCompleteMode**: Determines the mode of autocompletion behavior.
- **AutoComplete.AutoAddItem**: Determines whether the text entered should be saved for future autocompletion suggestions.

### Methods

- None specific to this configuration are highlighted in the given context.

## Code Examples

Here is a basic example of configuring a TextBox control to employ AutoSuggest behavior:

```csharp
// Assuming a TextBox control named 'textBox1' is present in the form
textBox1.AutoCompleteMode = AutoCompleteMode.Suggest;
textBox1.AutoCompleteSource = AutoCompleteSource.CustomSource;
textBox1.AutoCompleteCustomSource = new AutoCompleteStringCollection();

// Enabling autocompletion to add entered items
textBox1.AutoComplete.CustomItems.Add("AutoComplete Mode");
textBox1.AutoComplete.CustomItems.Add("AutoSuggest");

// Setting AutoAddItem to true
textBox1.AutoComplete.AutoAddItem = true;
```

### Cross References

- For further details on AutoComplete Modes, refer to the AutoComplete Modes topic in the documentation.
- See also: AutoCompleteSource, AutoCompleteStringCollection, AutoComplete.

### RAG Annotations

<!-- tags: [Syncfusion, WinForms, TextBox, AutoComplete, AutoSuggest, AutoAddItem] keywords: [AutoCompleteMode, AutoSuggest, CustomSource, AutoCompleteStringCollection, AutoAddItem] -->

```