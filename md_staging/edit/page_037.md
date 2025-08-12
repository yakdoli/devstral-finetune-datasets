```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: edit
page_number: 037
page_id: edit#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:24Z
fidelity: lossless
-->

## EnableMD5 Property

### Overview
- Focuses on the EnableMD5 property which determines whether the MD5 algorithm is enabled or disabled in the application.
- Provides code samples in C# and VB.NET to illustrate how to enable the MD5 algorithm programmatically.
- Includes a note on how to enable FIPS (Federal Information Processing Standards) compliance in Windows settings.

### Content

#### Table: EnableMD5 Property
| Property      | Description                                                                 |
|---------------|------------------------------------------------------------------------------|
| EnableMD5     | Specifies whether to enable or disable the MD5 algorithm.                  |

#### Code Samples

**C#**
```csharp
this.editControl1.EnableMD5 = true;
```

**VB.NET**
```vb
Me.editControl1.EnableMD5 = True
```

#### Note: Enabling FIPS
To enable FIPS compliance:
1. Click **Start**, click **Control Panel**, and then click on **Administrative Tools**.
2. Double-click **Local Security Policy**.
3. Double-click **Local Policies**.
4. Click **Security Options**. Under the **Policies** listed in the right pane, double-click **System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing**.
5. Select **Enabled** to enable FIPS on your machine.

### 4.2.4 Keystroke - Action Combinations Binding

#### Overview
- Describes the action-keystroke binding functionality in Edit Control.
- Explains how to customize keystroke combinations to perform standard or custom commands in the designer.

#### Keystroke Binding Process
Edit Control offers the ability to customize action-keystroke bindings. You can bind any desired keystroke combination to standard commands like Copy, Cut, Paste, or Find. The procedure is as follows:

1. In the **Editor Keys Binding** dialog box, select the desired standard command. The default shortcuts assigned for a particular command are listed in the combobox under the **Shortcut(s)** for selected command: label.
2. Set the focus to the **Edit Box Press TAB** to navigate to the shortcuts drop-down list.
3. Press the desired key or key combination.
4. Click the **Assign** button to assign this keystroke combination as the shortcut for that particular standard command. Click **OK**.

#### API Reference
- The `KeyBinder` property is used to get the key binder.
- The `KeyBindingProcessor` property is used to get/set the key binding processor.

<!-- tags: [syncfusion, winforms, enablemd5, keystroke binding, action combinations, fips, editcontrol] keywords: [enablemd5, keystroke, action combinations, fips, keybinding, editcontrol] -->
```