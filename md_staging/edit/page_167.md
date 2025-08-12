```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: edit
page_number: 167
page_id: edit#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:59Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Filtering AutoComplete Items

Edit Control provides options to filter items in AutoComplete. This can be done by using the **FilterAutoCompletemItems** property.

| **Edit Control Property** | **Description** |
|---------------------------|-----------------|
| FilterAutoCompletemItems  | Gets / sets value indicating whether Context Choice items should be filtered while typing. |

The **FilterAutoCompletemItems** property, when set to **True**, filters the item in the AutoComplete Context Choice, and the filtered item alone will be visible. When set to **False**, all the items will be visible, and the selection will be navigated to the item.

![Figure 57: Filtering Items in AutoComplete Context Choice](https://i.imgur.com/placeholder.png)

## Showing / Hiding Context Choice Pop-up

You can also programmatically show / hide the Context Choice pop-up by calling the **ShowContextChoice** and **CloseContextChoice** methods.

### C#

```csharp
// Shows the Context Choice pop-up window.
this.editControl.ShowContextChoice();

// Closes the ContextChoice pop-up window.
this.editControl.CloseContextChoice();
```

### VB.NET

```vb
' Shows the Context Choice pop-up window.
Me.editControl1.ShowContextChoice()

' Closes the ContextChoice pop-up window.
```
```html
<!-- tags: [product, edit, filterautocompleteitems, showcontextchoice, closecontextchoice, windowsforms, version] keywords: [filterautocompleteitems, showcontextchoice, closecontextchoice, autocomplete, context choice, windows forms] -->
```