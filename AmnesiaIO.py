import sublime
import sublime_plugin
import json
from urllib.request import Request, urlopen

API_URL = 'https://amnesia.io/api';
MSG_SUCCESS = 'Amnesia.io share link copied to clipboard';

class Amnesia(sublime_plugin.WindowCommand):
  def run(self, **args):
    settings = sublime.load_settings('AmnesiaIO.sublime-settings')

    def request(content):
      headers = {'Content-Type': 'application/json'}
      payload = str.encode(json.dumps({
        'content': content,
        'extension': getExtension(),
        'ttl': settings.get('ttl')
      }))
      req = Request(API_URL, data = payload, headers = headers)

      try:
          response = urlopen(req)
      except TypeError as error:
          return sublime.status_message(str(error))
      except URLError as error:
          return sublime.status_message('Error connecting to "%s"' % API_URL)

      responseJSON = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))

      sublime.set_clipboard(str(responseJSON['url']))
      sublime.status_message(MSG_SUCCESS)

    def getExtension():
      view = self.window.active_view()
      file_name = view.file_name()

      if file_name == None:
        extension = settings.get('defaultFormat')
      else:
        file_name_list = file_name.split('.')
        if len(file_name_list) < 2:
          extension = settings.get('defaultFormat')
        else:
          extension = file_name_list[-1]

      return extension

    def getRelevant():
      view = self.window.active_view()
      selections = view.sel()

      emptySelections = map(lambda sel: sel.a == sel.b, selections)
      if not all(emptySelections):
        trimmedSelections = filter(lambda sel: sel.a != sel.b, selections)
        return map(lambda s: view.substr(s), trimmedSelections)
      elif len(selections) > 1:
        return getLine()
      else:
        return getFile()

    def getFile():
      view = self.window.active_view()
      return [view.substr(sublime.Region(0, view.size()))]

    def getLine():
      view = self.window.active_view()
      return map(lambda region: view.substr(view.line(region)), view.sel())

    def getSelections():
      view = self.window.active_view()
      selections = view.sel()

      emptySelections = map(lambda sel: sel.a == sel.b, selections)
      if all(emptySelections):
        sublime.status_message('Selection empty')
        return False

      trimmedSelections = filter(lambda sel: sel.a != sel.b, selections)
      return map(lambda s: view.substr(s), trimmedSelections)

    def dispatch():
      if 'share' in args:
        share = args['share']
      else:
        share = 'relevant'

      if share == 'relevant':
        texts = getRelevant()
      elif share == 'selection':
        texts = getSelections()
      elif share == 'file':
        texts = getFile()
      elif share == 'line':
        texts = getLine()

      if(texts):
        request('\n'.join(texts))

    dispatch()
