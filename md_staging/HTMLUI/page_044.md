```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_044.jpeg
document_name: HTMLUI
page_number: 044
page_id: HTMLUI#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:16Z
fidelity: lossless
-->

## Loading Files from Embedded Resources

### Overview
- Learn how to load an HTML file from an embedded resource using `System.IO` and `System.Reflection`.
- Demonstrates loading an embedded HTML file and displaying its content in a WinForms application.

### Content

#### Loading HTML from Embedded Resources

The following code snippets illustrate how to load an HTML file marked as an embedded resource in a Windows Forms application.

```csharp
("LoadingFileFromResource.resfile.htm");

this.htmluiControl1.LoadHTML(htmlStream);
```

```vbnet
' Load the specified HTML file which is marked as the project's embedded resource.
Private htmlStream = CType(System.Reflection.Assembly.GetExecutingAssembly().GetManifestResourceStream("LoadingFileFromResource.resfile.htm"), Stream)
Me.HtmluiControl1.LoadHTML(htmlStream)
```

It is necessary to invoke the `System.IO` and `System.Reflection` namespaces to use the classes and their methods used in the code above.

##### Key Concepts
- **System.Reflection.Assembly.GetExecutingAssembly**: Retrieves the current assembly from which the code is running.
- **GetManifestResourceStream**: Loads the specified manifest resource from the assembly.
- **System.IO.Stream**: Provides a generic view of a sequence of bytes needed for embedded resource loading.

##### Note
The string entered inside the `GetManifestResourceStream` method is in reference to the Default namespace found in the Properties window of the C# file in the Solution Explorer. This may vary for the users.

The following image shows a file loaded from an embedded resource.

![File Loaded from Embedded Resource](https://i.imgur.com/8ym5pKu.png)

- **Title**: HTMLUI
- **Content**: LoadFileFromEmbeddedResource
- **Image**: Displays the Syncfusion logo and text "File Loaded From Embedded Resource".

### Conclusion
This section demonstrates the process of loading HTML files from embedded resources, ensuring seamless integration within a Windows Forms application.

### References
- Syncfusion WinForms Documentation

#### See also
- [Syncfusion HTMLUI Documentation](https://www.syncfusion.com/products/winforms/htmlui)
- [Embedding Resources in .NET Applications](https://docs.microsoft.com/dotnet/standard/assembly/manifestresources)

<!-- tags: [SyncfusionWinforms, HTMLUI, EmbeddedResources, System.IO, System.Reflection] keywords: [HTMLUI, embedded resources, System.IO, System.Reflection, Windows Forms, loading HTML, resources, manifest resources] -->
```
