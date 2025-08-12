```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: edit
page_number: 030
page_id: edit#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:42Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Code Example

```csharp
this.editControl.Language.Extensions.Add("aspx");
```

#### VB.NET

```vb
' Adding the necessary split definitions to the current language's Splits collection.
Me.editControl.Language.Splits.Add("<%")
Me.editControl.Language.Splits.Add("%>")

' Adding the necessary extension definitions to the current language's Extensions collection.
Me.editControl.Language.Extensions.Add("aspx")
```

6. **Invoke the `ResetCaches` method to apply these newly added configuration settings.**

#### C#

```csharp
// Reset the current configuration language cache to reflect these changes.
this.editControl.Language.ResetCaches();
```

#### VB.NET

```vb
' Reset the current configuration language cache to reflect these changes.
Me.editControl.Language.ResetCaches()
```

### See Also

- **Creating a Custom Language Configuration File**

## 4.2 Editing Features

Essential Edit comes with advanced editing features. Some of the important features discussed in this section are given below.

### 4.2.1 Undo / Redo Actions

Action Grouping allows you to specify a set of actions as groups for **Undo / Redo** purposes. When an action group is created, and a set of actions is added to it, the entire set is considered as one entity. This implies that the set of actions can be performed or undone using the **Redo** or **Undo** method call. You can use the `UndoGroupOpen`, `UndoGroupClose`, and `UndoGroupCancel` methods to programmatically manipulate the undo / redo action grouping.

---

<!-- tags: [edit, windowsforms, undo, redo, actiongrouping, syncfusionwinforms] keywords: [undo, redo, actiongrouping, editfeatures, windowsforms, syncfusionedit, essentialedit, programmingapi, customization, csharp] -->
```