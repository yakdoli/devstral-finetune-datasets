```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_397.jpeg
document_name: tools
page_number: 397
page_id: tools#page_397
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The flat styles for the button objects in a Calculator control is set using `CalculatorControl.FlatStyle` property. The styles are Flat, Popup, Standard (default) and System.

## Overview
- Flat style for button objects in a Calculator control.
- Using the `CalculatorControl.FlatStyle` property to set styles.
- Available styles: Flat, Popup, Standard (default), and System.

## Content

### Setting Flat Style in C#

Code in C# to set the `FlatStyle` property:

```csharp
this.calculatorControl1.FlatStyle =
System.Windows.Forms.FlatStyle.Flat;
```

### Setting Flat Style in VB.NET

Code in VB.NET to set the `FlatStyle` property:

```vb
Me.calculatorControl1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
```

### Button Styles in Calculator Control

#### Flat Style
- Buttons are displayed in a flat style with distinct color and border.
- Key buttons: Backspace, CE, C, digit buttons (7, 8, 9, 4, 5, 6, 1, 2, 3, 0), operation buttons (*, /, %, +, -, •, +/−, ., =), and memory buttons (MC, MR, MS, M+).

#### Popup Style
- Buttons are displayed in a popup style with distinct color and border.
- Key buttons: Backspace, CE, C, digit buttons (7, 8, 9, 4, 5, 6, 1, 2, 3, 0), operation buttons (*, /, %, +, -, •, +/−, ., =), and memory buttons (MC, MR, MS, M+).

#### Standard (Default) Style
- Buttons are displayed in the standard (default) style with distinct color and border.
- Key buttons: Backspace, CE, C, digit buttons (7, 8, 9, 4, 5, 6, 1, 2, 3, 0), operation buttons (*, /, %, +, -, •, +/−, ., =), and memory buttons (MC, MR, MS, M+).

#### System Style
- Buttons are displayed in the system style with distinct color and border.
- Key buttons: Backspace, CE, C, digit buttons (7, 8, 9, 4, 5, 6, 1, 2, 3, 0), operation buttons (*, /, %, +, -, •, +/−, ., =), and memory buttons (MC, MR, MS, M+).

### Visual Representation

1. **Flat Style:**
   - Displayed with clear, flat buttons.
   - Colors and borders are explicitly defined.

2. **Popup Style:**
   - Pop-up appearance with distinct styling options.

3. **Standard (Default) Style:**
   - Default appearance, matching the operating system's look and feel.
   ```markdown
   MC | 7 | 8 | 9 | / | sqrt
   MR | 4 | 5 | 6 | x | %
   MS | 1 | 2 | 3 | - | 1/x
   M+ | 0 | +/− | . | + | =
   ```
   - Buttons have subtle shadows and gradients.

4. **System Style:**
   - Matches the system's native button style.
   - ```markdown
     Backspace | CE | C
     MC | 7 | 8 | 9 | / | sqrt
     MR | 4 | 5 | 6 | x | %
     MS | 1 | 2 | 3 | - | 1/x
     M+ | 0 | +/− | . | + | =
     ```

### Summary
- Different styles for button objects in a Calculator control can be configured using the `FlatStyle` property.
- The available styles include Flat, Popup, Standard (default), and System.

<!-- tags: [syncfusion, windows forms, calculator control, flatstyle] keywords: [flat style, popup, standard, system, button objects, calculator control, property, style configuration] -->
```