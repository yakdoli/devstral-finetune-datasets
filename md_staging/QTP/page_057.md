```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_057.jpeg
document_name: QTP
page_number: 057
page_id: QTP#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:13Z
fidelity: lossless
-->

## Content

### TabPageAdv Methods

| Method               | Description                                                |
|----------------------|------------------------------------------------------------|
| SelectPage(object tab) | Selects the tab page in the TabPageAdv control.        |
| RightClick(object tab) | Performs a rightclick on the tab page in the TabPageAdv control. |
| ClosePage(object tab) | Closes the tab page in the TabPageAdv control.          |

### XPTaskBar

| Method                | Description                                               |
|-----------------------|-----------------------------------------------------------|
| Expand(string headerText) | Expands the content area of the task bar box.        |
| Collapse(string headerText) | Collapses the content area of the task bar box.     |
| ItemClick(string headerText, string itemText) | Performs click on the item described in the tag. |

### Helper Functions

| Method                                           | Description                                                                 |
|--------------------------------------------------|-----------------------------------------------------------------------------|
| string GetTag(int itemIndex)                    | Retrieves the tag information for the given item index.                    |
| string GetHeaderText()                          | Retrieves the group or header text of the task bar box being called.        |
| string GetItemText(int itemIndex)               | Retrieves the item text for the given item index from the task bar box called |
| int GetTaskBarBoxCount()                       | Gets the number of task bar boxes in the XPTaskBar.                          |
| int GetExpandedTaskBarBoxCount()                | Gets the number of expanded task bar boxes.                                 |
| int GetCollapsedTaskBarBoxCount()              | Gets the number of collapsed task bar boxes.                                |
| bool FindItem(string itemText, out string headerText, out int itemIndex); | Helps to find an item's existence.                                       |

### TextBoxExt

## API Reference

### Methods

#### Expand(string headerText)
- **Description**: Expands the content area of the task bar box.

#### Collapse(string headerText)
- **Description**: Collapses the content area of the task bar box.

#### ItemClick(string headerText, string itemText)
- **Description**: Performs click on the item described in the tag.

#### string GetTag(int itemIndex)
- **Description**: Retrieves the tag information for the given item index.

#### string GetHeaderText()
- **Description**: Retrieves the group or header text of the task bar box being called.

#### string GetItemText(int itemIndex)
- **Description**: Retrieves the item text for the given item index from the task bar box called.

#### int GetTaskBarBoxCount()
- **Description**: Gets the number of task bar boxes in the XPTaskBar.

#### int GetExpandedTaskBarBoxCount()
- **Description**: Gets the number of expanded task bar boxes.

#### int GetCollapsedTaskBarBoxCount()
- **Description**: Gets the number of collapsed task bar boxes.

#### bool FindItem(string itemText, out string headerText, out int itemIndex)
- **Description**: Helps to find an item's existence.

## Code Examples

### C# Example: Expanding a Task Bar Box

```csharp
// Example code to expand a task bar box
xptaskBar.Expand("Header Text");
```

### C# Example: Collapsing a Task Bar Box

```csharp
// Example code to collapse a task bar box
xptaskBar.Collapse("Header Text");
```

### C# Example: Clicking an Item in a Task Bar Box

```csharp
// Example code to click an item in a task bar box
xptaskBar.ItemClick("Header Text", "Item Text");
```

## Page-level Navigation/TOC

- **TabPageAdv Methods**
- **XPTaskBar**
- **Helper Functions**
- **TextBoxExt**

## Cross References

- Related controls and features in Syncfusion Winforms.
- Additional functionality descriptions and examples can be found in the main documentation.

<!-- tags: [Syncfusion Winforms, TabPageAdv, XPTaskBar, Helper Functions, TextBoxExt] keywords: [TabPageAdv, XPTaskBar, GetTag, GetHeaderText, GetItemText, Expand, Collapse, ItemClick, ToolBarBox, FindItem] -->
```