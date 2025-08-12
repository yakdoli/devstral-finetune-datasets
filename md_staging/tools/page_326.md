```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_326.jpeg
document_name: tools
page_number: 326
page_id: tools#page_326
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:07Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
this.comboBoxAutoComplete1.AutoCompleteSource = 
System.Windows.Forms.AutoCompleteSource.CustomSource;
this.Controls.Add(this.comboBoxAutoComplete1);
```

### [VB.NET]

```vb
Me.comboBoxAutoComplete1.AutoCompleteCustomSource.AddRange(New String() { 
    "Custom", "Customizing", "Customizable" })
Me.comboBoxAutoComplete1.AutoCompleteMode = 
System.Windows.Forms.AutoCompleteMode.SuggestAppend
Me.comboBoxAutoComplete1.AutoCompleteSource = 
System.Windows.Forms.AutoCompleteSource.CustomSource
Me.Controls.Add(Me.comboBoxAutoComplete1)
```

### 4. Run the application.

![ComboBoxAutoComplete with CustomSource](https://via.placeholder.com/100x100 "Caption for Figure 139: ComboBoxAutoComplete with CustomSource")

### See Also

- [Concpts and Features](#)
- **3.5.1.2.3 Concepts and Features**

This section contains information about using the ComboBoxAutoComplete control in some commonly used scenarios.

#### 3.5.1.2.3.1 Behavior Settings

<!-- tags: [ComboBoxAutoComplete, CustomSource, AutoCompleteSource, AutoCompleteMode, SuggestAppend, Behavior Settings] keywords: [ComboBoxAutoComplete, CustomSource, AutoCompleteSource, AutoCompleteMode, SuggestAppend, Behavior Settings] -->
``` 
