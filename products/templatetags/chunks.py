from django import template

register = template.Library()


@register.filter(name='chunks')
def chunk(lst_item,chunks_size):
    chunk=[]
    i=0
    for items in lst_item:
        chunk.append(items)
        i=i+1
        if i==chunks_size:
            yield chunk
            i=0
            chunk=[]
    if chunk:       
        yield chunk
            
    
