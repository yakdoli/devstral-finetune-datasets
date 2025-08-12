```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: edit
page_number: 168
page_id: edit#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:38Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview

- Demonstrates the Context Choice feature in a sample installation.
- Provides code example for closing the Context Choice.
- Highlights the Context Prompt feature and its benefits.

---

## Content

### Context Choice Example

A sample demonstrating the Context Choice feature is available in the below sample installation path.

```vb
Me.editControl.CloseContextChoice()
```

### Installation Path

The sample is located at:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Intellisense Functions\ContextChoiceandPromptDemo
```

### See Also

- **Context Prompt**

---

### 4.6.6.2.2.3 Context Prompt

The **Context Prompt** feature allows you to create pop-ups for displaying variations of syntax for the text input by using the **Context Choice**. This feature is modeled on the **Parameter Info** intellisense feature of Visual Studio. Each of the context prompt items can have a syntax specifier string and text message providing additional information on each item. The user is able to scroll through the syntax variations either by using the UP/DOWN ARROW keys or clicking on the UP/DOWN buttons on the pop-up.

## API Reference

### Methods

- **CloseContextChoice()**
  - Closes the current context choice.

## Code Examples

```vb
' Example of using Context Prompt
Me.editControl.CloseContextChoice()
```

## Cross References

- **See Also:**
  - Context Prompt

---

<!-- tags: [syncfusion winforms, context choice, context prompt, edit windows, essential studio, intellisense, parameter info] keywords: [context choice, context prompt, intellisense, parameter info, syntax variations, sample installation, documentation, code example] -->
```