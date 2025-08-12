```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_400.jpeg
document_name: grid
page_number: 400
page_id: grid#page_400
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:49Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

When you have your derived `SyncfusionCommand` class, whenever an action is taken, you will have to create a proper instance of your derived `SyncfusionCommand` class and add it to the `GridControl.CommandStack.UndoStack`. Thus, when Essential Grid needs to undo this action, your command will be popped from the `UndoStack`, and the `execute` method will be called indicating that this action needs to be undone. (Also, at this point, Essential Grid will add this same instance to the `RedoStack` so that the action can later be redone if necessary.)

### 4.1.4.10 Serialization

The following serialization techniques are discussed in this section:

#### 4.1.4.10.1 Word Converter

Export to Word is one of the most common functionalities required in the .NET world. The Essential Grid control has built-in support for Word Export. Users can download the data from the Grid Control into a Word document for offline verification and/or computation. This can be achieved by making use of the `GridWordConverter` class. This section will walk you through the conversion of the contents of the grid to a Word file as well as discuss the various converter options.

The `GridWordConverter` class derives from `GridWordConverterBase`. It contains a number of methods that help in exporting different components of the grid.

#### Properties

Here is a list of the properties offered by `GridWordConverter`. By setting these properties, you can choose the elements you need to export.

| Property     | Description                                 |
|--------------|---------------------------------------------|
| `ShowHeader` | Specifies if header should be displayed.    |
| `ShowFooter` | Indicates if footer should be displayed.    |

#### Method

`GridWordConverter` control provides a method called `GridToWord`. This is the method that does the conversion of grid contents to a Word file. It accepts two parameters: grid to be converted and filename of the destination Word document.

#### Syntax

---

<!-- tags: [Syncfusion, Windows Forms, Grid, Serialization, GridWordConverter, Word Export] keywords: [grid, word converter, serialization, showheader, showfooter, GridToWord] -->
```