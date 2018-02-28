import re
import os
import urllib

def ValidatePrefs():
  DefaultPrefs = ("folder")

class Folders2CollectionsMovieAgent(Agent.Movies):
  name, primary_provider, fallback_agent, contributes_to, languages, accepts_from = 'Folders2Collections', True, False, None, [Locale.Language.English,], [] 

  def search(self, results, media, lang, manual=False):
    Log.Info('=== Search ============================================================================================================')
    Log.Info("Title: '%s', name: '%s', filename: '%s', manual: '%s', year: '%s'" % (media.title, media.name, media.filename, str(manual), media.year))
    path = media.filename
    if path:
      path     = urllib.unquote(path)
      Log.Info(path)
      filename = os.path.splitext(os.path.basename(path))[0]
      Log.Info(filename)
    else: filename=""
    Log.Info("".ljust(157, '-'))
    Log.Info("search() - Title: '%s'  -> '%s'" % (media.title,filename))
    results.Append( MetadataSearchResult(id=str(media.title), name=filename, year=media.year, lang=lang, score=100))

  def update(self, metadata, media, lang, force):
    Log.Info('=== Update ==='.ljust(157, '='))
    Log.Info("id: {}, title: {}, lang: {}, force: {}".format(metadata.id, metadata.title, lang, force))
    filename  = media.items[0].parts[0].file.decode('utf-8')
    dirname   = os.path.dirname(filename)
    cleanname = os.path.splitext(os.path.basename(filename))[0]
    pathlist = dirname.split(os.sep)
    folderid = Prefs['folder']
    raw = pathlist[int(folderid)]
    clean = raw.replace("."," ")
    final = clean.title()
    Log("filename: '%s', cleanname: '%s', dirname: '%s'" %(filename, cleanname, dirname))
    metadata.title = cleanname
    Log("pathlist: '%s', folderid: '%s'" %(pathlist, folderid))
    Log("collection: '%s'" %(raw))
    metadata.collections.clear()
    metadata.collections.add(final) 
    Log('update() ended')