import wikipedia as w
from abc import ABC, abstractmethod
#print(w.summary('путин'))
w.set_lang('ru')

class Wikipedia(ABC):
    @abstractmethod
    def search(request):
        try:
            page = w.page(request)
            title = page.title
            text = page.content.split('.')[:10]
            content = '.'.join(text)+'.'
            return title, content
        except:
            title, content = None, None