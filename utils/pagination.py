from django.core.paginator import Paginator


def initial_pagination(request, itens, itens_per_page, paginator:Paginator): 
   
    paginator = Paginator(itens, itens_per_page)
    number_page = request.GET.get('page')
    page_obj = paginator.get_page(number_page)
    
    return make_pagination(5, paginator.num_pages, page_obj.number)    



def make_pagination(qtd_page_busca:int, total_page:int, current_page:int):
    middle = qtd_page_busca // 2 + 1

    if qtd_page_busca >= total_page:
        return {
            'range': [i for i in range(1, total_page + 1)],
            'first_page': 1,
            'last_page': total_page,
            'first_out_range': False,
            'last_out_range': True,
            'current': current_page
        }

    if current_page <= middle:
        return {
            'range': [i for i in range(1, qtd_page_busca + 1)],
            'first_page': 1,
            'last_page': total_page,
            'first_out_range': False,
            'last_out_range': True,
            'current': current_page
        }

        #return [i for i in range(1, qtd_page_busca + 1)]
    if current_page > middle and current_page <= total_page - (middle - 1):
        return {
            'range': [current_page + i for i in range(-(middle - 1), middle)],
            'first_page': 1,
            'last_page': total_page,
            'first_out_range': True,
            'last_out_range': True,
            'current': current_page
        }

        #return [current_page + i for i in range(-(middle - 1), middle)]
    
    
    if current_page > total_page - (middle - 1):
        return {
            'range': [i for i in range(total_page - (qtd_page_busca - 1), total_page + 1)],
            'first_page': 1,
            'last_page': total_page,
            'first_out_range': True,
            'last_out_range': False,
            'current': current_page
        }
        
        #return [i for i in range(total_page - (qtd_page_busca - 1), total_page + 1)]
