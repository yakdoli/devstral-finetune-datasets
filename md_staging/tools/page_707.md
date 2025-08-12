```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_707.jpeg
document_name: tools
page_number: 707
page_id: tools#page_707
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- This section discusses the tools and settings available for customizing the FolderBrowser control in Windows Forms.
- Covers the use of flags to modify the behavior of the FolderBrowser Dialog.
- Provides examples in both C# and VB.NET to demonstrate the application of specific FolderBrowser styles.
- Introduces the concept of Editor Controls, focusing on rich edit controls supported by Syncfusion.
- Describes the features and functionality of the CurrencyEdit control.

## Content

### 3.5.7.1.5 Frequently Asked Questions

This section will help you become more familiar in using the FolderBrowser control.

#### 3.5.7.1.5.1 What are FolderBrowser Flags?

Flags can be used to set various styles for the FolderBrowser Dialog. Each style has its own behavior, and these styles can be added or removed to get the desired style for the FolderBrowser Dialog.

Look at the below given snippet to apply "RestrictToSubfolders" style and to remove the "ShowTextBox" style for the FolderBrowser Dialog.

```csharp
this.folderBrowser1.Style &= ~FolderBrowserStyles.RestrictToSubfolders;
this.folderBrowser1.Style |= FolderBrowserStyles.ShowTextBox;
```

```vb.net
Me.folderBrowser1.Style = Me.folderBrowser1.Style And Not _
    FolderBrowserStyles.RestrictToSubfolders
Me.folderBrowser1.Style = Me.folderBrowser1.Style Or _
    FolderBrowserStyles.ShowTextBox
```

### 3.5.8 Editor Controls

The following are the rich edit controls supported by Syncfusion.

#### 3.5.8.1 CurrencyEdit

**CurrencyEdit** embeds a **CurrencyTextBox** control and a button to provide a drop-down calculator to enable calculations with the contents of the **CurrencyTextBox**. The **CurrencyEdit** control provides an easy way to collect and display the currency data.

## API Reference (if applicable)

Not applicable for this specific section.

## Code Examples (multi-language supported)

- **C# Example**:
  ```csharp
  this.folderBrowser1.Style &= ~FolderBrowserStyles.RestrictToSubfolders;
  this.folderBrowser1.Style |= FolderBrowserStyles.ShowTextBox;
  ```

- **VB.NET Example**:
  ```vb.net
  Me.folderBrowser1.Style = Me.folderBrowser1.Style And Not _
      FolderBrowserStyles.RestrictToSubfolders
  Me.folderBrowser1.Style = Me.folderBrowser1.Style Or _
      FolderBrowserStyles.ShowTextBox
  ```

## Cross References

- Refer to the sections on FolderBrowser styles and Editor Controls for more details.

<!-- tags: [Syncfusion Winforms, Editor Controls, FolderBrowser, CurrencyEdit] keywords: [FolderBrowser control, FolderBrowserDialog, FolderBrowserFlags, CurrencyTextBox, CurrencyEdit, editor controls, control styles] -->
```