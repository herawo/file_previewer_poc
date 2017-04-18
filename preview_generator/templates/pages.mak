<html>
    <head >
        <title>Image Preview - Pages</title>
    </head>

    <body py:strip="True">
        <h2>Pages</h2>
        <a href="${tg.url('/documents/{doc_id}/pages/1'.format(doc_id=document_id))}">
            <button type="button"> pages </button>
        </a>

    </body>
</html>
