```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: edit
page_number: 098
page_id: edit#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:17Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes the behavior of the AutoIndentMode property in a Windows Forms application when the Enter key is pressed.
- Explains the three possible settings of AutoIndentMode: None, Smart, and Block.
- Demonstrates the default indentation behavior for each setting with examples and visual figures.

## Content

### AutoIndentMode = "None"
When Enter is pressed while the AutoIndentMode is set to None, the text is not indented.

**Figure 29: AutoIndentMode = "None"**

![AutoIndentMode = "None"](https://user-images.githubusercontent.com/13168560/164609507-ea2d79cf-83e3-42ab-a2ef-3bf21f868f17.png)

### AutoIndentMode = "Smart"
When the AutoIndentMode is set to Smart, the next line is indented by one TabSize from the first column of the previous line when Enter is pressed.

**Figure 30: AutoIndentMode = "Smart"**

![AutoIndentMode = "Smart"](https://user-images.githubusercontent.com/13168560/164609523-24c85c3c-78c6-4f78-94ce-90d96dd5e8b2.png)

When the AutoIndentMode is set to Block, the next line begins at the same column as the previous line on pressing the ENTER key.

```html
<!-- tags: [syncfusion, winforms, autoformatter, autoindentmode, indentation, none, smart, block] keywords: [autoindentmode, enter, indentation, tabsize, blockmode, smartmode, none] -->
```
```