```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_922.jpeg
document_name: tools
page_number: 922
page_id: tools#page_922
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Sorting the Items

Sorting of the items can be enabled using the `Sorted` property. By default, it is set to `false`.

### Code Example: C#

```csharp
this.fontListBox1.Sorted = true;
```

### Code Example: VB.NET

```vb
Me.fontListBox1.Sorted = True
```

## AutoCompleting the Items

The `FontListBox` control has the ability to auto-complete the items as we type in the listbox. This feature is enabled by setting the `UseAutoComplete` property to `true`.

### Code Example: C#

```csharp
this.fontListBox1.UseAutoComplete = true;
```

### Code Example: VB.NET

```vb
Me.fontListBox1.UseAutoComplete = True
```

## 3.5.9.1.4 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

### 3.5.9.1.4.1 How to display the scrollbars always, irrespective of the number of items

The scrollbar can be always made visible, irrespective of the number of items present in it, by setting the `ScrollAlwaysVisible` property to `true`.

### Code Example: C#

```csharp
this.fontListBox1.ScrollAlwaysVisible = true;
```

### Code Example: VB.NET

```vb
Me.fontListBox1.ScrollAlwaysVisible = True
```

<!-- tags: [sort, auto-complete, scrolling, FontListBox, Syncfusion Winforms] keywords: [scrollbars, always visible, task-based queries, frequently asked questions, Windows Forms, sorting, auto-complete, scrollAlwaysVisible property, Syncfusion tools] -->
```