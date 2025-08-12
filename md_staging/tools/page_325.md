```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_325.jpeg
document_name: tools
page_number: 325
page_id: tools#page_325
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:30Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### 3.5.1.2.2.2 Through Code

The embedded AutoComplete control in a ComboBoxAutoComplete control is exposed through the `AutoCompleteControl` property. The `Datasource` property of the `AutoCompleteControl` specifies the data that will be used for the auto completion of the combo box. It can be created programmatically as follows.

#### Steps to Implement

1. **Include the required namespace.**

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vb.net
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create an instance of the ComboBoxAutoComplete control class.**

   ```csharp
   private Syncfusion.Windows.Forms.Tools.ComboBoxAutoComplete comboBoxAutoComplete1;
   this.comboBoxAutoComplete1 = new Syncfusion.Windows.Forms.Tools.ComboBoxAutoComplete();
   ```

   ```vb.net
   Private comboBoxAutoComplete1 As Syncfusion.Windows.Forms.Tools.ComboBoxAutoComplete
   Me.comboBoxAutoComplete1 = New Syncfusion.Windows.Forms.Tools.ComboBoxAutoComplete()
   ```

3. **Set data source and add the control to the form.**

   ```csharp
   this.comboBoxAutoComplete1.AutoCompleteCustomSource.AddRange(new string[] { "Custom", "Customizing", "Customizable" });
   this.comboBoxAutoComplete1.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.SuggestAppend;
   ```

---

```html
<!-- tags: [ComboBoxAutoComplete, AutoCompleteControl, Datasource, Windows Forms, Syncfusion Winforms] keywords: [ComboBoxAutoComplete, AutoComplete, Datasource, AutoCompleteControl, Configure AutoComplete, Code Example, C#, VB.NET] -->
``` 
``` 
