<html>
    <head >
        <title>Image Preview - Small</title>
    </head>

    <body py:strip="True">
        <h2>small</h2>
        <img src="${tg.url('{url}'.format(url=url))}" alt="small_preview" style="width:256px;height:256px;">
    </body>
</html>
