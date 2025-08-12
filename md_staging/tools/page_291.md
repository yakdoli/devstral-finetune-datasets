```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: tools
page_number: 291
page_id: tools#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of `AutoComplete` control in Windows Forms.
- Focuses on `CaseSensitive` and `OverrideCombo` properties of `AutoComplete`.

## Content

### CaseSensitive

```vb.net
Me.autoComplete1.CaseSensitive = True
```

**Figure 123: CaseSensitive = "True"**

![](attachment:///images/Figure_123_case_sensitive.png)

### Overriding Combo

The ComboBox drop-down can be suppressed and overridden by the AutoComplete control using the `OverrideCombo` property.

#### C#

```csharp
this.autoComplete1.OverrideCombo = true;
```

#### VB.NET

```vb.net
Me.autoComplete1.OverrideCombo = True
```

### Sorting

The items in the list can be sorted automatically by setting `AutoSortList` to true.

#### AutoComplete Properties

| AutoComplete Properties | Description |
|--------------------------|-------------|
| AutoSortList             | Specifies whether default sorting is to be performed. |

#### C#

```csharp
this.autoComplete1.AutoSortList = true;
```

#### VB.NET

```vb.net
Me.autoComplete1.AutoSortList = True
```

## API Reference

### Properties

- **AutoSortList:** Specifies whether default sorting is to be performed.

## Code Examples

#### Example 1: Setting AutoSortList

**C#**

```csharp
this.autoComplete1.AutoSortList = true;
```

**VB.NET**

```vb.net
Me.autoComplete1.AutoSortList = True
```

#### Example 2: Configuring CaseSensitive

**C#**

```csharp
this.autoComplete1.CaseSensitive = true;
```

**VB.NET**

```vb.net
Me.autoComplete1.CaseSensitive = True
```

## Cross References

- Refer to the main documentation for more details on `AutoComplete` control configurations and usage scenarios.

<!-- tags: [AutoComplete, AutoSortList, OverrideCombo, CaseSensitive] keywords: [AutoComplete, Windows Forms, properties, CaseSensitive, OverrideCombo, AutoSortList, VB.NET, C#] -->
```