```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_697.jpeg
document_name: tools
page_number: 697
page_id: tools#page_697
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
// Declare the FolderBrowser component.
private Syncfusion.Windows.Forms.FolderBrowser folderBrowser1;

// Create an instance of the FolderBrowser component.
this.folderBrowser1 = new Syncfusion.Windows.Forms.FolderBrowser(this.components);
```

```vb.net
' Declare the FolderBrowser component.
Private folderBrowser1 As Syncfusion.Windows.Forms.FolderBrowser

' Create an instance of the FolderBrowser component.
Me.folderBrowser1 = New Syncfusion.Windows.Forms.FolderBrowser(Me.components)
```

## Setting the FolderBrowser.StartLocation and FolderBrowser.Style Property Values

### Step 1: C#

```csharp
// Specify the Start location.
this.folderBrowser1.StartLocation = Syncfusion.Windows.Forms.FolderBrowserFolder.MyComputer;

// Specify the styles for the FolderBrowser Dialog.
this.folderBrowser1.Style = (Syncfusion.Windows.Forms.FolderBrowserStyles.RestrictToFilesystem | Syncfusion.Windows.Forms.FolderBrowserStyles.BrowseForComputer);
```

### Step 1: VB.NET

```vb.net
' Specify the Start location.
Me.folderBrowser1.StartLocation = Syncfusion.Windows.Forms.FolderBrowserFolder.MyComputer

' Specify the styles for the FolderBrowser Dialog.
Me.folderBrowser1.Style = Syncfusion.Windows.Forms.FolderBrowserStyles.RestrictToFilesystem Or Syncfusion.Windows.Forms.FolderBrowserStyles.BrowseForComputer
```

## Invoking the FolderBrowser.ShowDialog() Method

### Step 3: C#

```csharp
// Invoke the FolderBrowser.ShowDialog() method to display the FolderBrowser Dialog.
this.folderBrowser1.ShowDialog();
```

<!-- tags: [Syncfusion, Winforms, FolderBrowser, Dialog, ShowDialog, C#, VB.NET] keywords: [Syncfusion, Winforms, FolderBrowser, StartLocation, Style, MyComputer, RestrictToFilesystem, BrowseForComputer, ShowDialog, C#, VB.NET] -->
```