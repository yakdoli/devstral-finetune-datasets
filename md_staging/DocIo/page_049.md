<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_049.jpeg
document_name: DocIo
page_number: 049
page_id: DocIo#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:35Z
fidelity: lossless
-->

# Essential DocIO

A controller action cannot return an action result directly. For example, if you want to return a view from a controller action, you don't return a ViewResult. Instead, you call the `View` method. The `View` method instantiates a new `ViewResult` and returns the new `ViewResult` to the browser.

## Extension Methods

Extension Methods enable you to "add" methods to existing types without creating a new derived type, recompiling, or otherwise modifying the original type. An extension method is a special kind of static method, but is called as if it were an instance method on the extended type.

Extension methods are defined as static methods, but are called by using the instance method syntax. The first parameter of this method specifies the type on which the method operates, and is preceded by the "this" modifier. Extension methods are only in scope when you explicitly import the namespace into your source code with a using directive.

An extension method named `ExportAsActionResult` has to be created to add the Controller class. The `ExportAsActionResult` method returns a `DocResult`.

### Example: `ExportAsActionResult` Extension Method

```csharp
public static DocResult ExportAsActionResult(this IWordDocument document, string filename, FormatType formattype, HttpResponse response, HttpContentDisposition contentDisposition)
{
    return new DocResult(document, filename, formattype, response, contentDisposition);
}
```

### Step 3: Controller

Add the following code in the Controller's action result.

#### HelloWorld Action Method Example

```csharp
public ActionResult HelloWorld()
{
    return View();
}
[AcceptVerbs(HttpVerbs.Post)]
```

## API Reference

### ExportAsActionResult Method

- **Parameters**:
  - `document`: Type - `IWordDocument`
  - `filename`: Type - `string`
  - `formattype`: Type - `FormatType`
  - `response`: Type - `HttpResponse`
  - `contentDisposition`: Type - `HttpContentDisposition`

## Code Examples

The provided example demonstrates how to use the `ExportAsActionResult` extension method to return a `DocResult` from an action in a controller.

## Notes

In the preceding code example, one extension is defined for the type, `IWordDocument`.

## Cross References

See also:
- [DocIo Overview]
- [Controller Actions in ASP.NET MVC]
- [Static Methods in C#]

<!-- tags: [DocIo, extension methods, ASP.NET MVC, controller, static methods, C#] keywords: [ExportAsActionResult, IWordDocument, DocResult, action result, controller action] -->