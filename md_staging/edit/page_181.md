```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: edit
page_number: 181
page_id: edit#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:01Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

The brush for the Context ToolTip background can be set by using the ContextTooltipBackgroundBrush property.

## Code Example: Setting Context Tooltip Background Brush

### C#

```csharp
this.editControl1.ContextTooltipBackgroundBrush = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent05, System.Drawing.Color.LavenderBlush, System.Drawing.Color.Khaki);
```

### VB.NET

```vbnet
Me.editControl1.ContextTooltipBackgroundBrush = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.PatternStyle.Percent05, System.Drawing.Color.LavenderBlush, System.Drawing.Color.Khaki)
```

## Border Settings

The border color of the Context ToolTip form is set by using the ContextTooltipBorderColor property.

| Edit Control Property        | Description                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------|
| ContextTooltipBorderColor   | Specifies the color of the Context Tooltip form border.<br>Used when UseXPStyle property is set to False. Otherwise 3D border is drawn. |

### C#

```csharp
this.editControl1.ContextTooltipBorderColor = System.Drawing.Color.Orange;
```

### VB.NET

```vbnet
Me.editControl1.ContextTooltipBorderColor = System.Drawing.Color.Orange
```

## Showing the ToolTip

The Context ToolTip window can be shown by setting the ShowContextTooltip property to True.

### C#

```csharp
// Shows the Context ToolTip pop-up window.
```

### References

- **See also:** `ContextTooltipBackgroundBrush`, `ContextTooltipBorderColor`, `ShowContextTooltip`
<!-- tags: [Syncfusion Winforms, Context Control, Tooltip, Property] keywords: [ContextTooltipBackgroundBrush, ContextTooltipBorderColor, ShowContextTooltip] -->
```