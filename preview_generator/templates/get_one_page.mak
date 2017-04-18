<html>
    <head >
        <title>Image Preview</title>
    </head>

    <body>
        <% id_prev = int(document_id)-1 %>
        <% id_next = int(document_id)+1 %>

        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_prev,p_id=0))}">
            <button type="button"> Previous </button>
        </a>
         <img src="${tg.url('/documents/{d_id}/pages/0/small'.format(d_id=document_id))}" alt="Small not supported" style="width:300px;height:300px;"/>
         <img src="${tg.url('/documents/{d_id}/pages/0/large'.format(d_id=document_id))}" alt="Large not supported" style="width:300px;height:300px;"/>
         <iframe src="${tg.url('/documents/{d_id}/pages/0/pdf'.format(d_id=document_id))}" alt="PDF not supported" style="width:300px;height:300px;"></iframe>
         <iframe src="${tg.url('/documents/{d_id}/pages/0/text'.format(d_id=document_id))}" alt="Text not supported" style="width:300px;height:300px;"></iframe>
         <iframe src="${tg.url('/documents/{d_id}/pages/0/html'.format(d_id=document_id))}" alt="HTML not supported" style="width:300px;height:300px;"></iframe>
        <a href="${tg.url('/documents/{d_id}/pages/{p_id}'.format(d_id=id_next, p_id=0))}">
            <button type="button"> Next </button>
        </a>

    </body>
</html>