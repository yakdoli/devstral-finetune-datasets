```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_097.jpeg
document_name: edit
page_number: 097
page_id: edit#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:10Z
fidelity: lossless
-->

## Overview
- Describes text navigation features for positioning the caret within an indentation block.
- Introduces auto indentation support in the Edit control to suit user requirements.
- Lists methods and properties for customizing text navigation and auto indentation settings.

## Content

### Text Navigation

It is also possible to position the caret at the beginning or end of the indentation block by using the `JumpToIndentBlockStart` and `JumpToIndentBlockEnd` methods respectively.

| Edit Control Method             | Description              |
|---------------------------------|--------------------------|
| JumpToIndentBlockStart         | Jumps to the start of the block. |
| JumpToIndentBlockEnd           | Jumps to the end of the block. |

**Refer to the Indentation Guidelines Demo sample for more information in this regard.**

Path to demo sample:

```
.. \My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Edit.Windows\Samples\2.0\Text Navigation\IndentationGuidelinesDemo
```

### Auto Indentation

#### Overview

The Edit control offers advanced text indentation support to suit the requirements of the user.

The properties listed in the following table can be used to customize the auto indentation settings of the Edit control.

| Property                 | Description                                                                 |
|--------------------------|------------------------------------------------------------------------------|
| AutoIndentMode           | Specifies mode of auto indentation. The options provided are <br> - None <br> - Block <br> - Smart |
| AutoIndentGuideline      | Gets/sets the value that specifies whether indent guideline should <br> be shown automatically after cursor repositioning. |

#### Code Examples

**[C#]**
```csharp
// Sets the AutoIntentMode.
this.editControl1.AutoIndentMode = 
Syncfusion.Windows.Forms.Edit.Enums.AutoIndentMode.None;
```

**[VB.NET]**
```vb
' Sets the AutoIntentMode.
Me.editControl1.AutoIndentMode = 
Syncfusion.Windows.Forms.Edit.Enums.AutoIndentMode.None
```

## API Reference

### Properties

- **AutoIndentMode**: Specifies the mode of auto indentation.
  - **Options**:
    - None
    - Block
    - Smart
- **AutoIndentGuideline**: Gets/sets whether the indent guideline should be shown automatically after cursor repositioning.

## RAG Annotations

<!-- tags: [Edit Control, Indentation, Text Navigation, Auto Indentation, Syncfusion Windows Forms] keywords: [caret, JumpToIndentBlockStart, JumpToIndentBlockEnd, AutoIndentMode, AutoIndentGuideline, Indentation Guidelines Demo, Text Navigation, Windows Forms, Syncfusion] -->
```