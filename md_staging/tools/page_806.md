```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_806.jpeg
document_name: tools
page_number: 806
page_id: tools#page_806
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:57Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

![](image.png)

Figure 508: CurrencyTextBox Being Resized at Run Time, When WordWrap = "True"

![](image-1.png)

Figure 509: CurrencyTextBox Control with Horizontal and Vertical Scrollbars

### Password Character

We can display password characters instead of the digits in the text field using the `PasswordChar` property. To use the system password character in the text field, set the `UseSystemPasswordChar` property to `true`.

#### C#

```csharp
this.currencyTextBox1.UseSystemPasswordChar = false;
this.currencyTextBox1.PasswordChar = '*';
```

#### VB.NET

```vb
Me.currencyTextBox1.UseSystemPasswordChar = False
Me.currencyTextBox1.PasswordChar = "*"
```

![](image-2.png)

Figure 510: PasswordChar = "*"

### Banner Text Support

We can set banner text for the CurrencyTextBox control. Refer to the `BannerTextProvider Component` topic for more details.

## Footer

© 2013 Syncfusion. All rights reserved. 806 | Page
```

<!-- tags: [product, windows forms, essential tools, currency textbox, password character, banner text support] keywords: [currencytextbox, passwordchar, usesystempasswordchar, banner text, syncfusion winforms] -->