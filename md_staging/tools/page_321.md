```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_321.jpeg
document_name: tools
page_number: 321
page_id: tools#page_321
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:05:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Introduces the MultiSuggestExtended mode.
- Explains how to retrieve matching items from a data source.
- Discusses the ComboBoxAutoComplete control.

## Content

### MultiSuggestExtended

This mode highlights all possible matches from Multiple columns, for the current content of the Active edit control, presented in the form of a popup window, with a selectable list of matches.

#### Code Examples

##### C#

```csharp
this.autoComplete1.SetAutoComplete(this.textBoxExt1 ,
    Syncfusion.Windows.Forms.Tools.AutoCompleteModes.MultiSuggestExtended);
```

##### VB.NET

```vb
Me.autoComplete1.SetAutoComplete(Me.textBoxExt1 ,
    Syncfusion.Windows.Forms.Tools.AutoCompleteModes.MultiSuggestExtended)
```

#### Figure

![Figure 134: MultiSuggestExtended Mode](https://via.placeholder.com/300x200)

### How to retrieve the corresponding matching item from a Datasource for the selected Item in the AutoComplete Control?

This can be done using AutoCompleteItemSelected Event which is discussed in **External Datasource** topic.

#### ComboBoxAutoComplete

The ComboBoxAutoComplete control combines a combo box control with an AutoComplete control to provide autocompletion for that instance of the combo box.

## Page-level Navigation/TOC (if applicable)

- MultiSuggestExtended
- How to retrieve the corresponding matching item from a Datasource for the selected Item in the AutoComplete Control
- ComboBoxAutoComplete

## RAG Annotations

<!-- tags: [Windows Forms, AutoComplete, Syncfusion, ComboBox, MultiSuggestExtended] keywords: [AutoSuggestExtended, AutoCompleteItemSelected, Datasource, ComboBoxAutoComplete, autocompletion] -->
```