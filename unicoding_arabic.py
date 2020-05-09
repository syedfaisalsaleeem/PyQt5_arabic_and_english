from gi.repository import Gtk
label = Gtk.Label()
text = "Fu\u00dfb\u00e4lle"
label.set_text(text)
txt = label.get_text()
#type(txt), txt