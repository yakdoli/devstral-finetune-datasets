```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: grid
page_number: 200
page_id: grid#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:02:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

[C#]

```csharp
this.gridControl1.ShowCurrentCellBorderBehavior =
    GridShowCurrentCellBorder.AlwaysVisible;
```

## 2. Using VB.NET

[VB.NET]

```vb
'
' Set the ShowCurrentCellBorderBehavior property.
Me.gridControl1.ShowCurrentCellBorderBehavior =
    GridShowCurrentCellBorder.AlwaysVisible
```

### 4.1.4.2.12 Browse-Only Grid

The BrowseOnly property permits the Grid control to be set to a non-editable state without affecting its background appearance, displaying an unavailable effect, etc.

This feature is available in the GridDataBoundGrid and GridGrouping controls, and it is directly exposed under the controls' properties.

Applying this property will reflect in all cell types and will make the Grid non-editable. It affects the following cell types as follows:

- **ComboBox**—Items in the drop-down can be viewed but cannot be selected.
- **CheckBox**—Items cannot be selected or deselected.
- **Textbox**—Text cannot be entered in default edit mode

DropDown cells like MonthCalendar, ColorEdit, etc. will behave the same as the ComboBox cell type: items can be viewed but cannot be selected.

## Properties

| Property   | Description                                                                 | Type     | Data Type |
|------------|-------------------------------------------------------------------------------|----------|-----------|
| BrowseOnly | Gets or sets a value to determine whether the Grid should be available only for viewing and not for editing. | Boolean   | true/false |

## 4.1.4.2.12.1 Sample Link

```plaintext
{installed drive}\AppData\Local\Syncfusion\EssentialStudio\{version}\Windows\Grid.Windows\Samples\2.0\Cell Types\Editor Cell Demo
```

<!-- tags: [product, module, control, api, version?]] keywords: [k1, k2, ...] -->
```