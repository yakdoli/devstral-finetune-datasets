```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_336.jpeg
document_name: tools
page_number: 336
page_id: tools#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

### Method Properties and Their Descriptions

| Property/Method       | Description                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------|
| `AutoAppend`          | Specifies whether autoappend is enabled or not (`true` or `false`)                                   |
| `categoryName`        | Category to which contents in this control belong to.                                               |
| `items`               | Reference to an item list.                                                                          |
| `maxItems`            | Specifies the maximum number of items.                                                              |
| `GetAutoAppend`       | Returns the `AutoAppend` info associated with the control. The parameter is the control.              |

### Code Examples

#### C#

```csharp
// Calling this will enable AutoAppend behavior in the control.
autoappend1.SetAutoAppend(cmbBox, new AutoAppendInfo(true, "category name", al, 10)); // al is an IList object
```

#### VB.NET

```vb
' Calling this will enable AutoAppend behavior in the control.
autoappend1.SetAutoAppend(cmbBox, New AutoAppendInfo(True, "category name", al, 10)) ' al is an IList object
```

### See Also

- [Adding New Entries Programmatically](#)
- [3.5.1.2.4.3 Adding New Entries Programmatically](#)

### Adding New Entries Programmatically

To add or move an item to the top of controls' `AutoAppend` list, call the method `InsertOrMoveToTop`. If the item is already present, it will be moved to the first place; otherwise, it will be added.

- **Arguments**: 
  - First one is the associated control.
  - Second is the value in string.

#### C#

```csharp
this.autoAppend1.InsertOrMoveToTop(this.comboBox1, "www.syncfusion.com");
```

#### VB.NET

```vb
' Example code to be filled if available.
```

---

<!-- tags: [Syncfusion Winforms, AutoAppend, Control Properties, Programmatically Adding Entries] keywords: [AutoAppendInfo, control, maxItems, items, categoryName, GetAutoAppend, InsertOrMoveToTop, AutoAppend behavior, Adding Entries Programmatically] -->
```