```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_812.jpeg
document_name: tools
page_number: 812
page_id: tools#page_812
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Allow Null Property

The following code snippets show how to configure a null string and set the `AllowNull` property for a `CurrencyTextBox` control.

#### Code Examples

```csharp
this.currencyTextBox1.NullString = "NULL";
this.currencyTextBox1.AllowNull = true;
```

```vb.net
Me.currencyTextBox1.NullString = "NULL"
Me.currencyTextBox1.AllowNull = True
```

#### Figure 515: `NullString = "NULL"`

![Figure 515: NullString = "NULL"](image.png)

### Currency Symbol Property

The currency symbol that will be used for formatting the display is specified by setting the `CurrencySymbol` property to any special characters.

#### Table: CurrencyTextBox Property Description

| CurrencyTextBox Property | Description                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------|
| `CurrencySymbol`          | This property specifies the currency symbol to be used in the `CurrencyTextBox`. The default value is `$`. |

#### Code Examples

```csharp
this.currencyTextBox1.CurrencySymbol = "#";
```

```vb.net
Me.currencyTextBox1.CurrencySymbol = "#"
```

### Appearance

#### Themes

The `CurrencyTextBox` control can be themed by setting `ThemesEnabled` to `true`.

#### Table: CurrencyTextBox Property Description

| CurrencyTextBox Property | Description |
|---------------------------|-------------|
| `ThemesEnabled`           | Uses themes for styling.             |

## Code Examples (Appearance)

### Themes

```csharp
this.currencyTextBox1.ThemesEnabled = true;
```

```vb.net
Me.currencyTextBox1.ThemesEnabled = True
```

## API Reference

### Methods
- `SetNullString(String nullString)`: Sets the null string for the `CurrencyTextBox`.
- `SetAllowNull(bool allowNull)`: Enables or disables the null value support.
- `SetCurrencySymbol(String currencySymbol)`: Sets the currency symbol for the `CurrencyTextBox`.
- `SetThemesEnabled(bool enabled)`: Enables or disables themes for the `CurrencyTextBox`.

### Properties
- `NullString`: Gets or sets the null string.
- `AllowNull`: Enables or disables the null value support.
- `CurrencySymbol`: Gets or sets the currency symbol.
- `ThemesEnabled`: Gets or sets whether the control is themed.

## RAG Annotations

<!-- tags: [syncfusion, winforms, currencytextbox, allownull, currenciesymbol, appearance, themes] keywords: [nullstring, specialcharacters, formatting, defaultvalue, themeenabled, runtimestyles] -->
```