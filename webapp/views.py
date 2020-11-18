from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,View,TemplateView,FormView,RedirectView
# Create your views here.
import ttg

# 'p ^ q ^ r',  'p V  q V r',  p V (~q) ->r
class IndexMainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw = ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r'])
        context['pira_table_truths'] = raw
        print(raw)
        print(type(raw))
        raw_ = str(raw)
        raw_ = raw_.replace('+','').replace('-','').replace('||','').replace(' ','').replace('and',' & ').replace('or', ' ó ').replace('\n','')

        raw_arr = raw_.split('|')
        raw_arr.remove('')
        print(raw_arr)

        return context


