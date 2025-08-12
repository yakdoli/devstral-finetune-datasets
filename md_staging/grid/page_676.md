```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_676.jpeg
document_name: grid
page_number: 676
page_id: grid#page_676
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:00Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### 4.3.4.2.3 Binding to Custom Collections

**Custom Collections** provides a way to store arbitrary objects in a structured fashion that can be bound to the grouping grid. All the data binding is based on a set of interfaces that define different capabilities of objects and collections within the context of accessing and navigating through data. These interfaces set up a two-way communication between the bound grid and the objects collection used by the same grid. Those collections may be custom business objects collection or may be the one provided by .NET Framework itself like DataView.

The data binding interfaces will allow you to create collections of custom objects where you want to present those collections of objects together, through the grid or you can navigate through the objects to view them through the same grid and interact with them. Some of these interfaces are `IList`, `ITypedList`, or `IBindingList` whose definitions are given below.

#### The IList Interface

Using this interface, you can create an ordered, indexed set of data items. The `IList` interface is one of the most important interfaces in data binding, because complex data-bound controls can only be bound to collections that implement `IList`. This interface lets you manage the collection's data by adding, removing, inserting and accessing items.

The data source implementing the `IList` interface must have at least one record in order to make the bound controls like grid, to create any rows. It will not be notified of any data changes and thus the changes must be updated manually.

#### The ITypedList Interface

`ITypedList` is suitable for complex data binding process where you want to control which columns are visible, with which description and how they should be treated, for example, should they be read only, even there is a set clause in the property definition. Using this interface, you can tell the bound grid exactly how the objects inside a bound collection have to show up in the control and which properties should show up and how they should be treated.

In this case, it is not necessary to have any records for the rows to be created. Like `IList`, the data source will not be notified when items are added or removed from the list.

#### The IBindingList Interface

To ensure a functional and responsive bound grid, consider implementing the `IBindingList` interface for more dynamic binding scenarios, where the grid is notified of changes in the underlying data collection, allowing automatic updates to the grid's rows and columns.

<!-- tags: [Syncfusion, Winforms, grid, binding, custom collections, IList, ITypedList, IBindingList] keywords: [custom objects, two-way communication, data changes, record, visibility, dynamic changes, control] -->
```