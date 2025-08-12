```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_861.jpeg
document_name: tools
page_number: 861
page_id: tools#page_861
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:34Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Documentation of various events related to property changes in Syncfusion WinForms.
- Detailed description of the `Border3DStyleChanged` event and its handling.

## Content

The following table lists various events that occur when specific properties are changed:

| Event Name                     | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| CharacterCasingChanged         | This event occurs when the CharacterCasing property is changed.           |
| HideSelectionChanged           | This event occurs when the HideSelection property is changed.              |
| MaskCustomValidate             | This event is handled to provide custom behavior to any mask characters.   |
| MaskSatisfied                  | This event is raised when the required fields in a mask have been satisfied after new text has been entered / the text changes. |
| MaximumSizeChanged             | This event occurs when the MaximumSize property is changed.               |
| MinimumSizeChanged             | This event occurs when the MinimumSize property is changed.               |
| MultilineChanged               | This event occurs when the Multiline property is changed.                 |
| ReadOnlyChanged                | This event occurs when the ReadOnly property is changed.                  |
| TextAlignChanged               | This event occurs when the TextAlign property is changed.                 |
| ThemesEnabledChanged           | This event occurs when the ThemesEnabled property is changed.             |

### 3.5.8.8.4.1 Border3DStyleChanged

This event occurs when the Border3DStyle property is changed. The Border3DStyle property indicates the style of the 3D border.

The event handler receives an argument of type EventArgs containing data related to this event.

#### Code Example

```csharp
private void maskedEditBox1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine(" Border3DStyleChanged event is raised ");
}
```

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms
  - Events related to property changes
    - CharacterCasingChanged
    - HideSelectionChanged
    - MaskCustomValidate
    - MaskSatisfied
    - MaximumSizeChanged
    - MinimumSizeChanged
    - MultilineChanged
    - ReadOnlyChanged
    - TextAlignChanged
    - ThemesEnabledChanged
    - Border3DStyleChanged

## Cross References
- See also: events, property changes, Windows Forms, Syncfusion WinForms.

<!-- tags: [Windows Forms, Syncfusion Winforms, events, properties, property changes] keywords: [CharacterCasingChanged, HideSelectionChanged, MaskCustomValidate, MaskSatisfied, MaximumSizeChanged, MinimumSizeChanged, MultilineChanged, ReadOnlyChanged, TextAlignChanged, ThemesEnabledChanged, Border3DStyleChanged, Event Handling, C#] -->
```