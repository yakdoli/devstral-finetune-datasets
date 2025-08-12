```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_448.jpeg
document_name: XlsIO
page_number: 448
page_id: XlsIO#page_448
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:19:00Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
private void AddSubFoldersFiles()
{
    foreach (DirectoryInfo dInfo in arr)
    {
        FileInfo[] fInfo = dInfo.GetFiles();
        foreach (FileInfo file in fInfo)
        {
            string str = file.FullName;
            stream = new FileStream(str, FileMode.Open, FileAccess.Read);
            FileAttributes att = File.GetAttributes(str);
            zipArchive.AddItem(new Syncfusion.Compression.Zip.ZipArchiveItem(str, stream, true, att));
        }
    }
}

// Browse folder.
private void button2_Click(object sender, EventArgs e)
{
    // Select the folder to be zipped.
    FolderBrowserDialog fldrDialog = new FolderBrowserDialog();
    fldrDialog.Description = "Select the folder to zip. Note: All its subfolders and its files will zip too.";
    if (fldrDialog.ShowDialog() == DialogResult.OK)
    {
        this.textBox1.Text = fldrDialog.SelectedPath;
        this.button1.Enabled = true;
    }
}

// Close
private void button3_Click(object sender, EventArgs e)
{
    Close();
}
```

### [VB.NET]

```vb
Private Sub SubFoldersFiles(ByVal path As String)
    Dim dInfo As New DirectoryInfo(path)
    For Each d As DirectoryInfo In dInfo.GetDirectories()
        SubFoldersFiles(d.FullName)
        arr.Add(d)
    Next
End Sub
```

## API Reference

### Namespace: Syncfusion.Compression.Zip

#### Methods
- **AddItem(ZipArchiveItem item):**
  Adds the specified `ZipArchiveItem` to the zip archive.
  - **Parameters:**
    - `item`: The `ZipArchiveItem` to be added.
  - **Returns:** `void`

#### Classes
- **ZipArchiveItem**
  Represents a item in the zip archive.
  - **Constructors:**
    - **ZipArchiveItem(string name, Stream contents, bool canWrite, FileAttributes fileAttributes):**
      Creates a new `ZipArchiveItem` with the specified name, contents, write access, and file attributes.
      - **Parameters:**
        - `name`: The file name of the zip entry.
        - `contents`: The `Stream` containing the contents of the entry.
        - `canWrite`: A boolean indicating whether the entry can be written.
        - `fileAttributes`: The file attributes of the entry.

### Classes
- **FolderBrowserDialog**
  Displays a dialog that allows the user to select a folder.
  - **Methods:**
    - **ShowDialog():**
      Displays the dialog as a modal dialog.
    - **GetSelectedPath():**
      Gets the path of the selected folder.
    - **Description:**
      Sets the description text for the dialog.

### Properties
- **SelectedPath:**
  Gets or sets the path of the folder selected by the user.

## Code Examples

```csharp
using Syncfusion.Compression.Zip;

// Example of creating a zip archive
ZipArchive zipArchive = new ZipArchive(zipFilePath, FileMode.Create, FileAccess.Write);
AddSubFoldersFiles(zipArchive);
zipArchive.Close();
```

## Cross References

See also:
- [FolderBrowserDialog](https://help.syncfusion.com/windowsforms/folderbrowserdialog)
- [ZipCompression in C#](https://help.syncfusion.com/windowsforms/zipcompression)

<!-- tags: [Syncfusion Winforms, XlsIO, ZipCompression, FolderBrowserDialog, C#, VB.NET] keywords: [zipArchive, zipArchiveItem, fileAttributes, Browse folder, subfolders, files, winforms, folderbrowserdialog, close] -->
```