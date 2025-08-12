```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: QTP
page_number: 031
page_id: QTP#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:03:05Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of high-level recording in QuickTest Professional (QTP) for Syncfusion controls.
- Highlights differences between high-level and low-level recording methods.
- Provides an example of Syncfusion control recognition in QTP.

## Content

### High-Level Recording in QuickTest Professional

The image shows a QuickTest Professional interface executing a script targeting a Syncfusion GridControl. The grid displays various types of cells, including:

- **CheckBox Cells**: Cell A3 and B3 with checkboxes.
- **PushButton Cells**: Cell A7 and B7 with push buttons labeled "PushButton 1" and "PushButton 2".
- **Password Cells**: Cell A10 is filled with asterisks to represent password input.
- **Currency Cells**: Cells A13 and B13 display monetary values: "$456.00" and "(€739.00)".
- **MaskEdit Cells**: Cell A16 and B16 show formatted input: "(440-091-11)" and "( -- )".
- **Formula Cell**: Cell G6 contains a formula: "4 + 2 + 2 = 8".
- **Radio Button Cells**: Cell A19 and B19 with radio buttons labeled "radio 0" and "radio 1".

The script recorded in QTP includes the following commands:

```plaintext
1: SwWindow("GridControl").Activate
2: SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell 14,4
3: SwWindow("GridControl").Move 336,246
4: SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell 15,6
```

#### Explanation of Recording

This is called **high-level recording** because:

- The events are recorded with the method names of the `Syncfusion` namespace after QTP recognizes the Syncfusion control.
- Unlike low-level recording, where the Syncfusion controls are not recognized by QTP, and events are recorded using default method names.

**Low-Level Recording vs. High-Level Recording**:

- **Low-Level Recording**: QTP does not recognize Syncfusion controls and records events using default method names.
- **High-Level Recording**: QTP recognizes Syncfusion controls and records events with the correct method names, providing more precise and maintainable test scripts.

### Observations

- The QTP interface is shown in **Expert View**, indicating a detailed view of the recorded actions.
- The red "Recording" bar at the bottom of the QTP interface indicates that the recording is in progress.
- The grid in the Syncfusion application is clearly demonstrated, illustrating various input types and cell functionalities.

## API Reference

### Namespaces and Methods

#### Syncfusion Namespace
- **SwWindow**: Used to interact with the grid window.
- **SwObject**: Used to manipulate specific objects within the grid.
- **Activate**: Activates the grid control.
- **SetCurrentCell**: Sets the focus to a particular cell in the grid.
- **Move**: Moves the cursor to a specific position.

## Code Examples

### High-Level Recording Example
```csharp
SwWindow("GridControl").Activate;
SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell(14, 4);
SwWindow("GridControl").Move(336, 246);
SwWindow("GridControl").SwObject("gridControl1").SetCurrentCell(15, 6);
```

### Low-Level Recording Example
```csharp
// Default method names without Syncfusion recognition
SwWindow("GridControl").Activate;
SwWindow("GridControl").SwObject("gridControl1").ActiveCell(14, 4);
SwWindow("GridControl").Move(336, 246);
SwWindow("GridControl").SwObject("gridControl1").ActiveCell(15, 6);
```

## Cross References

- Refer to the Syncfusion QuickTest Professional integration documentation for more details on configuration and setup.
- See the QTP user guide for general information on low-level and high-level recording techniques.

## RAG Annotations
<!-- tags: [quicktest professional, qtp, syncfusion gridcontrol, high-level recording, low-level recording, gridcontrol example, api recognition] keywords: [syncfusion, qtp, gridcontrol, high-level, low-level, recording, test automation, checkbox, pushbutton, password, currency, maskedit, formula, radiobutton] -->
```