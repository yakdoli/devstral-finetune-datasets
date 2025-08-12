```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_394.jpeg
document_name: tools
page_number: 394
page_id: tools#page_394
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Figure 198: Backspace Button text Font Arial, 9, Bold; Color="Black"](attachment:calculator_ui.png)

## Overview
- Focuses on keyboard support features for the Calculator control in Essential Tools for Windows Forms.
- Describes how the control mimics the functionality of a standard calculator using both mouse and keyboard inputs.
- Lists Keyboard equivalents for various Calculator buttons.

## Content

### Runtime Features

#### Keyboard Support

This section elaborates the keyboard support for the control.

Essential Tools Calculator control does the functionality of a normal calculator, using the Mouse or Keyboard, at run time. The control provides Keyboard equivalents for the Calculator buttons. They are listed in the below table.

| Button    | Description                                       | Keyboard Equivalent |
|-----------|---------------------------------------------------|---------------------|
| Backspace | Deletes the last digit of the displayed number. | BACKSPACE           |
| CE        | Clears the displayed number.                     | DELETE              |
| C        | Clears the current calculation.                   | ESC                 |
| MC        | Clears any number stored in memory.              | CTRL+L              |
| 7        | Puts this number in the calculator display.       | 7                   |
| 8        | Puts this number in the calculator display.       | 8                   |

## API Reference (if applicable)

### Methods

- **Description**: Methods related to the Calculator control.
- **Parameters**: 
  - Type: Description
  - Type: Description
- **Returns**: Type + description.
- **Exceptions**: 
  - Exception 1
  - Exception 2

## Code Examples (multi-language supported)

C# Example:
```csharp
using Syncfusion.Windows.Forms.Tools;

// Code snippet for configuring the Calculator control
Calculator calculator = new Calculator();
calculator.KeyboardSupport = true;
// Additional configuration as needed
```

## Page-level Navigation/TOC (if applicable)

- Runtime Features
  - Keyboard Support

## Cross References

- See also:
  - essential-tools-overview
  - windows-forms-controls-calculator

## RAG Annotations

<!-- tags: [essential-tools, windows-forms, calculator, runtime-features, keyboard-support, version-11.4.0.26] keywords: [keyboard equivalents, mouse support, calculator control, runtime features, syncfusion winforms, Essential Tools for Windows Forms] -->
```