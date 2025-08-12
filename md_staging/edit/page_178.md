```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: edit
page_number: 178
page_id: edit#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:08Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

```csharp
' Gets or sets selected item.
e.List.SelectedItem.BoldedItems.SelectedItem = 
    e.List.SelectedItem.BoldedItems(iBoldedIndex)
End If
End If
End Sub
```

### Showing / Hiding Context Prompt Pop-up

You can also programmatically show / hide the Context Prompt pop-up using the `ShowContextPrompt` and `CloseContextPrompt` methods.

#### C#

```csharp
// Shows the Context Prompt pop-up window.
this.editControl1.ShowContextPrompt();

// Closes the Context Prompt pop-up window.
this.editControl1.CloseContextPrompt();
```

#### VB.NET

```vb.net
' Shows the Context Prompt pop-up window.
Me.editControl1.ShowContextPrompt()

' Closes the Context Prompt pop-up window.
Me.editControl1.CloseContextPrompt()
```

A sample demonstrating the Context Prompt feature is available in the below sample installation path:

```
.. \My Documents \Syncfusion \EssentialStudio \Version
Number \Windows \Edit.Windows \Samples \2.0 \Intellisense
Functions \ContextChoiceandPromptDemo
```

### 4.6.6.2.2.4 Context ToolTip

The Context ToolTip displays helpful tooltips when the mouse is hovered over a lexem in the Edit Control. This feature is modeled on the **Quick Info** intellisense feature of Visual Studio. Whenever the mouse hovers over a token, the `UpdateContextTooltip` event is fired for quick information on the lexem. If some text information is provided, it is displayed in a tooltip.

---

© 2013 Syncfusion. All rights reserved. 178 |
```