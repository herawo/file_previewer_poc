<html>
    <head >
        <title>Image Preview</title>
    </head>

    <body>
        <% id_doc_prev = int(document_id)-1 %>
        <% id_doc_next = int(document_id)+1 %>
        <% id_page_prev = int(page_id)-1 %>
        <% id_page_next = int(page_id)+1 %>

        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_doc_prev,p_id=0))}">
            <button type="button"> Previous Document</button>
        </a>
        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=document_id,p_id=id_page_prev))}">
            <button type="button"> Previous Page</button>
        </a>
          <img src="${tg.url('/documents/{d_id}/pages/{p_id}/small'.format(d_id=document_id, p_id=page_id))}" alt="Small not supported" style="width:300px;height:300px;"/>
          <img src="${tg.url('/documents/{d_id}/pages/{p_id}/large'.format(d_id=document_id, p_id=page_id))}" alt="Large not supported" style="width:300px;height:300px;"/>
         <iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/pdf'.format(d_id=document_id, p_id=document_id))}" alt="PDF not supported" style="width:300px;height:300px;"></iframe>
         <iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/text'.format(d_id=document_id, p_id=page_id))}" alt="Text not supported" style="width:300px;height:300px;"></iframe>
         <iframe src="${tg.url('/documents/{d_id}/pages/{p_id}/html'.format(d_id=document_id, p_id=page_id))}" alt="HTML not supported" style="width:300px;height:300px;"></iframe>

        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=document_id, p_id=id_page_next))}">
            <button type="button"> Next Page</button>
        </a>
        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_doc_next,p_id=0))}">
            <button type="button"> Next Document</button>
        </a>

    </body>
</html>