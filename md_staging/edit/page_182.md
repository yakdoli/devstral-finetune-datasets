```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: edit
page_number: 182
page_id: edit#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:20Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

```csharp
this.editControl1.ShowContextTooltip = true;
```

```vb
' Shows the Context ToolTip pop-up window.
Me.editControl1.ShowContextTooltip = True
```

### ToolTip Delay

It is also possible to specify the time delay after which the tooltip should be displayed by using the **ToolTipDelay** property.

#### C#

```csharp
// Displays the tooltip pop-up after 1000 milliseconds ( 1 sec )
this.editControl1.ToolTipDelay = 1000;
```

#### VB

```vb
' Displays the tooltip pop-up after 1000 milliseconds ( 1 sec )
Me.editControl1.ToolTipDelay = 1000
```

### Closing the ToolTip

The Context ToolTip window is closed by using the **CloseContextTooltip** method.

#### C#

```csharp
// Closes the Context ToolTip pop-up window.
this.editControl1.CloseContextTooltip();
```

#### VB.NET

```vb
' Closes the Context ToolTip pop-up window.
Me.editControl1.CloseContextTooltip();
```

A sample demonstrating the Context Tooltip feature is available in the below sample installation path:

```
..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Intellisense Functions\\ContextTooltipDemo
```

## Page-level Navigation/TOC (if applicable)

---

## Cross References

See also: [Tooltip properties in Syncfusion Winforms](#)

## RAG Annotations

<!-- tags: [tooltip, context tooltip, winforms, syncfusion, toolTipDelay, closeContextTooltip] keywords: [tooltip display delay, closing tooltip, Windows Forms, Syncfusion Winforms] -->
```