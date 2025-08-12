```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_612.jpeg
document_name: grid
page_number: 612
page_id: grid#page_612
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The `GridEngine` class adds the plumbing for displaying the data in a Grid Grouping control. You can specify the datasource using the `DataSource` and `DataMember` properties through the designer. It is instantiated with the virtual `GridGroupingControl.CreateEngine` method. If you want to customize the engine object, you should subclass this class and should override the `CreateEngine` method.

The `GridEngine` object is the main grouping engine object. It is derived from the `Syncfusion.Grouping.Engine` base class and adds Windows Forms specific functionality such as support for a `Forms BindingContext` and `CurrencyManager`. `GridEngine` also has special overrides of the virtual `Engine.CreateTableDescriptor` and `Engine.CreateTable` methods so that the grid-specific derived `GridTable` class and `GridTableDescriptor` class are instantiated.

## 4.3.4 Concepts and Features

This section provides you a basic insight into the grid grouping control architecture packed with detailed information on the features of the Essential Grid. It will also give you an overview of the major control classes.

Here you will learn about the following concepts which will help you to get familiar with Grid Grouping control.

### 4.3.4.1 Performance

Grid Grouping control has an **extremely high performance standard**. It can handle very high frequency updates and refresh scenarios. It also offers complete support for Virtual Mode wherein the data will be loaded only on demand. By simply setting few properties, you can have the grid work with large amounts of data without a performance hit.

All the properties that affect grid performance are wrapped into a category named **Optimization**. Here is an image of the property grid listing various optimization properties.

## API Reference (if applicable)

Not applicable for this section.

## Code Examples (multi-language supported)

No code examples provided in this section.

## Cross References

Not applicable for this section.

<!-- tags: [Essential Grid, WinForms, GridEngine, Performance, Virtual Mode, Optimization] keywords: [grid grouping control, performance standard, Virtual Mode, optimization, performance hit, large data, Grouping control] -->
```