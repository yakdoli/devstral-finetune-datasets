```markdown
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_297.jpeg  
document_name: tools  
page_number: 297  
page_id: tools#page_297  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T10:03:48Z  
fidelity: lossless  
-->

## Essential Tools for Windows Forms

### Adding AutoComplete Custom Source Through String Collection Editor

#### Overview
- Demonstrates how to configure auto-completion in a `TextBox` control by adding custom suggestions.
- Uses the `String Collection Editor` to manage completion suggestions.
- The `AutoCompleteSource` property is set to `CustomSource` to enable custom suggestions.

#### Content

**Figure 126: Adding AutoComplete Custom Source Through String Collection Editor**

The process of setting up auto-completion involves configuring specific properties in the control's settings:

1. **Setting AutoCompleteSource Property to CustomSource:**
   - The `AutoCompleteSource` property must be set to `CustomSource` for the custom suggestions to take effect.

2. **Populating the String Collection:**
   - Use the `String Collection Editor` to add custom keywords or phrases.

   ![String Collection Editor Screenshot](attachment:StringCollectionEditor.png)

### Code Examples

#### C#

```csharp
this.textBox1.AutoCompleteSource =
System.Windows.Forms.AutoCompleteSource.CustomSource;

this.textBox1.AutoCompleteCustomSource.AddRange(new string []
{"Customization Settings", "Customization Properties",
"Customizing the items", "Custom Collections"});
```

#### VB.NET

```vb
Me.textBox1.AutoCompleteSource =
System.Windows.Forms.AutoCompleteSource.CustomSource
```

### Note
- The `Control.AutoCompleteSource` property should be set to "CustomSource" for this setting to be effective.

### API Reference

- **Namespace:** `System.Windows.Forms`
- **Class:** `TextBox`
- **Members:**
  - `AutoCompleteSource`: Configures how to retrieve suggestions.
  - `AutoCompleteCustomSource`: Manages the collection of custom suggestions.

### Cross References

- See also:
  - Documentation on configuring other auto-completion modes in the `TextBox` control.
  - Examples of using default completion sources such as `HistoryList` or `FileSystem`.

<!-- tags: custom auto-completion, string collection editor, windows forms, textbox control, autocomplete properties, syncfusion winforms version: 11.4.0.26 -->
```