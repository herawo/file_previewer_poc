<html>
    <head >
        <title>Image Preview</title>
    </head>

    <body>
        <table style = text-align:center;>
            <td>
                <% url_prev = prev_page %>
                <tr>
                    <a href="${tg.url('/documents/{doc_id}'.format(doc_id=url_prev))}">
                        <button type="button"> Previous </button>
                    </a>
                </tr>
            </td>
            <td>
                <tr>
                    <a href="${tg.url('/documents/{doc_id}/pages'.format(doc_id=document_id))}">
                        <img src="${tg.url('/img/{doc_id}'.format(doc_id=document_id))}" alt="Displaying issue" style="width:100px;height:100px;"/>
                    </a>
                </tr>
            </td>
            <td>
                <% url_next = next_page %>
                <tr>
                     <a href="${tg.url('/documents/{doc_id}'.format(doc_id=url_next))}">
                         <button type="button"> Next </button>
                     </a>
                </tr>
            </td>
        </table>
    </body>
</html>
