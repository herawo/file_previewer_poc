<html>
    <head >
        <title>Image Preview</title>
    </head>

    <body>

        <% id_doc_prev = int(document_id)-1 %>
        <% id_doc_next = int(document_id)+1 %>
        <% id_page_prev = int(page_id)-1 %>
        <% id_page_next = int(page_id)+1 %>

        <table width="100%">
            <tr>

             <td width="20%" height="100%"><img src="${tg.url('/documents/{d_id}/pages/{p_id}/small'.format(d_id=document_id, p_id=page_id))}" alt="Not implemented for this kind of document" style="width:100%;height:100%;"/></td>
             <td width="20%" height="100%"><img src="${tg.url('/documents/{d_id}/pages/{p_id}/large'.format(d_id=document_id, p_id=page_id))}" alt="Not implemented for this kind of document" style="width:100%;height:100%;"/></td>
             <td width="20%" height="100%"><iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/pdf'.format(d_id=document_id, p_id=page_id))}" style="width:100%;height:100%;"></iframe></td>
             <td width="20%" height="100%"><iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/text'.format(d_id=document_id, p_id=page_id))}" style="width:100%;height:100%;"></iframe></td>
             <td width="20%" height="100%"><iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/html'.format(d_id=document_id, p_id=page_id))}" style="width:100%;height:100%;"></iframe></td>

            </tr>

        </table>
        <hr>

        <table width="100%">
            <tr><td width="25%" style="text-align: center">
                <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_doc_prev,p_id=0))}">
                    <button type="button"> Previous Document</button>
                </a>
            </td>
            <td width="25%" style="text-align: center">
                % if int(page_id) > 0:
                <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=document_id,p_id=id_page_prev))}">
                    <button type="button"> Previous Page</button>
                </a>
                % endif
            </td>
            <td width="25%" style="text-align: center">
                %if int(page_id) < int(page_nb) - 1 :
                <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=document_id, p_id=id_page_next))}">
                    <button type="button"> Next Page</button>
                </a>
                %endif
            </td>
            <td width="25%" style="text-align: center">
                <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_doc_next,p_id=0))}">
                    <button type="button"> Next Document</button>
                </a>
            </td></tr>
        </table>

    </body>
</html>