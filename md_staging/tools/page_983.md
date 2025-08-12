```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_983.jpeg
document_name: tools
page_number: 983
page_id: tools#page_983
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Me.radioButtonAdv1.Checked = True
```

**Figure 635: Check States**

![Figure 635: Check States](https://i.imgur.com/3Ys6zjD.png)

## See Also

- `RadioButtonAdv Values`
- `Image Settings`
- `RadioButtonAdv Events`

### 3.5.11.2.3.1.2 RadioButtonAdv Values

This section discusses how values can be associated with the various check states.

Both integer and string values can be associated with the check states as follows.

| **RadioButtonAdv Properties** | **Description**                  |
| ----------------------------- | -------------------------------- |
| `CheckedInt`                  | Specifies the integer value when checked. |
| `CheckedString`               | Specifies the string value when checked. |
| `UncheckedInt`                | Specifies the integer value when Unchecked. |
| `UncheckedString`             | Specifies the string value when Unchecked. |
| `IntValue`                    | Gets / sets checked `RadioButtonAdv` in current container according to the `TabIndex`. |

#### C#

```csharp
this.radioButtonAdv1.CheckedInt = 3;
this.radioButtonAdv1.CheckedString = "RadioButtonAdv is Checked";
this.radioButtonAdv1.UncheckedInt = 3;
this.radioButtonAdv1.UncheckedString = "RadioButtonAdv is Unchecked";
this.radioButtonAdv1.IntValue = 5;
```

#### VB.NET
```vb
' No VB.NET code provided in the image
```
 <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```