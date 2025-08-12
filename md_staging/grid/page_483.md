```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_483.jpeg
document_name: grid
page_number: 483
page_id: grid#page_483
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates autosizing functionality in custom cell controls for Windows Forms Grid.
- Explains Enter Key Behavior property and its configuration options.
- Provides a visual representation of custom control integration in grid cells.

## Content

### Custom Cell Autosizing

Figure 187 illustrates the autosizing feature while adding custom controls in grid cells:

- **Data Entry User Controls** (Column B, Row 2):
  - Includes input fields labeled "Number1," "Number2," and "Sum."
  - Features a "Total" button for computation.

- **Choice List User Controls** (Column C, Row 3):
  - Contains a list titled "Hobbies" with checkboxes for options such as "Music," "Books," "Gardening," and "TV."

- **Slider Controls** (Column B, Row 4):
  - Placeholder for slider-based user input controls.

### Enter Key Behavior

#### Overview
This feature allows you to configure the Enter key behavior for the following Windows Forms Grid controls:
- Grid
- GridGrouping
- GridDataBoundGrid

By default, pressing Enter moves the cell selection to the right. The `EnterKeyBehavior` property enables you to modify this behavior.

#### Property Configuration
Using the `EnterKeyBehavior` property, you can define how the cell selection navigates when Enter is pressed. The property supports the following navigation options:

- **Bottom**
- **BottomRight**
- **Down**
- **Left**
- **MostLeft**
- **MostRight**

## API Reference

### Properties

- **EnterKeyBehavior**
  - **Type:** Enumeration
  - **Description:** Controls the navigation direction when the Enter key is pressed.
  - **Options:**
    - `Bottom`
    - `BottomRight`
    - `Down`
    - `Left`
    - `MostLeft`
    - `MostRight`

## Code Examples

```csharp
// Example: Setting EnterKeyBehavior to "Down"
GridControl grid = new GridControl();
grid.EnterKeyBehavior = GridNavigationKeyBehaviorEnum.Down;
```

## Page-level Navigation/TOC
- Custom Cell Autosizing
- Enter Key Behavior

## Cross References
- Refer to grids and controls documentation for more information on integration and configuration.
- See also: grid navigation, custom controls, data entry.

<!-- tags: [grid, windows forms, custom controls, autosizing, enter key behavior, navigation] keywords: [grids, custom controls, autosize, enter, key, behavior, navigation, data entry] -->
```