<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_107.jpeg
document_name: edit
page_number: 107
page_id: edit#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:21Z
fidelity: lossless
-->

## Overview

- Discusses the `Outlining Tooltip` feature in the Syncfusion Windows Forms `Edit Control`.
- Explains the functionality of displaying collapsed blocks of text.
- Describes the support for `Outlining Tooltip` events in the `Edit Control`.

## Content

### Figure 35: Outlining Tooltip displaying the Collapsed Block of Text

The figure illustrates an example of the `Outlining Tooltip` feature in the `Edit Control`:

```csharp
private void ReadCharset()
{
    TokenExpected(Token.CHARSET_SYM);
    SkipSpaces(false);
    {
        string charset = TokenExpected(Token.STRING);
        SkipSpaces(false);
        SymbolExpected(';');
        To_writer.WriteAttributeString("charset", charset);
    }
    if (TokenIs(Token.URI))
    {
        s = TokenExpected(Token.URI);
    }
    else
    {
        s = TokenExpected(Token.STRING);
    }
    SkipSpaces(false);
}
```

### Using Events

#### Supported Outlining Tooltip Events

Edit Control supports the following `Outlining Tooltip` events:

| Edit Control Event                | Description                                         |
|------------------------------------|-----------------------------------------------------|
| OutliningTooltipBeforePopup       | Occurs when outlining tooltip is about to be shown. |
| OutliningTooltipPopup             | Occurs when outlining tooltip is shown.             |
| OutliningTooltipClose             | Occurs when outlining tooltip is closed.            |

#### OutliningTooltipBeforePopup Event

The `OutliningTooltipBeforePopup` event is used to control the visibility of the `outlining tooltip`. The `ShowMode` property of the `OutliningTooltipBeforePopupEventArgs` is used for this purpose. By default, the `ShowMode` property is set to `On`.

```csharp
[C#]

private void editControl_OutliningTooltipBeforePopup(object sender,
Syncfusion.Windows.Forms.Edit.OutliningTooltipBeforePopupEventArgs e)
{
    // To display the outlining tooltip
    e.ShowMode = OutliningTooltipShowMode.On;
}
```

### Event Handling Example

The example demonstrates how to handle the `OutliningTooltipBeforePopup` event to control the visibility of the tooltip:

```csharp
private void editControl_OutliningTooltipBeforePopup(object sender,
    Syncfusion.Windows.Forms.Edit.OutliningTooltipBeforePopupEventArgs e)
{
    // To display the outlining tooltip
    e.ShowMode = OutliningTooltipShowMode.On;
}
```

## Code Examples

### Example 1: Handling OutliningTooltipBeforePopup Event

The following code snippet shows how to handle the `OutliningTooltipBeforePopup` event:

```csharp
private void editControl_OutliningTooltipBeforePopup(object sender,
    Syncfusion.Windows.Forms.Edit.OutliningTooltipBeforePopupEventArgs e)
{
    // To display the outlining tooltip
    e.ShowMode = OutliningTooltipShowMode.On;
}
```

## RAG Annotations

<!-- tags: [outlining tooltip, edit control, event handling, windows forms] keywords: [syncfusion, outliningtooltipbeforepopup, outliningtooltippopup, outliningtooltipclose, edit control, windows forms, visual studio, .net, csharp] -->