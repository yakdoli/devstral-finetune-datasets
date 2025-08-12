```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_323.jpeg
document_name: tools
page_number: 323
page_id: tools#page_323
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:19Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Adding and configuring Syncfusion ComboBoxAutoComplete control.
- Using the AutoCompleteCustomSource collection editor for injecting custom data.
- Specifying text completion behavior using ComboBoxAutoComplete.AutoCompleteMode.

### Content

#### Adding and Configuring ComboBoxAutoComplete Control
1. **Access the ComboBoxAutoComplete Control**
   - The ComboBoxAutoComplete control can be found under the "Syncfusion" section in the Toolbox, as shown in Figure 135.
   - Click and drag the control onto the form to add it.

   **Figure 135: ComboBoxAutoComplete control in Toolbox**

2. **Adding Items to ComboBoxAutoComplete**
   - Use the AutoCompleteCustomSource collection editor to add items to the ComboBoxAutoComplete control.
   - Open the properties of the ComboBoxAutoComplete control and navigate to the AutoCompleteCustomSource property.
   - Click on the "(Collection)" link to open the String Collection Editor.
   - Enter the items you wish to autocomplete, one per line.

   **Figure 136: Adding CustomSource to ComboBox**

3. **Specifying Text Completion Behavior**
   - The text completion behavior of the control can be tailored using the ComboBoxAutoComplete.AutoCompleteMode property.
   - The value of AutoCompleteMode determines how autocompletion is handled (e.g., None, Suggest, Append, etc.).

---

### Figures and Descriptions
- **Figure 135:** Displays the Syncfusion Toolbox with the ComboBoxAutoComplete control highlighted. This is the control that needs to be used for implementing autocompletion functionality.
- **Figure 136:** Illustrates the process of adding custom items to the ComboBoxAutoComplete control using the AutoCompleteCustomSource collection editor.

---

### Cross References
- For more details on configuring AutoCompleteMode and other properties, refer to the ComboBoxAutoComplete documentation in the Syncfusion WinForms user guide.

---

### RAG Annotations

#### Tags
- Syncfusion, Windows Forms, ComboBoxAutoComplete, AutoCompleteMode, AutoCompleteCustomSource, Designer

#### Keywords
- ComboBox, AutoComplete, Designer, Syncfusion, Windows Forms, Control Properties, AutoCompletion Settings
``` 
```