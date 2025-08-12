```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: tools
page_number: 320
page_id: tools#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### AutoComplete Functionality

The following steps demonstrate how to enable the AutoComplete functionality for a RichTextBox control using Syncfusion.Windows.Forms.Tools.

1. **Code Snippet - VB.NET**
   ```vb
   Me.autoCompletel.SetAutoComplete(Me.richTextBox1, Syncfusion.Windows.Forms.Tools.AutoCompleteModes.AutoSuggest)
   ```

2. **Explanation**  
   - **7.** The RichTextBox will be enabled with the AutoComplete functionality.
   - **8.**

### How to Match Items in All the Columns Using AutoCompleteControl

#### Matching Items in Multiple Columns

Matching items in multiple columns is possible using the AutoComplete control. To achieve this, the AutoCompleteModes must be set to either **MultiSuggest** or **MultiExtended** mode.

---

#### MultiSuggest Mode

- **Description:** Possible matches from multiple columns for the current content of the Active edit control will be presented in a popup window with a selectable list of matches.
- **Mode:** MultiSuggest mode is an extended mode of AutoSuggest. When this mode is selected, the user can get matching items from all the columns in the active edit control.

#### Code Example

- **C#**
  ```csharp
  this.autoCompletel.SetAutoComplete(this.textBoxExt1, Syncfusion.Windows.Forms.Tools.AutoCompleteModes.MultiSuggest);
  ```

- **VB.NET**
  ```vb
  Me.autoCompletel.SetAutoComplete(Me.textBoxExt1, Syncfusion.Windows.Forms.Tools.AutoCompleteModes.MultiSuggest)
  ```

#### Demonstration of MultiSuggest Mode

- **Figure 133: MultiSuggest Mode**
  ![MultiSuggest Mode](image.png)
  
  The figure above illustrates how the MultiSuggest mode provides matching items across multiple columns in the active edit control.

---

#### Notes

- Ensure that the appropriate `AutoCompleteModes` are set to enable cross-column matching.
- Use the provided code snippets to implement the AutoComplete functionality with either `MultiSuggest` or `MultiExtended` mode as required.

## See also:

- Syncfusion.Windows.Forms.Tools.AutoCompleteCompletionSource
- Syncfusion.Windows.Forms.Tools.AutoCompleteControl

### References

- Documentation: [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windowsforms/)
- Version: 11.4.0.26

<!-- tags: tools, windowsforms, auto-complete, multi-suggest, auto-complete-modes, rich-textbox, textbox, syncfusion-features keywords: auto-complete, multi-suggest, auto-complete-modes, rich-textbox, textbox, windowsforms -->
```