<html>
    <head >
        <title>Image Preview - Documents</title>
    </head>

    <body class="centre" py:strip="True">
        <h2>Documents</h2>

        % for index in range(int(document_nb)):
            <a href="${tg.url('/documents/{i}'.format(i=int(index)+1))}">
                <button type="button"> Documents ${int(index)+1}</button>
            </a>
            </br>
        % endfor
    </body>
</html>
