```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_790.jpeg
document_name: tools
page_number: 790
page_id: tools#page_790
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the PercentTextBox Events in Syncfusion Winforms.
- Lists various events triggered by changes in PercentTextBox properties.
- Provides detailed descriptions for each event.

## Content

### PercentTextBox Events

| PercentTextBox Events                 | Description                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------|
| BindablePercentValueChanged           | This event occurs when the BindablePercentValue property is changed.        |
| BindableValueChanged                  | This event occurs when the BindableValue property is changed.               |
| Border3DStyleChanged                  | This event occurs when the Border3DStyle property is changed.               |
| BorderColorChanged                    | This event occurs when the BorderColor property is changed.                 |
| BorderSidesChanged                    | This event occurs when the BorderSides property is changed.                 |
| BorderStyleChanged                    | This event occurs when the ClipText property is changed.                  |
| ClipTextChanged                       | This event occurs when the ClipText property is changed.                   |
| DoubleValueChanged                    | This event occurs when the DoubleValue property is changed.                |
| FormattedTextChanged                  | This event occurs when the FormattedText property is changed.             |
| HideSelectionChanged                  | This event occurs when the HideSelection property is changed.              |
| MinimumSizeChanged                    | This event occurs when the MinimumSize property is changed.                |
| MaximumSizeChanged                    | This event occurs when the MaximumSize property is changed.                |
| MultilineChanged                      | This event occurs when the Multiline property is changed.                 |

## API Reference
- **BindablePercentValueChanged**: Triggered when the `BindablePercentValue` property is modified.
- **BindableValueChanged**: Triggered when the `BindableValue` property is modified.
- **Border3DStyleChanged**: Triggered when the `Border3DStyle` property is modified.
- **BorderColorChanged**: Triggered when the `BorderColor` property is modified.
- **BorderSidesChanged**: Triggered when the `BorderSides` property is modified.
- **BorderStyleChanged**: Triggered when the `ClipText` property is modified.
- **ClipTextChanged**: Triggered when the `ClipText` property is modified.
- **DoubleValueChanged**: Triggered when the `DoubleValue` property is modified.
- **FormattedTextChanged**: Triggered when the `FormattedText` property is modified.
- **HideSelectionChanged**: Triggered when the `HideSelection` property is modified.
- **MinimumSizeChanged**: Triggered when the `MinimumSize` property is modified.
- **MaximumSizeChanged**: Triggered when the `MaximumSize` property is modified.
- **MultilineChanged**: Triggered when the `Multiline` property is modified.

## Code Examples

### Example: Handling `BindablePercentValueChanged` Event

```csharp
private void PercentTextBox_BindablePercentValueChanged(object sender, EventArgs e)
{
    PercentTextBox percentTextBox = sender as PercentTextBox;
    MessageBox.Show($"BindablePercentValue has changed to: {percentTextBox.BindablePercentValue}");
}
```

<!-- tags: [PercentTextBox, Events, Syncfusion Winforms, WinForms, event handling] keywords: [BindablePercentValueChanged, BindableValueChanged, Border3DStyleChanged, BorderColorChanged, BorderSidesChanged, BorderStyleChanged, ClipTextChanged, DoubleValueChanged, FormattedTextChanged, HideSelectionChanged, MinimumSizeChanged, MaximumSizeChanged, MultilineChanged] -->
```