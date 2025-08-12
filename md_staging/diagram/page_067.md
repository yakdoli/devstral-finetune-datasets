```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: diagram
page_number: 067
page_id: diagram#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:41Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Provides details on essential tools for adjusting node positions and sizes in Windows Forms.
- Describes functions for spacing, aligning, and standardizing node dimensions.
- Includes examples of using Nudge tools for directional adjustments.

## Content

### Alignment and Size Tools

| Tool Name      | Description                                                                 | Code Snippet                     |
|----------------|-----------------------------------------------------------------------------|----------------------------------|
| SpaceAcross    | Positions the selected nodes for equal horizontal spacing                 | `diagram1.SpaceAcross();`       |
| SpaceDown      | Positions the selected nodes for equal vertical spacing                   | `diagram1.SpaceDown();`         |
| SameSize       | Sets the width and height of the selected nodes to be equal.              | `diagram1.SameSize();`          |
| SameHeight     | Sets the height of the selected nodes to be equal.                       | `diagram1.SameHeight();`        |
| SameWidth      | Sets the width of the selected nodes to be equal.                        | `diagram1.SameWidth();`         |

### Nudge Tool

#### Overview
- The Nudge tools allow precise directional adjustments of components.
- The following screenshot illustrates the available Nudge tools.

#### Screenshot

```plaintext
               Nudge Left
               ↑
Nudge Up ← [  ], [  ], [  ], [  ] → Nudge Right
               ↓
               Nudge Down
```

**Figure 39: Nudge Tools**

### Nudge Tool Details

| Tool Name     | Description                                                                                                                         | Code Snippet                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| NudgeUp       | Nudge the selected components up by `Syncfusion.Windows.Forms.Diagram.Controls.Diagram.NudgeIncrement` units.                   | `diagram1.NudgeUp();`           |
| NudgeDown     | Nudge the selected components down by `Syncfusion.Windows.Forms.Diagram.Controls.Diagram.NudgeIncrement` units.                | `diagram1.NudgeDown();`         |
| NudgeLeft     | Nudge the selected components to the left by `Syncfusion.Windows.Forms.Diagram.Controls.Diagram.NudgeIncrement` units.         | `diagram1.NudgeLeft();`         |
| [unclear]     | [unclear]                                                                                                                         | [unclear]                       |

## Footer
© 2013 Syncfusion. All rights reserved.
67 | Page

<!-- tags: [Syncfusion Winforms, diagram, essential tools, node alignment, node sizing, Nudge tools] keywords: [SpaceAcross, SpaceDown, SameSize, SameHeight, SameWidth, NudgeUp, NudgeDown, NudgeLeft, NudgeIncrement, diagram tools] -->
```