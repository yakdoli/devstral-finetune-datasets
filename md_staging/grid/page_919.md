```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_919.jpeg
document_name: grid
page_number: 919
page_id: grid#page_919
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

![Figure: Selection Mode set to "MultiExtended"](image.png)

## Format ListBox Selections

ListBoxSelection appearance can be customized by setting the properties: SelectionBackColor, SelectionTextColor and ListBoxSelectionColorOptions.

By default, SystemColors.Highlight and SystemColors.HighlightText are the colors used as backcolor and textcolor to highlight the selected records. SelectionBackColor and SelectionTextColor property settings can be used to override these default colors.

ListBoxSelectionColorOptions is used to control the appearance of the selections. The GridListBoxSelectionColorOptions enumeration specifies the options for this property.

### List of Options

- **ApplySelectionColor**

Gets the required colors from the SelectionBackColor and SelectionTextColor properties.

### Code Example

```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.ApplySelectionColor;
this.gridGroupingControl1.TableOptions.SelectionBackColor = Color.PaleGreen;
```

## API Reference

### Properties

- **ListBoxSelectionColorOptions**
  - Gets or sets the color options for the ListBox selection.
  - Type: `GridListBoxSelectionColorOptions`

- **SelectionBackColor**
  - Gets or sets the background color for the selected records.
  - Type: `System.Drawing.Color`

- **SelectionTextColor**
  - Gets or sets the text color for the selected records.
  - Type: `System.Drawing.Color`

## Code Examples

- Customizing the ListBoxSelectionColorOptions:

```csharp
this.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.ApplySelectionColor;
this.gridGroupingControl1.TableOptions.SelectionBackColor = Color.PaleGreen;
```

```xml
<!-- tags: [Essential Grid, Windows Forms, ListBoxSelection, GridListBoxSelectionColorOptions] keywords: [Syncfusion, ListBoxSelectionColorOptions, SelectionBackColor, SelectionTextColor, Grid, Windows Forms] -->
```
```