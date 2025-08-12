```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: grouping
page_number: 027
page_id: grouping#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:16Z
fidelity: lossless
-->



### Essential Grouping

```vb
Dim i As Integer

For i = 0 To 10
    list.Add(New MyObject(r.Next(5)))
    Console.WriteLine(list(i))
Next

' Pause
Console.ReadLine()
End Sub
```

The console display showing random `MyObjects` is illustrated below:

![Console Display Showing Random MyObjects](https://i.imgur.com/oOaFZ.jpg)

**Figure 12: Console Display Showing Random MyObjects**

4. An `ArrayList` of Objects is created.

#### 4.1.2 Setting a Datasource In the Grouping Engine

Add the following grouping namespace for referring the assemblies deployed in the application.

**i** Refer Deploying Essential Grouping section to know about deploying Essential Grouping.

```csharp
using Syncfusion.Grouping;
```

**Note:** The namespace `Syncfusion.Grouping` should be included to utilize the Essential Grouping engine in your application.

---
```html
<!-- tags: [syncfusion, essential grouping, datasource, datasources, list, object] keywords: [essential grouping, setting, datasource, deploy, group grouping, syncfusion grouping] -->
```