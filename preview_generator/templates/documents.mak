<html>
    <head >
        <title>Image Preview - Documents</title>
    </head>

    <body class="centre" py:strip="True">
        <h2>Documents</h2>

        % for index in range(int(document_nb)):
            <a href="${tg.url('/documents/{i}'.format(i=index))}">
                <button type="button"> Documents ${index}</button>
            </a>
            </br>
        % endfor
    </body>
</html>
