```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: edit
page_number: 094
page_id: edit#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:02Z
fidelity: lossless
-->

## Overview
- Describes how to manage indentation guidelines in the current region using methods like `ShowIndentGuideline` and `HideIndentGuideline`.
- Demonstrates bracket highlighting features by enabling specific properties.
- Includes examples in both C# and VB.NET.

## Content

### Indention Guideline Management
The indent guideline for the current region can be set or modified using the `ShowIndentGuideline` method.

| Edit Control Method         | Description                                                                                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HideIndentGuideline        | Hides indentation guideline.                                                                                                                                    |
| ShowIndentGuideline        | If possible, shows indent guideline of the current region.                                                                                                     |

#### Code Examples

[C#]
```csharp
// Indentation Guidelines are displayed.
this.editControl.ShowIndentationGuidelines = true;

// Hide Indentation Guideline.
this.editControl.HideIndentGuideline();

// Show Indentation Guideline.
this.editControl.ShowIndentGuideline();
```

[VB.NET]
```vbnet
' Indentation Guidelines are displayed.
Me.editControl.ShowIndentationGuidelines = True

' Hide Indentation Guideline.
Me.editControl.HideIndentGuideline()

' Show Indentation Guideline.
Me.editControl.ShowIndentGuideline()
```

### Bracket Highlighting

The bracket highlighting feature can be activated by enabling the `ShowIndentationGuidelines` and `OnlyHighlightMatchingBraces` properties. Setting the `OnlyHighlightMatchingBraces` property to `True` enables bracket highlighting without displaying indentation guidelines.

## API Reference

- **Properties**
  - `ShowIndentationGuidelines`: Enables or disables the display of indentation guidelines.
  - `OnlyHighlightMatchingBraces`: Controls whether only matching braces are highlighted.

- **Methods**
  - `HideIndentGuideline()`: Hides the current indent guideline.
  - `ShowIndentGuideline()`: Shows the indent guideline for the current region.

## Code Examples (Multi-Language)

```csharp
// Example using C#
this.editControl.ShowIndentationGuidelines = true;
this.editControl.OnlyHighlightMatchingBraces = true;
```

```vbnet
' Example using VB.NET
Me.editControl.ShowIndentationGuidelines = True
Me.editControl.OnlyHighlightMatchingBraces = True
```

<!-- tags: [syncfusion, winforms, indentation, bracket-highlighting, edit-control, api] keywords: [indentation guidelines, bracket highlighting, showindentguideline, hideindentguideline, onlyhighlightmatchingbraces, edit control, c#, vb.net] -->
```