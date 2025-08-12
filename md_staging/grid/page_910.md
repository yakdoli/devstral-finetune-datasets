```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_910.jpeg
document_name: grid
page_number: 910
page_id: grid#page_910
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:35Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The GridGrouping control in Essential Grid provides field chooser support for stacked headers. The field chooser feature enables you to customize a column in a grid at run time without modifying the database it is bound to.

## Use Case Scenarios

When you want to show or hide the columns of a stacked header in a grid without deleting its bound records, you can achieve this using this feature.

## Properties

### Table 12: Property Table

| Property           | Description                                                                                          | Type       | Data Type |
|--------------------|------------------------------------------------------------------------------------------------------|------------|-----------|
| EnableColumnsInView | Used to enable or disable the column names in the field chooser dialog.                          | Property   | Boolean   |

## Constructor

### Constructor

| Constructor | Description                                                                                           | Parameters            | Type       | Return Type |
|-------------|-------------------------------------------------------------------------------------------------------|-----------------------|------------|-------------|
| FieldChooser | Used to wire the GridGroupingControl with the field chooser.                                       | `<GridGroupingControl>` | Constructor | class       |

## Sample Link

A demo of this feature is available in the following location:

```
..\AppData\Local\Syncfusion\EssentialStudio\{Installed Version}\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping Grid Layout\Field Chooser in Stacked Header Demo
```

## Adding Field Chooser Stacked Headers in GridGroupingControl

### Steps to Add Field Chooser

1. To add field chooser, create a constructor using the FieldChooser class and pass the GridGroupingControl as the parameter.

The following code illustrates this:

```csharp
// C#
```

## Footer
© 2013 Syncfusion. All rights reserved.
<!-- tags: [Essential Grid, Windows Forms, GridGrouping control, Field Chooser, Stacked Headers, properties, constructor, sample link, field chooser demo, GridGroupingControl, Farmatting] keywords: [Essential Grid, Windows Forms, Syncfusion Winforms, GridGrouping, Stacked Headers, field chooser, properties, constructor, demo, field chooser demo, GridGroupingControl, sample code, C#] -->
```