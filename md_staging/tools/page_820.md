```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_820.jpeg
document_name: tools
page_number: 820
page_id: tools#page_820
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:46Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Culture Settings

Here are examples in C# and VB.NET that demonstrate how to display culture settings:

#### [C#]

```csharp
this.label11.Text = this.currencyTextBox1.Culture.DisplayName;
this.label12.Text = this.currencyTextBox1.Culture.EnglishName;
this.label13.Text = this.currencyTextBox1.Culture.NativeName;
this.label14.Text = this.currencyTextBox1.Culture.ThreeLetterWindowsLanguageName;
```

#### [VB.NET]

```vb
Me.label11.Text = Me.currencyTextBox1.Culture.DisplayName
Me.label12.Text = Me.currencyTextBox1.Culture.EnglishName
Me.label13.Text = Me.currencyTextBox1.Culture.NativeName
Me.label14.Text = Me.currencyTextBox1.Culture.ThreeLetterWindowsLanguageName
```

**Figure 522: Culture Settings**

![Culture Settings](https://user.com/userimage.jpg)

#### Event Handling

- **CurrencyTextBox** triggers events in the following scenarios:
  - When the 3D border style is changed.
  - When the border color is changed.
  - When the border sides are altered.
  - When the decimal value property is modified.
  - When the Themes enabled property is changed.
  - Additionally, it fires an event when the input text is invalid.

---

**KeyDown**: Occurs when a key is pressed while the control has focus. The event handler receives an argument of type `KeyEventArgs`. This event can be used to add keyboard support to the `CurrencyTextBox`. Refer to **Adding the Key Support for Mega and Kilo**.

**ValidationError**: Triggered when an inappropriate character is encountered. The event handler receives an argument of type `ValidationEventArgs`.

## API Reference

### Events

- **KeyDown**
  - **Description**: Triggered when a key is pressed while the control has focus.
  - **Parameters**: `EventArgs` of type `KeyEventArgs`.

- **ValidationError**
  - **Description**: Triggered when an invalid character is entered.
  - **Parameters**: `EventArgs` of type `ValidationEventArgs`.

## Code Examples

The examples above demonstrate how to handle culture settings and event management in a `CurrencyTextBox` control.

---

#### Cross References
- **Adding the Key Support for Mega and Kilo**

<!-- tags: [syncfusion, winforms, currencytextbox, culture, eventhandling] keywords: [currencytextbox, culture, displayname, englishname, nativename, threeletterwindowslanguagename, keydown, validationerror] -->
```