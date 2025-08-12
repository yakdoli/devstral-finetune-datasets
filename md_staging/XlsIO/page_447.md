```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_447.jpeg
document_name: XlsIO
page_number: 447
page_id: XlsIO#page_447
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:41Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
void SubFoldersFiles(string path)
{
    DirectoryInfo dInfo = new DirectoryInfo(path);
    foreach (DirectoryInfo d in dInfo.GetDirectories())
    {
        SubFoldersFiles(d.FullName);
        arr.Add(d);
    }
}

// Zip and save the file.
private void button1_Click(object sender, EventArgs e)
{
    SubFoldersFiles(this.textBox1.Text);

    if (Directory.Exists(this.textBox1.Text))
    {
        AddRootFiles();

        AddSubFoldersFiles();

        // Saving zipped file.
        SaveFileDialog saveDialog = new SaveFileDialog();
        saveDialog.Filter = "Zip Files (*.zip)";
        if (saveDialog.ShowDialog() == DialogResult.OK)
            zipArchive.Save(saveDialog.FileName);

        zipArchive.Close();
        label1.Text = "Files Zipped successfully!";
        button1.Enabled = false;
    }
}

private void AddRootFiles()
{
    foreach (string rootfiles in Directory.GetFiles(this.textBox1.Text))
    {
        stream = new FileStream(rootfiles, FileMode.Open, FileAccess.Read);
        att = File.GetAttributes(rootfiles);
        item = new ZipArchiveItem(rootfiles, stream, true, att);
        zipArchive.AddItem(item);
    }
}
```

## API Reference

### Methods

- `SubFoldersFiles(string path)`
  - **Description**: Recursively processes subdirectories and files in the specified path.
  - **Parameters**:
    - `path`: The directory path to process.
  - **Returns**: void
  - **Description**: This method traverses each directory and folder within the specified path and adds them to a collection.

- `AddRootFiles()`
  - **Description**: Adds the root files to the zip archive.
  - **Parameters**: None
  - **Returns**: void
  - **Description**: This method iterates over the files in the root directory and adds each file to the zip archive.

### Events

- `button1_Click(object sender, EventArgs e)`
  - **Description**: Handles the button click event to initiate the zipping process.
  - **Parameters**:
    - `sender`: The source of the event.
    - `e`: Event arguments.
  - **Returns**: void
  - **Description**: This method is triggered when the button is clicked, executing the process to zip and save files.

<!-- tags: [Syncfusion Winforms, XlsIO, Zip Archiving, File Management] keywords: [subfolders, files, zip, save, directory, recursion, event handling, stream, attributes, archive] -->
```