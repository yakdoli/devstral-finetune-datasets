```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: edit
page_number: 145
page_id: edit#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:34Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
Me.editControl.FindHistory.Insert(0, CType(ATH.addedItem, Object))
Me.editControl.FindHistory.Remove(0)
Me.editControl.FindHistory.Sort()
Me.editControl.FindHistory.Clear()
```

**Note:** The above methods can also be set for the `ReplaceHistory` and `ReplaceSearchHistory` properties.

A sample which demonstrates the above features is available in the below sample installation path:

```
..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\FindReplaceDemo
```

## 4.6.5 Enhanced Find Dialog

Essential Edit control **Find Dialog** is now enhanced with an alert message box. This displays the alert message box when find reaches the starting point of the search again.

**Note:** In search option **Current Selection**, click **OK** in alert message box, then the search area is selected again automatically as in VS editor.

## API Reference

### Namespaces, Classes, and Members
- **Methods/Properties**: `FindHistory`, `ReplaceHistory`, `ReplaceSearchHistory`
- **Parameters**:
  - Insert: Position `0`, `CType` for casting
  - Remove: `Object` related details
  - Sort: Sorting logic
  - Clear: Empties history

## Code Examples

```vb
Me.editControl.FindHistory.Insert(0, CType(ATH.addedItem, Object))
Me.editControl.FindHistory.Remove(0)
Me.editControl.FindHistory.Sort()
Me.editControl.FindHistory.Clear()
```

## Cross References
- Refer to **4.6.5 Enhanced Find Dialog** for further details on how the alert message box works.

<!-- tags: [Essential Edit, Windows Forms, Find Dialog, Replace History, Search History, Syncfusion Winforms] keywords: [ReplaceHistory, ReplaceSearchHistory, FindHistory, Enhanced Find Dialog, alert message box] -->
```