```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: grid
page_number: 125
page_id: grid#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:40:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Covers technical aspects of the Essential Grid control in Windows Forms.
- Focuses on consistent application performance and text handling.
- Discusses support for text editing, DPI settings, and color coding.

## Content

### Table: Criteria, Supporting Features, Remarks, and Explanations

| Criteria                                                                                   | Supporting Features | Remarks                                                                                                    | Explanations                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| consistent throughout<br />an application's<br />performance.                             |                      |                                                                                                           |                                                                                                                                                                                                                      |
| (f) Textual information<br />shall be provided<br />through operating<br />system functions for<br />displaying text. The<br />minimum information<br />that shall be made available is text<br />content, text input caret<br />location, and text<br />attributes. | Fully<br />Supported                             | The runtime support is also provided in order to change the text and its style. The format could be modified with the settings. | The validation on the text with the runtime is fully supported. The Format dialog can be wired to the cell in order to change the settings. From the caret position, the nearest character can be obtained from the underlying text. |
| (g) Applications shall not override user<br />selected contrast and color selections and<br />other individual display<br />attributes.                           | Fully<br />Supported                             | The settings handled in the grid will not be affected by the application.                                                           | Supports with the DPI setting, also the contrast does not affect with the variations.                                                                                                                                               |
| (h) When animation is displayed, the<br />information shall be<br />displayable in at least<br />one non-animated<br />presentation mode at the option<br />of the user.                               | Not<br />Applicable                              | This behavior is application oriented, where the animation provided in the cells will be in specific bounds and the rest of the area can be used to provide non-animated content. |                                                                                                                                                                                                                      |
| (i) Color coding shall not be used as the only means of conveying<br />information, indicating<br />an action, prompting a<br />response, or                      | Fully<br />Supported                             | Essential Grid controls provide complete functionality that conforms to the                                                                                                                                                     | Essential Grid abide by the default validation rules and constraints such that, while entering invalid values in cells, along with red color being highlighted, it prompts the respective system error message, which requires |

## API Reference
Not applicable on this page.

## Code Examples
Not applicable on this page.

## RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Text Handling, DPI Settings, Color Coding] keywords: [runtime support, text validation, animation, contrast, color attributes] -->
```