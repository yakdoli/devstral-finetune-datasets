```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: edit
page_number: 077
page_id: edit#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:55Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## TAB key Functionality

The TransferFocusOnTab property allows you to specify, if the Edit Control should process the TAB key as a text input, or transfer the focus to the next control (by the order of TabIndex property value) on the Form or the User Control hosting the Edit Control.

### Example in C#

```csharp
// Insert tabs into the EditControl as text input.
this.editControl1.TransferFocusOnTab = false;

// Transfer focus to the next control.
this.editControl1.TransferFocusOnTab = true;
```

### Example in VB.NET

```vbnet
' Insert tabs into the EditControl as text input.
this.editControl1.TransferFocusOnTab = False

' Transfer focus to the next control.
this.editControl1.TransferFocusOnTab = True
```

## TAB key Functionality on Selected Text

The below given methods can be used to convert the spaces in a selected region into tabs and vice versa. Tab symbols can also be added, inserted, or removed from selected text.

### Edit Control Methods and Descriptions

| Edit Control Method        | Description                                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| TabifySelection            | Lets you convert the spaces in the selected region into equivalent number of tabs.                                                                    |
| UntabifySelection          | Lets you convert the tabs in the selected region into equivalent number of spaces.                                                                  |
| AddTabsToSelection         | Adds leading tab symbol to the selected lines, or just inserts the tab symbol.                                                                      |
| RemoveTabsFromSelection    | Removes leading tab symbol (or its spaces equivalent) from selected lines.                                                                          |

### C# Example

```csharp
// Example usage for methods
this.editControl1.TabifySelection();
this.editControl1.UntabifySelection();
this.editControl1.AddTabsToSelection();
this.editControl1.RemoveTabsFromSelection();
```

---

<!-- tags: [syncfusion, windows forms, edit control, tab key functionality, c#, vb.net] keywords: [tabifyselection, untabifyselection, addtabstoselection, removetabfromselection, transferfocusontab, selected text, synchronization, tedious] -->
```