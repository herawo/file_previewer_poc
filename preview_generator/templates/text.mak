<html>
    <head >
        <title>Image Preview - Text</title>
    </head>

    <body py:strip="True">
        <h2>text</h2>
        <iframe src="${tg.url('{url}'.format(url=url))}" alt="text_preview" style="width:256px;height:128px;">
    </body>
</html>